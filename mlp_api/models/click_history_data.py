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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class ClickHistoryData(BaseModel):
    """
    ClickHistoryData
    """
    creation_time: Optional[StrictInt] = Field(default=None, alias="creationTime")
    account_id: Optional[StrictInt] = Field(default=None, alias="accountId")
    entity_id: Optional[StrictInt] = Field(default=None, alias="entityId")
    entity_type: Optional[StrictStr] = Field(default=None, alias="entityType")
    page_url: StrictStr = Field(default=..., alias="pageUrl")
    description: Optional[StrictStr] = None
    event_type: StrictStr = Field(default=..., alias="eventType")
    element_id: Optional[StrictInt] = Field(default=None, alias="elementId")
    __properties = ["creationTime", "accountId", "entityId", "entityType", "pageUrl", "description", "eventType", "elementId"]

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
    def from_json(cls, json_str: str) -> ClickHistoryData:
        """Create an instance of ClickHistoryData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClickHistoryData:
        """Create an instance of ClickHistoryData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClickHistoryData.parse_obj(obj)

        _obj = ClickHistoryData.parse_obj({
            "creation_time": obj.get("creationTime"),
            "account_id": obj.get("accountId"),
            "entity_id": obj.get("entityId"),
            "entity_type": obj.get("entityType"),
            "page_url": obj.get("pageUrl"),
            "description": obj.get("description"),
            "event_type": obj.get("eventType"),
            "element_id": obj.get("elementId")
        })
        return _obj


