import http
from collections.abc import Callable
from typing import List, Optional, Tuple, Union

from fastapi import Response
from pydantic import BaseModel, create_model

import mlp_sdk.types as types
from mlp_sdk.abstract import TASK_TYPE, Task
from mlp_sdk.allowed_types import BASE_FIELD_NAME_TO_TYPE


class MlpBaseModel(BaseModel):
    @classmethod
    def with_fields(cls, name, **field_definitions):
        return create_model(name, __base__=cls, **field_definitions)


def get_type(type_: str, task: TASK_TYPE, method_name: str):
    type_splitted = type_.split()
    if hasattr(types, type_):
        return getattr(types, type_)

    elif "Config" in type_ or "Schema" in type_:
        return getattr(task, f"get_{method_name}_config_schema")()

    elif type_ in BASE_FIELD_NAME_TO_TYPE:
        return BASE_FIELD_NAME_TO_TYPE[type_]
    elif type_splitted[0] == "array":
        inner_type = getattr(types, type_splitted[1])
        return List[inner_type]
    else:
        raise AttributeError(f"Unknown attribute {type_} in task {task}")


def get_method_view(task: TASK_TYPE, method_name: str) -> Optional[Union[Callable, Tuple[Callable, BaseModel]]]:
    if not isinstance(task, Task):
        return None

    descriptor = task.get_descriptor()
    if method_name not in descriptor.methods:
        return None

    input_arg_to_type = {
        k: (get_type(v.type, task, method_name), ...) for k, v in descriptor.methods[method_name].input.items()
    }
    output = descriptor.methods[method_name].output.type

    RequestModel = MlpBaseModel.with_fields(
        f"{task.__class__.__name__}_{method_name}_RequestModel", **input_arg_to_type
    )
    output_splitted = output.split()
    if output_splitted[0] == "array":
        ResponseModel = List[getattr(types, output_splitted[1])]
    else:
        ResponseModel = getattr(types, output) if output != "null" else None

    class ViewWrapped:
        def __init__(self):
            self.task = task

        def __call__(self, request: RequestModel) -> Union[Response, ResponseModel]:
            response = getattr(self.task, method_name)(
                **{
                    (k if not k.startswith("_") else k[1:]): getattr(request, k)
                    for k in request.__dict__
                    if not k.startswith("__")
                }
            )
            if ResponseModel is None:
                response = Response(status_code=http.HTTPStatus.OK)
            return response

    if ResponseModel is None:
        return ViewWrapped()
    return ViewWrapped(), ResponseModel
