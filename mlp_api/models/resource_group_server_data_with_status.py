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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator
from mlp_api.models.server_capacity_data import ServerCapacityData

class ResourceGroupServerDataWithStatus(BaseModel):
    """
    ResourceGroupServerDataWithStatus
    """
    id: StrictInt = Field(...)
    name: StrictStr = Field(...)
    status: StrictStr = Field(...)
    server_ip: Optional[StrictStr] = Field(default=None, alias="serverIp")
    jump_host_ip: Optional[StrictStr] = Field(default=None, alias="jumpHostIp")
    resources: ServerCapacityData = Field(...)
    description: Optional[StrictStr] = None
    is_auto_created: StrictBool = Field(default=..., alias="isAutoCreated")
    raw_configuration: StrictStr = Field(default=..., alias="rawConfiguration")
    tariffication_price: Union[StrictFloat, StrictInt] = Field(default=..., alias="tarifficationPrice")
    tariffication_period: Optional[StrictStr] = Field(default=None, alias="tarifficationPeriod")
    __properties = ["id", "name", "status", "serverIp", "jumpHostIp", "resources", "description", "isAutoCreated", "rawConfiguration", "tarifficationPrice", "tarifficationPeriod"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('RUNNING', 'STARTING', 'STOPPED', 'UNAVAILABLE', 'DELETING'):
            raise ValueError("must be one of enum values ('RUNNING', 'STARTING', 'STOPPED', 'UNAVAILABLE', 'DELETING')")
        return value

    @validator('tariffication_period')
    def tariffication_period_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SECOND', 'MINUTE', 'HOUR', 'DAY', 'MONTH', 'YEAR'):
            raise ValueError("must be one of enum values ('SECOND', 'MINUTE', 'HOUR', 'DAY', 'MONTH', 'YEAR')")
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
    def from_json(cls, json_str: str) -> ResourceGroupServerDataWithStatus:
        """Create an instance of ResourceGroupServerDataWithStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResourceGroupServerDataWithStatus:
        """Create an instance of ResourceGroupServerDataWithStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResourceGroupServerDataWithStatus.parse_obj(obj)

        _obj = ResourceGroupServerDataWithStatus.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "server_ip": obj.get("serverIp"),
            "jump_host_ip": obj.get("jumpHostIp"),
            "resources": ServerCapacityData.from_dict(obj.get("resources")) if obj.get("resources") is not None else None,
            "description": obj.get("description"),
            "is_auto_created": obj.get("isAutoCreated"),
            "raw_configuration": obj.get("rawConfiguration"),
            "tariffication_price": obj.get("tarifficationPrice"),
            "tariffication_period": obj.get("tarifficationPeriod")
        })
        return _obj


