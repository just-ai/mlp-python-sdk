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


from typing import Dict, List
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from mlp_api.models.method_descriptor_data import MethodDescriptorData
from mlp_api.models.schema_file_data import SchemaFileData

class ServiceDescriptorData(BaseModel):
    """
    ServiceDescriptorData
    """
    name: StrictStr = Field(...)
    schema_files: conlist(SchemaFileData) = Field(..., alias="schemaFiles")
    fittable: StrictBool = Field(...)
    methods: Dict[str, MethodDescriptorData] = Field(...)
    __properties = ["name", "schemaFiles", "fittable", "methods"]

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
    def from_json(cls, json_str: str) -> ServiceDescriptorData:
        """Create an instance of ServiceDescriptorData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in schema_files (list)
        _items = []
        if self.schema_files:
            for _item in self.schema_files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['schemaFiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in methods (dict)
        _field_dict = {}
        if self.methods:
            for _key in self.methods:
                if self.methods[_key]:
                    _field_dict[_key] = self.methods[_key].to_dict()
            _dict['methods'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServiceDescriptorData:
        """Create an instance of ServiceDescriptorData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServiceDescriptorData.parse_obj(obj)

        _obj = ServiceDescriptorData.parse_obj({
            "name": obj.get("name"),
            "schema_files": [SchemaFileData.from_dict(_item) for _item in obj.get("schemaFiles")] if obj.get("schemaFiles") is not None else None,
            "fittable": obj.get("fittable"),
            "methods": dict(
                (_k, MethodDescriptorData.from_dict(_v))
                for _k, _v in obj.get("methods").items()
            )
            if obj.get("methods") is not None
            else None
        })
        return _obj

