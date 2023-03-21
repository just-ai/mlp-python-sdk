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


class DatasetInfoData(
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
        
            @staticmethod
            def id() -> typing.Type['DatasetPK']:
                return DatasetPK
            datasetAccountName = schemas.StrSchema
            description = schemas.StrSchema
            dataType = schemas.StrSchema
            
            
            class accessMode(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "private": "PRIVATE",
                        "public": "PUBLIC",
                        "restricted": "RESTRICTED",
                    }
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("private")
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("public")
                
                @schemas.classproperty
                def RESTRICTED(cls):
                    return cls("restricted")
            warning = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "id": id,
                "datasetAccountName": datasetAccountName,
                "description": description,
                "dataType": dataType,
                "accessMode": accessMode,
                "warning": warning,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'DatasetPK': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datasetAccountName"]) -> MetaOapg.properties.datasetAccountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataType"]) -> MetaOapg.properties.dataType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessMode"]) -> MetaOapg.properties.accessMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["warning"]) -> MetaOapg.properties.warning: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "id", "datasetAccountName", "description", "dataType", "accessMode", "warning", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['DatasetPK', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datasetAccountName"]) -> typing.Union[MetaOapg.properties.datasetAccountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataType"]) -> typing.Union[MetaOapg.properties.dataType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessMode"]) -> typing.Union[MetaOapg.properties.accessMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["warning"]) -> typing.Union[MetaOapg.properties.warning, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "id", "datasetAccountName", "description", "dataType", "accessMode", "warning", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union['DatasetPK', schemas.Unset] = schemas.unset,
        datasetAccountName: typing.Union[MetaOapg.properties.datasetAccountName, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        dataType: typing.Union[MetaOapg.properties.dataType, str, schemas.Unset] = schemas.unset,
        accessMode: typing.Union[MetaOapg.properties.accessMode, str, schemas.Unset] = schemas.unset,
        warning: typing.Union[MetaOapg.properties.warning, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DatasetInfoData':
        return super().__new__(
            cls,
            *_args,
            name=name,
            id=id,
            datasetAccountName=datasetAccountName,
            description=description,
            dataType=dataType,
            accessMode=accessMode,
            warning=warning,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.dataset_pk import DatasetPK
