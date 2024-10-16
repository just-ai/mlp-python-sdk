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
from pydantic import BaseModel, Field, StrictStr

class DeprecatedDatasetInfoWithContentData(BaseModel):
    """
    DeprecatedDatasetInfoWithContentData
    """
    name: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    data_type: Optional[StrictStr] = Field(default=None, alias="dataType")
    content: Optional[StrictStr] = None
    __properties = ["name", "description", "dataType", "content"]

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
    def from_json(cls, json_str: str) -> DeprecatedDatasetInfoWithContentData:
        """Create an instance of DeprecatedDatasetInfoWithContentData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeprecatedDatasetInfoWithContentData:
        """Create an instance of DeprecatedDatasetInfoWithContentData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeprecatedDatasetInfoWithContentData.parse_obj(obj)

        _obj = DeprecatedDatasetInfoWithContentData.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "data_type": obj.get("dataType"),
            "content": obj.get("content")
        })
        return _obj


