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
from pydantic import BaseModel, Field, conlist
from mlp_api.models.account_config_dump import AccountConfigDump
from mlp_api.models.difference_i_account_data_dump_errors_inner import DifferenceIAccountDataDumpErrorsInner

class DifferenceIAccountConfigDump(BaseModel):
    """
    DifferenceIAccountConfigDump
    """
    before: Optional[AccountConfigDump] = None
    after: Optional[AccountConfigDump] = None
    errors: conlist(DifferenceIAccountDataDumpErrorsInner) = Field(...)
    __properties = ["before", "after", "errors"]

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
    def from_json(cls, json_str: str) -> DifferenceIAccountConfigDump:
        """Create an instance of DifferenceIAccountConfigDump from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of before
        if self.before:
            _dict['before'] = self.before.to_dict()
        # override the default output from pydantic by calling `to_dict()` of after
        if self.after:
            _dict['after'] = self.after.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DifferenceIAccountConfigDump:
        """Create an instance of DifferenceIAccountConfigDump from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DifferenceIAccountConfigDump.parse_obj(obj)

        _obj = DifferenceIAccountConfigDump.parse_obj({
            "before": AccountConfigDump.from_dict(obj.get("before")) if obj.get("before") is not None else None,
            "after": AccountConfigDump.from_dict(obj.get("after")) if obj.get("after") is not None else None,
            "errors": [DifferenceIAccountDataDumpErrorsInner.from_dict(_item) for _item in obj.get("errors")] if obj.get("errors") is not None else None
        })
        return _obj


