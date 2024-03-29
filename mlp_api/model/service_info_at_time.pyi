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


class ServiceInfoAtTime(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "modelNameAtTime",
            "modelId",
        }
        
        class properties:
            modelId = schemas.Int64Schema
            modelNameAtTime = schemas.StrSchema
            actualModelName = schemas.StrSchema
            __annotations__ = {
                "modelId": modelId,
                "modelNameAtTime": modelNameAtTime,
                "actualModelName": actualModelName,
            }
    
    modelNameAtTime: MetaOapg.properties.modelNameAtTime
    modelId: MetaOapg.properties.modelId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelId"]) -> MetaOapg.properties.modelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelNameAtTime"]) -> MetaOapg.properties.modelNameAtTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actualModelName"]) -> MetaOapg.properties.actualModelName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["modelId", "modelNameAtTime", "actualModelName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelId"]) -> MetaOapg.properties.modelId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelNameAtTime"]) -> MetaOapg.properties.modelNameAtTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actualModelName"]) -> typing.Union[MetaOapg.properties.actualModelName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["modelId", "modelNameAtTime", "actualModelName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        modelNameAtTime: typing.Union[MetaOapg.properties.modelNameAtTime, str, ],
        modelId: typing.Union[MetaOapg.properties.modelId, decimal.Decimal, int, ],
        actualModelName: typing.Union[MetaOapg.properties.actualModelName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServiceInfoAtTime':
        return super().__new__(
            cls,
            *_args,
            modelNameAtTime=modelNameAtTime,
            modelId=modelId,
            actualModelName=actualModelName,
            _configuration=_configuration,
            **kwargs,
        )
