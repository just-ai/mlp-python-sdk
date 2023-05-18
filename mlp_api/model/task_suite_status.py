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


class TaskSuiteStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "accountId",
            "created",
            "completed",
            "originalDatasetId",
            "newDatasetId",
        }
        
        class properties:
            accountId = schemas.Int64Schema
            originalDatasetId = schemas.Int64Schema
            newDatasetId = schemas.Int64Schema
            created = schemas.DateTimeSchema
            completed = schemas.BoolSchema
            __annotations__ = {
                "accountId": accountId,
                "originalDatasetId": originalDatasetId,
                "newDatasetId": newDatasetId,
                "created": created,
                "completed": completed,
            }
    
    accountId: MetaOapg.properties.accountId
    created: MetaOapg.properties.created
    completed: MetaOapg.properties.completed
    originalDatasetId: MetaOapg.properties.originalDatasetId
    newDatasetId: MetaOapg.properties.newDatasetId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originalDatasetId"]) -> MetaOapg.properties.originalDatasetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["newDatasetId"]) -> MetaOapg.properties.newDatasetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completed"]) -> MetaOapg.properties.completed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountId", "originalDatasetId", "newDatasetId", "created", "completed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originalDatasetId"]) -> MetaOapg.properties.originalDatasetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["newDatasetId"]) -> MetaOapg.properties.newDatasetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completed"]) -> MetaOapg.properties.completed: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountId", "originalDatasetId", "newDatasetId", "created", "completed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accountId: typing.Union[MetaOapg.properties.accountId, decimal.Decimal, int, ],
        created: typing.Union[MetaOapg.properties.created, str, datetime, ],
        completed: typing.Union[MetaOapg.properties.completed, bool, ],
        originalDatasetId: typing.Union[MetaOapg.properties.originalDatasetId, decimal.Decimal, int, ],
        newDatasetId: typing.Union[MetaOapg.properties.newDatasetId, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaskSuiteStatus':
        return super().__new__(
            cls,
            *_args,
            accountId=accountId,
            created=created,
            completed=completed,
            originalDatasetId=originalDatasetId,
            newDatasetId=newDatasetId,
            _configuration=_configuration,
            **kwargs,
        )
