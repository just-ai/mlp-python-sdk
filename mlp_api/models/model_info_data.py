# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from mlp_api.models.data_image_mount_data import DataImageMountData
from mlp_api.models.dataset_info_data import DatasetInfoData
from mlp_api.models.fit_config_data import FitConfigData
from mlp_api.models.image_info_data import ImageInfoData
from mlp_api.models.model_batches_data import ModelBatchesData
from mlp_api.models.model_info_pk import ModelInfoPK
from mlp_api.models.model_limits_data import ModelLimitsData
from mlp_api.models.model_public_settings_data import ModelPublicSettingsData
from mlp_api.models.model_retries_data import ModelRetriesData
from mlp_api.models.model_timeouts_data import ModelTimeoutsData
from mlp_api.models.persistent_volume_data import PersistentVolumeData

class ModelInfoData(BaseModel):
    """
    ModelInfoData
    """
    id: ModelInfoPK = Field(...)
    model_account_name: Optional[StrictStr] = Field(None, alias="modelAccountName")
    model_account_display_name: Optional[StrictStr] = Field(None, alias="modelAccountDisplayName")
    model_name: StrictStr = Field(..., alias="modelName")
    image_account_id: StrictInt = Field(..., alias="imageAccountId")
    image_id: Optional[StrictInt] = Field(None, alias="imageId")
    image: Optional[ImageInfoData] = None
    model_group_id: Optional[StrictInt] = Field(None, alias="modelGroupId")
    model_group_name: Optional[StrictStr] = Field(None, alias="modelGroupName")
    training_dataset_account_id: Optional[StrictInt] = Field(None, alias="trainingDatasetAccountId")
    training_dataset_id: Optional[StrictInt] = Field(None, alias="trainingDatasetId")
    training_dataset: Optional[DatasetInfoData] = Field(None, alias="trainingDataset")
    training_dataset_type: Optional[StrictStr] = Field(None, alias="trainingDatasetType")
    training_fit_config_id: Optional[StrictInt] = Field(None, alias="trainingFitConfigId")
    training_fit_config: Optional[FitConfigData] = Field(None, alias="trainingFitConfig")
    fit_template_model_id: Optional[StrictInt] = Field(None, alias="fitTemplateModelId")
    composite: StrictBool = Field(...)
    task_type: Optional[StrictStr] = Field(None, alias="taskType")
    training_model_account_id: Optional[StrictInt] = Field(None, alias="trainingModelAccountId")
    training_model_id: Optional[StrictInt] = Field(None, alias="trainingModelId")
    training_type: Optional[StrictStr] = Field(None, alias="trainingType")
    config: Optional[StrictStr] = None
    env: Optional[StrictStr] = None
    fittable: StrictBool = Field(...)
    hosting_type: StrictStr = Field(..., alias="hostingType")
    persistent_volumes: conlist(PersistentVolumeData) = Field(..., alias="persistentVolumes")
    data_image_mounts: conlist(DataImageMountData) = Field(..., alias="dataImageMounts")
    resource_group: Optional[StrictStr] = Field(None, alias="resourceGroup")
    timeouts: ModelTimeoutsData = Field(...)
    resource_limits: ModelLimitsData = Field(..., alias="resourceLimits")
    retries_config: ModelRetriesData = Field(..., alias="retriesConfig")
    batches_config: ModelBatchesData = Field(..., alias="batchesConfig")
    short_description: Optional[StrictStr] = Field(None, alias="shortDescription")
    languages: Optional[conlist(StrictStr, unique_items=True)] = None
    min_instances_count: Optional[StrictInt] = Field(None, alias="minInstancesCount")
    public_settings: ModelPublicSettingsData = Field(..., alias="publicSettings")
    restricted_image_access: StrictBool = Field(..., alias="restrictedImageAccess")
    last_activity: Optional[StrictInt] = Field(None, alias="lastActivity")
    favorite: StrictBool = Field(...)
    state: Optional[StrictStr] = None
    __properties = ["id", "modelAccountName", "modelAccountDisplayName", "modelName", "imageAccountId", "imageId", "image", "modelGroupId", "modelGroupName", "trainingDatasetAccountId", "trainingDatasetId", "trainingDataset", "trainingDatasetType", "trainingFitConfigId", "trainingFitConfig", "fitTemplateModelId", "composite", "taskType", "trainingModelAccountId", "trainingModelId", "trainingType", "config", "env", "fittable", "hostingType", "persistentVolumes", "dataImageMounts", "resourceGroup", "timeouts", "resourceLimits", "retriesConfig", "batchesConfig", "shortDescription", "languages", "minInstancesCount", "publicSettings", "restrictedImageAccess", "lastActivity", "favorite", "state"]

    @validator('training_type')
    def training_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('singleContainer', 'multipleFit'):
            raise ValueError("must be one of enum values ('singleContainer', 'multipleFit')")
        return value

    @validator('hosting_type')
    def hosting_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('EXTERNAL', 'INTERNAL'):
            raise ValueError("must be one of enum values ('EXTERNAL', 'INTERNAL')")
        return value

    @validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('RUNNING', 'STARTING', 'INACTIVE'):
            raise ValueError("must be one of enum values ('RUNNING', 'STARTING', 'INACTIVE')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ModelInfoData:
        """Create an instance of ModelInfoData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of training_dataset
        if self.training_dataset:
            _dict['trainingDataset'] = self.training_dataset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of training_fit_config
        if self.training_fit_config:
            _dict['trainingFitConfig'] = self.training_fit_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in persistent_volumes (list)
        _items = []
        if self.persistent_volumes:
            for _item in self.persistent_volumes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['persistentVolumes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in data_image_mounts (list)
        _items = []
        if self.data_image_mounts:
            for _item in self.data_image_mounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dataImageMounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of timeouts
        if self.timeouts:
            _dict['timeouts'] = self.timeouts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_limits
        if self.resource_limits:
            _dict['resourceLimits'] = self.resource_limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retries_config
        if self.retries_config:
            _dict['retriesConfig'] = self.retries_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of batches_config
        if self.batches_config:
            _dict['batchesConfig'] = self.batches_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public_settings
        if self.public_settings:
            _dict['publicSettings'] = self.public_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelInfoData:
        """Create an instance of ModelInfoData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelInfoData.parse_obj(obj)

        _obj = ModelInfoData.parse_obj({
            "id": ModelInfoPK.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "model_account_name": obj.get("modelAccountName"),
            "model_account_display_name": obj.get("modelAccountDisplayName"),
            "model_name": obj.get("modelName"),
            "image_account_id": obj.get("imageAccountId"),
            "image_id": obj.get("imageId"),
            "image": ImageInfoData.from_dict(obj.get("image")) if obj.get("image") is not None else None,
            "model_group_id": obj.get("modelGroupId"),
            "model_group_name": obj.get("modelGroupName"),
            "training_dataset_account_id": obj.get("trainingDatasetAccountId"),
            "training_dataset_id": obj.get("trainingDatasetId"),
            "training_dataset": DatasetInfoData.from_dict(obj.get("trainingDataset")) if obj.get("trainingDataset") is not None else None,
            "training_dataset_type": obj.get("trainingDatasetType"),
            "training_fit_config_id": obj.get("trainingFitConfigId"),
            "training_fit_config": FitConfigData.from_dict(obj.get("trainingFitConfig")) if obj.get("trainingFitConfig") is not None else None,
            "fit_template_model_id": obj.get("fitTemplateModelId"),
            "composite": obj.get("composite"),
            "task_type": obj.get("taskType"),
            "training_model_account_id": obj.get("trainingModelAccountId"),
            "training_model_id": obj.get("trainingModelId"),
            "training_type": obj.get("trainingType"),
            "config": obj.get("config"),
            "env": obj.get("env"),
            "fittable": obj.get("fittable"),
            "hosting_type": obj.get("hostingType"),
            "persistent_volumes": [PersistentVolumeData.from_dict(_item) for _item in obj.get("persistentVolumes")] if obj.get("persistentVolumes") is not None else None,
            "data_image_mounts": [DataImageMountData.from_dict(_item) for _item in obj.get("dataImageMounts")] if obj.get("dataImageMounts") is not None else None,
            "resource_group": obj.get("resourceGroup"),
            "timeouts": ModelTimeoutsData.from_dict(obj.get("timeouts")) if obj.get("timeouts") is not None else None,
            "resource_limits": ModelLimitsData.from_dict(obj.get("resourceLimits")) if obj.get("resourceLimits") is not None else None,
            "retries_config": ModelRetriesData.from_dict(obj.get("retriesConfig")) if obj.get("retriesConfig") is not None else None,
            "batches_config": ModelBatchesData.from_dict(obj.get("batchesConfig")) if obj.get("batchesConfig") is not None else None,
            "short_description": obj.get("shortDescription"),
            "languages": obj.get("languages"),
            "min_instances_count": obj.get("minInstancesCount"),
            "public_settings": ModelPublicSettingsData.from_dict(obj.get("publicSettings")) if obj.get("publicSettings") is not None else None,
            "restricted_image_access": obj.get("restrictedImageAccess"),
            "last_activity": obj.get("lastActivity"),
            "favorite": obj.get("favorite"),
            "state": obj.get("state")
        })
        return _obj

