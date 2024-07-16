import json
from argparse import ArgumentParser

import grpc

from mlp_sdk.grpc.mlp_grpc_pb2 import (
    ClientRequestProto,
    PayloadProto,
    PredictRequestProto,
)
from mlp_sdk.grpc.mlp_grpc_pb2_grpc import GateStub

if __name__ == "__main__":
    parser = ArgumentParser(description="Пример потокового запроса к LLM.")
    parser.add_argument(
        "--mlp_api_key",
        type=str,
        required=True,
        help="Токен доступа, можно получить во вкладе API Токены в Caila.",
    )
    args = parser.parse_args()

    mlp_api_key = args.mlp_api_key
    payload = json.dumps(
        {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "hello"}],
            "stream": True,
        }
    )
    request = ClientRequestProto(
        account="just-ai",
        model="openai-proxy",
        predict=PredictRequestProto(
            data=PayloadProto(
                dataType="https://caila.io/specs/mlp-data-gpt.yml#/ChatCompletionRequest",
                json=payload,
            )
        ),
        authToken=mlp_api_key,
    )

    with grpc.secure_channel(
        "gate.caila.io:443", credentials=grpc.ssl_channel_credentials()
    ) as channel:
        stub = GateStub(channel)
        for response in stub.processResponseStream(request):
            print(response.partialPredict)
