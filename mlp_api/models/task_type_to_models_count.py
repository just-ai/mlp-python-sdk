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



from pydantic import BaseModel, Field, StrictInt, StrictStr

class TaskTypeToModelsCount(BaseModel):
    """
    TaskTypeToModelsCount
    """
    task_type_name: StrictStr = Field(default=..., alias="taskTypeName")
    models_count: StrictInt = Field(default=..., alias="modelsCount")
    __properties = ["taskTypeName", "modelsCount"]

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
    def from_json(cls, json_str: str) -> TaskTypeToModelsCount:
        """Create an instance of TaskTypeToModelsCount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskTypeToModelsCount:
        """Create an instance of TaskTypeToModelsCount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskTypeToModelsCount.parse_obj(obj)

        _obj = TaskTypeToModelsCount.parse_obj({
            "task_type_name": obj.get("taskTypeName"),
            "models_count": obj.get("modelsCount")
        })
        return _obj


