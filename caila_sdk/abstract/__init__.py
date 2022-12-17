from typing import Union

from .task import Task
from .task_mixin import IsLearnableMixin, UpdatableMixin, BatchPredictableMixin

TASK_TYPE = Union[
    Task,
    IsLearnableMixin,
    UpdatableMixin,
    BatchPredictableMixin,
]
