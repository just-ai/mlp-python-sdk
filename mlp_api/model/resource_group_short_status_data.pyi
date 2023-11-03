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


class ResourceGroupShortStatusData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "servicesCount",
            "isDefault",
            "access",
            "name",
            "resourceGroupType",
            "serversCount",
            "enabledEviction",
            "enabledAutoScaling",
        }
        
        class properties:
            name = schemas.StrSchema
            isDefault = schemas.BoolSchema
            enabledAutoScaling = schemas.BoolSchema
            enabledEviction = schemas.BoolSchema
            
            
            class resourceGroupType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DOCKER(cls):
                    return cls("DOCKER")
                
                @schemas.classproperty
                def KUBERNETES(cls):
                    return cls("KUBERNETES")
                
                @schemas.classproperty
                def HOSTING_SERVER(cls):
                    return cls("HOSTING_SERVER")
            
            
            class access(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("PRIVATE")
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("PUBLIC")
            serversCount = schemas.Int32Schema
            servicesCount = schemas.Int32Schema
            ownerId = schemas.Int64Schema
            __annotations__ = {
                "name": name,
                "isDefault": isDefault,
                "enabledAutoScaling": enabledAutoScaling,
                "enabledEviction": enabledEviction,
                "resourceGroupType": resourceGroupType,
                "access": access,
                "serversCount": serversCount,
                "servicesCount": servicesCount,
                "ownerId": ownerId,
            }
    
    servicesCount: MetaOapg.properties.servicesCount
    isDefault: MetaOapg.properties.isDefault
    access: MetaOapg.properties.access
    name: MetaOapg.properties.name
    resourceGroupType: MetaOapg.properties.resourceGroupType
    serversCount: MetaOapg.properties.serversCount
    enabledEviction: MetaOapg.properties.enabledEviction
    enabledAutoScaling: MetaOapg.properties.enabledAutoScaling
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabledAutoScaling"]) -> MetaOapg.properties.enabledAutoScaling: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabledEviction"]) -> MetaOapg.properties.enabledEviction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceGroupType"]) -> MetaOapg.properties.resourceGroupType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serversCount"]) -> MetaOapg.properties.serversCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["servicesCount"]) -> MetaOapg.properties.servicesCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerId"]) -> MetaOapg.properties.ownerId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "isDefault", "enabledAutoScaling", "enabledEviction", "resourceGroupType", "access", "serversCount", "servicesCount", "ownerId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabledAutoScaling"]) -> MetaOapg.properties.enabledAutoScaling: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabledEviction"]) -> MetaOapg.properties.enabledEviction: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceGroupType"]) -> MetaOapg.properties.resourceGroupType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serversCount"]) -> MetaOapg.properties.serversCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["servicesCount"]) -> MetaOapg.properties.servicesCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerId"]) -> typing.Union[MetaOapg.properties.ownerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "isDefault", "enabledAutoScaling", "enabledEviction", "resourceGroupType", "access", "serversCount", "servicesCount", "ownerId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        servicesCount: typing.Union[MetaOapg.properties.servicesCount, decimal.Decimal, int, ],
        isDefault: typing.Union[MetaOapg.properties.isDefault, bool, ],
        access: typing.Union[MetaOapg.properties.access, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        resourceGroupType: typing.Union[MetaOapg.properties.resourceGroupType, str, ],
        serversCount: typing.Union[MetaOapg.properties.serversCount, decimal.Decimal, int, ],
        enabledEviction: typing.Union[MetaOapg.properties.enabledEviction, bool, ],
        enabledAutoScaling: typing.Union[MetaOapg.properties.enabledAutoScaling, bool, ],
        ownerId: typing.Union[MetaOapg.properties.ownerId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResourceGroupShortStatusData':
        return super().__new__(
            cls,
            *_args,
            servicesCount=servicesCount,
            isDefault=isDefault,
            access=access,
            name=name,
            resourceGroupType=resourceGroupType,
            serversCount=serversCount,
            enabledEviction=enabledEviction,
            enabledAutoScaling=enabledAutoScaling,
            ownerId=ownerId,
            _configuration=_configuration,
            **kwargs,
        )
