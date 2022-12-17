#!/bin/bash

ROOT=$(dirname $0)
cd $ROOT

export DOCKER_BUILDKIT=1
docker build . -f Dockerfile-grpc-tools \
              --build-arg USER=$USER \
              --build-arg UID=$(id -u) \
              --build-arg GID=$(id -g) \
              --network=host \
              -t grpc-tools

rm -Rf ./caila_sdk/grpc/mpl*

docker run -v $(pwd):/app -it grpc-tools \
 python3 -m grpc_tools.protoc -I ./specs/ --python_out=./caila_sdk/grpc --grpc_python_out=./caila_sdk/grpc ./specs/mpl-grpc.proto

#<!--  from from caila_sdk.grpc import gate_pb2 as gate__pb2  -->
sed -i "s/import mpl_grpc_pb2 as mpl__grpc__pb2/import caila_sdk.grpc.mpl_grpc_pb2 as mpl__grpc__pb2/g" "caila_sdk/grpc/mpl_grpc_pb2_grpc.py"

