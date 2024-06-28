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
from pydantic import BaseModel, Field, StrictBool, StrictInt

class ModelPublicSettingsData(BaseModel):
    """
    ModelPublicSettingsData
    """
    is_public: Optional[StrictBool] = Field(default=None, alias="isPublic")
    available_in_jaicp: Optional[StrictBool] = Field(default=None, alias="availableInJaicp")
    featured: Optional[StrictBool] = None
    featured_list_order: Optional[StrictInt] = Field(default=None, alias="featuredListOrder")
    hidden: Optional[StrictBool] = None
    public_testing_allowed: Optional[StrictBool] = Field(default=None, alias="publicTestingAllowed")
    __properties = ["isPublic", "availableInJaicp", "featured", "featuredListOrder", "hidden", "publicTestingAllowed"]

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
    def from_json(cls, json_str: str) -> ModelPublicSettingsData:
        """Create an instance of ModelPublicSettingsData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelPublicSettingsData:
        """Create an instance of ModelPublicSettingsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelPublicSettingsData.parse_obj(obj)

        _obj = ModelPublicSettingsData.parse_obj({
            "is_public": obj.get("isPublic"),
            "available_in_jaicp": obj.get("availableInJaicp"),
            "featured": obj.get("featured"),
            "featured_list_order": obj.get("featuredListOrder"),
            "hidden": obj.get("hidden"),
            "public_testing_allowed": obj.get("publicTestingAllowed")
        })
        return _obj

