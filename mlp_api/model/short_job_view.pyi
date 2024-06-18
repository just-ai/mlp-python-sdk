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


class ShortJobView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "currentStep",
            "jobId",
            "children",
            "percentage",
            "title",
            "viewStatus",
        }
        
        class properties:
            jobId = schemas.StrSchema
            title = schemas.StrSchema
            
            
            class children(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ShortJobView']:
                        return ShortJobView
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ShortJobView'], typing.List['ShortJobView']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'children':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ShortJobView':
                    return super().__getitem__(i)
            percentage = schemas.Float64Schema
            
            
            class viewStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def IDLE(cls):
                    return cls("IDLE")
                
                @schemas.classproperty
                def RUN(cls):
                    return cls("RUN")
                
                @schemas.classproperty
                def REVERTING(cls):
                    return cls("REVERTING")
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("COMPLETED")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
                
                @schemas.classproperty
                def REVERTED(cls):
                    return cls("REVERTED")
            currentStep = schemas.StrSchema
            __annotations__ = {
                "jobId": jobId,
                "title": title,
                "children": children,
                "percentage": percentage,
                "viewStatus": viewStatus,
                "currentStep": currentStep,
            }
    
    currentStep: MetaOapg.properties.currentStep
    jobId: MetaOapg.properties.jobId
    children: MetaOapg.properties.children
    percentage: MetaOapg.properties.percentage
    title: MetaOapg.properties.title
    viewStatus: MetaOapg.properties.viewStatus
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["children"]) -> MetaOapg.properties.children: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["percentage"]) -> MetaOapg.properties.percentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["viewStatus"]) -> MetaOapg.properties.viewStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentStep"]) -> MetaOapg.properties.currentStep: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["jobId", "title", "children", "percentage", "viewStatus", "currentStep", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobId"]) -> MetaOapg.properties.jobId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["children"]) -> MetaOapg.properties.children: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["percentage"]) -> MetaOapg.properties.percentage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["viewStatus"]) -> MetaOapg.properties.viewStatus: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentStep"]) -> MetaOapg.properties.currentStep: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["jobId", "title", "children", "percentage", "viewStatus", "currentStep", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        currentStep: typing.Union[MetaOapg.properties.currentStep, str, ],
        jobId: typing.Union[MetaOapg.properties.jobId, str, ],
        children: typing.Union[MetaOapg.properties.children, list, tuple, ],
        percentage: typing.Union[MetaOapg.properties.percentage, decimal.Decimal, int, float, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        viewStatus: typing.Union[MetaOapg.properties.viewStatus, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShortJobView':
        return super().__new__(
            cls,
            *_args,
            currentStep=currentStep,
            jobId=jobId,
            children=children,
            percentage=percentage,
            title=title,
            viewStatus=viewStatus,
            _configuration=_configuration,
            **kwargs,
        )
