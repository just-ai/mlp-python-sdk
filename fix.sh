set -e

echo ===============      ruff format       ===============
uv run ruff format

echo ===============       ruff check       ===============
uv run ruff check --fix
