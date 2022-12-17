from typing import Type

from pydantic import BaseModel

from caila_sdk.abstract.task import Task
from caila_sdk.abstract.task_mixin import WithIndexedDataMixin
from caila_sdk.types import Item, ScoredItems, FlagsCollection, ItemsCollection, ScoredItemsCollection, TextsCollection
from caila_sdk.hosting.host import host


class MyCustomPredictSchema(BaseModel):
    top_n: int


class MyCustomTask(Task, WithIndexedDataMixin):
    @property
    def init_config_schema(self) -> Type[BaseModel]:
        return BaseModel

    def _predict(self, data: TextsCollection, config: MyCustomPredictSchema) -> ScoredItemsCollection:
        result = ScoredItemsCollection(items_list=[ScoredItems(items=[Item(value="prediction")], scores=[0.99])])
        return result

    def add_data(self, data: TextsCollection, ids: ItemsCollection) -> None:
        print("Add data done")

    def remove_data(self, data_ids: ItemsCollection) -> None:
        print("Remove data done")

    def get_data(self, data_ids: ItemsCollection) -> TextsCollection:
        result = TextsCollection(texts=["test text"])
        return result

    def has_data(self, data_ids: ItemsCollection) -> FlagsCollection:
        return FlagsCollection(flags=[True, False])

    @property
    def is_initialized(self) -> bool:
        return True


if __name__ == "__main__":
    host(MyCustomTask, BaseModel(), 5000)
