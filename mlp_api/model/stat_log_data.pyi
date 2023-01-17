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


class StatLogData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "args",
            "recordId",
            "accountId",
            "code",
            "level",
            "message",
            "timestamp",
        }
        
        class properties:
            accountId = schemas.Int64Schema
            recordId = schemas.Int64Schema
            timestamp = schemas.StrSchema
            
            
            class level(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INFO(cls):
                    return cls("INFO")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
            code = schemas.StrSchema
            args = schemas.DictSchema
            message = schemas.StrSchema
            userId = schemas.Int64Schema
            imageId = schemas.Int64Schema
            modelId = schemas.Int64Schema
            jobId = schemas.Int64Schema
            __annotations__ = {
                "accountId": accountId,
                "recordId": recordId,
                "timestamp": timestamp,
                "level": level,
                "code": code,
                "args": args,
                "message": message,
                "userId": userId,
                "imageId": imageId,
                "modelId": modelId,
                "jobId": jobId,
            }
    
    args: MetaOapg.properties.args
    recordId: MetaOapg.properties.recordId
    accountId: MetaOapg.properties.accountId
    code: MetaOapg.properties.code
    level: MetaOapg.properties.level
    message: MetaOapg.properties.message
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recordId"]) -> MetaOapg.properties.recordId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["args"]) -> MetaOapg.properties.args: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageId"]) -> MetaOapg.properties.imageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelId"]) -> MetaOapg.properties.modelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountId", "recordId", "timestamp", "level", "code", "args", "message", "userId", "imageId", "modelId", "jobId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recordId"]) -> MetaOapg.properties.recordId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["args"]) -> MetaOapg.properties.args: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageId"]) -> typing.Union[MetaOapg.properties.imageId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelId"]) -> typing.Union[MetaOapg.properties.modelId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> typing.Union[MetaOapg.properties.jobId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountId", "recordId", "timestamp", "level", "code", "args", "message", "userId", "imageId", "modelId", "jobId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        args: typing.Union[MetaOapg.properties.args, dict, frozendict.frozendict, ],
        recordId: typing.Union[MetaOapg.properties.recordId, decimal.Decimal, int, ],
        accountId: typing.Union[MetaOapg.properties.accountId, decimal.Decimal, int, ],
        code: typing.Union[MetaOapg.properties.code, str, ],
        level: typing.Union[MetaOapg.properties.level, str, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, ],
        userId: typing.Union[MetaOapg.properties.userId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        imageId: typing.Union[MetaOapg.properties.imageId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        modelId: typing.Union[MetaOapg.properties.modelId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        jobId: typing.Union[MetaOapg.properties.jobId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatLogData':
        return super().__new__(
            cls,
            *_args,
            args=args,
            recordId=recordId,
            accountId=accountId,
            code=code,
            level=level,
            message=message,
            timestamp=timestamp,
            userId=userId,
            imageId=imageId,
            modelId=modelId,
            jobId=jobId,
            _configuration=_configuration,
            **kwargs,
        )