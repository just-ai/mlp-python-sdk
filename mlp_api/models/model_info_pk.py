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

class ModelInfoPK(BaseModel):
    """
    ModelInfoPK
    """
    account_id: StrictInt = Field(default=..., alias="accountId")
    model_id: StrictInt = Field(default=..., alias="modelId")
    __properties = ["accountId", "modelId"]

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
    def from_json(cls, json_str: str) -> ModelInfoPK:
        """Create an instance of ModelInfoPK from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelInfoPK:
        """Create an instance of ModelInfoPK from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelInfoPK.parse_obj(obj)

        _obj = ModelInfoPK.parse_obj({
            "account_id": obj.get("accountId"),
            "model_id": obj.get("modelId")
        })
        return _obj

