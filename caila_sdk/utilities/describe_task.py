from inspect import signature
from typing import Union, Type

from caila_sdk.abstract.task import Task
from caila_sdk.abstract.task_mixin import IsLearnableMixin, WithIndexedDataMixin, WithLoadableDataMixin, UpdatableMixin

TASK_TYPES = Type[
    Union[
        Task,
        IsLearnableMixin,
        WithIndexedDataMixin,
        WithLoadableDataMixin,
        UpdatableMixin
    ]
]


def describe_task(task: TASK_TYPES):
    predict_data_type = signature(getattr(task, "_predict")).parameters["data"].annotation
    predict_config_type = task.get_predict_config_schema()
    predict_return_type = signature(getattr(task, "_predict")).return_annotation
    task_signature = {
        "predict": {
            "args": {"data": predict_data_type},
            "config": predict_config_type,
            "return": predict_return_type,
        }
    }

    if issubclass(task, IsLearnableMixin):
        fit_inputs_type = signature(getattr(task, "_fit")).parameters["train_data"].annotation
        fit_targets_type = signature(getattr(task, "_fit")).parameters["targets"].annotation
        fit_model_id_type = signature(getattr(task, "_fit")).parameters["model_id"].annotation

        fit_config_type = task.get_fit_config_schema()
        fit_return_type = signature(getattr(task, "_fit")).return_annotation

        task_signature["fit"] = {
            "args": {"train_data": fit_inputs_type, "targets": fit_targets_type, "model_id": fit_model_id_type},
            "config": fit_config_type,
            "return": fit_return_type,
        }

    if issubclass(task, WithIndexedDataMixin):
        add_data_data_type = signature(getattr(task, "add_data")).parameters["data"].annotation
        add_data_ids_type = signature(getattr(task, "add_data")).parameters["ids"].annotation
        task_signature["add_data"] = {
            "args": {"data": add_data_data_type, "ids": add_data_ids_type},
            "return": None,
        }

        remove_data_data_ids_type = signature(getattr(task, "remove_data")).parameters["data_ids"].annotation
        task_signature["remove_data"] = {
            "args": {"data_ids": remove_data_data_ids_type},
            "return": None,
        }

        has_data_data_ids_type = signature(getattr(task, "has_data")).parameters["data_ids"].annotation
        has_data_return_type = signature(getattr(task, "has_data")).return_annotation
        task_signature["has_data"] = {
            "args": {"data_ids": has_data_data_ids_type},
            "return": has_data_return_type,
        }

        get_data_data_ids_type = signature(getattr(task, "get_data")).parameters["data_ids"].annotation
        get_data_return_type = signature(getattr(task, "get_data")).return_annotation
        task_signature["get_data"] = {
            "args": {"data_ids": get_data_data_ids_type},
            "return": get_data_return_type,
        }

    if issubclass(task, UpdatableMixin):
        update_config_type = task.get_update_config_schema()
        update_return_type = signature(getattr(task, "_update"))
        task_signature["update"] = {
            "config": update_config_type,
            "return": update_return_type
        }

    return task_signature
