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


class ModelDefaults(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "batches",
            "resourceGroup",
            "retries",
            "timeouts",
            "limits",
        }
        
        class properties:
        
            @staticmethod
            def timeouts() -> typing.Type['ModelTimeoutsData']:
                return ModelTimeoutsData
        
            @staticmethod
            def retries() -> typing.Type['ModelRetriesData']:
                return ModelRetriesData
        
            @staticmethod
            def batches() -> typing.Type['ModelBatchesData']:
                return ModelBatchesData
        
            @staticmethod
            def limits() -> typing.Type['ModelLimitsData']:
                return ModelLimitsData
            resourceGroup = schemas.StrSchema
            __annotations__ = {
                "timeouts": timeouts,
                "retries": retries,
                "batches": batches,
                "limits": limits,
                "resourceGroup": resourceGroup,
            }
    
    batches: 'ModelBatchesData'
    resourceGroup: MetaOapg.properties.resourceGroup
    retries: 'ModelRetriesData'
    timeouts: 'ModelTimeoutsData'
    limits: 'ModelLimitsData'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeouts"]) -> 'ModelTimeoutsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retries"]) -> 'ModelRetriesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batches"]) -> 'ModelBatchesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limits"]) -> 'ModelLimitsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceGroup"]) -> MetaOapg.properties.resourceGroup: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timeouts", "retries", "batches", "limits", "resourceGroup", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeouts"]) -> 'ModelTimeoutsData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retries"]) -> 'ModelRetriesData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batches"]) -> 'ModelBatchesData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limits"]) -> 'ModelLimitsData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceGroup"]) -> MetaOapg.properties.resourceGroup: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timeouts", "retries", "batches", "limits", "resourceGroup", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        batches: 'ModelBatchesData',
        resourceGroup: typing.Union[MetaOapg.properties.resourceGroup, str, ],
        retries: 'ModelRetriesData',
        timeouts: 'ModelTimeoutsData',
        limits: 'ModelLimitsData',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelDefaults':
        return super().__new__(
            cls,
            *_args,
            batches=batches,
            resourceGroup=resourceGroup,
            retries=retries,
            timeouts=timeouts,
            limits=limits,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.model_batches_data import ModelBatchesData
from mlp_api.model.model_limits_data import ModelLimitsData
from mlp_api.model.model_retries_data import ModelRetriesData
from mlp_api.model.model_timeouts_data import ModelTimeoutsData
