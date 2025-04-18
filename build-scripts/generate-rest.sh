#!/bin/sh

set -e
ROOT=$(realpath $(dirname $0))
cd "$ROOT"
PROJECT_ROOT=$(realpath $ROOT/..)

docker build . -f Dockerfile-openapi \
            --build-arg USER=$USER \
            --build-arg UID=$(id -u) \
            --build-arg GID=$(id -g) \
            -t openapi-generator

cd $PROJECT_ROOT

echo $(pwd)

rm -Rf src/mlp_sdk/mlp_api
rm -Rf src/mlp_sdk/storage_api

docker run --rm -v "${PWD}":/app openapi-generator generate  \
    -i /app/api-specs/mlp-rest-api.yml  -g python-pydantic-v1   -o /app/openapi-generator-output/mlp-rest-api \
    --additional-properties=packageName=mlp_sdk.mlp_api

docker run --rm -v "${PWD}":/app openapi-generator generate  \
    -i /app/api-specs/mlp-storage-api.yml  -g python-pydantic-v1   -o /app/openapi-generator-output/mlp-storage-api \
    --additional-properties=packageName=mlp_sdk.storage_api


find openapi-generator-output -name "*.py" -exec grep -l "allow_population_by_field_name" {} \; | xargs sed -i 's/allow_population_by_field_name/populate_by_name/g'

mv openapi-generator-output/mlp-rest-api/mlp_sdk/mlp_api src/mlp_sdk/
mv openapi-generator-output/mlp-storage-api/mlp_sdk/storage_api src/mlp_sdk/

rm -Rf openapi-generator-output

