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


class ResourceGroupAutoScalingConfiguration(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "minServersCount",
        }
        
        class properties:
            minServersCount = schemas.Int32Schema
            serverId = schemas.Int64Schema
            serverConfiguration = schemas.StrSchema
            maxServersCount = schemas.Int32Schema
            cooldownPeriodMinutes = schemas.Int32Schema
            __annotations__ = {
                "minServersCount": minServersCount,
                "serverId": serverId,
                "serverConfiguration": serverConfiguration,
                "maxServersCount": maxServersCount,
                "cooldownPeriodMinutes": cooldownPeriodMinutes,
            }
    
    minServersCount: MetaOapg.properties.minServersCount
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minServersCount"]) -> MetaOapg.properties.minServersCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serverId"]) -> MetaOapg.properties.serverId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serverConfiguration"]) -> MetaOapg.properties.serverConfiguration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxServersCount"]) -> MetaOapg.properties.maxServersCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cooldownPeriodMinutes"]) -> MetaOapg.properties.cooldownPeriodMinutes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["minServersCount", "serverId", "serverConfiguration", "maxServersCount", "cooldownPeriodMinutes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minServersCount"]) -> MetaOapg.properties.minServersCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serverId"]) -> typing.Union[MetaOapg.properties.serverId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serverConfiguration"]) -> typing.Union[MetaOapg.properties.serverConfiguration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxServersCount"]) -> typing.Union[MetaOapg.properties.maxServersCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cooldownPeriodMinutes"]) -> typing.Union[MetaOapg.properties.cooldownPeriodMinutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["minServersCount", "serverId", "serverConfiguration", "maxServersCount", "cooldownPeriodMinutes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        minServersCount: typing.Union[MetaOapg.properties.minServersCount, decimal.Decimal, int, ],
        serverId: typing.Union[MetaOapg.properties.serverId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        serverConfiguration: typing.Union[MetaOapg.properties.serverConfiguration, str, schemas.Unset] = schemas.unset,
        maxServersCount: typing.Union[MetaOapg.properties.maxServersCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cooldownPeriodMinutes: typing.Union[MetaOapg.properties.cooldownPeriodMinutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResourceGroupAutoScalingConfiguration':
        return super().__new__(
            cls,
            *_args,
            minServersCount=minServersCount,
            serverId=serverId,
            serverConfiguration=serverConfiguration,
            maxServersCount=maxServersCount,
            cooldownPeriodMinutes=cooldownPeriodMinutes,
            _configuration=_configuration,
            **kwargs,
        )
