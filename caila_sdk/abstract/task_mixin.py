from abc import abstractmethod
from inspect import signature
from typing import Type, List, get_args

from pydantic import BaseModel

from caila_sdk.abstract.task import ABCTask
from caila_sdk.abstract.task_utils import is_allowed_input_type


class IsLearnableMixin(ABCTask):
    __METHODS = [
        '_fit',
        'prune_state',
    ]
    __IS_LEARNABLE = True

    def _check_fit_input_types(
            self,
            train_data: BaseModel,
            targets: BaseModel,
            model_dir: str,
            previous_model_dir: str,
    ) -> None:
        if not is_allowed_input_type(type(self), "_fit", "train_data", type(train_data)):
            raise RuntimeError()
        if not is_allowed_input_type(type(self), "_fit", "targets", type(targets)):
            raise RuntimeError()
        if not is_allowed_input_type(type(self), "_fit", "model_dir", type(model_dir)):
            raise RuntimeError()
        if not is_allowed_input_type(type(self), "_fit", "previous_model_dir", type(previous_model_dir)):
            raise RuntimeError()

    @abstractmethod
    def _fit(
            self,
            train_data: BaseModel,
            targets: BaseModel,
            config: BaseModel,
            model_dir: str,
            previous_model_dir: str,

    ) -> None:
        pass

    def fit(
            self,
            train_data: BaseModel,
            targets: BaseModel,
            config: BaseModel,
            model_dir: str = '',
            previous_model_dir: str = '',
    ) -> None:
        self._check_config_validness(config, "fit")
        self._check_fit_input_types(train_data, targets, model_dir, previous_model_dir)
        self._fit(train_data, targets, config, model_dir, previous_model_dir)
        self._save_state()

    @classmethod
    def get_fit_config_schema(cls) -> Type[BaseModel]:
        return signature(getattr(cls, "_fit")).parameters["config"].annotation

    @abstractmethod
    def _save_state(self) -> None:
        pass

    @abstractmethod
    def _load_state(self) -> None:
        pass

    @abstractmethod
    def prune_state(self, model_dir: str = '') -> None:
        pass

    @property
    @abstractmethod
    def is_fitted(self) -> bool:
        pass


class UpdatableMixin(ABCTask):
    __METHODS = [
        '_update',
    ]
    __IS_LEARNABLE = False

    @abstractmethod
    def _update(self, config: BaseModel) -> None:
        pass

    def update(self, config: BaseModel) -> None:
        self._check_config_validness(config, "update")
        self._update(config)

    @classmethod
    def get_update_config_schema(cls) -> Type[BaseModel]:
        return signature(getattr(cls, "_update")).parameters["config"].annotation


class BatchPredictableMixin(ABCTask):
    __METHODS = [
        '_predict_batch'
    ]

    @property
    def is_batch_predictable(self):
        return True

    def _check_predict_batch_input_type(self, data: List[BaseModel]) -> None:
        data_annotation_type = signature(getattr(type(self), "_predict_batch")).parameters["data"].annotation
        inner_value = get_args(data_annotation_type)[0]
        if not type(data) == list:
            raise RuntimeError("Expected data annotation is List[BaseModel].")
        else:
            for data_el in data:
                if data_el.schema()["title"] != inner_value.schema()["title"]:
                    raise RuntimeError(f"Expected List[{inner_value.schema()['title']}] "
                                       "found input with type {data_el.schema()['title']}")
            if not is_allowed_input_type(type(self), "_predict_batch", "data", type(data[0])):
                raise RuntimeError

    def predict_batch(self, data: List[BaseModel], config: List[BaseModel]) -> List[BaseModel]:
        self._check_config_validness(config, "predict_batch")
        self._check_predict_batch_input_type(data)
        return self._predict_batch(data, config)

    @abstractmethod
    def _predict_batch(self, data: List[BaseModel], config: List[BaseModel]) -> List[BaseModel]:
        pass

    @classmethod
    def get_predict_batch_config_schema(cls) -> Type[BaseModel]:
        return signature(getattr(cls, "_predict_batch")).parameters["config"].annotation
