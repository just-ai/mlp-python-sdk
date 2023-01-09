from typing import Type

import uvicorn
from pydantic import BaseModel

from mpl_sdk.transport.MplActionSDK import MplActionSDK

from mpl_sdk.abstract import TASK_TYPE
from mpl_sdk.hosting.application import prepare_app


def host(
        task: Type[TASK_TYPE],
        params: BaseModel,
        port: int,
):
    app = prepare_app(task, initialization_params=params)
    uvicorn.run(app, host="0.0.0.0", port=port)


def host_mpl_cloud(
        task: Type[TASK_TYPE],
        params: BaseModel,
):
    if isinstance(params, str):
        init_config_type = task.get_init_config_schema()
        params = init_config_type.parse_raw(params)

    mpl = MplActionSDK()
    if task.is_learnable:
        mpl.register_impl(task(params, mpl.pipeline_client))
    else:
        mpl.register_impl(task(params))
    mpl.start()
    mpl.block_until_shutdown()
