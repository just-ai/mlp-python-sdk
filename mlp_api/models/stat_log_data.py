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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class StatLogData(BaseModel):
    """
    StatLogData
    """
    account_id: StrictInt = Field(default=..., alias="accountId")
    record_id: StrictInt = Field(default=..., alias="recordId")
    user_id: Optional[StrictInt] = Field(default=None, alias="userId")
    node: Optional[StrictStr] = None
    image_id: Optional[StrictInt] = Field(default=None, alias="imageId")
    model_id: Optional[StrictInt] = Field(default=None, alias="modelId")
    job_id: Optional[StrictInt] = Field(default=None, alias="jobId")
    resource_group: Optional[StrictStr] = Field(default=None, alias="resourceGroup")
    timestamp: StrictStr = Field(...)
    level: StrictStr = Field(...)
    code: StrictStr = Field(...)
    args: Dict[str, Any] = Field(...)
    message: StrictStr = Field(...)
    __properties = ["accountId", "recordId", "userId", "node", "imageId", "modelId", "jobId", "resourceGroup", "timestamp", "level", "code", "args", "message"]

    @validator('level')
    def level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('INFO', 'ERROR'):
            raise ValueError("must be one of enum values ('INFO', 'ERROR')")
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
    def from_json(cls, json_str: str) -> StatLogData:
        """Create an instance of StatLogData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StatLogData:
        """Create an instance of StatLogData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StatLogData.parse_obj(obj)

        _obj = StatLogData.parse_obj({
            "account_id": obj.get("accountId"),
            "record_id": obj.get("recordId"),
            "user_id": obj.get("userId"),
            "node": obj.get("node"),
            "image_id": obj.get("imageId"),
            "model_id": obj.get("modelId"),
            "job_id": obj.get("jobId"),
            "resource_group": obj.get("resourceGroup"),
            "timestamp": obj.get("timestamp"),
            "level": obj.get("level"),
            "code": obj.get("code"),
            "args": obj.get("args"),
            "message": obj.get("message")
        })
        return _obj


