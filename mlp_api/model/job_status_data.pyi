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


class JobStatusData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "accountId",
            "jobId",
            "state",
            "jobType",
            "done",
        }
        
        class properties:
            accountId = schemas.Int64Schema
            jobId = schemas.Int64Schema
            jobType = schemas.StrSchema
            state = schemas.StrSchema
            done = schemas.BoolSchema
            error = schemas.BoolSchema
            errorMessage = schemas.StrSchema
            __annotations__ = {
                "accountId": accountId,
                "jobId": jobId,
                "jobType": jobType,
                "state": state,
                "done": done,
                "error": error,
                "errorMessage": errorMessage,
            }
    
    accountId: MetaOapg.properties.accountId
    jobId: MetaOapg.properties.jobId
    state: MetaOapg.properties.state
    jobType: MetaOapg.properties.jobType
    done: MetaOapg.properties.done
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobType"]) -> MetaOapg.properties.jobType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["done"]) -> MetaOapg.properties.done: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorMessage"]) -> MetaOapg.properties.errorMessage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountId", "jobId", "jobType", "state", "done", "error", "errorMessage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobType"]) -> MetaOapg.properties.jobType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["done"]) -> MetaOapg.properties.done: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorMessage"]) -> typing.Union[MetaOapg.properties.errorMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountId", "jobId", "jobType", "state", "done", "error", "errorMessage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accountId: typing.Union[MetaOapg.properties.accountId, decimal.Decimal, int, ],
        jobId: typing.Union[MetaOapg.properties.jobId, decimal.Decimal, int, ],
        state: typing.Union[MetaOapg.properties.state, str, ],
        jobType: typing.Union[MetaOapg.properties.jobType, str, ],
        done: typing.Union[MetaOapg.properties.done, bool, ],
        error: typing.Union[MetaOapg.properties.error, bool, schemas.Unset] = schemas.unset,
        errorMessage: typing.Union[MetaOapg.properties.errorMessage, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobStatusData':
        return super().__new__(
            cls,
            *_args,
            accountId=accountId,
            jobId=jobId,
            state=state,
            jobType=jobType,
            done=done,
            error=error,
            errorMessage=errorMessage,
            _configuration=_configuration,
            **kwargs,
        )
