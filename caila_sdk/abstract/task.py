from abc import abstractmethod
from inspect import signature
from typing import Type

from pydantic import BaseModel

from caila_sdk.transport.CailaActionSDK import PipelineClient
from caila_sdk.abstract.abc_task import ABCTask
from caila_sdk.abstract.task_utils import is_allowed_input_type


class Task(ABCTask):
    __METHODS = [
        '__init__',
        '_predict',
    ]
    __IS_LEARNABLE = False

    def __init__(self, config: BaseModel, pipeline_client: PipelineClient = None):
        self.pipeline_client = pipeline_client
        self._check_config_validness(config, "init")

    @classmethod
    def get_init_config_schema(cls) -> Type[BaseModel]:
        return signature(getattr(cls, "__init__")).parameters["config"].annotation

    def _check_predict_input_type(self, data: BaseModel) -> None:
        if not is_allowed_input_type(type(self), "_predict", "data", type(data)):
            raise RuntimeError

    def predict(self, data: BaseModel, config: BaseModel) -> BaseModel:
        self._check_config_validness(config, "predict")
        self._check_predict_input_type(data)
        return self._predict(data, config)

    @abstractmethod
    def _predict(self, data: BaseModel, config: BaseModel) -> BaseModel:
        pass

    @classmethod
    def get_predict_config_schema(cls) -> Type[BaseModel]:
        return signature(getattr(cls, "_predict")).parameters["config"].annotation
