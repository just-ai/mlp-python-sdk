import sys
import threading
from typing import Type

from pydantic import BaseModel

from mlp_sdk.abstract import Task
from mlp_sdk.hosting.host import host_mlp_cloud
from mlp_sdk.types import Items, Item, TextsCollection
from mlp_sdk.transport.MlpServiceSDK import MlpResponseHeaders

class MyCustomPredictSchema(BaseModel):
    top_n: int


class MyCustomTask(Task):
    @property
    def init_config_schema(self) -> Type[BaseModel]:
        return BaseModel

    def predict(self, data: TextsCollection, config: BaseModel) -> Items:
        items = [Item(value="a")] * len(data.texts)
        result = Items(items=items)

        MlpResponseHeaders.headers["Z-custom-billing"] = "101"

        return result


if __name__ == '__main__':
    host_mlp_cloud(task=MyCustomTask, params=BaseModel())
