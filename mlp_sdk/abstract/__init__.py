from typing import Union

from .task import Task
from .task_mixin import LearnableMixin, UpdatableMixin, BatchPredictableMixin

TASK_TYPE = Union[
    Task,
    LearnableMixin,
    UpdatableMixin,
    BatchPredictableMixin,
]
