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

if [ -z $SERVER ]; then
  # check parallel env exists
  SRV=https://caila.$BRANCH.caila-ci-feature.lo.test-ai.net
  CHECK=$(curl -si $SRV/api/mlpgate/version | head -n 1 | grep 200)
  if [ "$CHECK" ]; then
    SERVER=$SRV
  fi
fi


echo $SERVER

if [ ! -z $SERVER ]; then

  echo go
  curl --silent $SERVER/static/mlpgate/api-docs.yaml -o mlp-rest-api.yml
  sed "s/- url:.*/- url: https:\/\/app.caila.io/g" -i mlp-rest-api.yml

  curl --silent $SERVER/static/mlpgate/mlp-grpc.proto -o mlp-grpc.proto

fi