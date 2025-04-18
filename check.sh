set -e

echo ===============  refresh requirements  ===============
uv sync

echo ===============      ruff format       ===============
.venv/bin/ruff format --check

echo ===============       ruff check       ===============
.venv/bin/ruff check

echo ===============         pyright        ===============
.venv/bin/pyright

#echo ===============          pytest        ===============
#.venv/bin/pytest
