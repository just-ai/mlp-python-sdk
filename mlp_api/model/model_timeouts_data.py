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


class ModelTimeoutsData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "predictTimeoutSec",
            "podStartTimeoutSec",
        }
        
        class properties:
            podStartTimeoutSec = schemas.Int64Schema
            predictTimeoutSec = schemas.Int64Schema
            fitTimeoutSec = schemas.Int64Schema
            __annotations__ = {
                "podStartTimeoutSec": podStartTimeoutSec,
                "predictTimeoutSec": predictTimeoutSec,
                "fitTimeoutSec": fitTimeoutSec,
            }
    
    predictTimeoutSec: MetaOapg.properties.predictTimeoutSec
    podStartTimeoutSec: MetaOapg.properties.podStartTimeoutSec
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["podStartTimeoutSec"]) -> MetaOapg.properties.podStartTimeoutSec: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["predictTimeoutSec"]) -> MetaOapg.properties.predictTimeoutSec: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fitTimeoutSec"]) -> MetaOapg.properties.fitTimeoutSec: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["podStartTimeoutSec", "predictTimeoutSec", "fitTimeoutSec", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["podStartTimeoutSec"]) -> MetaOapg.properties.podStartTimeoutSec: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["predictTimeoutSec"]) -> MetaOapg.properties.predictTimeoutSec: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fitTimeoutSec"]) -> typing.Union[MetaOapg.properties.fitTimeoutSec, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["podStartTimeoutSec", "predictTimeoutSec", "fitTimeoutSec", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        predictTimeoutSec: typing.Union[MetaOapg.properties.predictTimeoutSec, decimal.Decimal, int, ],
        podStartTimeoutSec: typing.Union[MetaOapg.properties.podStartTimeoutSec, decimal.Decimal, int, ],
        fitTimeoutSec: typing.Union[MetaOapg.properties.fitTimeoutSec, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelTimeoutsData':
        return super().__new__(
            cls,
            *_args,
            predictTimeoutSec=predictTimeoutSec,
            podStartTimeoutSec=podStartTimeoutSec,
            fitTimeoutSec=fitTimeoutSec,
            _configuration=_configuration,
            **kwargs,
        )
