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
            def resources() -> typing.Type['Resources']:
                return Resources
            isAutoCreated = schemas.BoolSchema
            rawConfiguration = schemas.StrSchema
            price = schemas.StrSchema
            description = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "status": status,
                "resources": resources,
                "isAutoCreated": isAutoCreated,
                "rawConfiguration": rawConfiguration,
                "price": price,
                "description": description,
            }
    
    isAutoCreated: MetaOapg.properties.isAutoCreated
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
    def __getitem__(self, name: typing_extensions.Literal["isAutoCreated"]) -> MetaOapg.properties.isAutoCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rawConfiguration"]) -> MetaOapg.properties.rawConfiguration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "status", "resources", "isAutoCreated", "rawConfiguration", "price", "description", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["isAutoCreated"]) -> MetaOapg.properties.isAutoCreated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rawConfiguration"]) -> MetaOapg.properties.rawConfiguration: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "status", "resources", "isAutoCreated", "rawConfiguration", "price", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        isAutoCreated: typing.Union[MetaOapg.properties.isAutoCreated, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        resources: 'Resources',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        rawConfiguration: typing.Union[MetaOapg.properties.rawConfiguration, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        price: typing.Union[MetaOapg.properties.price, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResourceGroupServerDataWithStatus':
        return super().__new__(
            cls,
            *_args,
            isAutoCreated=isAutoCreated,
            name=name,
            resources=resources,
            id=id,
            rawConfiguration=rawConfiguration,
            status=status,
            price=price,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.resources import Resources
