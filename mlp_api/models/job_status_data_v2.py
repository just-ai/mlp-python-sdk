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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator

class JobStatusDataV2(BaseModel):
    """
    JobStatusDataV2
    """
    job_id: StrictStr = Field(default=..., alias="jobId")
    job_status: StrictStr = Field(default=..., alias="jobStatus")
    start_time: StrictInt = Field(default=..., alias="startTime")
    end_time: Optional[StrictInt] = Field(default=None, alias="endTime")
    name: StrictStr = Field(...)
    parents: conlist(StrictStr) = Field(...)
    percentage: Optional[StrictInt] = None
    current_command_name: Optional[StrictStr] = Field(default=None, alias="currentCommandName")
    original_exception: Optional[StrictStr] = Field(default=None, alias="originalException")
    priority_name: StrictStr = Field(default=..., alias="priorityName")
    error_message: Optional[StrictStr] = Field(default=None, alias="errorMessage")
    account_id: Optional[StrictInt] = Field(default=None, alias="accountId")
    model_id: Optional[StrictInt] = Field(default=None, alias="modelId")
    instance_id: Optional[StrictInt] = Field(default=None, alias="instanceId")
    group_owner_id: Optional[StrictInt] = Field(default=None, alias="groupOwnerId")
    group_name: Optional[StrictStr] = Field(default=None, alias="groupName")
    server_id: Optional[StrictInt] = Field(default=None, alias="serverId")
    wait_for: Optional[conlist(StrictStr)] = Field(default=None, alias="waitFor")
    __properties = ["jobId", "jobStatus", "startTime", "endTime", "name", "parents", "percentage", "currentCommandName", "originalException", "priorityName", "errorMessage", "accountId", "modelId", "instanceId", "groupOwnerId", "groupName", "serverId", "waitFor"]

    @validator('job_status')
    def job_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('IDLE', 'RUN', 'REVERTING', 'COMPLETED', 'FAILED', 'REVERTED'):
            raise ValueError("must be one of enum values ('IDLE', 'RUN', 'REVERTING', 'COMPLETED', 'FAILED', 'REVERTED')")
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
    def from_json(cls, json_str: str) -> JobStatusDataV2:
        """Create an instance of JobStatusDataV2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobStatusDataV2:
        """Create an instance of JobStatusDataV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobStatusDataV2.parse_obj(obj)

        _obj = JobStatusDataV2.parse_obj({
            "job_id": obj.get("jobId"),
            "job_status": obj.get("jobStatus"),
            "start_time": obj.get("startTime"),
            "end_time": obj.get("endTime"),
            "name": obj.get("name"),
            "parents": obj.get("parents"),
            "percentage": obj.get("percentage"),
            "current_command_name": obj.get("currentCommandName"),
            "original_exception": obj.get("originalException"),
            "priority_name": obj.get("priorityName"),
            "error_message": obj.get("errorMessage"),
            "account_id": obj.get("accountId"),
            "model_id": obj.get("modelId"),
            "instance_id": obj.get("instanceId"),
            "group_owner_id": obj.get("groupOwnerId"),
            "group_name": obj.get("groupName"),
            "server_id": obj.get("serverId"),
            "wait_for": obj.get("waitFor")
        })
        return _obj


