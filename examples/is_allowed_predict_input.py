from typing import Type

from pydantic import BaseModel

from mlp_sdk.abstract.task import Task
from mlp_sdk.types import InflectorTextsCollection, ScoredItemsCollection


class MyCustomTaskInitSchema(BaseModel):
    language: str


class MyCustomTask(Task):
    def __init__(self, config: MyCustomTaskInitSchema) -> None:
        super().__init__(config)
        self.language = config.language

    @property
    def init_config_schema(self) -> Type[BaseModel]:
        return MyCustomTaskInitSchema

    def predict(self, data: InflectorTextsCollection, config: BaseModel) -> str:
        return f"Done for language: {self.language}"

    @property
    def predict_config_schema(self) -> Type[BaseModel]:
        return BaseModel


if __name__ == "__main__":
    task = MyCustomTask(config=MyCustomTaskInitSchema(language="ru"))
    print(task.predict(InflectorTextsCollection(texts=[], tags=[]), config=BaseModel()))
    # Raises
    print(task.predict(ScoredItemsCollection(items_list=[]), config=BaseModel()))
