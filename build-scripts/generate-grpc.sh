#!/bin/bash

set -e
ROOT=$(realpath $(dirname $0))
PROJECT_ROOT=$(realpath $ROOT/..)
cd "$PROJECT_ROOT"

docker build . -f build-scripts/Dockerfile-dev \
            --build-arg USER=$USER \
            --build-arg UID=$(id -u) \
            --build-arg GID=$(id -g) \
            -t mlp-python-sdk-tools

rm -f ./src/mlp_sdk/mlp_connector/grpc_/*.py*

docker run -v $(pwd)/src:/app/src -v $(pwd)/api-specs:/app/api-specs mlp-python-sdk-tools \
  .venv/bin/python -m grpc_tools.protoc -I ./api-specs --python_out=./src/mlp_sdk/mlp_connector/grpc_ --pyi_out=./src/mlp_sdk/mlp_connector/grpc_ --grpc_python_out=./src/mlp_sdk/mlp_connector/grpc_ ./api-specs/mlp-grpc.proto

sed -i "s/import mlp_grpc_pb2 as mlp__grpc__pb2/import mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2 as mlp__grpc__pb2/g" "src/mlp_sdk/mlp_connector/grpc_/mlp_grpc_pb2_grpc.py"
