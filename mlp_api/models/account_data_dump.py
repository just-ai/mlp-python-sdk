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
from mlp_api.models.data_image_dump import DataImageDump
from mlp_api.models.image_dump import ImageDump
from mlp_api.models.model_dump import ModelDump
from mlp_api.models.model_group_dump import ModelGroupDump
from mlp_api.models.server_template_dump import ServerTemplateDump

class AccountDataDump(BaseModel):
    """
    AccountDataDump
    """
    api_tokens: Optional[conlist(StrictStr)] = Field(default=None, alias="apiTokens")
    model_groups: Optional[conlist(ModelGroupDump)] = Field(default=None, alias="modelGroups")
    images: Optional[conlist(ImageDump)] = None
    data_images: Optional[conlist(DataImageDump)] = Field(default=None, alias="dataImages")
    models: Optional[conlist(ModelDump)] = None
    server_templates: Optional[conlist(ServerTemplateDump)] = Field(default=None, alias="serverTemplates")
    __properties = ["apiTokens", "modelGroups", "images", "dataImages", "models", "serverTemplates"]

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
    def from_json(cls, json_str: str) -> AccountDataDump:
        """Create an instance of AccountDataDump from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in model_groups (list)
        _items = []
        if self.model_groups:
            for _item in self.model_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['modelGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in data_images (list)
        _items = []
        if self.data_images:
            for _item in self.data_images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dataImages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in models (list)
        _items = []
        if self.models:
            for _item in self.models:
                if _item:
                    _items.append(_item.to_dict())
            _dict['models'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in server_templates (list)
        _items = []
        if self.server_templates:
            for _item in self.server_templates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serverTemplates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountDataDump:
        """Create an instance of AccountDataDump from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountDataDump.parse_obj(obj)

        _obj = AccountDataDump.parse_obj({
            "api_tokens": obj.get("apiTokens"),
            "model_groups": [ModelGroupDump.from_dict(_item) for _item in obj.get("modelGroups")] if obj.get("modelGroups") is not None else None,
            "images": [ImageDump.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "data_images": [DataImageDump.from_dict(_item) for _item in obj.get("dataImages")] if obj.get("dataImages") is not None else None,
            "models": [ModelDump.from_dict(_item) for _item in obj.get("models")] if obj.get("models") is not None else None,
            "server_templates": [ServerTemplateDump.from_dict(_item) for _item in obj.get("serverTemplates")] if obj.get("serverTemplates") is not None else None
        })
        return _obj

