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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from mlp_api.models.status_info import StatusInfo

class ModelInstanceData(BaseModel):
    """
    ModelInstanceData
    """
    id: StrictInt = Field(...)
    name: Optional[StrictStr] = None
    status_info: StatusInfo = Field(default=..., alias="statusInfo")
    restart_count: StrictInt = Field(default=..., alias="restartCount")
    last_restart_timestamp: Optional[StrictStr] = Field(default=None, alias="lastRestartTimestamp")
    created_timestamp: Optional[StrictStr] = Field(default=None, alias="createdTimestamp")
    instance_hosting_type: Optional[StrictStr] = Field(default=None, alias="instanceHostingType")
    __properties = ["id", "name", "statusInfo", "restartCount", "lastRestartTimestamp", "createdTimestamp", "instanceHostingType"]

    @validator('instance_hosting_type')
    def instance_hosting_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('deployment', 'pod', 'docker', 'external', 'hostingServer'):
            raise ValueError("must be one of enum values ('deployment', 'pod', 'docker', 'external', 'hostingServer')")
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
    def from_json(cls, json_str: str) -> ModelInstanceData:
        """Create an instance of ModelInstanceData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of status_info
        if self.status_info:
            _dict['statusInfo'] = self.status_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelInstanceData:
        """Create an instance of ModelInstanceData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelInstanceData.parse_obj(obj)

        _obj = ModelInstanceData.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status_info": StatusInfo.from_dict(obj.get("statusInfo")) if obj.get("statusInfo") is not None else None,
            "restart_count": obj.get("restartCount"),
            "last_restart_timestamp": obj.get("lastRestartTimestamp"),
            "created_timestamp": obj.get("createdTimestamp"),
            "instance_hosting_type": obj.get("instanceHostingType")
        })
        return _obj


