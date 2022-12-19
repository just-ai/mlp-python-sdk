import sys
from typing import Type

from pydantic import BaseModel

from caila_sdk.abstract import Task
from caila_sdk.hosting.host import host_caila_cloud_gate
from caila_sdk.types import Items, Item, TextsCollection


class MyCustomPredictSchema(BaseModel):
    top_n: int


class MyCustomTask(Task):
    @property
    def init_config_schema(self) -> Type[BaseModel]:
        return BaseModel

    def predict(self, data: TextsCollection, config: BaseModel) -> Items:
        result = Items(items=[Item("a")] * len(data.texts))
        return result


if __name__ == '__main__':
    url = sys.argv[1]
    token = sys.argv[2]
    host_caila_cloud_gate(task=MyCustomTask, params=BaseModel(), url=url, connection_token=token)
