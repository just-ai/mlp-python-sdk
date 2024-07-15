# coding: utf-8

"""
    Datatypes specification for GPT task type

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from mlp_api.models.parts_chat_message import PartsChatMessage
from mlp_api.models.text_chat_message import TextChatMessage
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

CHATMESSAGE_ONE_OF_SCHEMAS = ["PartsChatMessage", "TextChatMessage"]

class ChatMessage(BaseModel):
    """
    ChatMessage
    """
    # data type: TextChatMessage
    oneof_schema_1_validator: Optional[TextChatMessage] = None
    # data type: PartsChatMessage
    oneof_schema_2_validator: Optional[PartsChatMessage] = None
    if TYPE_CHECKING:
        actual_instance: Union[PartsChatMessage, TextChatMessage]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(CHATMESSAGE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
        'PartsChatMessage': 'PartsChatMessage',
        'TextChatMessage': 'TextChatMessage'
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ChatMessage.construct()
        error_messages = []
        match = 0
        # validate data type: TextChatMessage
        if not isinstance(v, TextChatMessage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TextChatMessage`")
        else:
            match += 1
        # validate data type: PartsChatMessage
        if not isinstance(v, PartsChatMessage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PartsChatMessage`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ChatMessage with oneOf schemas: PartsChatMessage, TextChatMessage. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ChatMessage with oneOf schemas: PartsChatMessage, TextChatMessage. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ChatMessage:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ChatMessage:
        """Returns the object represented by the json string"""
        instance = ChatMessage.construct()
        error_messages = []
        match = 0

        # deserialize data into TextChatMessage
        try:
            instance.actual_instance = TextChatMessage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PartsChatMessage
        try:
            instance.actual_instance = PartsChatMessage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ChatMessage with oneOf schemas: PartsChatMessage, TextChatMessage. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ChatMessage with oneOf schemas: PartsChatMessage, TextChatMessage. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


