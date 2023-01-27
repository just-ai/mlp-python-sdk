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


class ModelLimitsData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "ephemeralDiskRequest",
            "gpuRequested",
            "cpuLimit",
            "memoryRequest",
            "memoryLimit",
            "cpuRequest",
            "ephemeralDiskLimit",
        }
        
        class properties:
            cpuRequest = schemas.StrSchema
            cpuLimit = schemas.StrSchema
            memoryRequest = schemas.StrSchema
            memoryLimit = schemas.StrSchema
            ephemeralDiskRequest = schemas.StrSchema
            ephemeralDiskLimit = schemas.StrSchema
            gpuRequested = schemas.BoolSchema
            __annotations__ = {
                "cpuRequest": cpuRequest,
                "cpuLimit": cpuLimit,
                "memoryRequest": memoryRequest,
                "memoryLimit": memoryLimit,
                "ephemeralDiskRequest": ephemeralDiskRequest,
                "ephemeralDiskLimit": ephemeralDiskLimit,
                "gpuRequested": gpuRequested,
            }
    
    ephemeralDiskRequest: MetaOapg.properties.ephemeralDiskRequest
    gpuRequested: MetaOapg.properties.gpuRequested
    cpuLimit: MetaOapg.properties.cpuLimit
    memoryRequest: MetaOapg.properties.memoryRequest
    memoryLimit: MetaOapg.properties.memoryLimit
    cpuRequest: MetaOapg.properties.cpuRequest
    ephemeralDiskLimit: MetaOapg.properties.ephemeralDiskLimit
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpuRequest"]) -> MetaOapg.properties.cpuRequest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpuLimit"]) -> MetaOapg.properties.cpuLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memoryRequest"]) -> MetaOapg.properties.memoryRequest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memoryLimit"]) -> MetaOapg.properties.memoryLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ephemeralDiskRequest"]) -> MetaOapg.properties.ephemeralDiskRequest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ephemeralDiskLimit"]) -> MetaOapg.properties.ephemeralDiskLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gpuRequested"]) -> MetaOapg.properties.gpuRequested: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cpuRequest", "cpuLimit", "memoryRequest", "memoryLimit", "ephemeralDiskRequest", "ephemeralDiskLimit", "gpuRequested", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpuRequest"]) -> MetaOapg.properties.cpuRequest: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpuLimit"]) -> MetaOapg.properties.cpuLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memoryRequest"]) -> MetaOapg.properties.memoryRequest: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memoryLimit"]) -> MetaOapg.properties.memoryLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ephemeralDiskRequest"]) -> MetaOapg.properties.ephemeralDiskRequest: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ephemeralDiskLimit"]) -> MetaOapg.properties.ephemeralDiskLimit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gpuRequested"]) -> MetaOapg.properties.gpuRequested: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cpuRequest", "cpuLimit", "memoryRequest", "memoryLimit", "ephemeralDiskRequest", "ephemeralDiskLimit", "gpuRequested", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ephemeralDiskRequest: typing.Union[MetaOapg.properties.ephemeralDiskRequest, str, ],
        gpuRequested: typing.Union[MetaOapg.properties.gpuRequested, bool, ],
        cpuLimit: typing.Union[MetaOapg.properties.cpuLimit, str, ],
        memoryRequest: typing.Union[MetaOapg.properties.memoryRequest, str, ],
        memoryLimit: typing.Union[MetaOapg.properties.memoryLimit, str, ],
        cpuRequest: typing.Union[MetaOapg.properties.cpuRequest, str, ],
        ephemeralDiskLimit: typing.Union[MetaOapg.properties.ephemeralDiskLimit, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelLimitsData':
        return super().__new__(
            cls,
            *_args,
            ephemeralDiskRequest=ephemeralDiskRequest,
            gpuRequested=gpuRequested,
            cpuLimit=cpuLimit,
            memoryRequest=memoryRequest,
            memoryLimit=memoryLimit,
            cpuRequest=cpuRequest,
            ephemeralDiskLimit=ephemeralDiskLimit,
            _configuration=_configuration,
            **kwargs,
        )
