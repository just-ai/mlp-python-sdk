import os
import pathlib
import time
from typing import Dict, Optional, List

import grpc
import yaml
from mlp_api.apis.tags import model_endpoint_api, process_endpoint_api, dataset_endpoint_api

from mlp_api import Configuration, ApiClient
from mlp_sdk.grpc import mlp_grpc_pb2_grpc, mlp_grpc_pb2
from mlp_sdk.log.setup_logging import get_logger
from mlp_sdk.transport.MlpServiceSDK import MlpResponseHeaders

__default_config = pathlib.Path(__file__).parent / "config.yml"

CONFIG = yaml.safe_load(open(os.environ.get("MLP_CONFIG_FILE", __default_config)))
RECONNECT_ERROR_CODES = ["mlp.gate.gate_is_shut_down"]


class MlpClientSDK:

    def __init__(self, config=CONFIG):
        self.config = config
        self.account_id = os.environ.get('MLP_ACCOUNT_ID')
        self.model_id = os.environ.get('MLP_MODEL_ID')
        self.urls = None
        self.token = None
        self.grpc_secure = None
        self.log = get_logger('MlpClientSDK')
        self.channel = None

    def init(self, urls: Optional[List[str]] = None, token=None, grpc_secure: Optional[bool] = None):
        self.urls: List[str] = os.environ.get('MLP_GRPC_HOST', 'gate.caila.io').split(",") if not urls else urls
        self.token = os.environ['MLP_CLIENT_TOKEN'] if not token else token
        self.grpc_secure = os.environ.get('MLP_GRPC_SECURE', 'true').lower() == 'true' if not grpc_secure else grpc_secure
        self.log.debug("Starting mpl client for url " + self.urls[0])

        self.__connect()

    def predict(self, account, model, data, config="{}", headers=None) -> mlp_grpc_pb2.PredictResponseProto:
        return self.predict_full(account, model, data, config, headers).predict

    def predict_full(self, account, model, data, config="{}", headers=None) -> mlp_grpc_pb2.ServiceToGateProto:

        if isinstance(data, str):
            data = str.encode(data)

        if headers is None:
            headers = {}

        request = mlp_grpc_pb2.ClientRequestProto(
            account=account,
            model=model,
            authToken=self.token,
            predict=mlp_grpc_pb2.PredictRequestProto(
                data=mlp_grpc_pb2.PayloadProto(json=data),
                config=mlp_grpc_pb2.PayloadProto(json=config)
            ),
            headers=headers
        )

        return self.predict_raw(request)

    def predict_raw(self, request: mlp_grpc_pb2.ClientRequestProto) -> mlp_grpc_pb2.ServiceToGateProto:
        if hasattr(MlpResponseHeaders, 'headers'):
            request_id = MlpResponseHeaders.headers.get("Z-requestId")
            if request_id is not None and "Z-requestId" not in request.headers:
                request.headers["Z-requestId"] = request_id

            billing_key = MlpResponseHeaders.headers.get("MLP-BILLING-KEY")
            if billing_key is not None:
                request.headers["MLP-BILLING-KEY"] = billing_key

        response: Optional[mlp_grpc_pb2.ClientResponseProto] = self.__process_request_with_retry(request)

        res = response.WhichOneof('body')
        if res == 'predict':
            return response
        elif res == 'error':
            self.log.error(f'Error from gate. Error \n{response.error}')
            raise MlpClientException(response.error.code, response.error.message, response.error.args)
        else:
            raise MlpClientException("wrong-response", "Wrong response type: $response", {})

    def ext(self, account, model, method, data, headers=None) -> mlp_grpc_pb2.ExtendedResponseProto:
        if headers is None:
            headers = {}

        request = mlp_grpc_pb2.ClientRequestProto(
            account=account,
            model=model,
            authToken=self.token,
            ext=mlp_grpc_pb2.ExtendedRequestProto(
                methodName=method,
                params=data
            ),
            headers=headers
        )

        return self.ext_raw(request)

    def ext_raw(self, request: mlp_grpc_pb2.ClientRequestProto) -> mlp_grpc_pb2.ExtendedResponseProto:
        response: Optional[mlp_grpc_pb2.ClientResponseProto] = self.__process_request_with_retry(request)

        res = response.WhichOneof('body')
        if res == 'ext':
            return response.ext
        elif res == 'error':
            self.log.error(f'Error from gate. Error \n{response.error}')
            raise MlpClientException(response.error.code, response.error.message, response.error.args)
        else:
            raise MlpClientException("wrong-response", "Wrong response type: $response", {})

    def __process_request_with_retry(self, request):
        response: Optional[mlp_grpc_pb2.ClientResponseProto] = None

        request_retry_timeout_seconds = self.config["sdk"]["request_retry_timeout_seconds"]
        end_time = time.time() + request_retry_timeout_seconds

        request_retry_max_attempts = self.config["sdk"]["request_retry_max_attempts"]
        request_retry_backoff_seconds = self.config["sdk"]["request_retry_backoff_seconds"]
        request_retry_error_codes = self.config["sdk"]["request_retry_error_codes"]

        request_retry_failures = 0

        while time.time() < end_time:
            try:
                response = self.stub.process(request)

                has_error = response.WhichOneof('body') == 'error'
                should_retry = has_error and response.error.code in request_retry_error_codes
                should_reconnect = has_error and response.error.code in RECONNECT_ERROR_CODES

                if should_reconnect:
                    self.__connect()

                if not should_retry and not should_reconnect:
                    break

                request_retry_failures += 1
                if request_retry_failures >= request_retry_max_attempts:
                    break

                self.log.error(f'Error from gate, attempt {request_retry_failures}:\n{response.error}')
                time.sleep(request_retry_backoff_seconds)
                continue
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
        channel_options = [
            ('grpc.keepalive_time_ms', self.config["grpc"]["keepalive_time_ms"]),
            ('grpc.keepalive_timeout_ms', self.config["grpc"]["keepalive_timeout_ms"]),
            ('grpc.keepalive_permit_without_calls', self.config["grpc"]["keepalive_permit_without_calls"]),
            ('grpc.max_send_message_length', self.config["grpc"]["max_send_message_length"]),
            ('grpc.max_receive_message_length', self.config["grpc"]["max_receive_message_length"])
        ]

        if self.grpc_secure:
            if hasattr(os.environ, "GRPC_SSL_CA_FILE_PATH"):
                with open(os.environ["GRPC_SSL_CA_FILE_PATH"], 'rb') as f:
                    creds = grpc.ssl_channel_credentials(f.read())
            else:
                creds = grpc.ssl_channel_credentials()

            new_channel = grpc.secure_channel(self.urls[0], creds, options=channel_options)
        else:
            new_channel = grpc.insecure_channel(self.urls[0], options=channel_options)

        self.stub = mlp_grpc_pb2_grpc.GateStub(new_channel)

        previous_channel = self.channel
        self.channel = new_channel

        if previous_channel is not None:
            previous_channel.close()

class MlpRestClient:

    def __init__(self, url: Optional[str] = None, token=None, config=CONFIG):
        self.config = config
        self.log = get_logger('MlpRestClient')
        self.account_id = os.environ.get('MLP_ACCOUNT_ID')
        self.model_id = os.environ.get('MLP_MODEL_ID')
        self.rest_url = os.environ.get('MLP_REST_URL', "https://app.caila.io") if not url else url
        self.client_token = os.environ['MLP_CLIENT_TOKEN'] if not token else token
        self.log.debug("Creating mpl client with url " + self.rest_url)

        configuration = Configuration(host=self.rest_url)
        self.api_client = ApiClient(configuration, "MLP-API-KEY", self.client_token)

        self.modelApi = model_endpoint_api.ModelEndpointApi(self.api_client)
        self.processApi = process_endpoint_api.ProcessEndpointApi(self.api_client)
        self.datasetApi = dataset_endpoint_api.DatasetEndpointApi(self.api_client)
        
class MlpClientException(Exception):
    def __init__(self, error_code: str, error_message: str, args: Dict[str, str]):
        self.error_code: str = error_code
        self.error_message: str = error_message
        self.args: Dict[str, str] = args

    def __str__(self):
        return f'MlpClientException({self.error_code}, {self.error_message}, {self.args})'
