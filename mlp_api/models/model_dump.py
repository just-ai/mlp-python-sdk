# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from mlp_api.models.data_image_mount_dump import DataImageMountDump
from mlp_api.models.document_dump import DocumentDump
from mlp_api.models.fit_config_dump import FitConfigDump
from mlp_api.models.model_archive_settings_data import ModelArchiveSettingsData
from mlp_api.models.model_auto_scaling_configuration import ModelAutoScalingConfiguration
from mlp_api.models.model_batches_data import ModelBatchesData
from mlp_api.models.model_billing_settings_data import ModelBillingSettingsData
from mlp_api.models.model_caching_data import ModelCachingData
from mlp_api.models.model_http_settings_data import ModelHttpSettingsData
from mlp_api.models.model_limits_data import ModelLimitsData
from mlp_api.models.model_priority_queue_data import ModelPriorityQueueData
from mlp_api.models.model_public_settings_data import ModelPublicSettingsData
from mlp_api.models.model_retries_data import ModelRetriesData
from mlp_api.models.model_timeouts_data import ModelTimeoutsData
from mlp_api.models.predict_config_dump import PredictConfigDump

class ModelDump(BaseModel):
    """
    ModelDump
    """
    name: StrictStr = Field(...)
    image_account: Optional[StrictStr] = Field(default=None, alias="imageAccount")
    image: StrictStr = Field(...)
    model_group: Optional[StrictStr] = Field(default=None, alias="modelGroup")
    is_public: Optional[StrictBool] = Field(default=None, alias="isPublic")
    config: Optional[Dict[str, Any]] = None
    env: Optional[Dict[str, Any]] = None
    additional_flags: Optional[conlist(StrictStr)] = Field(default=None, alias="additionalFlags")
    training_model_account: Optional[StrictStr] = Field(default=None, alias="trainingModelAccount")
    training_model_name: Optional[StrictStr] = Field(default=None, alias="trainingModelName")
    training_dataset_account: Optional[StrictStr] = Field(default=None, alias="trainingDatasetAccount")
    training_dataset_name: Optional[StrictStr] = Field(default=None, alias="trainingDatasetName")
    training_fit_config_name: Optional[StrictStr] = Field(default=None, alias="trainingFitConfigName")
    task_type: Optional[StrictStr] = Field(default=None, alias="taskType")
    training_dataset_type: Optional[StrictStr] = Field(default=None, alias="trainingDatasetType")
    fit_template_model_name: Optional[StrictStr] = Field(default=None, alias="fitTemplateModelName")
    composite: Optional[StrictBool] = None
    prototype: Optional[StrictBool] = None
    reject_requests_if_inactive: Optional[StrictBool] = Field(default=None, alias="rejectRequestsIfInactive")
    fittable: Optional[StrictBool] = None
    training_type: Optional[StrictStr] = Field(default=None, alias="trainingType")
    hosting_type: Optional[StrictStr] = Field(default=None, alias="hostingType")
    data_image_mounts: Optional[conlist(DataImageMountDump)] = Field(default=None, alias="dataImageMounts")
    timeouts: Optional[ModelTimeoutsData] = None
    limits: Optional[ModelLimitsData] = None
    retries: Optional[ModelRetriesData] = None
    batches: Optional[ModelBatchesData] = None
    caching: Optional[ModelCachingData] = None
    priority_queue: Optional[ModelPriorityQueueData] = Field(default=None, alias="priorityQueue")
    auto_scaling_configuration: Optional[ModelAutoScalingConfiguration] = Field(default=None, alias="autoScalingConfiguration")
    docs: conlist(DocumentDump) = Field(...)
    predict_configs: conlist(PredictConfigDump) = Field(default=..., alias="predictConfigs")
    fit_configs: conlist(FitConfigDump) = Field(default=..., alias="fitConfigs")
    resource_group: Optional[StrictStr] = Field(default=None, alias="resourceGroup")
    short_description: Optional[StrictStr] = Field(default=None, alias="shortDescription")
    languages: Optional[conlist(StrictStr, unique_items=True)] = None
    available_in_jaicp: Optional[StrictBool] = Field(default=None, alias="availableInJaicp")
    featured: Optional[StrictBool] = None
    featured_list_order: Optional[StrictInt] = Field(default=None, alias="featuredListOrder")
    hidden: Optional[StrictBool] = None
    public_testing_allowed: Optional[StrictBool] = Field(default=None, alias="publicTestingAllowed")
    is_billing_enabled: Optional[StrictBool] = Field(default=None, alias="isBillingEnabled")
    billing_unit: Optional[StrictStr] = Field(default=None, alias="billingUnit")
    billing_unit_price_in_nano_token: Optional[StrictInt] = Field(default=None, alias="billingUnitPriceInNanoToken")
    free_unit_quota: Optional[StrictInt] = Field(default=None, alias="freeUnitQuota")
    aliases: Optional[conlist(StrictStr)] = None
    is_http_enabled: StrictBool = Field(default=..., alias="isHttpEnabled")
    http_port: Optional[StrictInt] = Field(default=None, alias="httpPort")
    main_page_endpoint: Optional[StrictStr] = Field(default=None, alias="mainPageEndpoint")
    archive_enabled: StrictBool = Field(default=..., alias="archiveEnabled")
    number_of_archived_requests: StrictInt = Field(default=..., alias="numberOfArchivedRequests")
    archive_encryption_enabled: StrictBool = Field(default=..., alias="archiveEncryptionEnabled")
    archive_encryption_public_key: Optional[StrictStr] = Field(default=None, alias="archiveEncryptionPublicKey")
    as_http_settings_data: ModelHttpSettingsData = Field(default=..., alias="asHttpSettingsData")
    as_public_settings_data: ModelPublicSettingsData = Field(default=..., alias="asPublicSettingsData")
    as_billing_settings_data: ModelBillingSettingsData = Field(default=..., alias="asBillingSettingsData")
    as_archive_settings_data: ModelArchiveSettingsData = Field(default=..., alias="asArchiveSettingsData")
    __properties = ["name", "imageAccount", "image", "modelGroup", "isPublic", "config", "env", "additionalFlags", "trainingModelAccount", "trainingModelName", "trainingDatasetAccount", "trainingDatasetName", "trainingFitConfigName", "taskType", "trainingDatasetType", "fitTemplateModelName", "composite", "prototype", "rejectRequestsIfInactive", "fittable", "trainingType", "hostingType", "dataImageMounts", "timeouts", "limits", "retries", "batches", "caching", "priorityQueue", "autoScalingConfiguration", "docs", "predictConfigs", "fitConfigs", "resourceGroup", "shortDescription", "languages", "availableInJaicp", "featured", "featuredListOrder", "hidden", "publicTestingAllowed", "isBillingEnabled", "billingUnit", "billingUnitPriceInNanoToken", "freeUnitQuota", "aliases", "isHttpEnabled", "httpPort", "mainPageEndpoint", "archiveEnabled", "numberOfArchivedRequests", "archiveEncryptionEnabled", "archiveEncryptionPublicKey", "asHttpSettingsData", "asPublicSettingsData", "asBillingSettingsData", "asArchiveSettingsData"]

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
        if value is None:
            return value

        if value not in ('EXTERNAL', 'INTERNAL', 'AUTOMATIC', 'HOSTING_SERVER'):
            raise ValueError("must be one of enum values ('EXTERNAL', 'INTERNAL', 'AUTOMATIC', 'HOSTING_SERVER')")
        return value

    @validator('billing_unit')
    def billing_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('calls', 'direct', 'custom'):
            raise ValueError("must be one of enum values ('calls', 'direct', 'custom')")
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
    def from_json(cls, json_str: str) -> ModelDump:
        """Create an instance of ModelDump from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict['limits'] = self.limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retries
        if self.retries:
            _dict['retries'] = self.retries.to_dict()
        # override the default output from pydantic by calling `to_dict()` of batches
        if self.batches:
            _dict['batches'] = self.batches.to_dict()
        # override the default output from pydantic by calling `to_dict()` of caching
        if self.caching:
            _dict['caching'] = self.caching.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority_queue
        if self.priority_queue:
            _dict['priorityQueue'] = self.priority_queue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auto_scaling_configuration
        if self.auto_scaling_configuration:
            _dict['autoScalingConfiguration'] = self.auto_scaling_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in docs (list)
        _items = []
        if self.docs:
            for _item in self.docs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['docs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in predict_configs (list)
        _items = []
        if self.predict_configs:
            for _item in self.predict_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['predictConfigs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fit_configs (list)
        _items = []
        if self.fit_configs:
            for _item in self.fit_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fitConfigs'] = _items
        # override the default output from pydantic by calling `to_dict()` of as_http_settings_data
        if self.as_http_settings_data:
            _dict['asHttpSettingsData'] = self.as_http_settings_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of as_public_settings_data
        if self.as_public_settings_data:
            _dict['asPublicSettingsData'] = self.as_public_settings_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of as_billing_settings_data
        if self.as_billing_settings_data:
            _dict['asBillingSettingsData'] = self.as_billing_settings_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of as_archive_settings_data
        if self.as_archive_settings_data:
            _dict['asArchiveSettingsData'] = self.as_archive_settings_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelDump:
        """Create an instance of ModelDump from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelDump.parse_obj(obj)

        _obj = ModelDump.parse_obj({
            "name": obj.get("name"),
            "image_account": obj.get("imageAccount"),
            "image": obj.get("image"),
            "model_group": obj.get("modelGroup"),
            "is_public": obj.get("isPublic"),
            "config": obj.get("config"),
            "env": obj.get("env"),
            "additional_flags": obj.get("additionalFlags"),
            "training_model_account": obj.get("trainingModelAccount"),
            "training_model_name": obj.get("trainingModelName"),
            "training_dataset_account": obj.get("trainingDatasetAccount"),
            "training_dataset_name": obj.get("trainingDatasetName"),
            "training_fit_config_name": obj.get("trainingFitConfigName"),
            "task_type": obj.get("taskType"),
            "training_dataset_type": obj.get("trainingDatasetType"),
            "fit_template_model_name": obj.get("fitTemplateModelName"),
            "composite": obj.get("composite"),
            "prototype": obj.get("prototype"),
            "reject_requests_if_inactive": obj.get("rejectRequestsIfInactive"),
            "fittable": obj.get("fittable"),
            "training_type": obj.get("trainingType"),
            "hosting_type": obj.get("hostingType"),
            "data_image_mounts": [DataImageMountDump.from_dict(_item) for _item in obj.get("dataImageMounts")] if obj.get("dataImageMounts") is not None else None,
            "timeouts": ModelTimeoutsData.from_dict(obj.get("timeouts")) if obj.get("timeouts") is not None else None,
            "limits": ModelLimitsData.from_dict(obj.get("limits")) if obj.get("limits") is not None else None,
            "retries": ModelRetriesData.from_dict(obj.get("retries")) if obj.get("retries") is not None else None,
            "batches": ModelBatchesData.from_dict(obj.get("batches")) if obj.get("batches") is not None else None,
            "caching": ModelCachingData.from_dict(obj.get("caching")) if obj.get("caching") is not None else None,
            "priority_queue": ModelPriorityQueueData.from_dict(obj.get("priorityQueue")) if obj.get("priorityQueue") is not None else None,
            "auto_scaling_configuration": ModelAutoScalingConfiguration.from_dict(obj.get("autoScalingConfiguration")) if obj.get("autoScalingConfiguration") is not None else None,
            "docs": [DocumentDump.from_dict(_item) for _item in obj.get("docs")] if obj.get("docs") is not None else None,
            "predict_configs": [PredictConfigDump.from_dict(_item) for _item in obj.get("predictConfigs")] if obj.get("predictConfigs") is not None else None,
            "fit_configs": [FitConfigDump.from_dict(_item) for _item in obj.get("fitConfigs")] if obj.get("fitConfigs") is not None else None,
            "resource_group": obj.get("resourceGroup"),
            "short_description": obj.get("shortDescription"),
            "languages": obj.get("languages"),
            "available_in_jaicp": obj.get("availableInJaicp"),
            "featured": obj.get("featured"),
            "featured_list_order": obj.get("featuredListOrder"),
            "hidden": obj.get("hidden"),
            "public_testing_allowed": obj.get("publicTestingAllowed"),
            "is_billing_enabled": obj.get("isBillingEnabled"),
            "billing_unit": obj.get("billingUnit"),
            "billing_unit_price_in_nano_token": obj.get("billingUnitPriceInNanoToken"),
            "free_unit_quota": obj.get("freeUnitQuota"),
            "aliases": obj.get("aliases"),
            "is_http_enabled": obj.get("isHttpEnabled"),
            "http_port": obj.get("httpPort"),
            "main_page_endpoint": obj.get("mainPageEndpoint"),
            "archive_enabled": obj.get("archiveEnabled"),
            "number_of_archived_requests": obj.get("numberOfArchivedRequests"),
            "archive_encryption_enabled": obj.get("archiveEncryptionEnabled"),
            "archive_encryption_public_key": obj.get("archiveEncryptionPublicKey"),
            "as_http_settings_data": ModelHttpSettingsData.from_dict(obj.get("asHttpSettingsData")) if obj.get("asHttpSettingsData") is not None else None,
            "as_public_settings_data": ModelPublicSettingsData.from_dict(obj.get("asPublicSettingsData")) if obj.get("asPublicSettingsData") is not None else None,
            "as_billing_settings_data": ModelBillingSettingsData.from_dict(obj.get("asBillingSettingsData")) if obj.get("asBillingSettingsData") is not None else None,
            "as_archive_settings_data": ModelArchiveSettingsData.from_dict(obj.get("asArchiveSettingsData")) if obj.get("asArchiveSettingsData") is not None else None
        })
        return _obj


