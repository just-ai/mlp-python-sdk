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


class FitConfigData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "default",
            "name",
            "id",
            "config",
        }
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['FitConfigPK']:
                return FitConfigPK
            name = schemas.StrSchema
            default = schemas.BoolSchema
            config = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "default": default,
                "config": config,
            }
    
    default: MetaOapg.properties.default
    name: MetaOapg.properties.name
    id: 'FitConfigPK'
    config: MetaOapg.properties.config
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'FitConfigPK': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default"]) -> MetaOapg.properties.default: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "default", "config", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'FitConfigPK': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default"]) -> MetaOapg.properties.default: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "default", "config", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        default: typing.Union[MetaOapg.properties.default, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: 'FitConfigPK',
        config: typing.Union[MetaOapg.properties.config, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FitConfigData':
        return super().__new__(
            cls,
            *_args,
            default=default,
            name=name,
            id=id,
            config=config,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.fit_config_pk import FitConfigPK
