# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from mlp_api import schemas  # noqa: F401


class InstanceLastState(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def running() -> typing.Type['InstanceStateRunning']:
                return InstanceStateRunning
        
            @staticmethod
            def terminated() -> typing.Type['InstanceStateTerminated']:
                return InstanceStateTerminated
        
            @staticmethod
            def waiting() -> typing.Type['InstanceStateWaiting']:
                return InstanceStateWaiting
            __annotations__ = {
                "running": running,
                "terminated": terminated,
                "waiting": waiting,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["running"]) -> 'InstanceStateRunning': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminated"]) -> 'InstanceStateTerminated': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["waiting"]) -> 'InstanceStateWaiting': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["running", "terminated", "waiting", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["running"]) -> typing.Union['InstanceStateRunning', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminated"]) -> typing.Union['InstanceStateTerminated', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["waiting"]) -> typing.Union['InstanceStateWaiting', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["running", "terminated", "waiting", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        running: typing.Union['InstanceStateRunning', schemas.Unset] = schemas.unset,
        terminated: typing.Union['InstanceStateTerminated', schemas.Unset] = schemas.unset,
        waiting: typing.Union['InstanceStateWaiting', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InstanceLastState':
        return super().__new__(
            cls,
            *_args,
            running=running,
            terminated=terminated,
            waiting=waiting,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.instance_state_running import InstanceStateRunning
from mlp_api.model.instance_state_terminated import InstanceStateTerminated
from mlp_api.model.instance_state_waiting import InstanceStateWaiting
