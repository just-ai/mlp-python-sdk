#!/usr/bin/env bash
# ruff (version from uv.lock) + unit tests when env and gRPC code exist; pyright/REST generation stay in CI.
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

if git diff --cached --quiet -- '*.py' '*pyproject.toml' '*uv.lock' '*.proto' '*.yml'; then
  exit 0
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "[build] не найден uv, а зависимости и инструменты SDK ведёт он. Поставь его: https://docs.astral.sh/uv/getting-started/installation/" >&2
  exit 1
fi

RUFF_VERSION="$(awk '/^name = "ruff"$/{found=1;next} found&&/^version = /{gsub(/[version="[:space:]]/,"");print;exit}' uv.lock)"
if [ -z "$RUFF_VERSION" ]; then
  echo "[build] в uv.lock не нашёлся пакет ruff — линт нечем гонять той же версией, что у проекта." >&2
  exit 1
fi

echo "[build] ruff ${RUFF_VERSION} (версия из uv.lock)"
uv tool run "ruff@${RUFF_VERSION}" check .

if uv run --no-sync --directory ./tests python -c 'import pytest, mlp_sdk.mlp_connector.grpc_.mlp_grpc_pb2' >/dev/null 2>&1; then
  uv run --no-sync --directory ./tests pytest -q -p no:cacheprovider --no-cov
else
  echo "[build] юнит-тесты НЕ прогнаны: нет окружения (uv sync) или gRPC-кода (bash build-scripts/generate-grpc.sh)." >&2
  echo "[build] они гоняются в CI (stage test, make generate test)." >&2
fi
