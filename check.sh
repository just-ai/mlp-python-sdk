set -e

echo ===============  refresh requirements  ===============
uv sync

echo ===============      ruff format       ===============
uv run ruff format --check

echo ===============       ruff check       ===============
uv run ruff check

echo ===============         pyright        ===============
uv tool run pyright

echo ===============          pytest        ===============
uv run pytest
