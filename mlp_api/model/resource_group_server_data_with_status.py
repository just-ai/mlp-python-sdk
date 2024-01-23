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


class ResourceGroupServerDataWithStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "resources",
            "id",
            "rawConfiguration",
            "status",
        }
        
        class properties:
            id = schemas.Int64Schema
            name = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "RUNNING": "RUNNING",
                        "STARTING": "STARTING",
                        "STOPPED": "STOPPED",
                        "UNAVAILABLE": "UNAVAILABLE",
                        "DELETING": "DELETING",
                    }
                
                @schemas.classproperty
                def RUNNING(cls):
                    return cls("RUNNING")
                
                @schemas.classproperty
                def STARTING(cls):
                    return cls("STARTING")
                
                @schemas.classproperty
                def STOPPED(cls):
                    return cls("STOPPED")
                
                @schemas.classproperty
                def UNAVAILABLE(cls):
                    return cls("UNAVAILABLE")
                
                @schemas.classproperty
                def DELETING(cls):
                    return cls("DELETING")
        
            @staticmethod
            def resources() -> typing.Type['Resources']:
                return Resources
            rawConfiguration = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "status": status,
                "resources": resources,
                "rawConfiguration": rawConfiguration,
            }
    
    name: MetaOapg.properties.name
    resources: 'Resources'
    id: MetaOapg.properties.id
    rawConfiguration: MetaOapg.properties.rawConfiguration
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resources"]) -> 'Resources': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rawConfiguration"]) -> MetaOapg.properties.rawConfiguration: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "status", "resources", "rawConfiguration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> 'Resources': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rawConfiguration"]) -> MetaOapg.properties.rawConfiguration: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "status", "resources", "rawConfiguration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        resources: 'Resources',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        rawConfiguration: typing.Union[MetaOapg.properties.rawConfiguration, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResourceGroupServerDataWithStatus':
        return super().__new__(
            cls,
            *_args,
            name=name,
            resources=resources,
            id=id,
            rawConfiguration=rawConfiguration,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.resources import Resources
