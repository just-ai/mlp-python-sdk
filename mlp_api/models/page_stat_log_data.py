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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, conlist
from mlp_api.models.pageable_object import PageableObject
from mlp_api.models.sort_object import SortObject
from mlp_api.models.stat_log_data import StatLogData

class PageStatLogData(BaseModel):
    """
    PageStatLogData
    """
    total_elements: Optional[StrictInt] = Field(default=None, alias="totalElements")
    total_pages: Optional[StrictInt] = Field(default=None, alias="totalPages")
    pageable: Optional[PageableObject] = None
    first: Optional[StrictBool] = None
    size: Optional[StrictInt] = None
    content: Optional[conlist(StatLogData)] = None
    number: Optional[StrictInt] = None
    sort: Optional[SortObject] = None
    last: Optional[StrictBool] = None
    number_of_elements: Optional[StrictInt] = Field(default=None, alias="numberOfElements")
    empty: Optional[StrictBool] = None
    __properties = ["totalElements", "totalPages", "pageable", "first", "size", "content", "number", "sort", "last", "numberOfElements", "empty"]

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
    def from_json(cls, json_str: str) -> PageStatLogData:
        """Create an instance of PageStatLogData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pageable
        if self.pageable:
            _dict['pageable'] = self.pageable.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in content (list)
        _items = []
        if self.content:
            for _item in self.content:
                if _item:
                    _items.append(_item.to_dict())
            _dict['content'] = _items
        # override the default output from pydantic by calling `to_dict()` of sort
        if self.sort:
            _dict['sort'] = self.sort.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PageStatLogData:
        """Create an instance of PageStatLogData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PageStatLogData.parse_obj(obj)

        _obj = PageStatLogData.parse_obj({
            "total_elements": obj.get("totalElements"),
            "total_pages": obj.get("totalPages"),
            "pageable": PageableObject.from_dict(obj.get("pageable")) if obj.get("pageable") is not None else None,
            "first": obj.get("first"),
            "size": obj.get("size"),
            "content": [StatLogData.from_dict(_item) for _item in obj.get("content")] if obj.get("content") is not None else None,
            "number": obj.get("number"),
            "sort": SortObject.from_dict(obj.get("sort")) if obj.get("sort") is not None else None,
            "last": obj.get("last"),
            "number_of_elements": obj.get("numberOfElements"),
            "empty": obj.get("empty")
        })
        return _obj


