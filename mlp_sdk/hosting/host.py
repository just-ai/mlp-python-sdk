from typing import Dict
from typing import Type

import uvicorn
from pydantic import BaseModel

from mlp_sdk.abstract import TASK_TYPE
from mlp_sdk.hosting.application import prepare_app
from mlp_sdk.transport.MlpServiceSDK import MlpServiceSDK, CONFIG


def host(
        task: Type[TASK_TYPE],
        params: BaseModel,
        port: int,
):
    app = prepare_app(task, initialization_params=params)
    uvicorn.run(app, host="0.0.0.0", port=port)


def host_mlp_cloud(
        task: Type[TASK_TYPE],
        params: BaseModel,
        config: Dict = CONFIG
):
    if isinstance(params, str):
        init_config_type = task.get_init_config_schema()
        params = init_config_type.parse_raw(params)

    mpl = MlpServiceSDK(config)
    mpl.register_impl(task(params, mpl))
    mpl.start()
    mpl.block_until_shutdown()
