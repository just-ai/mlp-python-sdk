from pydantic import BaseModel
from typing import List

from caila_gate.proto.gate_pb2 import ActionDescriptorProto, MethodDescriptorProto, ParamDescriptorProto

from mpl_sdk.abstract.task import Task
from mpl_sdk.abstract.task_mixin import LearnableMixin, BatchPredictableMixin, UpdatableMixin
from mpl_sdk.types import TextsCollection, ScoredItemsCollection, ItemsCollection


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

    def prune_state(self, model_dir: str = '') -> None:
        pass

    def _load_state(self) -> None:
        pass

    def fit(
            self,
            train_data: TextsCollection,
            targets: ItemsCollection,
            config: FitConfigSchema,
            model_dir: str,
            previous_model_dir: str,
    ) -> None:
        pass

    @property
    def is_fitted(self) -> bool:
        return True


class MyTaskWithBatchPredictableMixin(BatchPredictableMixin):
    def predict_batch(
            self, data: List[TextsCollection],
            config: List[PredictConfigSchema]
    ) -> List[ScoredItemsCollection]:
        pass


class MyTaskWithUpdatableMixin(UpdatableMixin):
    def update(self, config: InitConfigSchema) -> None:
        pass


class MySuperTask(MyTask, MyTaskLearnableMixin, MyTaskWithBatchPredictableMixin, MyTaskWithUpdatableMixin):
    pass


def test_task_descriptor():
    assert MyTask.get_descriptor() == ActionDescriptorProto(
        name='MyTask',
        fittable=False,
        methods={
            'init': MethodDescriptorProto(
                input={'config': ParamDescriptorProto(type='InitConfigSchema')},
                output=ParamDescriptorProto(type='null'),
            ),
            'predict': MethodDescriptorProto(
                input={
                    'config': ParamDescriptorProto(type='PredictConfigSchema'),
                    'data': ParamDescriptorProto(type='TextsCollection'),
                },
                output=ParamDescriptorProto(type='ScoredItemsCollection'),
            ),
        }
    )


def test_batch_task_descriptor():
    assert MyTaskWithBatchPredictableMixin.get_descriptor() == ActionDescriptorProto(
        name='MyTaskWithBatchPredictableMixin',
        fittable=False,
        methods={
            'predict_batch': MethodDescriptorProto(
                input={
                    'config': ParamDescriptorProto(type='array PredictConfigSchema'),
                    'data': ParamDescriptorProto(type='array TextsCollection'),
                },
                output=ParamDescriptorProto(type='array ScoredItemsCollection'),
            ),
        }
    )


def test_fit_descriptor():
    assert MyTaskLearnableMixin.get_descriptor() == ActionDescriptorProto(
        name='MyTaskLearnableMixin',
        fittable=True,
        methods={
            'fit': MethodDescriptorProto(
                input={
                    'config': ParamDescriptorProto(type='FitConfigSchema'),
                    'train_data': ParamDescriptorProto(type='TextsCollection'),
                    'targets': ParamDescriptorProto(type='ItemsCollection'),
                    'model_dir': ParamDescriptorProto(type='str'),
                    'previous_model_dir': ParamDescriptorProto(type='str'),
                },
                output=ParamDescriptorProto(type='null'),
            ),
            'prune_state': MethodDescriptorProto(
                input={
                    'model_dir': ParamDescriptorProto(type='str')
                },
                output=ParamDescriptorProto(type='null'),
            ),
        }
    )


def test_update_task_descriptor():
    assert MyTaskWithUpdatableMixin.get_descriptor() == ActionDescriptorProto(
        name='MyTaskWithUpdatableMixin',
        fittable=False,
        methods={
            'update': MethodDescriptorProto(
                input={
                    'config': ParamDescriptorProto(type='InitConfigSchema'),
                },
                output=ParamDescriptorProto(type='null'),
            ),
        }
    )


def test_overall_descriptor():
    assert MySuperTask.get_descriptor() == ActionDescriptorProto(
        name='MySuperTask',
        fittable=True,
        methods={
            'init': MethodDescriptorProto(
                input={'config': ParamDescriptorProto(type='InitConfigSchema')},
                output=ParamDescriptorProto(type='null'),
            ),
            'predict': MethodDescriptorProto(
                input={
                    'config': ParamDescriptorProto(type='PredictConfigSchema'),
                    'data': ParamDescriptorProto(type='TextsCollection'),
                },
                output=ParamDescriptorProto(type='ScoredItemsCollection'),
            ),
            'predict_batch': MethodDescriptorProto(
                input={
                    'config': ParamDescriptorProto(type='array PredictConfigSchema'),
                    'data': ParamDescriptorProto(type='array TextsCollection'),
                },
                output=ParamDescriptorProto(type='array ScoredItemsCollection'),
            ),
            'fit': MethodDescriptorProto(
                input={
                    'config': ParamDescriptorProto(type='FitConfigSchema'),
                    'train_data': ParamDescriptorProto(type='TextsCollection'),
                    'model_dir': ParamDescriptorProto(type='str'),
                    'previous_model_dir': ParamDescriptorProto(type='str'),
                    'targets': ParamDescriptorProto(type='ItemsCollection')
                },
                output=ParamDescriptorProto(type='null'),
            ),
            'prune_state': MethodDescriptorProto(
                input={
                    'model_dir': ParamDescriptorProto(type='str'),
                },
                output=ParamDescriptorProto(type='null'),
            ),
            'update': MethodDescriptorProto(
                input={
                    'config': ParamDescriptorProto(type='InitConfigSchema'),
                },
                output=ParamDescriptorProto(type='null'),
            ),
        }
    )
