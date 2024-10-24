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
from pydantic import BaseModel, Field, StrictStr
from mlp_api.models.audio_format_options import AudioFormatOptions

class TtsRequestData(BaseModel):
    """
    TtsRequestData
    """
    model: Optional[StrictStr] = None
    text: StrictStr = Field(...)
    voice: Optional[StrictStr] = None
    output_audio_spec: Optional[AudioFormatOptions] = Field(default=None, alias="outputAudioSpec")
    __properties = ["model", "text", "voice", "outputAudioSpec"]

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
    def from_json(cls, json_str: str) -> TtsRequestData:
        """Create an instance of TtsRequestData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of output_audio_spec
        if self.output_audio_spec:
            _dict['outputAudioSpec'] = self.output_audio_spec.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TtsRequestData:
        """Create an instance of TtsRequestData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TtsRequestData.parse_obj(obj)

        _obj = TtsRequestData.parse_obj({
            "model": obj.get("model"),
            "text": obj.get("text"),
            "voice": obj.get("voice"),
            "output_audio_spec": AudioFormatOptions.from_dict(obj.get("outputAudioSpec")) if obj.get("outputAudioSpec") is not None else None
        })
        return _obj


