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


from typing import Dict
from pydantic import BaseModel, Field, StrictBool, StrictStr
from mlp_api.models.param_type_data import ParamTypeData

class MethodDescriptorData(BaseModel):
    """
    MethodDescriptorData
    """
    name: StrictStr = Field(...)
    params: Dict[str, ParamTypeData] = Field(...)
    output: ParamTypeData = Field(...)
    fitted: StrictBool = Field(...)
    __properties = ["name", "params", "output", "fitted"]

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
    def from_json(cls, json_str: str) -> MethodDescriptorData:
        """Create an instance of MethodDescriptorData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in params (dict)
        _field_dict = {}
        if self.params:
            for _key in self.params:
                if self.params[_key]:
                    _field_dict[_key] = self.params[_key].to_dict()
            _dict['params'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of output
        if self.output:
            _dict['output'] = self.output.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MethodDescriptorData:
        """Create an instance of MethodDescriptorData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MethodDescriptorData.parse_obj(obj)

        _obj = MethodDescriptorData.parse_obj({
            "name": obj.get("name"),
            "params": dict(
                (_k, ParamTypeData.from_dict(_v))
                for _k, _v in obj.get("params").items()
            )
            if obj.get("params") is not None
            else None,
            "output": ParamTypeData.from_dict(obj.get("output")) if obj.get("output") is not None else None,
            "fitted": obj.get("fitted")
        })
        return _obj

