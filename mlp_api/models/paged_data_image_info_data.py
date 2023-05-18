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


from typing import List
from pydantic import BaseModel, Field, conlist
from mlp_api.models.data_image_info_data import DataImageInfoData
from mlp_api.models.pagination import Pagination

class PagedDataImageInfoData(BaseModel):
    """
    PagedDataImageInfoData
    """
    paging: Pagination = Field(...)
    records: conlist(DataImageInfoData) = Field(...)
    __properties = ["paging", "records"]

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
    def from_json(cls, json_str: str) -> PagedDataImageInfoData:
        """Create an instance of PagedDataImageInfoData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of paging
        if self.paging:
            _dict['paging'] = self.paging.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in records (list)
        _items = []
        if self.records:
            for _item in self.records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['records'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PagedDataImageInfoData:
        """Create an instance of PagedDataImageInfoData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PagedDataImageInfoData.parse_obj(obj)

        _obj = PagedDataImageInfoData.parse_obj({
            "paging": Pagination.from_dict(obj.get("paging")) if obj.get("paging") is not None else None,
            "records": [DataImageInfoData.from_dict(_item) for _item in obj.get("records")] if obj.get("records") is not None else None
        })
        return _obj

