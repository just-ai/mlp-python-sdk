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


class InstanceStateTerminated(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            startedAt = schemas.StrSchema
            finishedAt = schemas.StrSchema
            exitCode = schemas.Int32Schema
            reason = schemas.StrSchema
            message = schemas.StrSchema
            __annotations__ = {
                "startedAt": startedAt,
                "finishedAt": finishedAt,
                "exitCode": exitCode,
                "reason": reason,
                "message": message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startedAt"]) -> MetaOapg.properties.startedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finishedAt"]) -> MetaOapg.properties.finishedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exitCode"]) -> MetaOapg.properties.exitCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["startedAt", "finishedAt", "exitCode", "reason", "message", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startedAt"]) -> typing.Union[MetaOapg.properties.startedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finishedAt"]) -> typing.Union[MetaOapg.properties.finishedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exitCode"]) -> typing.Union[MetaOapg.properties.exitCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["startedAt", "finishedAt", "exitCode", "reason", "message", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        startedAt: typing.Union[MetaOapg.properties.startedAt, str, schemas.Unset] = schemas.unset,
        finishedAt: typing.Union[MetaOapg.properties.finishedAt, str, schemas.Unset] = schemas.unset,
        exitCode: typing.Union[MetaOapg.properties.exitCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InstanceStateTerminated':
        return super().__new__(
            cls,
            *_args,
            startedAt=startedAt,
            finishedAt=finishedAt,
            exitCode=exitCode,
            reason=reason,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )
