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



from pydantic import BaseModel, Field, StrictInt

class FitConfigPK(BaseModel):
    """
    FitConfigPK
    """
    account_id: StrictInt = Field(default=..., alias="accountId")
    model_id: StrictInt = Field(default=..., alias="modelId")
    config_id: StrictInt = Field(default=..., alias="configId")
    __properties = ["accountId", "modelId", "configId"]

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
    def from_json(cls, json_str: str) -> FitConfigPK:
        """Create an instance of FitConfigPK from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FitConfigPK:
        """Create an instance of FitConfigPK from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FitConfigPK.parse_obj(obj)

        _obj = FitConfigPK.parse_obj({
            "account_id": obj.get("accountId"),
            "model_id": obj.get("modelId"),
            "config_id": obj.get("configId")
        })
        return _obj


