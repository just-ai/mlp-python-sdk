#!/bin/bash

export DOCKER_BUILDKIT=1
docker build . --network=host -f Dockerfile-mlp-sdk-build \
               -t mlp_sdk_build --no-cache

docker run --network=host -v $(pwd):/mlp_python_sdk mlp_sdk_build pip install .
docker run --network=host -v $(pwd):/mlp_python_sdk mlp_sdk_build pip wheel .

sudo rm -Rf $(find . -name __pycache__)