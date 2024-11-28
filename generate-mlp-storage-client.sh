#!/bin/sh

set -e
ROOT=$(dirname $0)
cd $ROOT

#TODO create container with userid to avoid sudo usage

sudo rm -Rf ./openapi-generator-output
docker run --rm -v ${PWD}:/app openapitools/openapi-generator-cli:v7.6.0 generate  \
    -i /app/mlp-specs/mlp-storage-api.yml  -g python-pydantic-v1   -o /app/openapi-generator-output \
    --additional-properties=packageName=storage_api

sudo chown $USER:$USER -R openapi-generator-output
sudo rm -Rf storage_api
mv openapi-generator-output/storage_api .
rm -Rf openapi-generator-output