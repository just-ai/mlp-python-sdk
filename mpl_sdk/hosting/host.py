from typing import Optional, Any, Type

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
        url: Any,
        connection_token: Optional[Any] = None,
):
    if isinstance(params, str):
        init_config_type = task.get_init_config_schema()
        params = init_config_type.parse_raw(params)

    mpl = MplActionSDK()
    if task.is_batch_predictable:
        mpl.register_impl(task(params, mpl.pipeline_client))
    else:
        mpl.register_impl(task(params))
    mpl.start([url], connection_token)
    mpl.block_until_shutdown()
