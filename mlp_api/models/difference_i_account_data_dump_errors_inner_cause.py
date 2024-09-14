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
from pydantic import BaseModel, Field, StrictStr, conlist
from mlp_api.models.difference_i_account_data_dump_errors_inner_cause_stack_trace_inner import DifferenceIAccountDataDumpErrorsInnerCauseStackTraceInner

class DifferenceIAccountDataDumpErrorsInnerCause(BaseModel):
    """
    DifferenceIAccountDataDumpErrorsInnerCause
    """
    stack_trace: Optional[conlist(DifferenceIAccountDataDumpErrorsInnerCauseStackTraceInner)] = Field(default=None, alias="stackTrace")
    message: Optional[StrictStr] = None
    localized_message: Optional[StrictStr] = Field(default=None, alias="localizedMessage")
    __properties = ["stackTrace", "message", "localizedMessage"]

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
    def from_json(cls, json_str: str) -> DifferenceIAccountDataDumpErrorsInnerCause:
        """Create an instance of DifferenceIAccountDataDumpErrorsInnerCause from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in stack_trace (list)
        _items = []
        if self.stack_trace:
            for _item in self.stack_trace:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stackTrace'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DifferenceIAccountDataDumpErrorsInnerCause:
        """Create an instance of DifferenceIAccountDataDumpErrorsInnerCause from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DifferenceIAccountDataDumpErrorsInnerCause.parse_obj(obj)

        _obj = DifferenceIAccountDataDumpErrorsInnerCause.parse_obj({
            "stack_trace": [DifferenceIAccountDataDumpErrorsInnerCauseStackTraceInner.from_dict(_item) for _item in obj.get("stackTrace")] if obj.get("stackTrace") is not None else None,
            "message": obj.get("message"),
            "localized_message": obj.get("localizedMessage")
        })
        return _obj

