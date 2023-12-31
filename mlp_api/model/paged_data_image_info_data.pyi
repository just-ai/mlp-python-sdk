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


class PagedDataImageInfoData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "records",
            "paging",
        }
        
        class properties:
        
            @staticmethod
            def paging() -> typing.Type['Pagination']:
                return Pagination
            
            
            class records(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DataImageInfoData']:
                        return DataImageInfoData
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DataImageInfoData'], typing.List['DataImageInfoData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'records':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DataImageInfoData':
                    return super().__getitem__(i)
            __annotations__ = {
                "paging": paging,
                "records": records,
            }
    
    records: MetaOapg.properties.records
    paging: 'Pagination'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paging"]) -> 'Pagination': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["records"]) -> MetaOapg.properties.records: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["paging", "records", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paging"]) -> 'Pagination': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["records"]) -> MetaOapg.properties.records: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["paging", "records", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        records: typing.Union[MetaOapg.properties.records, list, tuple, ],
        paging: 'Pagination',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PagedDataImageInfoData':
        return super().__new__(
            cls,
            *_args,
            records=records,
            paging=paging,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.data_image_info_data import DataImageInfoData
from mlp_api.model.pagination import Pagination
