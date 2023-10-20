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


class ResourceGroupData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "tolerations",
            "name",
            "affinity",
        }
        
        class properties:
            name = schemas.StrSchema
            tolerations = schemas.DictSchema
            affinity = schemas.DictSchema
            accountId = schemas.Int64Schema
            accountName = schemas.StrSchema
            ownerId = schemas.Int64Schema
            isDefault = schemas.BoolSchema
            enabledAutoScaling = schemas.BoolSchema
            enabledEviction = schemas.BoolSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "KUBERNETES": "KUBERNETES",
                    }
                
                @schemas.classproperty
                def KUBERNETES(cls):
                    return cls("KUBERNETES")
            
            
            class access(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PRIVATE": "PRIVATE",
                        "PUBLIC": "PUBLIC",
                    }
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("PRIVATE")
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("PUBLIC")
            __annotations__ = {
                "name": name,
                "tolerations": tolerations,
                "affinity": affinity,
                "accountId": accountId,
                "accountName": accountName,
                "ownerId": ownerId,
                "isDefault": isDefault,
                "enabledAutoScaling": enabledAutoScaling,
                "enabledEviction": enabledEviction,
                "type": type,
                "access": access,
            }
    
    tolerations: MetaOapg.properties.tolerations
    name: MetaOapg.properties.name
    affinity: MetaOapg.properties.affinity
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tolerations"]) -> MetaOapg.properties.tolerations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["affinity"]) -> MetaOapg.properties.affinity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountName"]) -> MetaOapg.properties.accountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerId"]) -> MetaOapg.properties.ownerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabledAutoScaling"]) -> MetaOapg.properties.enabledAutoScaling: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabledEviction"]) -> MetaOapg.properties.enabledEviction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "tolerations", "affinity", "accountId", "accountName", "ownerId", "isDefault", "enabledAutoScaling", "enabledEviction", "type", "access", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tolerations"]) -> MetaOapg.properties.tolerations: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["affinity"]) -> MetaOapg.properties.affinity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> typing.Union[MetaOapg.properties.accountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountName"]) -> typing.Union[MetaOapg.properties.accountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerId"]) -> typing.Union[MetaOapg.properties.ownerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDefault"]) -> typing.Union[MetaOapg.properties.isDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabledAutoScaling"]) -> typing.Union[MetaOapg.properties.enabledAutoScaling, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabledEviction"]) -> typing.Union[MetaOapg.properties.enabledEviction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> typing.Union[MetaOapg.properties.access, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "tolerations", "affinity", "accountId", "accountName", "ownerId", "isDefault", "enabledAutoScaling", "enabledEviction", "type", "access", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tolerations: typing.Union[MetaOapg.properties.tolerations, dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        affinity: typing.Union[MetaOapg.properties.affinity, dict, frozendict.frozendict, ],
        accountId: typing.Union[MetaOapg.properties.accountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        accountName: typing.Union[MetaOapg.properties.accountName, str, schemas.Unset] = schemas.unset,
        ownerId: typing.Union[MetaOapg.properties.ownerId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isDefault: typing.Union[MetaOapg.properties.isDefault, bool, schemas.Unset] = schemas.unset,
        enabledAutoScaling: typing.Union[MetaOapg.properties.enabledAutoScaling, bool, schemas.Unset] = schemas.unset,
        enabledEviction: typing.Union[MetaOapg.properties.enabledEviction, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        access: typing.Union[MetaOapg.properties.access, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResourceGroupData':
        return super().__new__(
            cls,
            *_args,
            tolerations=tolerations,
            name=name,
            affinity=affinity,
            accountId=accountId,
            accountName=accountName,
            ownerId=ownerId,
            isDefault=isDefault,
            enabledAutoScaling=enabledAutoScaling,
            enabledEviction=enabledEviction,
            type=type,
            access=access,
            _configuration=_configuration,
            **kwargs,
        )
