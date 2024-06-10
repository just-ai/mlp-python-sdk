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



from pydantic import BaseModel, Field, StrictBool

class FrontendSettings(BaseModel):
    """
    FrontendSettings
    """
    is_system_account: StrictBool = Field(default=..., alias="isSystemAccount")
    is_billing_enabled: StrictBool = Field(default=..., alias="isBillingEnabled")
    is_archive_enabled: StrictBool = Field(default=..., alias="isArchiveEnabled")
    is_extended_landing: StrictBool = Field(default=..., alias="isExtendedLanding")
    __properties = ["isSystemAccount", "isBillingEnabled", "isArchiveEnabled", "isExtendedLanding"]

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
    def from_json(cls, json_str: str) -> FrontendSettings:
        """Create an instance of FrontendSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FrontendSettings:
        """Create an instance of FrontendSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FrontendSettings.parse_obj(obj)

        _obj = FrontendSettings.parse_obj({
            "is_system_account": obj.get("isSystemAccount"),
            "is_billing_enabled": obj.get("isBillingEnabled"),
            "is_archive_enabled": obj.get("isArchiveEnabled"),
            "is_extended_landing": obj.get("isExtendedLanding")
        })
        return _obj


