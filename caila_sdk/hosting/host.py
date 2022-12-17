from typing import Optional, Any, Type

import uvicorn
from pydantic import BaseModel

from caila_sdk.transport.CailaActionSDK import CailaActionSDK

from caila_sdk.abstract import TASK_TYPE
from caila_sdk.hosting.application import prepare_app


def host(
        task: Type[TASK_TYPE],
        params: BaseModel,
        port: int,
):
    app = prepare_app(task, initialization_params=params)
    uvicorn.run(app, host="0.0.0.0", port=port)


def host_caila_cloud_gate(
        task: Type[TASK_TYPE],
        params: BaseModel,
        url: Any,
        connection_token: Optional[Any] = None,
):
    if isinstance(params, str):
        init_config_type = task.get_init_config_schema()
        params = init_config_type.parse_raw(params)

    caila = CailaActionSDK()
    if task.is_batch_predictable:
        caila.registerImpl(task(params, caila.pipelineClient))
    else:
        caila.registerImpl(task(params))
    caila.start([url], connection_token)
    caila.blockUntilShutdown()
