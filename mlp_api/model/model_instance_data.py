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


class ModelInstanceData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "statusInfo",
            "restartCount",
            "id",
            "instanceHostingType",
        }
        
        class properties:
            id = schemas.Int64Schema
        
            @staticmethod
            def statusInfo() -> typing.Type['StatusInfo']:
                return StatusInfo
            restartCount = schemas.Int32Schema
            
            
            class instanceHostingType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "deployment": "DEPLOYMENT",
                        "pod": "POD",
                        "external": "EXTERNAL",
                        "hostingServer": "HOSTING_SERVER",
                    }
                
                @schemas.classproperty
                def DEPLOYMENT(cls):
                    return cls("deployment")
                
                @schemas.classproperty
                def POD(cls):
                    return cls("pod")
                
                @schemas.classproperty
                def EXTERNAL(cls):
                    return cls("external")
                
                @schemas.classproperty
                def HOSTING_SERVER(cls):
                    return cls("hostingServer")
            name = schemas.StrSchema
            lastRestartTimestamp = schemas.StrSchema
            createdTimestamp = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "statusInfo": statusInfo,
                "restartCount": restartCount,
                "instanceHostingType": instanceHostingType,
                "name": name,
                "lastRestartTimestamp": lastRestartTimestamp,
                "createdTimestamp": createdTimestamp,
            }
    
    statusInfo: 'StatusInfo'
    restartCount: MetaOapg.properties.restartCount
    id: MetaOapg.properties.id
    instanceHostingType: MetaOapg.properties.instanceHostingType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusInfo"]) -> 'StatusInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restartCount"]) -> MetaOapg.properties.restartCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instanceHostingType"]) -> MetaOapg.properties.instanceHostingType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastRestartTimestamp"]) -> MetaOapg.properties.lastRestartTimestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdTimestamp"]) -> MetaOapg.properties.createdTimestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "statusInfo", "restartCount", "instanceHostingType", "name", "lastRestartTimestamp", "createdTimestamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusInfo"]) -> 'StatusInfo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restartCount"]) -> MetaOapg.properties.restartCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instanceHostingType"]) -> MetaOapg.properties.instanceHostingType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastRestartTimestamp"]) -> typing.Union[MetaOapg.properties.lastRestartTimestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdTimestamp"]) -> typing.Union[MetaOapg.properties.createdTimestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "statusInfo", "restartCount", "instanceHostingType", "name", "lastRestartTimestamp", "createdTimestamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        statusInfo: 'StatusInfo',
        restartCount: typing.Union[MetaOapg.properties.restartCount, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        instanceHostingType: typing.Union[MetaOapg.properties.instanceHostingType, str, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        lastRestartTimestamp: typing.Union[MetaOapg.properties.lastRestartTimestamp, str, schemas.Unset] = schemas.unset,
        createdTimestamp: typing.Union[MetaOapg.properties.createdTimestamp, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelInstanceData':
        return super().__new__(
            cls,
            *_args,
            statusInfo=statusInfo,
            restartCount=restartCount,
            id=id,
            instanceHostingType=instanceHostingType,
            name=name,
            lastRestartTimestamp=lastRestartTimestamp,
            createdTimestamp=createdTimestamp,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.status_info import StatusInfo
