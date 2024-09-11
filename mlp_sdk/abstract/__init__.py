from typing import Union

from .task import Task
from .task_mixin import BatchPredictableMixin, LearnableMixin, UpdatableMixin

TASK_TYPE = Union[
    Task,
    LearnableMixin,
    UpdatableMixin,
    BatchPredictableMixin,
]
