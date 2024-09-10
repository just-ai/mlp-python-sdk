from typing import List, Type

import pytest
from pydantic import BaseModel, ValidationError

from mlp_sdk.abstract.task import Task
from mlp_sdk.types import InflectorConformerTextsCollectionTest, InflectorTextsCollection


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


class WrongSchema(BaseModel):
    param: int


class MyCustomTask(Task):
    @property
    def init_config_schema(self) -> Type[BaseModel]:
        return BaseModel

    def predict(
        self,
        data: InflectorConformerTextsCollectionTest,
        config: NerPredictConfigSchema,
    ) -> InflectorTextsCollection:
        result = InflectorTextsCollection()
        result.texts.append("Done")
        return result

    @property
    def predict_config_schema(self) -> Type[BaseModel]:
        return NerPredictConfigSchema


def test_simple_config():
    task = MyCustomTask(config=BaseModel())

    # CorrectSchema but empty: pydantic raises
    with pytest.raises(ValidationError):
        task.predict(
            InflectorConformerTextsCollectionTest(texts=[], tags=[], numbers=[]), config=NerPredictConfigSchema()
        )

    # Wrong schema
    with pytest.raises(RuntimeError):
        task.predict(InflectorConformerTextsCollectionTest(texts=[], tags=[], numbers=[]), config=WrongSchema(param=10))
