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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator
from mlp_api.models.resource_group_auto_scaling_configuration import ResourceGroupAutoScalingConfiguration

class ResourceGroupShortStatusData(BaseModel):
    """
    ResourceGroupShortStatusData
    """
    name: StrictStr = Field(...)
    owner_id: Optional[StrictInt] = Field(default=None, alias="ownerId")
    is_default: StrictBool = Field(default=..., alias="isDefault")
    enabled_eviction: StrictBool = Field(default=..., alias="enabledEviction")
    enabled_auto_scaling: StrictBool = Field(default=..., alias="enabledAutoScaling")
    resource_group_type: StrictStr = Field(default=..., alias="resourceGroupType")
    access: StrictStr = Field(...)
    servers_count: StrictInt = Field(default=..., alias="serversCount")
    services_count: StrictInt = Field(default=..., alias="servicesCount")
    auto_scaling_configuration: Optional[ResourceGroupAutoScalingConfiguration] = Field(default=None, alias="autoScalingConfiguration")
    __properties = ["name", "ownerId", "isDefault", "enabledEviction", "enabledAutoScaling", "resourceGroupType", "access", "serversCount", "servicesCount", "autoScalingConfiguration"]

    @validator('resource_group_type')
    def resource_group_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DOCKER', 'KUBERNETES', 'HOSTING_SERVER', 'SHARED_RESOURCE_QUOTA'):
            raise ValueError("must be one of enum values ('DOCKER', 'KUBERNETES', 'HOSTING_SERVER', 'SHARED_RESOURCE_QUOTA')")
        return value

    @validator('access')
    def access_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('PRIVATE', 'PUBLIC', 'SHARED_POOL'):
            raise ValueError("must be one of enum values ('PRIVATE', 'PUBLIC', 'SHARED_POOL')")
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
    def from_json(cls, json_str: str) -> ResourceGroupShortStatusData:
        """Create an instance of ResourceGroupShortStatusData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of auto_scaling_configuration
        if self.auto_scaling_configuration:
            _dict['autoScalingConfiguration'] = self.auto_scaling_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResourceGroupShortStatusData:
        """Create an instance of ResourceGroupShortStatusData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResourceGroupShortStatusData.parse_obj(obj)

        _obj = ResourceGroupShortStatusData.parse_obj({
            "name": obj.get("name"),
            "owner_id": obj.get("ownerId"),
            "is_default": obj.get("isDefault"),
            "enabled_eviction": obj.get("enabledEviction"),
            "enabled_auto_scaling": obj.get("enabledAutoScaling"),
            "resource_group_type": obj.get("resourceGroupType"),
            "access": obj.get("access"),
            "servers_count": obj.get("serversCount"),
            "services_count": obj.get("servicesCount"),
            "auto_scaling_configuration": ResourceGroupAutoScalingConfiguration.from_dict(obj.get("autoScalingConfiguration")) if obj.get("autoScalingConfiguration") is not None else None
        })
        return _obj


