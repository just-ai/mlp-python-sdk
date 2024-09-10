from typing import List

from pydantic import BaseModel

from mlp_sdk.abstract.task import Task
from mlp_sdk.abstract.task_mixin import BatchPredictableMixin
from mlp_sdk.types import InflectorConformerTextsCollectionTest, InflectorTextsCollection


class MyTaskPredictConfigSchema(BaseModel):
    lang: str
    engine: str


class MyCustomTask(Task):
    def predict(
        self,
        data: InflectorConformerTextsCollectionTest,
        config: MyTaskPredictConfigSchema,
    ) -> InflectorTextsCollection:
        result = InflectorTextsCollection(texts=[], tags=[])
        result.texts.append("Done")
        return result


class MyCustomTaskWithBatch(Task, BatchPredictableMixin):
    def predict(
        self,
        data: InflectorConformerTextsCollectionTest,
        config: MyTaskPredictConfigSchema,
    ) -> InflectorTextsCollection:
        result = InflectorTextsCollection(texts=[], tags=[])
        result.texts.append("Done")
        return result

    def predict_batch(
        self, data: List[InflectorConformerTextsCollectionTest], config: MyTaskPredictConfigSchema
    ) -> List[InflectorTextsCollection]:
        result = [InflectorTextsCollection(texts=["Done"], tags=[]) for _ in range(2)]
        return result


def test_simple_config():
    task = MyCustomTask(config=BaseModel())
    print(
        task.predict(
            InflectorConformerTextsCollectionTest(texts=[], tags=[], numbers=[]),
            config=MyTaskPredictConfigSchema(lang="ru", engine="spacy"),
        )
    )


def test_simple_config_with_batch():
    task = MyCustomTaskWithBatch(config=BaseModel())
    print(
        task.predict_batch(
            [InflectorConformerTextsCollectionTest(texts=[], tags=[], numbers=[])],
            config=MyTaskPredictConfigSchema(lang="ru", engine="spacy"),
        )
    )
