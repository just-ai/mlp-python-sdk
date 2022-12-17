#!/bin/sh

ROOT=$(dirname $0)
cd $ROOT

#TODO container with userid
#TODO separate module?
docker run --rm -v ${PWD}/../mpl-specs:/spec -v ${PWD}:/app openapitools/openapi-generator-cli generate   -i /spec/mpl-rest-api.yml  -g python   -o /app/out
