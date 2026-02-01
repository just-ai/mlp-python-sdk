#!/bin/sh

set -e
ROOT=$(realpath $(dirname $0))
cd "$ROOT"
PROJECT_ROOT=$(realpath $ROOT/..)

cd $PROJECT_ROOT

docker build . -f ./build-scripts/Dockerfile-openapi -t openapi-generator \
            --build-arg USER=just \
            --build-arg UID=1230 \
            --build-arg GID=1230

echo $(pwd)
mkdir openapi-generator-output

rm -Rf src/mlp_sdk/mlp_api
rm -Rf src/mlp_sdk/storage_api

docker rm openapi-container || echo "Уже удален"
docker run --name openapi-container openapi-generator generate  \
    -i api-specs/mlp-rest-api.yml  -g python-pydantic-v1   -o openapi-generator-output/mlp-rest-api \
    --additional-properties=packageName=mlp_sdk.mlp_api

docker cp openapi-container:/app/openapi-generator-output/mlp-rest-api ./openapi-generator-output/mlp-rest-api
docker rm openapi-container

docker run --name openapi-container openapi-generator generate  \
    -i api-specs/mlp-storage-api.yml  -g python-pydantic-v1   -o openapi-generator-output/mlp-storage-api \
    --additional-properties=packageName=mlp_sdk.storage_api

docker cp openapi-container:/app/openapi-generator-output/mlp-storage-api ./openapi-generator-output/mlp-storage-api
docker rm openapi-container

find openapi-generator-output -name "*.py" -exec grep -l "allow_population_by_field_name" {} \; | xargs sed -i 's/allow_population_by_field_name/populate_by_name/g'

find openapi-generator-output -name "*.py" -exec grep -l ", unique_items=True" {} \; | xargs sed -i 's/, unique_items=True//g'

mv openapi-generator-output/mlp-rest-api/mlp_sdk/mlp_api src/mlp_sdk/
mv openapi-generator-output/mlp-storage-api/mlp_sdk/storage_api src/mlp_sdk/

rm -Rf openapi-generator-output
