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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from mlp_api.models.event_source import EventSource

class EventData(BaseModel):
    """
    EventData
    """
    name: StrictStr = Field(...)
    type: Optional[StrictStr] = None
    created_timestamp: Optional[StrictStr] = Field(None, alias="createdTimestamp")
    message: Optional[StrictStr] = None
    reason: Optional[StrictStr] = None
    source: Optional[EventSource] = None
    first_seen_timestamp: Optional[StrictStr] = Field(None, alias="firstSeenTimestamp")
    last_seen_timestamp: Optional[StrictStr] = Field(None, alias="lastSeenTimestamp")
    count: Optional[StrictInt] = None
    kind: Optional[StrictStr] = None
    field_path: Optional[StrictStr] = Field(None, alias="fieldPath")
    namespace: StrictStr = Field(...)
    __properties = ["name", "type", "createdTimestamp", "message", "reason", "source", "firstSeenTimestamp", "lastSeenTimestamp", "count", "kind", "fieldPath", "namespace"]

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
    def from_json(cls, json_str: str) -> EventData:
        """Create an instance of EventData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventData:
        """Create an instance of EventData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventData.parse_obj(obj)

        _obj = EventData.parse_obj({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "created_timestamp": obj.get("createdTimestamp"),
            "message": obj.get("message"),
            "reason": obj.get("reason"),
            "source": EventSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "first_seen_timestamp": obj.get("firstSeenTimestamp"),
            "last_seen_timestamp": obj.get("lastSeenTimestamp"),
            "count": obj.get("count"),
            "kind": obj.get("kind"),
            "field_path": obj.get("fieldPath"),
            "namespace": obj.get("namespace")
        })
        return _obj

