import yaml
from pydantic import BaseModel
from typing import List
from pathlib import Path

from mlp_sdk.abstract.task import Task
from mlp_sdk.abstract.task_mixin import LearnableMixin, BatchPredictableMixin, UpdatableMixin
from mlp_sdk.types import TextsCollection, ScoredItemsCollection, ItemsCollection, ServiceInfo, DatasetInfo


class InitConfigSchema(BaseModel):
    init_param_1: bool
    init_param_2: str
    init_param_3: List[str]


class PredictConfigSchema(BaseModel):
    predict_param_1: bool
    predict_param_2: str
    predict_param_3: List[str]


class FitConfigSchema(BaseModel):
    fit_param_1: bool
    fit_param_2: str
    fit_param_3: List[str]


class MyTask(Task):
    def __init__(self, config: InitConfigSchema) -> None:
        pass

    def predict(
            self,
            data: TextsCollection,
            config: PredictConfigSchema,
    ) -> ScoredItemsCollection:
        return ScoredItemsCollection(items_list=[])


class MyTaskLearnableMixin(LearnableMixin):
    def _save_state(self) -> None:
        pass

    def _load_state(self) -> None:
        pass

    def prune_state(self, model_dir: str = '') -> None:
        pass

    def fit(
            self,
            train_data: TextsCollection,
            targets: ItemsCollection,
            config: FitConfigSchema,
            target_service_info: ServiceInfo,
            dataset_info: DatasetInfo,
            model_dir: str = '',
            previous_model_dir: str = '',
    ) -> None:
        pass

    @property
    def is_fitted(self) -> bool:
        return True


class MyTaskWithBatchPredictableMixin(BatchPredictableMixin):
    def predict_batch(
            self, data: List[TextsCollection],
            config: PredictConfigSchema
    ) -> List[ScoredItemsCollection]:
        pass


class MyTaskWithUpdatableMixin(UpdatableMixin):
    def update(self, config: InitConfigSchema) -> None:
        pass


class MySuperTask(MyTask, MyTaskLearnableMixin, MyTaskWithBatchPredictableMixin, MyTaskWithUpdatableMixin):
    pass


def prettify(s):
    return yaml.dump(s, allow_unicode=True).strip()


def test_task_schema():
    with open(Path(__file__).parent.absolute() / 'test_data' / 'task_schema.yml') as fin:
        assert fin.read().strip() == prettify(MyTask.get_schema())


def test_fit_schema():
    with open(Path(__file__).parent.absolute() / 'test_data' / 'fit_schema.yml') as fin:
        assert fin.read().strip() == prettify(MyTaskLearnableMixin.get_schema())


def test_batch_schema():
    with open(Path(__file__).parent.absolute() / 'test_data' / 'batch_schema.yml') as fin:
        assert fin.read().strip() == prettify(MyTaskWithBatchPredictableMixin.get_schema())


def test_update_schema():
    with open(Path(__file__).parent.absolute() / 'test_data' / 'update_schema.yml') as fin:
        assert fin.read().strip() == prettify(MyTaskWithUpdatableMixin.get_schema())


def test_overall_schema():
    assert prettify({
        **MyTask.get_schema(),
        **MyTaskLearnableMixin.get_schema(),
        **MyTaskWithUpdatableMixin.get_schema(),
        **MyTaskWithBatchPredictableMixin.get_schema(),
    }) == prettify(MySuperTask.get_schema())
