set -e
set -v

BASEDIR=$(dirname "$0")
cd $BASEDIR

BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [ $BRANCH == 'dev' ]; then
  SERVER=https://caila.caila-ci-dev.lo.test-ai.net
fi
if [ $BRANCH == 'stable' ]; then
  SERVER=https://caila.stable.caila-x-sls.test-ai.net
fi
if [ $BRANCH == 'separate-sdk' ]; then
  SERVER=https://caila.separate-sdk.caila-ci-feature.lo.test-ai.net
fi


echo $SERVER

if [ $SERVER ]; then

  echo go
  curl --silent $SERVER/static/mlpgate/api-docs.yaml -o mlp-rest-api.yml
  sed "s/- url:.*/- url: https:\/\/app.caila.io/g" -i mlp-rest-api.yml

  curl --silent $SERVER/static/mlpgate/mlp-grpc.proto -o mlp-grpc.proto

fi