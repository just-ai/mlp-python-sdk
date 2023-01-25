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


class Sort(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            unsorted = schemas.BoolSchema
            sorted = schemas.BoolSchema
            empty = schemas.BoolSchema
            __annotations__ = {
                "unsorted": unsorted,
                "sorted": sorted,
                "empty": empty,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unsorted"]) -> MetaOapg.properties.unsorted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sorted"]) -> MetaOapg.properties.sorted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["empty"]) -> MetaOapg.properties.empty: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["unsorted", "sorted", "empty", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unsorted"]) -> typing.Union[MetaOapg.properties.unsorted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sorted"]) -> typing.Union[MetaOapg.properties.sorted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["empty"]) -> typing.Union[MetaOapg.properties.empty, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["unsorted", "sorted", "empty", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        unsorted: typing.Union[MetaOapg.properties.unsorted, bool, schemas.Unset] = schemas.unset,
        sorted: typing.Union[MetaOapg.properties.sorted, bool, schemas.Unset] = schemas.unset,
        empty: typing.Union[MetaOapg.properties.empty, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Sort':
        return super().__new__(
            cls,
            *_args,
            unsorted=unsorted,
            sorted=sorted,
            empty=empty,
            _configuration=_configuration,
            **kwargs,
        )
