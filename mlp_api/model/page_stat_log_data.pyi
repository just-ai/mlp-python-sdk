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


class PageStatLogData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            totalElements = schemas.Int64Schema
            totalPages = schemas.Int32Schema
            size = schemas.Int32Schema
            
            
            class content(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StatLogData']:
                        return StatLogData
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['StatLogData'], typing.List['StatLogData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'content':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StatLogData':
                    return super().__getitem__(i)
            number = schemas.Int32Schema
        
            @staticmethod
            def sort() -> typing.Type['Sort']:
                return Sort
            first = schemas.BoolSchema
            numberOfElements = schemas.Int32Schema
            last = schemas.BoolSchema
        
            @staticmethod
            def pageable() -> typing.Type['PageableObject']:
                return PageableObject
            empty = schemas.BoolSchema
            __annotations__ = {
                "totalElements": totalElements,
                "totalPages": totalPages,
                "size": size,
                "content": content,
                "number": number,
                "sort": sort,
                "first": first,
                "numberOfElements": numberOfElements,
                "last": last,
                "pageable": pageable,
                "empty": empty,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalElements"]) -> MetaOapg.properties.totalElements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort"]) -> 'Sort': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfElements"]) -> MetaOapg.properties.numberOfElements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageable"]) -> 'PageableObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["empty"]) -> MetaOapg.properties.empty: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["totalElements", "totalPages", "size", "content", "number", "sort", "first", "numberOfElements", "last", "pageable", "empty", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalElements"]) -> typing.Union[MetaOapg.properties.totalElements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> typing.Union[MetaOapg.properties.totalPages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content"]) -> typing.Union[MetaOapg.properties.content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort"]) -> typing.Union['Sort', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first"]) -> typing.Union[MetaOapg.properties.first, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfElements"]) -> typing.Union[MetaOapg.properties.numberOfElements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last"]) -> typing.Union[MetaOapg.properties.last, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageable"]) -> typing.Union['PageableObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["empty"]) -> typing.Union[MetaOapg.properties.empty, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["totalElements", "totalPages", "size", "content", "number", "sort", "first", "numberOfElements", "last", "pageable", "empty", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        totalElements: typing.Union[MetaOapg.properties.totalElements, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        content: typing.Union[MetaOapg.properties.content, list, tuple, schemas.Unset] = schemas.unset,
        number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sort: typing.Union['Sort', schemas.Unset] = schemas.unset,
        first: typing.Union[MetaOapg.properties.first, bool, schemas.Unset] = schemas.unset,
        numberOfElements: typing.Union[MetaOapg.properties.numberOfElements, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last: typing.Union[MetaOapg.properties.last, bool, schemas.Unset] = schemas.unset,
        pageable: typing.Union['PageableObject', schemas.Unset] = schemas.unset,
        empty: typing.Union[MetaOapg.properties.empty, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PageStatLogData':
        return super().__new__(
            cls,
            *_args,
            totalElements=totalElements,
            totalPages=totalPages,
            size=size,
            content=content,
            number=number,
            sort=sort,
            first=first,
            numberOfElements=numberOfElements,
            last=last,
            pageable=pageable,
            empty=empty,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.pageable_object import PageableObject
from mlp_api.model.sort import Sort
from mlp_api.model.stat_log_data import StatLogData
