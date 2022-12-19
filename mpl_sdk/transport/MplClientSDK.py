import logging
import os
import pathlib
import sys
import time
from typing import Dict, Optional, List

import grpc
import yaml

from mpl_sdk.grpc import mpl_grpc_pb2_grpc, mpl_grpc_pb2

__default_config = pathlib.Path(__file__).parent / "config.yml"

CONFIG = yaml.safe_load(open(os.environ.get("MPL_CONFIG_FILE", __default_config)))

logging.basicConfig(format=CONFIG["logging"]["format"],
                    level=logging.getLevelName(CONFIG["logging"]["level"]),
                    stream=sys.stdout)


class MplClientSDK:

    def __init__(self):
        self.urls = None
        self.token = None
        self.grpc_secure = None
        self.log = logging.getLogger('MplClientSDK')
        self.channel = None

    def init(self, urls: Optional[List[str]] = None, token=None, grpc_secure: Optional[bool] = None):
        self.urls: List[str] = os.environ['MPL_URL'].split(",") if not urls else urls
        self.token = os.environ['MPL_TOKEN'] if not token else token
        self.grpc_secure = os.environ['MPL_GRPC_SECURE'].lower() == 'true' if not grpc_secure else grpc_secure
        self.log.debug("Starting mpl client for url " + self.urls[0])

        self.__connect()

    def predict(self, account, model, data, config="{}") -> mpl_grpc_pb2.PredictResponseProto:

        if isinstance(data, str):
            data = str.encode(data)

        request = mpl_grpc_pb2.ClientRequestProto(
            account=account,
            model=model,
            authToken=self.token,
            predict=mpl_grpc_pb2.PredictRequestProto(
                data=mpl_grpc_pb2.PayloadProto(json=data),
                config=mpl_grpc_pb2.PayloadProto(json=config)
            )
        )

        response: Optional[mpl_grpc_pb2.ClientResponseProto] = self.__process_request_with_retry(request)

        if response.predict is not None:
            return response.predict
        elif response.error is not None:
            self.log.error(f'Error from gate. Error \n{response.error}')
            raise CailaClientException(response.error.code, response.error.message, response.error.argsMap)
        else:
            raise CailaClientException("wrong-response", "Wrong response type: $response", {})

    def __process_request_with_retry(self, request):
        response: Optional[mpl_grpc_pb2.ClientResponseProto] = None

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
                    raise CailaClientException(f'{rpc_error.code()}', f'{rpc_error.details()}', {})

        if response is None:
            raise CailaClientException(
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
        self.stub = mpl_grpc_pb2_grpc.GateStub(self.channel)


class CailaClientException(Exception):
    def __init__(self, error_code: str, error_message: str, args: Dict[str, str]):
        self.error_code: str = error_code
        self.error_message: str = error_message
        self.args: Dict[str, str] = args

    def __str__(self):
        return f'CailaClientException({self.error_code}, {self.error_message}, {self.args})'
