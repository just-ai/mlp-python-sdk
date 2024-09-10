from typing import List

from pydantic import BaseModel

from mlp_sdk.abstract.task import Task
from mlp_sdk.abstract.task_mixin import BatchPredictableMixin, LearnableMixin, UpdatableMixin
from mlp_sdk.grpc.mlp_grpc_pb2 import MethodDescriptorProto, ParamDescriptorProto, ServiceDescriptorProto
from mlp_sdk.types import DatasetInfo, ItemsCollection, ScoredItemsCollection, ServiceInfo, TextsCollection


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

    def prune_state(self, model_dir: str = "") -> None:
        pass

    def _load_state(self) -> None:
        pass

    def fit(
        self,
        train_data: TextsCollection,
        targets: ItemsCollection,
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


class MyTaskWithBatchPredictableMixin(BatchPredictableMixin):
    def predict_batch(self, data: List[TextsCollection], config: PredictConfigSchema) -> List[ScoredItemsCollection]:
        pass


class MyTaskWithUpdatableMixin(UpdatableMixin):
    def update(self, config: InitConfigSchema) -> None:
        pass


class MySuperTask(MyTask, MyTaskLearnableMixin, MyTaskWithBatchPredictableMixin, MyTaskWithUpdatableMixin):
    pass


def test_task_descriptor():
    assert MyTask.get_descriptor() == ServiceDescriptorProto(
        name="MyTask",
        fittable=False,
        methods={
            "init": MethodDescriptorProto(
                input={"config": ParamDescriptorProto(type="InitConfigSchema")},
                output=ParamDescriptorProto(type="null"),
            ),
            "predict": MethodDescriptorProto(
                input={
                    "config": ParamDescriptorProto(type="PredictConfigSchema"),
                    "data": ParamDescriptorProto(type="TextsCollection"),
                },
                output=ParamDescriptorProto(type="ScoredItemsCollection"),
            ),
        },
        schemaFiles={
            "schema": "init:\n  config:\n    properties:\n      init_param_1:\n        title: Init Param 1\n        type: boolean\n      init_param_2:\n        title: Init Param 2\n        type: string\n      init_param_3:\n        items:\n          type: string\n        title: Init Param 3\n        type: array\n    required:\n    - init_param_1\n    - init_param_2\n    - init_param_3\n    title: InitConfigSchema\n    type: object\n  return: null\npredict:\n  config:\n    properties:\n      predict_param_1:\n        title: Predict Param 1\n        type: boolean\n      predict_param_2:\n        title: Predict Param 2\n        type: string\n      predict_param_3:\n        items:\n          type: string\n        title: Predict Param 3\n        type: array\n    required:\n    - predict_param_1\n    - predict_param_2\n    - predict_param_3\n    title: PredictConfigSchema\n    type: object\n  data:\n    properties:\n      texts:\n        items:\n          type: string\n        title: Texts\n        type: array\n    required:\n    - texts\n    title: TextsCollection\n    type: object\n  return:\n    definitions:\n      Item:\n        properties:\n          value:\n            title: Value\n            type: string\n        required:\n        - value\n        title: Item\n        type: object\n      ScoredItems:\n        properties:\n          items:\n            items:\n              $ref: '#/definitions/Item'\n            title: Items\n            type: array\n          scores:\n            items:\n              type: number\n            title: Scores\n            type: array\n        required:\n        - items\n        - scores\n        title: ScoredItems\n        type: object\n    properties:\n      items_list:\n        items:\n          $ref: '#/definitions/ScoredItems'\n        title: Items List\n        type: array\n    required:\n    - items_list\n    title: ScoredItemsCollection\n    type: object\n"  # noqa: E501
        },
    )


def test_batch_task_descriptor():
    assert MyTaskWithBatchPredictableMixin.get_descriptor() == ServiceDescriptorProto(
        name="MyTaskWithBatchPredictableMixin",
        fittable=False,
        methods={
            "predict_batch": MethodDescriptorProto(
                input={
                    "config": ParamDescriptorProto(type="PredictConfigSchema"),
                    "data": ParamDescriptorProto(type="array TextsCollection"),
                },
                output=ParamDescriptorProto(type="array ScoredItemsCollection"),
            ),
        },
        schemaFiles={
            "schema": "predict_batch:\n  config:\n    properties:\n      predict_param_1:\n        title: Predict Param 1\n        type: boolean\n      predict_param_2:\n        title: Predict Param 2\n        type: string\n      predict_param_3:\n        items:\n          type: string\n        title: Predict Param 3\n        type: array\n    required:\n    - predict_param_1\n    - predict_param_2\n    - predict_param_3\n    title: PredictConfigSchema\n    type: object\n  data:\n    definitions:\n      TextsCollection:\n        properties:\n          texts:\n            items:\n              type: string\n            title: Texts\n            type: array\n        required:\n        - texts\n        title: TextsCollection\n        type: object\n    items:\n      $ref: '#/definitions/TextsCollection'\n    type: array\n  return:\n    definitions:\n      ScoredItemsCollection:\n        definitions:\n          Item:\n            properties:\n              value:\n                title: Value\n                type: string\n            required:\n            - value\n            title: Item\n            type: object\n          ScoredItems:\n            properties:\n              items:\n                items:\n                  $ref: '#/definitions/Item'\n                title: Items\n                type: array\n              scores:\n                items:\n                  type: number\n                title: Scores\n                type: array\n            required:\n            - items\n            - scores\n            title: ScoredItems\n            type: object\n        properties:\n          items_list:\n            items:\n              $ref: '#/definitions/ScoredItems'\n            title: Items List\n            type: array\n        required:\n        - items_list\n        title: ScoredItemsCollection\n        type: object\n    items:\n      $ref: '#/definitions/ScoredItemsCollection'\n    type: array\n"  # noqa: E501
        },
    )


def test_fit_descriptor():
    assert MyTaskLearnableMixin.get_descriptor() == ServiceDescriptorProto(
        name="MyTaskLearnableMixin",
        fittable=True,
        methods={
            "fit": MethodDescriptorProto(
                input={
                    "config": ParamDescriptorProto(type="FitConfigSchema"),
                    "train_data": ParamDescriptorProto(type="TextsCollection"),
                    "targets": ParamDescriptorProto(type="ItemsCollection"),
                    "target_service_info": ParamDescriptorProto(type="ServiceInfo"),
                    "dataset_info": ParamDescriptorProto(type="DatasetInfo"),
                    "model_dir": ParamDescriptorProto(type="str"),
                    "previous_model_dir": ParamDescriptorProto(type="str"),
                },
                output=ParamDescriptorProto(type="null"),
            ),
            "prune_state": MethodDescriptorProto(
                input={"model_dir": ParamDescriptorProto(type="str")},
                output=ParamDescriptorProto(type="null"),
            ),
        },
        schemaFiles={
            "schema": "fit:\n  config:\n    properties:\n      fit_param_1:\n        title: Fit Param 1\n        type: boolean\n      fit_param_2:\n        title: Fit Param 2\n        type: string\n      fit_param_3:\n        items:\n          type: string\n        title: Fit Param 3\n        type: array\n    required:\n    - fit_param_1\n    - fit_param_2\n    - fit_param_3\n    title: FitConfigSchema\n    type: object\n  dataset_info:\n    properties:\n      accountId:\n        title: Accountid\n        type: integer\n      datasetId:\n        title: Datasetid\n        type: integer\n      name:\n        title: Name\n        type: string\n      type:\n        title: Type\n        type: string\n    required:\n    - accountId\n    - datasetId\n    - name\n    - type\n    title: DatasetInfo\n    type: object\n  model_dir:\n    title: str\n    type: string\n  previous_model_dir:\n    title: str\n    type: string\n  return: null\n  target_service_info:\n    properties:\n      accountId:\n        title: Accountid\n        type: integer\n      authToken:\n        title: Authtoken\n        type: string\n      bucketName:\n        title: Bucketname\n        type: string\n      modelId:\n        title: Modelid\n        type: integer\n      modelName:\n        title: Modelname\n        type: string\n    required:\n    - accountId\n    - modelId\n    - modelName\n    - authToken\n    title: ServiceInfo\n    type: object\n  targets:\n    definitions:\n      Item:\n        properties:\n          value:\n            title: Value\n            type: string\n        required:\n        - value\n        title: Item\n        type: object\n      Items:\n        properties:\n          items:\n            items:\n              $ref: '#/definitions/Item'\n            title: Items\n            type: array\n        required:\n        - items\n        title: Items\n        type: object\n    properties:\n      items_list:\n        items:\n          $ref: '#/definitions/Items'\n        title: Items List\n        type: array\n    required:\n    - items_list\n    title: ItemsCollection\n    type: object\n  train_data:\n    properties:\n      texts:\n        items:\n          type: string\n        title: Texts\n        type: array\n    required:\n    - texts\n    title: TextsCollection\n    type: object\nprune_state:\n  model_dir:\n    title: str\n    type: string\n  return: null\n"  # noqa: E501
        },
    )


def test_update_task_descriptor():
    assert MyTaskWithUpdatableMixin.get_descriptor() == ServiceDescriptorProto(
        name="MyTaskWithUpdatableMixin",
        fittable=False,
        methods={
            "update": MethodDescriptorProto(
                input={
                    "config": ParamDescriptorProto(type="InitConfigSchema"),
                },
                output=ParamDescriptorProto(type="null"),
            ),
        },
        schemaFiles={
            "schema": "update:\n  config:\n    properties:\n      init_param_1:\n        title: Init Param 1\n        type: boolean\n      init_param_2:\n        title: Init Param 2\n        type: string\n      init_param_3:\n        items:\n          type: string\n        title: Init Param 3\n        type: array\n    required:\n    - init_param_1\n    - init_param_2\n    - init_param_3\n    title: InitConfigSchema\n    type: object\n  return: null\n"  # noqa: E501
        },
    )


def test_overall_descriptor():
    assert MySuperTask.get_descriptor() == ServiceDescriptorProto(
        name="MySuperTask",
        fittable=True,
        methods={
            "init": MethodDescriptorProto(
                input={"config": ParamDescriptorProto(type="InitConfigSchema")},
                output=ParamDescriptorProto(type="null"),
            ),
            "predict": MethodDescriptorProto(
                input={
                    "config": ParamDescriptorProto(type="PredictConfigSchema"),
                    "data": ParamDescriptorProto(type="TextsCollection"),
                },
                output=ParamDescriptorProto(type="ScoredItemsCollection"),
            ),
            "predict_batch": MethodDescriptorProto(
                input={
                    "config": ParamDescriptorProto(type="PredictConfigSchema"),
                    "data": ParamDescriptorProto(type="array TextsCollection"),
                },
                output=ParamDescriptorProto(type="array ScoredItemsCollection"),
            ),
            "fit": MethodDescriptorProto(
                input={
                    "config": ParamDescriptorProto(type="FitConfigSchema"),
                    "train_data": ParamDescriptorProto(type="TextsCollection"),
                    "target_service_info": ParamDescriptorProto(type="ServiceInfo"),
                    "dataset_info": ParamDescriptorProto(type="DatasetInfo"),
                    "model_dir": ParamDescriptorProto(type="str"),
                    "previous_model_dir": ParamDescriptorProto(type="str"),
                    "targets": ParamDescriptorProto(type="ItemsCollection"),
                },
                output=ParamDescriptorProto(type="null"),
            ),
            "prune_state": MethodDescriptorProto(
                input={
                    "model_dir": ParamDescriptorProto(type="str"),
                },
                output=ParamDescriptorProto(type="null"),
            ),
            "update": MethodDescriptorProto(
                input={
                    "config": ParamDescriptorProto(type="InitConfigSchema"),
                },
                output=ParamDescriptorProto(type="null"),
            ),
        },
        schemaFiles={
            "schema": "fit:\n  config:\n    properties:\n      fit_param_1:\n        title: Fit Param 1\n        type: boolean\n      fit_param_2:\n        title: Fit Param 2\n        type: string\n      fit_param_3:\n        items:\n          type: string\n        title: Fit Param 3\n        type: array\n    required:\n    - fit_param_1\n    - fit_param_2\n    - fit_param_3\n    title: FitConfigSchema\n    type: object\n  dataset_info:\n    properties:\n      accountId:\n        title: Accountid\n        type: integer\n      datasetId:\n        title: Datasetid\n        type: integer\n      name:\n        title: Name\n        type: string\n      type:\n        title: Type\n        type: string\n    required:\n    - accountId\n    - datasetId\n    - name\n    - type\n    title: DatasetInfo\n    type: object\n  model_dir:\n    title: str\n    type: string\n  previous_model_dir:\n    title: str\n    type: string\n  return: null\n  target_service_info:\n    properties:\n      accountId:\n        title: Accountid\n        type: integer\n      authToken:\n        title: Authtoken\n        type: string\n      bucketName:\n        title: Bucketname\n        type: string\n      modelId:\n        title: Modelid\n        type: integer\n      modelName:\n        title: Modelname\n        type: string\n    required:\n    - accountId\n    - modelId\n    - modelName\n    - authToken\n    title: ServiceInfo\n    type: object\n  targets:\n    definitions:\n      Item:\n        properties:\n          value:\n            title: Value\n            type: string\n        required:\n        - value\n        title: Item\n        type: object\n      Items:\n        properties:\n          items:\n            items:\n              $ref: '#/definitions/Item'\n            title: Items\n            type: array\n        required:\n        - items\n        title: Items\n        type: object\n    properties:\n      items_list:\n        items:\n          $ref: '#/definitions/Items'\n        title: Items List\n        type: array\n    required:\n    - items_list\n    title: ItemsCollection\n    type: object\n  train_data: &id001\n    properties:\n      texts:\n        items:\n          type: string\n        title: Texts\n        type: array\n    required:\n    - texts\n    title: TextsCollection\n    type: object\ninit:\n  config: &id004\n    properties:\n      init_param_1:\n        title: Init Param 1\n        type: boolean\n      init_param_2:\n        title: Init Param 2\n        type: string\n      init_param_3:\n        items:\n          type: string\n        title: Init Param 3\n        type: array\n    required:\n    - init_param_1\n    - init_param_2\n    - init_param_3\n    title: InitConfigSchema\n    type: object\n  return: null\npredict:\n  config: &id002\n    properties:\n      predict_param_1:\n        title: Predict Param 1\n        type: boolean\n      predict_param_2:\n        title: Predict Param 2\n        type: string\n      predict_param_3:\n        items:\n          type: string\n        title: Predict Param 3\n        type: array\n    required:\n    - predict_param_1\n    - predict_param_2\n    - predict_param_3\n    title: PredictConfigSchema\n    type: object\n  data: *id001\n  return: &id003\n    definitions:\n      Item:\n        properties:\n          value:\n            title: Value\n            type: string\n        required:\n        - value\n        title: Item\n        type: object\n      ScoredItems:\n        properties:\n          items:\n            items:\n              $ref: '#/definitions/Item'\n            title: Items\n            type: array\n          scores:\n            items:\n              type: number\n            title: Scores\n            type: array\n        required:\n        - items\n        - scores\n        title: ScoredItems\n        type: object\n    properties:\n      items_list:\n        items:\n          $ref: '#/definitions/ScoredItems'\n        title: Items List\n        type: array\n    required:\n    - items_list\n    title: ScoredItemsCollection\n    type: object\npredict_batch:\n  config: *id002\n  data:\n    definitions:\n      TextsCollection: *id001\n    items:\n      $ref: '#/definitions/TextsCollection'\n    type: array\n  return:\n    definitions:\n      ScoredItemsCollection: *id003\n    items:\n      $ref: '#/definitions/ScoredItemsCollection'\n    type: array\nprune_state:\n  model_dir:\n    title: str\n    type: string\n  return: null\nupdate:\n  config: *id004\n  return: null\n"  # noqa: E501
        },
    )
