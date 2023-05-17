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



from pydantic import BaseModel, Field, StrictBool, StrictStr
from mlp_api.models.status import Status

class CheckResult(BaseModel):
    """
    CheckResult
    """
    name: StrictStr = Field(...)
    critical: StrictBool = Field(...)
    status: Status = Field(...)
    __properties = ["name", "critical", "status"]

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
    def from_json(cls, json_str: str) -> CheckResult:
        """Create an instance of CheckResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CheckResult:
        """Create an instance of CheckResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CheckResult.parse_obj(obj)

        _obj = CheckResult.parse_obj({
            "name": obj.get("name"),
            "critical": obj.get("critical"),
            "status": Status.from_dict(obj.get("status")) if obj.get("status") is not None else None
        })
        return _obj

