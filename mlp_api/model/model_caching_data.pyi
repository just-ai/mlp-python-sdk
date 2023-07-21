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


class ModelCachingData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "mongoUri",
            "recordsLimit",
            "enabled",
            "collectionName",
        }
        
        class properties:
            enabled = schemas.BoolSchema
            mongoUri = schemas.StrSchema
            collectionName = schemas.StrSchema
            recordsLimit = schemas.Int64Schema
            __annotations__ = {
                "enabled": enabled,
                "mongoUri": mongoUri,
                "collectionName": collectionName,
                "recordsLimit": recordsLimit,
            }
    
    mongoUri: MetaOapg.properties.mongoUri
    recordsLimit: MetaOapg.properties.recordsLimit
    enabled: MetaOapg.properties.enabled
    collectionName: MetaOapg.properties.collectionName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mongoUri"]) -> MetaOapg.properties.mongoUri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collectionName"]) -> MetaOapg.properties.collectionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recordsLimit"]) -> MetaOapg.properties.recordsLimit: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enabled", "mongoUri", "collectionName", "recordsLimit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mongoUri"]) -> MetaOapg.properties.mongoUri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collectionName"]) -> MetaOapg.properties.collectionName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recordsLimit"]) -> MetaOapg.properties.recordsLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enabled", "mongoUri", "collectionName", "recordsLimit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        mongoUri: typing.Union[MetaOapg.properties.mongoUri, str, ],
        recordsLimit: typing.Union[MetaOapg.properties.recordsLimit, decimal.Decimal, int, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, ],
        collectionName: typing.Union[MetaOapg.properties.collectionName, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelCachingData':
        return super().__new__(
            cls,
            *_args,
            mongoUri=mongoUri,
            recordsLimit=recordsLimit,
            enabled=enabled,
            collectionName=collectionName,
            _configuration=_configuration,
            **kwargs,
        )
