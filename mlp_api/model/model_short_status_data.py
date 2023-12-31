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


class ModelShortStatusData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "instances",
            "state",
        }
        
        class properties:
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "RUNNING": "RUNNING",
                        "STARTING": "STARTING",
                        "INACTIVE": "INACTIVE",
                        "SLEEPING": "SLEEPING",
                    }
                
                @schemas.classproperty
                def RUNNING(cls):
                    return cls("RUNNING")
                
                @schemas.classproperty
                def STARTING(cls):
                    return cls("STARTING")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
                
                @schemas.classproperty
                def SLEEPING(cls):
                    return cls("SLEEPING")
        
            @staticmethod
            def instances() -> typing.Type['InstancesStatusData']:
                return InstancesStatusData
        
            @staticmethod
            def lastJob() -> typing.Type['JobStatusData']:
                return JobStatusData
            startTimeSeconds = schemas.Float32Schema
            __annotations__ = {
                "state": state,
                "instances": instances,
                "lastJob": lastJob,
                "startTimeSeconds": startTimeSeconds,
            }
    
    instances: 'InstancesStatusData'
    state: MetaOapg.properties.state
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instances"]) -> 'InstancesStatusData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastJob"]) -> 'JobStatusData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTimeSeconds"]) -> MetaOapg.properties.startTimeSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["state", "instances", "lastJob", "startTimeSeconds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instances"]) -> 'InstancesStatusData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastJob"]) -> typing.Union['JobStatusData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTimeSeconds"]) -> typing.Union[MetaOapg.properties.startTimeSeconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["state", "instances", "lastJob", "startTimeSeconds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        instances: 'InstancesStatusData',
        state: typing.Union[MetaOapg.properties.state, str, ],
        lastJob: typing.Union['JobStatusData', schemas.Unset] = schemas.unset,
        startTimeSeconds: typing.Union[MetaOapg.properties.startTimeSeconds, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelShortStatusData':
        return super().__new__(
            cls,
            *_args,
            instances=instances,
            state=state,
            lastJob=lastJob,
            startTimeSeconds=startTimeSeconds,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.instances_status_data import InstancesStatusData
from mlp_api.model.job_status_data import JobStatusData
