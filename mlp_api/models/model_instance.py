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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator
from mlp_api.models.model_instance_pk import ModelInstancePK

class ModelInstance(BaseModel):
    """
    ModelInstance
    """
    id: ModelInstancePK = Field(...)
    connection_token: StrictStr = Field(default=..., alias="connectionToken")
    created: datetime = Field(...)
    last_heart_beat: datetime = Field(default=..., alias="lastHeartBeat")
    type: StrictStr = Field(...)
    kube_type: Optional[StrictStr] = Field(default=None, alias="kubeType")
    resource_name: Optional[StrictStr] = Field(default=None, alias="resourceName")
    alias: Optional[StrictStr] = None
    custom_data: Optional[StrictStr] = Field(default=None, alias="customData")
    delete_timestamp: Optional[datetime] = Field(default=None, alias="deleteTimestamp")
    is_evictable: StrictBool = Field(default=..., alias="isEvictable")
    hosting_server_id: Optional[StrictStr] = Field(default=None, alias="hostingServerId")
    server_id: Optional[StrictInt] = Field(default=None, alias="serverId")
    status: StrictStr = Field(...)
    __properties = ["id", "connectionToken", "created", "lastHeartBeat", "type", "kubeType", "resourceName", "alias", "customData", "deleteTimestamp", "isEvictable", "hostingServerId", "serverId", "status"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('initialCheck', 'singleFit', 'singleFitPool', 'multipleFit', 'predict'):
            raise ValueError("must be one of enum values ('initialCheck', 'singleFit', 'singleFitPool', 'multipleFit', 'predict')")
        return value

    @validator('kube_type')
    def kube_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('deployment', 'pod', 'docker', 'external', 'hostingServer'):
            raise ValueError("must be one of enum values ('deployment', 'pod', 'docker', 'external', 'hostingServer')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('IDLE', 'SCHEDULED', 'STARTED', 'DELETED', 'FAILED'):
            raise ValueError("must be one of enum values ('IDLE', 'SCHEDULED', 'STARTED', 'DELETED', 'FAILED')")
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
    def from_json(cls, json_str: str) -> ModelInstance:
        """Create an instance of ModelInstance from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelInstance:
        """Create an instance of ModelInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelInstance.parse_obj(obj)

        _obj = ModelInstance.parse_obj({
            "id": ModelInstancePK.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "connection_token": obj.get("connectionToken"),
            "created": obj.get("created"),
            "last_heart_beat": obj.get("lastHeartBeat"),
            "type": obj.get("type"),
            "kube_type": obj.get("kubeType"),
            "resource_name": obj.get("resourceName"),
            "alias": obj.get("alias"),
            "custom_data": obj.get("customData"),
            "delete_timestamp": obj.get("deleteTimestamp"),
            "is_evictable": obj.get("isEvictable"),
            "hosting_server_id": obj.get("hostingServerId"),
            "server_id": obj.get("serverId"),
            "status": obj.get("status")
        })
        return _obj


