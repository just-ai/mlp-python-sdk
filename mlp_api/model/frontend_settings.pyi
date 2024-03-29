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


class FrontendSettings(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "isBillingEnabled",
            "isSystemAccount",
            "isExtendedLanding",
        }
        
        class properties:
            isSystemAccount = schemas.BoolSchema
            isBillingEnabled = schemas.BoolSchema
            isExtendedLanding = schemas.BoolSchema
            __annotations__ = {
                "isSystemAccount": isSystemAccount,
                "isBillingEnabled": isBillingEnabled,
                "isExtendedLanding": isExtendedLanding,
            }
    
    isBillingEnabled: MetaOapg.properties.isBillingEnabled
    isSystemAccount: MetaOapg.properties.isSystemAccount
    isExtendedLanding: MetaOapg.properties.isExtendedLanding
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSystemAccount"]) -> MetaOapg.properties.isSystemAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isBillingEnabled"]) -> MetaOapg.properties.isBillingEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isExtendedLanding"]) -> MetaOapg.properties.isExtendedLanding: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isSystemAccount", "isBillingEnabled", "isExtendedLanding", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSystemAccount"]) -> MetaOapg.properties.isSystemAccount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isBillingEnabled"]) -> MetaOapg.properties.isBillingEnabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isExtendedLanding"]) -> MetaOapg.properties.isExtendedLanding: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isSystemAccount", "isBillingEnabled", "isExtendedLanding", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        isBillingEnabled: typing.Union[MetaOapg.properties.isBillingEnabled, bool, ],
        isSystemAccount: typing.Union[MetaOapg.properties.isSystemAccount, bool, ],
        isExtendedLanding: typing.Union[MetaOapg.properties.isExtendedLanding, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FrontendSettings':
        return super().__new__(
            cls,
            *_args,
            isBillingEnabled=isBillingEnabled,
            isSystemAccount=isSystemAccount,
            isExtendedLanding=isExtendedLanding,
            _configuration=_configuration,
            **kwargs,
        )
