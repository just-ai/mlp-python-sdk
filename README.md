# mlp-sdk

## Начало работы
1. Настройте `~/.netrc` для установки зависимостей из внутреннего nexus-а
```txt
machine nexus.just-ai.com
login <user>
password <pass>
```
2. Настройте окружение
```bash
pip install uv
make venv
. .venv/bin/activate
```
3. Протестируйте работоспособность команд репозитория
```bash
make generate
make test
make check
make build
```

## Обновление версии mlp-sdk
1. Можете настроить `~/.pypirc`
2. Обновите версию, если нужно для тестирования (следите, чтобы у версии был тег `dev*`)
```bash
uv run python -m mlp_apps_ci_utils.bump_version
```
3. Деплой версии, если нужно для тестирования (только во внутренний nexus)
```bash
make build
make deploy
```

## Обновление зависимостей
Пример:
```bash
uv add grpcio --latest
uv add grpcio==1.71.0
```
