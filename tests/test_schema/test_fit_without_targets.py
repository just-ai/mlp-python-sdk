from pydantic import BaseModel

from mlp_sdk.abstract.task_mixin import LearnableMixin
from mlp_sdk.types import DatasetInfo, ServiceInfo, TextsCollection


class FitConfigSchema(BaseModel):
    fit_param_1: str


class MyTaskLearnableMixin(LearnableMixin):
    def _save_state(self) -> None:
        pass

    def _load_state(self) -> None:
        pass

    def prune_state(self, model_dir: str) -> None:
        pass

    def fit(
        self,
        train_data: TextsCollection,
        targets: BaseModel,
        config: FitConfigSchema,
        target_service_info: ServiceInfo,
        dataset_info: DatasetInfo,
        model_dir: str,
        previous_model_dir: str = "",
    ) -> None:
        pass

    @property
    def is_fitted(self) -> bool:
        return True


def test_fit_without_targets():
    task = MyTaskLearnableMixin()
    train_data = TextsCollection(texts=["test1"])
    config = FitConfigSchema(fit_param_1="test")
    service_info = ServiceInfo(accountId=12, modelId=32, modelName="name", authToken="token", bucketName="bucket")
    dataset_info = DatasetInfo(accountId=12, datasetId=32, name="name", type="json")

    task.fit(train_data, None, config, service_info, dataset_info, "test", "")
