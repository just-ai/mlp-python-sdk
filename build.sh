#!/bin/bash

set -e
ROOT=$(realpath $(dirname $0))
cd "$ROOT"

if [ -z "$1" ]; then
    BRANCH=$(git rev-parse --abbrev-ref HEAD)
else
    BRANCH=$1
fi

#     BUILD CONTAINER WITH TOOLS
docker build . -f ./build-scripts/Dockerfile-dev \
            --build-arg USER=$USER \
            --build-arg UID=$(id -u) \
            --build-arg GID=$(id -g) \
            -t mlp-python-sdk-tools

#     EXECUTE ALL CHECKs
mkdir ./pytest-report | true
mkdir ./htmlcov | true
mkdir ./dist | true
UV_CMD="docker run -i --rm \
  -v $HOME/.pypirc:/home/$USER/.pypirc \
  -v $(pwd)/src:/app/src \
  -v $(pwd)/tests:/app/tests  \
  -v $(pwd)/htmlcov:/app/htmlcov  \
  -v $(pwd)/pytest-report:/app/pytest-report \
  -v $(pwd)/dist:/app/dist \
  mlp-python-sdk-tools"

echo ===============      ruff format       ===============
$UV_CMD \
    .venv/bin/ruff format --check src/

echo ===============       ruff check       ===============
$UV_CMD \
    .venv/bin/ruff check src/

echo ===============         pyright        ===============
$UV_CMD \
    .venv/bin/pyright src/

#echo ===============          pytest        ===============
#$UV_CMD \
#    .venv/bin/pytest tests/

#echo ===============      check coverage    ===============
#total_cov=$($UV_CMD uv run tests/check_pycov.py | tr -d '\r')
#
#if [[ "$total_cov" != "100" ]]; then
#    echo ""
#    echo "Ошибка: не полное тестовое покрытие: $total_cov%. Сборка остановлена."
#    exit 1
#fi

#     BUILD AND PUBLISH
echo ===============     Build package    ===============
rm -f dist/*
$UV_CMD \
    uv run python -m build

echo ===============     Upload to nexus     ===============
$UV_CMD \
    .venv/bin/twine upload --repository nexus --verbose \
    /app/dist/*.whl

# в nexus-open не надо пушить dev версии
$UV_CMD \
    .venv/bin/twine upload --repository nexus-open --verbose \
    /app/dist/*.whl

