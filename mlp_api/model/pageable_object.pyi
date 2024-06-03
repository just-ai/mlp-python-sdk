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


class PageableObject(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            offset = schemas.Int64Schema
        
            @staticmethod
            def sort() -> typing.Type['SortObject']:
                return SortObject
            pageNumber = schemas.Int32Schema
            pageSize = schemas.Int32Schema
            paged = schemas.BoolSchema
            unpaged = schemas.BoolSchema
            __annotations__ = {
                "offset": offset,
                "sort": sort,
                "pageNumber": pageNumber,
                "pageSize": pageSize,
                "paged": paged,
                "unpaged": unpaged,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> 'SortObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageSize"]) -> MetaOapg.properties.pageSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paged"]) -> MetaOapg.properties.paged: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unpaged"]) -> MetaOapg.properties.unpaged: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["offset", "sort", "pageNumber", "pageSize", "paged", "unpaged", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["offset"]) -> typing.Union[MetaOapg.properties.offset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> typing.Union['SortObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageNumber"]) -> typing.Union[MetaOapg.properties.pageNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageSize"]) -> typing.Union[MetaOapg.properties.pageSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paged"]) -> typing.Union[MetaOapg.properties.paged, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unpaged"]) -> typing.Union[MetaOapg.properties.unpaged, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["offset", "sort", "pageNumber", "pageSize", "paged", "unpaged", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        offset: typing.Union[MetaOapg.properties.offset, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sort: typing.Union['SortObject', schemas.Unset] = schemas.unset,
        pageNumber: typing.Union[MetaOapg.properties.pageNumber, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pageSize: typing.Union[MetaOapg.properties.pageSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        paged: typing.Union[MetaOapg.properties.paged, bool, schemas.Unset] = schemas.unset,
        unpaged: typing.Union[MetaOapg.properties.unpaged, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PageableObject':
        return super().__new__(
            cls,
            *_args,
            offset=offset,
            sort=sort,
            pageNumber=pageNumber,
            pageSize=pageSize,
            paged=paged,
            unpaged=unpaged,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.sort_object import SortObject
