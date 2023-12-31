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


class PredictConfigPK(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "accountId",
            "modelId",
            "configId",
        }
        
        class properties:
            accountId = schemas.Int64Schema
            modelId = schemas.Int64Schema
            configId = schemas.Int64Schema
            __annotations__ = {
                "accountId": accountId,
                "modelId": modelId,
                "configId": configId,
            }
    
    accountId: MetaOapg.properties.accountId
    modelId: MetaOapg.properties.modelId
    configId: MetaOapg.properties.configId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelId"]) -> MetaOapg.properties.modelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configId"]) -> MetaOapg.properties.configId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountId", "modelId", "configId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelId"]) -> MetaOapg.properties.modelId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configId"]) -> MetaOapg.properties.configId: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountId", "modelId", "configId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accountId: typing.Union[MetaOapg.properties.accountId, decimal.Decimal, int, ],
        modelId: typing.Union[MetaOapg.properties.modelId, decimal.Decimal, int, ],
        configId: typing.Union[MetaOapg.properties.configId, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PredictConfigPK':
        return super().__new__(
            cls,
            *_args,
            accountId=accountId,
            modelId=modelId,
            configId=configId,
            _configuration=_configuration,
            **kwargs,
        )
