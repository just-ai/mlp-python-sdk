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


from typing import Any, Dict
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class SharedPoolQuota(BaseModel):
    """
    SharedPoolQuota
    """
    owner_id: StrictInt = Field(default=..., alias="ownerId")
    group_name: StrictStr = Field(default=..., alias="groupName")
    group_type: StrictStr = Field(default=..., alias="groupType")
    access_policy: Dict[str, Any] = Field(default=..., alias="accessPolicy")
    cpu_limit: StrictStr = Field(default=..., alias="cpuLimit")
    memory_limit: StrictStr = Field(default=..., alias="memoryLimit")
    ephemeral_disk_limit: StrictStr = Field(default=..., alias="ephemeralDiskLimit")
    gpu_instances_limit: StrictInt = Field(default=..., alias="gpuInstancesLimit")
    base_instances_limit: StrictInt = Field(default=..., alias="baseInstancesLimit")
    derived_instances_limit: StrictInt = Field(default=..., alias="derivedInstancesLimit")
    __properties = ["ownerId", "groupName", "groupType", "accessPolicy", "cpuLimit", "memoryLimit", "ephemeralDiskLimit", "gpuInstancesLimit", "baseInstancesLimit", "derivedInstancesLimit"]

    @validator('group_type')
    def group_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DOCKER', 'KUBERNETES', 'HOSTING_SERVER', 'SHARED_RESOURCE_QUOTA'):
            raise ValueError("must be one of enum values ('DOCKER', 'KUBERNETES', 'HOSTING_SERVER', 'SHARED_RESOURCE_QUOTA')")
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
    def from_json(cls, json_str: str) -> SharedPoolQuota:
        """Create an instance of SharedPoolQuota from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SharedPoolQuota:
        """Create an instance of SharedPoolQuota from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SharedPoolQuota.parse_obj(obj)

        _obj = SharedPoolQuota.parse_obj({
            "owner_id": obj.get("ownerId"),
            "group_name": obj.get("groupName"),
            "group_type": obj.get("groupType"),
            "access_policy": obj.get("accessPolicy"),
            "cpu_limit": obj.get("cpuLimit"),
            "memory_limit": obj.get("memoryLimit"),
            "ephemeral_disk_limit": obj.get("ephemeralDiskLimit"),
            "gpu_instances_limit": obj.get("gpuInstancesLimit"),
            "base_instances_limit": obj.get("baseInstancesLimit"),
            "derived_instances_limit": obj.get("derivedInstancesLimit")
        })
        return _obj

