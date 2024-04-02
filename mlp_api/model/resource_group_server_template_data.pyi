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


class ResourceGroupServerTemplateData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "tarifficationPrice",
            "templateName",
            "type",
            "rawConfiguration",
        }
        
        class properties:
            templateName = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DOCKER(cls):
                    return cls("DOCKER")
                
                @schemas.classproperty
                def KUBERNETES(cls):
                    return cls("KUBERNETES")
                
                @schemas.classproperty
                def HOSTING_SERVER(cls):
                    return cls("HOSTING_SERVER")
                
                @schemas.classproperty
                def SHARED_RESOURCE_QUOTA(cls):
                    return cls("SHARED_RESOURCE_QUOTA")
            rawConfiguration = schemas.StrSchema
            tarifficationPrice = schemas.NumberSchema
        
            @staticmethod
            def capacity() -> typing.Type['Resources']:
                return Resources
            description = schemas.StrSchema
            
            
            class tarifficationPeriod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SECOND(cls):
                    return cls("SECOND")
                
                @schemas.classproperty
                def MINUTE(cls):
                    return cls("MINUTE")
                
                @schemas.classproperty
                def HOUR(cls):
                    return cls("HOUR")
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("DAY")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("MONTH")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("YEAR")
            __annotations__ = {
                "templateName": templateName,
                "type": type,
                "rawConfiguration": rawConfiguration,
                "tarifficationPrice": tarifficationPrice,
                "capacity": capacity,
                "description": description,
                "tarifficationPeriod": tarifficationPeriod,
            }
    
    tarifficationPrice: MetaOapg.properties.tarifficationPrice
    templateName: MetaOapg.properties.templateName
    type: MetaOapg.properties.type
    rawConfiguration: MetaOapg.properties.rawConfiguration
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateName"]) -> MetaOapg.properties.templateName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rawConfiguration"]) -> MetaOapg.properties.rawConfiguration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tarifficationPrice"]) -> MetaOapg.properties.tarifficationPrice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capacity"]) -> 'Resources': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tarifficationPeriod"]) -> MetaOapg.properties.tarifficationPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["templateName", "type", "rawConfiguration", "tarifficationPrice", "capacity", "description", "tarifficationPeriod", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateName"]) -> MetaOapg.properties.templateName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rawConfiguration"]) -> MetaOapg.properties.rawConfiguration: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tarifficationPrice"]) -> MetaOapg.properties.tarifficationPrice: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capacity"]) -> typing.Union['Resources', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tarifficationPeriod"]) -> typing.Union[MetaOapg.properties.tarifficationPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["templateName", "type", "rawConfiguration", "tarifficationPrice", "capacity", "description", "tarifficationPeriod", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tarifficationPrice: typing.Union[MetaOapg.properties.tarifficationPrice, decimal.Decimal, int, float, ],
        templateName: typing.Union[MetaOapg.properties.templateName, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        rawConfiguration: typing.Union[MetaOapg.properties.rawConfiguration, str, ],
        capacity: typing.Union['Resources', schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        tarifficationPeriod: typing.Union[MetaOapg.properties.tarifficationPeriod, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResourceGroupServerTemplateData':
        return super().__new__(
            cls,
            *_args,
            tarifficationPrice=tarifficationPrice,
            templateName=templateName,
            type=type,
            rawConfiguration=rawConfiguration,
            capacity=capacity,
            description=description,
            tarifficationPeriod=tarifficationPeriod,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.resources import Resources
