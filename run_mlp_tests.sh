#!/bin/bash

export DOCKER_BUILDKIT=1
docker build . --network=host -f Dockerfile-mlp-sdk-test \
               --build-arg S3_STORAGE_CONFIG="$S3_STORAGE_CONFIG" \
               -t mlp_sdk_tests --no-cache

docker run --network=host -v $(pwd):/mlp_python_sdk mlp_sdk_tests pip install .
docker run --network=host -v $(pwd):/mlp_python_sdk mlp_sdk_tests pytest