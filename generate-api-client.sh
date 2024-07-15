#!/bin/sh

set -e
ROOT=$(dirname $0)
cd $ROOT

#TODO create container with userid to avoid sudo usage

sudo rm -Rf ./openapi-generator-output

docker run --rm -v ${PWD}:/app openapitools/openapi-generator-cli:v7.6.0 generate  \
    -i /app/mlp-specs/mlp-rest-api.yml  -g python-pydantic-v1   -o /app/openapi-generator-output \
    --additional-properties=packageName=mlp_api

sudo chown $USER:$USER -R openapi-generator-output
sudo rm -Rf mlp_api
mv openapi-generator-output/mlp_api .

rm -Rf openapi-generator-output
