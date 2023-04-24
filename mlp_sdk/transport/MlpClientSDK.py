import os
import pathlib
import time
from typing import Dict, Optional, List

import grpc
import yaml
from mlp_api.apis.tags import model_endpoint_api

from mlp_api import Configuration, ApiClient
from mlp_sdk.grpc import mlp_grpc_pb2_grpc, mlp_grpc_pb2
from mlp_sdk.log.setup_logging import get_logger

__default_config = pathlib.Path(__file__).parent / "config.yml"

CONFIG = yaml.safe_load(open(os.environ.get("MLP_CONFIG_FILE", __default_config)))



class MlpClientSDK:

    def __init__(self):
        self.account_id = os.environ['MLP_ACCOUNT_ID']
        self.model_id = os.environ['MLP_MODEL_ID']
        self.urls = None
        self.token = None
        self.grpc_secure = None
        self.log = get_logger('MlpClientSDK', CONFIG["logging"]["level"])
        self.channel = None

    def init(self, urls: Optional[List[str]] = None, token=None, grpc_secure: Optional[bool] = None):
        self.urls: List[str] = os.environ['MLP_GRPC_HOST'].split(",") if not urls else urls
        self.token = os.environ['MLP_CLIENT_TOKEN'] if not token else token
        self.grpc_secure = os.environ['MLP_GRPC_SECURE'].lower() == 'true' if not grpc_secure else grpc_secure
        self.log.debug("Starting mpl client for url " + self.urls[0])

        self.__connect()

    def predict(self, account, model, data, config="{}") -> mlp_grpc_pb2.PredictResponseProto:

        if isinstance(data, str):
            data = str.encode(data)

        request = mlp_grpc_pb2.ClientRequestProto(
            account=account,
            model=model,
            authToken=self.token,
            predict=mlp_grpc_pb2.PredictRequestProto(
                data=mlp_grpc_pb2.PayloadProto(json=data),
                config=mlp_grpc_pb2.PayloadProto(json=config)
            )
        )

        response: Optional[mlp_grpc_pb2.ClientResponseProto] = self.__process_request_with_retry(request)

        res = response.WhichOneof('body')
        if res == 'predict':
            return response.predict
        elif res == 'error':
            self.log.error(f'Error from gate. Error \n{response.error}')
            raise MlpClientException(response.error.code, response.error.message, response.error.argsMap)
        else:
            raise MlpClientException("wrong-response", "Wrong response type: $response", {})

    def ext(self, account, model, method, data) -> mlp_grpc_pb2.ExtendedResponseProto:
        request = mlp_grpc_pb2.ClientRequestProto(
            account=account,
            model=model,
            authToken=self.token,
            ext=mlp_grpc_pb2.ExtendedRequestProto(
                methodName=method,
                params=data
            )
        )

        response: Optional[mlp_grpc_pb2.ClientResponseProto] = self.__process_request_with_retry(request)

        res = response.WhichOneof('body')
        if res == 'ext':
            return response.ext
        elif res == 'error':
            self.log.error(f'Error from gate. Error \n{response.error}')
            raise MlpClientException(response.error.code, response.error.message, response.error.argsMap)
        else:
            raise MlpClientException("wrong-response", "Wrong response type: $response", {})

    def __process_request_with_retry(self, request):
        response: Optional[mlp_grpc_pb2.ClientResponseProto] = None

        request_retry_timeout_seconds = CONFIG["sdk"]["request_retry_timeout_seconds"]
        end_time = time.time() + request_retry_timeout_seconds

        while time.time() < end_time:
            try:
                response = self.stub.process(request)
                break
            except grpc.RpcError as rpc_error:
                if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                    self.__connect()
                else:
                    self.log.error(f'Error from grpc channel. Error \n{rpc_error.details()}')
                    raise MlpClientException(f'{rpc_error.code()}', f'{rpc_error.details()}', {})

        if response is None:
            raise MlpClientException(
                'UNAVAILABLE',
                f'Cannot connect after {request_retry_timeout_seconds} seconds',
                {}
            )

        return response

    def shutdown(self):
        self.channel.close()

    def __connect(self):
        if self.channel is not None:
            self.channel.close()

        if self.grpc_secure:
            if hasattr(os.environ, "GRPC_SSL_CA_FILE_PATH"):
                with open(os.environ["GRPC_SSL_CA_FILE_PATH"], 'rb') as f:
                    creds = grpc.ssl_channel_credentials(f.read())
            else:
                creds = grpc.ssl_channel_credentials()

            self.channel = grpc.secure_channel(self.urls[0], creds, options=[
                ('grpc.max_send_message_length', CONFIG["grpc"]["max_send_message_length"]),
                ('grpc.max_receive_message_length', CONFIG["grpc"]["max_receive_message_length"])
            ])
        else:
            self.channel = grpc.insecure_channel(self.urls[0], options=[
                ('grpc.max_send_message_length', CONFIG["grpc"]["max_send_message_length"]),
                ('grpc.max_receive_message_length', CONFIG["grpc"]["max_receive_message_length"])
            ])
        self.stub = mlp_grpc_pb2_grpc.GateStub(self.channel)

class MlpRestClient:

    def __init__(self, url: Optional[str] = None, token=None):
        self.log = get_logger('MlpRestClient', CONFIG["logging"]["level"])
        self.account_id = os.environ['MLP_ACCOUNT_ID']
        self.model_id = os.environ['MLP_MODEL_ID']
        self.rest_url = os.environ['MLP_REST_URL'] if not url else url
        self.client_token = os.environ['MLP_CLIENT_TOKEN'] if not token else token
        self.log.debug("Creating mpl client with url " + self.rest_url)

        configuration = Configuration(host=self.rest_url)
        self.api_client = ApiClient(configuration, "MLP-API-KEY", self.client_token)

        self.modelApi = model_endpoint_api.ModelEndpointApi(self.api_client)

class MlpClientException(Exception):
    def __init__(self, error_code: str, error_message: str, args: Dict[str, str]):
        self.error_code: str = error_code
        self.error_message: str = error_message
        self.args: Dict[str, str] = args

    def __str__(self):
        return f'MlpClientException({self.error_code}, {self.error_message}, {self.args})'
