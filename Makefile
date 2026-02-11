MAIN_BRANCH := v2
BRANCH_NAME := $${CI_COMMIT_REF_NAME:-$$(git rev-parse --abbrev-ref HEAD)}

all: check build

format:
	@pip install pre-commit
	@pre-commit install
	@echo +ruff format .
	@uv run ruff format .
	@echo +ruff check --fix .
	@uv run ruff check --fix .

check:
	@echo +ruff check .
	@uv run ruff check .
	@echo +pyright
	@uv tool run pyright

test: check
	uv run --directory ./tests pytest

clean:
	@rm -Rf dist htmlcov pytest-report
	@find . -name .coverage -delete
	@find . -name '*.pyc' -delete

venv:
	uv sync


rest:
	@./build-scripts/generate-rest.sh

grpc:
	@./build-scripts/generate-grpc.sh

generate: rest grpc

build: clean generate
	uv run python -m build

deploy:
	@
	if grep -q "version.*dev" pyproject.toml; then \
		echo "Deploying dev version into private nexus..."; \
		uv run twine upload --repository nexus --verbose ./dist/*.whl; \
	else \
		echo "Deploying release version into public nexus..."; \
		uv run twine upload --repository nexus-open --verbose ./dist/*.whl; \
	fi

.PHONY: venv build deploy rest grpc clean test check format all
