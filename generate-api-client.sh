#!/bin/sh

ROOT=$(dirname $0)
cd $ROOT

#TODO create container with userid to avoid sudo usage

sudo rm -Rf ./openapi-generator-output
docker run --rm -v ${PWD}:/app openapitools/openapi-generator-cli generate  \
    -i /app/specs/mpl-rest-api.yml  -g python   -o /app/openapi-generator-output \
    --additional-properties=packageName=mpl_api

sudo chown igor:igor -R openapi-generator-output
rm -Rf mpl_api
mv openapi-generator-output/mpl_api .
rm -Rf openapi-generator-output