set -e

echo ===============      ruff format       ===============
.venv/bin/ruff format

echo ===============       ruff check       ===============
.venv/bin/ruff check --fix
