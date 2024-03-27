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
            "lastHeartBeat",
            "created",
            "connectionToken",
            "id",
            "type",
            "kubeType",
            "isEvictable",
            "status",
        }
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['ModelInstancePK']:
                return ModelInstancePK
            connectionToken = schemas.StrSchema
            created = schemas.DateTimeSchema
            lastHeartBeat = schemas.DateTimeSchema
            
            
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
                def DOCKER(cls):
                    return cls("docker")
                
                @schemas.classproperty
                def EXTERNAL(cls):
                    return cls("external")
                
                @schemas.classproperty
                def HOSTING_SERVER(cls):
                    return cls("hostingServer")
            isEvictable = schemas.BoolSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def IDLE(cls):
                    return cls("IDLE")
                
                @schemas.classproperty
                def STARTED(cls):
                    return cls("STARTED")
                
                @schemas.classproperty
                def DELETED(cls):
                    return cls("DELETED")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
            resourceName = schemas.StrSchema
            alias = schemas.StrSchema
            customData = schemas.StrSchema
            deleteTimestamp = schemas.DateTimeSchema
            hostingServerId = schemas.StrSchema
            serverId = schemas.Int64Schema
            __annotations__ = {
                "id": id,
                "connectionToken": connectionToken,
                "created": created,
                "lastHeartBeat": lastHeartBeat,
                "type": type,
                "kubeType": kubeType,
                "isEvictable": isEvictable,
                "status": status,
                "resourceName": resourceName,
                "alias": alias,
                "customData": customData,
                "deleteTimestamp": deleteTimestamp,
                "hostingServerId": hostingServerId,
                "serverId": serverId,
            }
    
    lastHeartBeat: MetaOapg.properties.lastHeartBeat
    created: MetaOapg.properties.created
    connectionToken: MetaOapg.properties.connectionToken
    id: 'ModelInstancePK'
    type: MetaOapg.properties.type
    kubeType: MetaOapg.properties.kubeType
    isEvictable: MetaOapg.properties.isEvictable
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'ModelInstancePK': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionToken"]) -> MetaOapg.properties.connectionToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastHeartBeat"]) -> MetaOapg.properties.lastHeartBeat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kubeType"]) -> MetaOapg.properties.kubeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEvictable"]) -> MetaOapg.properties.isEvictable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceName"]) -> MetaOapg.properties.resourceName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alias"]) -> MetaOapg.properties.alias: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customData"]) -> MetaOapg.properties.customData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteTimestamp"]) -> MetaOapg.properties.deleteTimestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostingServerId"]) -> MetaOapg.properties.hostingServerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serverId"]) -> MetaOapg.properties.serverId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "connectionToken", "created", "lastHeartBeat", "type", "kubeType", "isEvictable", "status", "resourceName", "alias", "customData", "deleteTimestamp", "hostingServerId", "serverId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'ModelInstancePK': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionToken"]) -> MetaOapg.properties.connectionToken: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastHeartBeat"]) -> MetaOapg.properties.lastHeartBeat: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kubeType"]) -> MetaOapg.properties.kubeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEvictable"]) -> MetaOapg.properties.isEvictable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceName"]) -> typing.Union[MetaOapg.properties.resourceName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alias"]) -> typing.Union[MetaOapg.properties.alias, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customData"]) -> typing.Union[MetaOapg.properties.customData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteTimestamp"]) -> typing.Union[MetaOapg.properties.deleteTimestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostingServerId"]) -> typing.Union[MetaOapg.properties.hostingServerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serverId"]) -> typing.Union[MetaOapg.properties.serverId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "connectionToken", "created", "lastHeartBeat", "type", "kubeType", "isEvictable", "status", "resourceName", "alias", "customData", "deleteTimestamp", "hostingServerId", "serverId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        lastHeartBeat: typing.Union[MetaOapg.properties.lastHeartBeat, str, datetime, ],
        created: typing.Union[MetaOapg.properties.created, str, datetime, ],
        connectionToken: typing.Union[MetaOapg.properties.connectionToken, str, ],
        id: 'ModelInstancePK',
        type: typing.Union[MetaOapg.properties.type, str, ],
        kubeType: typing.Union[MetaOapg.properties.kubeType, str, ],
        isEvictable: typing.Union[MetaOapg.properties.isEvictable, bool, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        resourceName: typing.Union[MetaOapg.properties.resourceName, str, schemas.Unset] = schemas.unset,
        alias: typing.Union[MetaOapg.properties.alias, str, schemas.Unset] = schemas.unset,
        customData: typing.Union[MetaOapg.properties.customData, str, schemas.Unset] = schemas.unset,
        deleteTimestamp: typing.Union[MetaOapg.properties.deleteTimestamp, str, datetime, schemas.Unset] = schemas.unset,
        hostingServerId: typing.Union[MetaOapg.properties.hostingServerId, str, schemas.Unset] = schemas.unset,
        serverId: typing.Union[MetaOapg.properties.serverId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelInstance':
        return super().__new__(
            cls,
            *_args,
            lastHeartBeat=lastHeartBeat,
            created=created,
            connectionToken=connectionToken,
            id=id,
            type=type,
            kubeType=kubeType,
            isEvictable=isEvictable,
            status=status,
            resourceName=resourceName,
            alias=alias,
            customData=customData,
            deleteTimestamp=deleteTimestamp,
            hostingServerId=hostingServerId,
            serverId=serverId,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.model_instance_pk import ModelInstancePK
