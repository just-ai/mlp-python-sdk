import http
from inspect import _empty, signature
from typing import Type

from fastapi import FastAPI
from pydantic import BaseModel

from mlp_sdk.abstract import TASK_TYPE


def prepare_app(task_type: Type[TASK_TYPE], initialization_params: BaseModel) -> FastAPI:
    app = FastAPI()
    task = task_type(initialization_params)

    for method_name in list(task.get_descriptor().methods.keys()):
        if method_name == "init":
            continue

        endpoint = getattr(task, method_name)
        response_model = signature(endpoint).return_annotation

        if response_model != _empty:
            app.add_api_route(
                f"/{method_name}",
                endpoint=endpoint,
                methods=["POST"],
                name=method_name,
                response_model=response_model,
            )
        else:
            app.add_api_route(
                f"/{method_name}",
                endpoint=endpoint,
                methods=["POST"],
                name=method_name,
                response_model=None,
            )

    def health_check():
        return http.HTTPStatus.OK.phrase

    app.add_api_route("/healthCheck", endpoint=health_check, methods=["GET"], name="health_check")

    return app
