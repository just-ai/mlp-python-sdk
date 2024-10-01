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

class ModelBillingSettingsData(BaseModel):
    """
    ModelBillingSettingsData
    """
    is_billing_enabled: StrictBool = Field(default=..., alias="isBillingEnabled")
    billing_unit: Optional[StrictStr] = Field(default=None, alias="billingUnit")
    billing_unit_price_in_nano_token: Optional[StrictInt] = Field(default=None, alias="billingUnitPriceInNanoToken")
    billing_unit_price_in_currency: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="billingUnitPriceInCurrency")
    free_unit_quota: Optional[StrictInt] = Field(default=None, alias="freeUnitQuota")
    __properties = ["isBillingEnabled", "billingUnit", "billingUnitPriceInNanoToken", "billingUnitPriceInCurrency", "freeUnitQuota"]

    @validator('billing_unit')
    def billing_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('calls', 'direct', 'custom'):
            raise ValueError("must be one of enum values ('calls', 'direct', 'custom')")
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
    def from_json(cls, json_str: str) -> ModelBillingSettingsData:
        """Create an instance of ModelBillingSettingsData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelBillingSettingsData:
        """Create an instance of ModelBillingSettingsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelBillingSettingsData.parse_obj(obj)

        _obj = ModelBillingSettingsData.parse_obj({
            "is_billing_enabled": obj.get("isBillingEnabled"),
            "billing_unit": obj.get("billingUnit"),
            "billing_unit_price_in_nano_token": obj.get("billingUnitPriceInNanoToken"),
            "billing_unit_price_in_currency": obj.get("billingUnitPriceInCurrency"),
            "free_unit_quota": obj.get("freeUnitQuota")
        })
        return _obj


