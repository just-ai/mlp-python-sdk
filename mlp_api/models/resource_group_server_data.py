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

class ResourceGroupServerData(BaseModel):
    """
    ResourceGroupServerData
    """
    id: StrictInt = Field(...)
    name: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    is_auto_created: StrictBool = Field(default=..., alias="isAutoCreated")
    raw_configuration: StrictStr = Field(default=..., alias="rawConfiguration")
    template_capacity: Optional[ServerCapacityData] = Field(default=None, alias="templateCapacity")
    tariffication_price: Union[StrictFloat, StrictInt] = Field(default=..., alias="tarifficationPrice")
    tariffication_period: Optional[StrictStr] = Field(default=None, alias="tarifficationPeriod")
    __properties = ["id", "name", "description", "isAutoCreated", "rawConfiguration", "templateCapacity", "tarifficationPrice", "tarifficationPeriod"]

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
    def from_json(cls, json_str: str) -> ResourceGroupServerData:
        """Create an instance of ResourceGroupServerData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of template_capacity
        if self.template_capacity:
            _dict['templateCapacity'] = self.template_capacity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResourceGroupServerData:
        """Create an instance of ResourceGroupServerData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResourceGroupServerData.parse_obj(obj)

        _obj = ResourceGroupServerData.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "is_auto_created": obj.get("isAutoCreated"),
            "raw_configuration": obj.get("rawConfiguration"),
            "template_capacity": ServerCapacityData.from_dict(obj.get("templateCapacity")) if obj.get("templateCapacity") is not None else None,
            "tariffication_price": obj.get("tarifficationPrice"),
            "tariffication_period": obj.get("tarifficationPeriod")
        })
        return _obj


