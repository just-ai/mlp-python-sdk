from abc import abstractmethod
from inspect import signature
from typing import Type

from pydantic import BaseModel

from mpl_sdk.transport import MplActionSDK
from mpl_sdk.abstract.abc_task import ABCTask
from mpl_sdk.abstract.task_utils import is_allowed_input_type


class Task(ABCTask):
    __METHODS = [
        '__init__',
        'predict',
    ]
    __IS_LEARNABLE = False

    def __init__(self, config: BaseModel, action_sdk: MplActionSDK = None) -> None:
        self.pipeline_client = action_sdk.pipeline_client if action_sdk else None
        self._check_config_validness(config, "init")

    @classmethod
    def get_init_config_schema(cls) -> Type[BaseModel]:
        return signature(getattr(cls, "__init__")).parameters["config"].annotation

    def _check_predict_input_type(self, data: BaseModel) -> None:
        if not is_allowed_input_type(type(self), "predict", "data", type(data)):
            raise RuntimeError

    def pre_predict(self, data: BaseModel, config: BaseModel) -> None:
        self._check_config_validness(config, "predict")
        self._check_predict_input_type(data)

    @abstractmethod
    def predict(self, data: BaseModel, config: BaseModel) -> BaseModel:
        pass

    @classmethod
    def get_predict_config_schema(cls) -> Type[BaseModel]:
        return signature(getattr(cls, "predict")).parameters["config"].annotation
