import http
from typing import Type

from fastapi import FastAPI
from pydantic import BaseModel

from mlp_sdk.abstract import TASK_TYPE
from mlp_sdk.hosting.views.views import get_method_view


def prepare_app(task_type: Type[TASK_TYPE], initialization_params: BaseModel) -> FastAPI:
    app = FastAPI()
    task = task_type(initialization_params)

    for method_name in list(task.get_descriptor().methods.keys()):
        if method_name == "init":
            continue

        result = get_method_view(task, method_name)

        if result is not None:
            if isinstance(result, tuple) and len(result) == 2:
                app.add_api_route(
                    f"/{method_name}", endpoint=result[0], methods=["POST"], name=method_name, response_model=result[1]
                )
            else:
                app.add_api_route(
                    f"/{method_name}",
                    endpoint=result,
                    methods=["POST"],
                    name=method_name,
                )

    def health_check():
        return http.HTTPStatus.OK.phrase

    app.add_api_route("/healthCheck", endpoint=health_check, methods=["GET"], name="health_check")

    return app
