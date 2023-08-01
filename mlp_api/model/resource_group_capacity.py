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


class ResourceGroupCapacity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "diskMb",
            "gpuModels",
            "nodes",
            "milliCpu",
            "ramMb",
            "gpu",
            "vramMb",
        }
        
        class properties:
            milliCpu = schemas.Int64Schema
            ramMb = schemas.Int64Schema
            diskMb = schemas.Int64Schema
            gpu = schemas.Int32Schema
            
            
            class gpuModels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'gpuModels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class nodes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nodes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            vramMb = schemas.Int32Schema
            vRamMb = schemas.Int32Schema
            __annotations__ = {
                "milliCpu": milliCpu,
                "ramMb": ramMb,
                "diskMb": diskMb,
                "gpu": gpu,
                "gpuModels": gpuModels,
                "nodes": nodes,
                "vramMb": vramMb,
                "vRamMb": vRamMb,
            }
    
    diskMb: MetaOapg.properties.diskMb
    gpuModels: MetaOapg.properties.gpuModels
    nodes: MetaOapg.properties.nodes
    milliCpu: MetaOapg.properties.milliCpu
    ramMb: MetaOapg.properties.ramMb
    gpu: MetaOapg.properties.gpu
    vramMb: MetaOapg.properties.vramMb
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["milliCpu"]) -> MetaOapg.properties.milliCpu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ramMb"]) -> MetaOapg.properties.ramMb: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["diskMb"]) -> MetaOapg.properties.diskMb: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gpu"]) -> MetaOapg.properties.gpu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gpuModels"]) -> MetaOapg.properties.gpuModels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodes"]) -> MetaOapg.properties.nodes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vramMb"]) -> MetaOapg.properties.vramMb: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vRamMb"]) -> MetaOapg.properties.vRamMb: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["milliCpu", "ramMb", "diskMb", "gpu", "gpuModels", "nodes", "vramMb", "vRamMb", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["milliCpu"]) -> MetaOapg.properties.milliCpu: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ramMb"]) -> MetaOapg.properties.ramMb: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["diskMb"]) -> MetaOapg.properties.diskMb: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gpu"]) -> MetaOapg.properties.gpu: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gpuModels"]) -> MetaOapg.properties.gpuModels: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodes"]) -> MetaOapg.properties.nodes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vramMb"]) -> MetaOapg.properties.vramMb: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vRamMb"]) -> typing.Union[MetaOapg.properties.vRamMb, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["milliCpu", "ramMb", "diskMb", "gpu", "gpuModels", "nodes", "vramMb", "vRamMb", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        diskMb: typing.Union[MetaOapg.properties.diskMb, decimal.Decimal, int, ],
        gpuModels: typing.Union[MetaOapg.properties.gpuModels, list, tuple, ],
        nodes: typing.Union[MetaOapg.properties.nodes, list, tuple, ],
        milliCpu: typing.Union[MetaOapg.properties.milliCpu, decimal.Decimal, int, ],
        ramMb: typing.Union[MetaOapg.properties.ramMb, decimal.Decimal, int, ],
        gpu: typing.Union[MetaOapg.properties.gpu, decimal.Decimal, int, ],
        vramMb: typing.Union[MetaOapg.properties.vramMb, decimal.Decimal, int, ],
        vRamMb: typing.Union[MetaOapg.properties.vRamMb, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ResourceGroupCapacity':
        return super().__new__(
            cls,
            *_args,
            diskMb=diskMb,
            gpuModels=gpuModels,
            nodes=nodes,
            milliCpu=milliCpu,
            ramMb=ramMb,
            gpu=gpu,
            vramMb=vramMb,
            vRamMb=vRamMb,
            _configuration=_configuration,
            **kwargs,
        )
