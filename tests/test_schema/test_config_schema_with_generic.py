from pydantic import BaseModel
from typing import List

from caila_sdk.abstract.task import Task
from caila_sdk.types import InflectorConformerTextsCollectionTest, InflectorTextsCollection


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

    def predict(
            self,
            data: InflectorConformerTextsCollectionTest,
            config: NerPredictConfigSchema,
    ) -> InflectorTextsCollection:

        result = InflectorTextsCollection(texts=[], tags=[])
        result.texts.append("Done")
        return result


def test_simple_config():
    task = MyCustomTask(config=BaseModel())
    predict_schema = NerPredictConfigSchema(
        lang="zh",
        engines=["duckling", "chn"],
        systemEntities=SystemEntities(
            entities=[Entity(name="duckling.number", version="v2")]
        ),
        params=ParamsType(
            duckling_context=DucklingContext(locale="zh_ZH")
        )

    )
    task.predict(InflectorConformerTextsCollectionTest(texts=[], tags=[], numbers=[]), config=predict_schema)

    print(MyCustomTask.get_schema())
    print(MyCustomTask.get_descriptor())
