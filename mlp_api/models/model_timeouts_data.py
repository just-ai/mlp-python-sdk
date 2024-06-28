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
from pydantic import BaseModel, Field, StrictInt

class ModelTimeoutsData(BaseModel):
    """
    ModelTimeoutsData
    """
    pod_start_timeout_sec: StrictInt = Field(default=..., alias="podStartTimeoutSec")
    predict_timeout_sec: StrictInt = Field(default=..., alias="predictTimeoutSec")
    fit_timeout_sec: Optional[StrictInt] = Field(default=None, alias="fitTimeoutSec")
    __properties = ["podStartTimeoutSec", "predictTimeoutSec", "fitTimeoutSec"]

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
    def from_json(cls, json_str: str) -> ModelTimeoutsData:
        """Create an instance of ModelTimeoutsData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelTimeoutsData:
        """Create an instance of ModelTimeoutsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelTimeoutsData.parse_obj(obj)

        _obj = ModelTimeoutsData.parse_obj({
            "pod_start_timeout_sec": obj.get("podStartTimeoutSec"),
            "predict_timeout_sec": obj.get("predictTimeoutSec"),
            "fit_timeout_sec": obj.get("fitTimeoutSec")
        })
        return _obj

