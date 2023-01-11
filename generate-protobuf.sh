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

rm -Rf ./mpl_sdk/grpc/mpl*

docker run -v $(pwd):/app grpc-tools \
 python3 -m grpc_tools.protoc -I ./mpl-specs/ --python_out=./mpl_sdk/grpc --grpc_python_out=./mpl_sdk/grpc ./mpl-specs/mpl-grpc.proto

#<!--  from from mpl_sdk.grpc import gate_pb2 as gate__pb2  -->
sed -i "s/import mpl_grpc_pb2 as mpl__grpc__pb2/import mpl_sdk.grpc.mpl_grpc_pb2 as mpl__grpc__pb2/g" "mpl_sdk/grpc/mpl_grpc_pb2_grpc.py"

