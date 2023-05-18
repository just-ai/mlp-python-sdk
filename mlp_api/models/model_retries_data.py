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


from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist

class ModelRetriesData(BaseModel):
    """
    ModelRetriesData
    """
    max_retries: StrictInt = Field(..., alias="maxRetries")
    timeouts_ms: conlist(StrictInt) = Field(..., alias="timeoutsMs")
    __properties = ["maxRetries", "timeoutsMs"]

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
    def from_json(cls, json_str: str) -> ModelRetriesData:
        """Create an instance of ModelRetriesData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelRetriesData:
        """Create an instance of ModelRetriesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelRetriesData.parse_obj(obj)

        _obj = ModelRetriesData.parse_obj({
            "max_retries": obj.get("maxRetries"),
            "timeouts_ms": obj.get("timeoutsMs")
        })
        return _obj

