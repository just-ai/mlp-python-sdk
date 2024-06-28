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



from pydantic import BaseModel, Field, StrictStr
from mlp_api.models.model_batches_data import ModelBatchesData
from mlp_api.models.model_limits_data import ModelLimitsData
from mlp_api.models.model_retries_data import ModelRetriesData
from mlp_api.models.model_timeouts_data import ModelTimeoutsData

class ModelDefaults(BaseModel):
    """
    ModelDefaults
    """
    timeouts: ModelTimeoutsData = Field(...)
    retries: ModelRetriesData = Field(...)
    batches: ModelBatchesData = Field(...)
    limits: ModelLimitsData = Field(...)
    resource_group: StrictStr = Field(default=..., alias="resourceGroup")
    __properties = ["timeouts", "retries", "batches", "limits", "resourceGroup"]

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
    def from_json(cls, json_str: str) -> ModelDefaults:
        """Create an instance of ModelDefaults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of timeouts
        if self.timeouts:
            _dict['timeouts'] = self.timeouts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retries
        if self.retries:
            _dict['retries'] = self.retries.to_dict()
        # override the default output from pydantic by calling `to_dict()` of batches
        if self.batches:
            _dict['batches'] = self.batches.to_dict()
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict['limits'] = self.limits.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelDefaults:
        """Create an instance of ModelDefaults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelDefaults.parse_obj(obj)

        _obj = ModelDefaults.parse_obj({
            "timeouts": ModelTimeoutsData.from_dict(obj.get("timeouts")) if obj.get("timeouts") is not None else None,
            "retries": ModelRetriesData.from_dict(obj.get("retries")) if obj.get("retries") is not None else None,
            "batches": ModelBatchesData.from_dict(obj.get("batches")) if obj.get("batches") is not None else None,
            "limits": ModelLimitsData.from_dict(obj.get("limits")) if obj.get("limits") is not None else None,
            "resource_group": obj.get("resourceGroup")
        })
        return _obj

