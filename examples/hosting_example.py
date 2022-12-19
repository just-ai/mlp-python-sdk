from typing import List, Type
from pydantic import BaseModel

from mpl_sdk.abstract.task import Task
from mpl_sdk.types import InflectorTextsCollection, TextsCollection
from mpl_sdk.hosting.host import host


class DucklingContext(BaseModel):
    locale: str


class ParamsType(BaseModel):
    duckling_context: DucklingContext


class Entity(BaseModel):
    name: str
    version = "v1"


class SystemEntities(BaseModel):
    entities: List[Entity]


class NerPredictConfigSchema(BaseModel):
    lang: str
    engines: List[str]
    params: ParamsType
    systemEntities: SystemEntities


class MyCustomTask(Task):

    @property
    def init_config_schema(self) -> Type[BaseModel]:
        return BaseModel

    def predict(self, data: InflectorTextsCollection, config: NerPredictConfigSchema) -> TextsCollection:
        result = TextsCollection(texts=[])
        result.texts.append("Done")
        return result

    @property
    def predict_config_schema(self) -> Type[BaseModel]:
        return NerPredictConfigSchema


if __name__ == "__main__":
    host(MyCustomTask, BaseModel(), 5000)
