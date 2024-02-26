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


class CreateResourceGroupData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            isDefault = schemas.BoolSchema
            enabledEviction = schemas.BoolSchema
            
            
            class access(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PRIVATE": "PRIVATE",
                        "PUBLIC": "PUBLIC",
                    }
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("PRIVATE")
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("PUBLIC")
            
            
            class resourceGroupType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "DOCKER": "DOCKER",
                        "KUBERNETES": "KUBERNETES",
                        "HOSTING_SERVER": "HOSTING_SERVER",
                    }
                
                @schemas.classproperty
                def DOCKER(cls):
                    return cls("DOCKER")
                
                @schemas.classproperty
                def KUBERNETES(cls):
                    return cls("KUBERNETES")
                
                @schemas.classproperty
                def HOSTING_SERVER(cls):
                    return cls("HOSTING_SERVER")
            enabledAutoScaling = schemas.BoolSchema
        
            @staticmethod
            def autoScalingConfiguration() -> typing.Type['ResourceGroupAutoScalingConfiguration']:
                return ResourceGroupAutoScalingConfiguration
            __annotations__ = {
                "name": name,
                "isDefault": isDefault,
                "enabledEviction": enabledEviction,
                "access": access,
                "resourceGroupType": resourceGroupType,
                "enabledAutoScaling": enabledAutoScaling,
                "autoScalingConfiguration": autoScalingConfiguration,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabledEviction"]) -> MetaOapg.properties.enabledEviction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceGroupType"]) -> MetaOapg.properties.resourceGroupType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabledAutoScaling"]) -> MetaOapg.properties.enabledAutoScaling: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoScalingConfiguration"]) -> 'ResourceGroupAutoScalingConfiguration': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "isDefault", "enabledEviction", "access", "resourceGroupType", "enabledAutoScaling", "autoScalingConfiguration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDefault"]) -> typing.Union[MetaOapg.properties.isDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabledEviction"]) -> typing.Union[MetaOapg.properties.enabledEviction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> typing.Union[MetaOapg.properties.access, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceGroupType"]) -> typing.Union[MetaOapg.properties.resourceGroupType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabledAutoScaling"]) -> typing.Union[MetaOapg.properties.enabledAutoScaling, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoScalingConfiguration"]) -> typing.Union['ResourceGroupAutoScalingConfiguration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "isDefault", "enabledEviction", "access", "resourceGroupType", "enabledAutoScaling", "autoScalingConfiguration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        isDefault: typing.Union[MetaOapg.properties.isDefault, bool, schemas.Unset] = schemas.unset,
        enabledEviction: typing.Union[MetaOapg.properties.enabledEviction, bool, schemas.Unset] = schemas.unset,
        access: typing.Union[MetaOapg.properties.access, str, schemas.Unset] = schemas.unset,
        resourceGroupType: typing.Union[MetaOapg.properties.resourceGroupType, str, schemas.Unset] = schemas.unset,
        enabledAutoScaling: typing.Union[MetaOapg.properties.enabledAutoScaling, bool, schemas.Unset] = schemas.unset,
        autoScalingConfiguration: typing.Union['ResourceGroupAutoScalingConfiguration', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateResourceGroupData':
        return super().__new__(
            cls,
            *_args,
            name=name,
            isDefault=isDefault,
            enabledEviction=enabledEviction,
            access=access,
            resourceGroupType=resourceGroupType,
            enabledAutoScaling=enabledAutoScaling,
            autoScalingConfiguration=autoScalingConfiguration,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.resource_group_auto_scaling_configuration import ResourceGroupAutoScalingConfiguration
