import json
import os
from pathlib import Path

import yaml

import mlp_sdk
from mlp_sdk.transport.config_enricher import enrich_config


def test_enrich_config():
    __default_config = Path(mlp_sdk.transport.config_enricher.__file__).parent / "config.yml"
    config = yaml.safe_load(open(__default_config))
    updated_config = config.copy()

    enrich_config(updated_config)
    assert config == updated_config

    os.environ.setdefault("MLP_SDK_SHUTDOWN_EVENT_TIMEOUT_SECONDS", "1")
    enrich_config(updated_config)
    assert updated_config['sdk']['shutdown_event_timeout_seconds'] == 1

    retry_error_codes = ["custom.error.code", "mlp-action.common.channel-closed-error"]
    os.environ.setdefault("MLP_SDK_REQUEST_RETRY_ERROR_CODES", json.dumps(retry_error_codes))
    enrich_config(updated_config)
    assert updated_config['sdk']['request_retry_error_codes'] == retry_error_codes
