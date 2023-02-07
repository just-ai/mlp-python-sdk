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


class ParaphrasingStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "statuses",
        }
        
        class properties:
            
            
            class statuses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TaskSuiteStatus']:
                        return TaskSuiteStatus
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TaskSuiteStatus'], typing.List['TaskSuiteStatus']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'statuses':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TaskSuiteStatus':
                    return super().__getitem__(i)
            __annotations__ = {
                "statuses": statuses,
            }
    
    statuses: MetaOapg.properties.statuses
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["statuses", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statuses"]) -> MetaOapg.properties.statuses: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["statuses", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        statuses: typing.Union[MetaOapg.properties.statuses, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ParaphrasingStatus':
        return super().__new__(
            cls,
            *_args,
            statuses=statuses,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.task_suite_status import TaskSuiteStatus