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


class ModelInstance(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "connectionToken",
            "started",
            "id",
            "type",
            "kubeType",
        }
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['ModelInstancePK']:
                return ModelInstancePK
            connectionToken = schemas.StrSchema
            started = schemas.DateTimeSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INITIAL_CHECK(cls):
                    return cls("initialCheck")
                
                @schemas.classproperty
                def SINGLE_FIT(cls):
                    return cls("singleFit")
                
                @schemas.classproperty
                def SINGLE_FIT_POOL(cls):
                    return cls("singleFitPool")
                
                @schemas.classproperty
                def MULTIPLE_FIT(cls):
                    return cls("multipleFit")
                
                @schemas.classproperty
                def PREDICT(cls):
                    return cls("predict")
            
            
            class kubeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DEPLOYMENT(cls):
                    return cls("deployment")
                
                @schemas.classproperty
                def POD(cls):
                    return cls("pod")
                
                @schemas.classproperty
                def EXTERNAL(cls):
                    return cls("external")
            resourceName = schemas.StrSchema
            alias = schemas.StrSchema
            customData = schemas.StrSchema
            deleteTimestamp = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "connectionToken": connectionToken,
                "started": started,
                "type": type,
                "kubeType": kubeType,
                "resourceName": resourceName,
                "alias": alias,
                "customData": customData,
                "deleteTimestamp": deleteTimestamp,
            }
    
    connectionToken: MetaOapg.properties.connectionToken
    started: MetaOapg.properties.started
    id: 'ModelInstancePK'
    type: MetaOapg.properties.type
    kubeType: MetaOapg.properties.kubeType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'ModelInstancePK': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionToken"]) -> MetaOapg.properties.connectionToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["started"]) -> MetaOapg.properties.started: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kubeType"]) -> MetaOapg.properties.kubeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceName"]) -> MetaOapg.properties.resourceName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alias"]) -> MetaOapg.properties.alias: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customData"]) -> MetaOapg.properties.customData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteTimestamp"]) -> MetaOapg.properties.deleteTimestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "connectionToken", "started", "type", "kubeType", "resourceName", "alias", "customData", "deleteTimestamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'ModelInstancePK': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionToken"]) -> MetaOapg.properties.connectionToken: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["started"]) -> MetaOapg.properties.started: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kubeType"]) -> MetaOapg.properties.kubeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceName"]) -> typing.Union[MetaOapg.properties.resourceName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alias"]) -> typing.Union[MetaOapg.properties.alias, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customData"]) -> typing.Union[MetaOapg.properties.customData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteTimestamp"]) -> typing.Union[MetaOapg.properties.deleteTimestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "connectionToken", "started", "type", "kubeType", "resourceName", "alias", "customData", "deleteTimestamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        connectionToken: typing.Union[MetaOapg.properties.connectionToken, str, ],
        started: typing.Union[MetaOapg.properties.started, str, datetime, ],
        id: 'ModelInstancePK',
        type: typing.Union[MetaOapg.properties.type, str, ],
        kubeType: typing.Union[MetaOapg.properties.kubeType, str, ],
        resourceName: typing.Union[MetaOapg.properties.resourceName, str, schemas.Unset] = schemas.unset,
        alias: typing.Union[MetaOapg.properties.alias, str, schemas.Unset] = schemas.unset,
        customData: typing.Union[MetaOapg.properties.customData, str, schemas.Unset] = schemas.unset,
        deleteTimestamp: typing.Union[MetaOapg.properties.deleteTimestamp, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelInstance':
        return super().__new__(
            cls,
            *_args,
            connectionToken=connectionToken,
            started=started,
            id=id,
            type=type,
            kubeType=kubeType,
            resourceName=resourceName,
            alias=alias,
            customData=customData,
            deleteTimestamp=deleteTimestamp,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.model_instance_pk import ModelInstancePK