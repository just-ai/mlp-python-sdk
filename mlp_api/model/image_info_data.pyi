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


class ImageInfoData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "image",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            image = schemas.StrSchema
        
            @staticmethod
            def id() -> typing.Type['ImageInfoPK']:
                return ImageInfoPK
            imageAccountName = schemas.StrSchema
            
            
            class accessMode(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("private")
                
                @schemas.classproperty
                def PUBLIC(cls):
                    return cls("public")
                
                @schemas.classproperty
                def RESTRICTED(cls):
                    return cls("restricted")
            __annotations__ = {
                "name": name,
                "image": image,
                "id": id,
                "imageAccountName": imageAccountName,
                "accessMode": accessMode,
            }
    
    image: MetaOapg.properties.image
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'ImageInfoPK': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageAccountName"]) -> MetaOapg.properties.imageAccountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessMode"]) -> MetaOapg.properties.accessMode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "image", "id", "imageAccountName", "accessMode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['ImageInfoPK', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageAccountName"]) -> typing.Union[MetaOapg.properties.imageAccountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessMode"]) -> typing.Union[MetaOapg.properties.accessMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "image", "id", "imageAccountName", "accessMode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        image: typing.Union[MetaOapg.properties.image, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union['ImageInfoPK', schemas.Unset] = schemas.unset,
        imageAccountName: typing.Union[MetaOapg.properties.imageAccountName, str, schemas.Unset] = schemas.unset,
        accessMode: typing.Union[MetaOapg.properties.accessMode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImageInfoData':
        return super().__new__(
            cls,
            *_args,
            image=image,
            name=name,
            id=id,
            imageAccountName=imageAccountName,
            accessMode=accessMode,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.image_info_pk import ImageInfoPK
