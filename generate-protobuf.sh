#!/bin/bash

ROOT=$(dirname $0)
cd $ROOT

export DOCKER_BUILDKIT=1
docker build . -f Dockerfile-grpc-tools \
              --build-arg USER=$USER \
              --build-arg UID=$(id -u) \
              --build-arg GID=$(id -g) \
              --network=host \
              --no-cache \
              -t grpc-tools

rm -Rf ./mlp_sdk/grpc/mlp*

docker run -v $(pwd):/app grpc-tools \
 python3 -m grpc_tools.protoc -I ./mlp-specs/ --python_out=./mlp_sdk/grpc --grpc_python_out=./mlp_sdk/grpc ./mlp-specs/mlp-grpc.proto

#<!--  from from mlp_sdk.grpc import gate_pb2 as gate__pb2  -->
sed -i "s/import mlp_grpc_pb2 as mlp__grpc__pb2/import mlp_sdk.grpc.mlp_grpc_pb2 as mlp__grpc__pb2/g" "mlp_sdk/grpc/mlp_grpc_pb2_grpc.py"

