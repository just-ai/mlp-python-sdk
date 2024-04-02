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
            "tarifficationPrice",
            "isAutoCreated",
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
            def resources() -> typing.Type['ServerCapacityData']:
                return ServerCapacityData
            isAutoCreated = schemas.BoolSchema
            rawConfiguration = schemas.StrSchema
            tarifficationPrice = schemas.NumberSchema
            description = schemas.StrSchema
            
            
            class tarifficationPeriod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SECOND": "SECOND",
                        "MINUTE": "MINUTE",
                        "HOUR": "HOUR",
                        "DAY": "DAY",
                        "MONTH": "MONTH",
                        "YEAR": "YEAR",
                    }
                
                @schemas.classproperty
                def SECOND(cls):
                    return cls("SECOND")
                
                @schemas.classproperty
                def MINUTE(cls):
                    return cls("MINUTE")
                
                @schemas.classproperty
                def HOUR(cls):
                    return cls("HOUR")
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("DAY")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("MONTH")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("YEAR")
            __annotations__ = {
                "id": id,
                "name": name,
                "status": status,
                "resources": resources,
                "isAutoCreated": isAutoCreated,
                "rawConfiguration": rawConfiguration,
                "tarifficationPrice": tarifficationPrice,
                "description": description,
                "tarifficationPeriod": tarifficationPeriod,
            }
    
    tarifficationPrice: MetaOapg.properties.tarifficationPrice
    isAutoCreated: MetaOapg.properties.isAutoCreated
    name: MetaOapg.properties.name
    resources: 'ServerCapacityData'
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
    def __getitem__(self, name: typing_extensions.Literal["resources"]) -> 'ServerCapacityData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAutoCreated"]) -> MetaOapg.properties.isAutoCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rawConfiguration"]) -> MetaOapg.properties.rawConfiguration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tarifficationPrice"]) -> MetaOapg.properties.tarifficationPrice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tarifficationPeriod"]) -> MetaOapg.properties.tarifficationPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "status", "resources", "isAutoCreated", "rawConfiguration", "tarifficationPrice", "description", "tarifficationPeriod", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> 'ServerCapacityData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAutoCreated"]) -> MetaOapg.properties.isAutoCreated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rawConfiguration"]) -> MetaOapg.properties.rawConfiguration: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tarifficationPrice"]) -> MetaOapg.properties.tarifficationPrice: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tarifficationPeriod"]) -> typing.Union[MetaOapg.properties.tarifficationPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "status", "resources", "isAutoCreated", "rawConfiguration", "tarifficationPrice", "description", "tarifficationPeriod", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tarifficationPrice: typing.Union[MetaOapg.properties.tarifficationPrice, decimal.Decimal, int, float, ],
        isAutoCreated: typing.Union[MetaOapg.properties.isAutoCreated, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        resources: 'ServerCapacityData',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        rawConfiguration: typing.Union[MetaOapg.properties.rawConfiguration, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        tarifficationPeriod: typing.Union[MetaOapg.properties.tarifficationPeriod, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResourceGroupServerDataWithStatus':
        return super().__new__(
            cls,
            *_args,
            tarifficationPrice=tarifficationPrice,
            isAutoCreated=isAutoCreated,
            name=name,
            resources=resources,
            id=id,
            rawConfiguration=rawConfiguration,
            status=status,
            description=description,
            tarifficationPeriod=tarifficationPeriod,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.server_capacity_data import ServerCapacityData
