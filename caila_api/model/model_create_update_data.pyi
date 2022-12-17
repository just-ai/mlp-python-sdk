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

from caila_api import schemas  # noqa: F401


class ModelCreateUpdateData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "modelName",
        }
        
        class properties:
            modelName = schemas.StrSchema
            imageId = schemas.Int64Schema
            trainingModelAccountId = schemas.Int64Schema
            trainingModelId = schemas.Int64Schema
            
            
            class trainingType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SINGLE_CONTAINER(cls):
                    return cls("singleContainer")
                
                @schemas.classproperty
                def MULTIPLE_FIT(cls):
                    return cls("multipleFit")
            trainingDatasetId = schemas.Int64Schema
            trainingFitConfigId = schemas.Int64Schema
            public = schemas.BoolSchema
            config = schemas.StrSchema
            env = schemas.StrSchema
            fittable = schemas.BoolSchema
            
            
            class persistentVolumes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PersistentVolumeData']:
                        return PersistentVolumeData
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['PersistentVolumeData'], typing.List['PersistentVolumeData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'persistentVolumes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PersistentVolumeData':
                    return super().__getitem__(i)
            
            
            class dataImageMounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DataImageMountData']:
                        return DataImageMountData
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DataImageMountData'], typing.List['DataImageMountData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dataImageMounts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DataImageMountData':
                    return super().__getitem__(i)
            resourceGroup = schemas.StrSchema
        
            @staticmethod
            def timeouts() -> typing.Type['ModelTimeoutsData']:
                return ModelTimeoutsData
        
            @staticmethod
            def resourceLimits() -> typing.Type['ModelLimitsData']:
                return ModelLimitsData
        
            @staticmethod
            def retriesConfig() -> typing.Type['ModelRetriesData']:
                return ModelRetriesData
        
            @staticmethod
            def batchesConfig() -> typing.Type['ModelBatchesData']:
                return ModelBatchesData
            __annotations__ = {
                "modelName": modelName,
                "imageId": imageId,
                "trainingModelAccountId": trainingModelAccountId,
                "trainingModelId": trainingModelId,
                "trainingType": trainingType,
                "trainingDatasetId": trainingDatasetId,
                "trainingFitConfigId": trainingFitConfigId,
                "public": public,
                "config": config,
                "env": env,
                "fittable": fittable,
                "persistentVolumes": persistentVolumes,
                "dataImageMounts": dataImageMounts,
                "resourceGroup": resourceGroup,
                "timeouts": timeouts,
                "resourceLimits": resourceLimits,
                "retriesConfig": retriesConfig,
                "batchesConfig": batchesConfig,
            }
    
    modelName: MetaOapg.properties.modelName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelName"]) -> MetaOapg.properties.modelName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageId"]) -> MetaOapg.properties.imageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingModelAccountId"]) -> MetaOapg.properties.trainingModelAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingModelId"]) -> MetaOapg.properties.trainingModelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingType"]) -> MetaOapg.properties.trainingType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDatasetId"]) -> MetaOapg.properties.trainingDatasetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingFitConfigId"]) -> MetaOapg.properties.trainingFitConfigId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public"]) -> MetaOapg.properties.public: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["env"]) -> MetaOapg.properties.env: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fittable"]) -> MetaOapg.properties.fittable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["persistentVolumes"]) -> MetaOapg.properties.persistentVolumes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataImageMounts"]) -> MetaOapg.properties.dataImageMounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceGroup"]) -> MetaOapg.properties.resourceGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeouts"]) -> 'ModelTimeoutsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceLimits"]) -> 'ModelLimitsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retriesConfig"]) -> 'ModelRetriesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batchesConfig"]) -> 'ModelBatchesData': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["modelName", "imageId", "trainingModelAccountId", "trainingModelId", "trainingType", "trainingDatasetId", "trainingFitConfigId", "public", "config", "env", "fittable", "persistentVolumes", "dataImageMounts", "resourceGroup", "timeouts", "resourceLimits", "retriesConfig", "batchesConfig", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelName"]) -> MetaOapg.properties.modelName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageId"]) -> typing.Union[MetaOapg.properties.imageId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingModelAccountId"]) -> typing.Union[MetaOapg.properties.trainingModelAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingModelId"]) -> typing.Union[MetaOapg.properties.trainingModelId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingType"]) -> typing.Union[MetaOapg.properties.trainingType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDatasetId"]) -> typing.Union[MetaOapg.properties.trainingDatasetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingFitConfigId"]) -> typing.Union[MetaOapg.properties.trainingFitConfigId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public"]) -> typing.Union[MetaOapg.properties.public, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union[MetaOapg.properties.config, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["env"]) -> typing.Union[MetaOapg.properties.env, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fittable"]) -> typing.Union[MetaOapg.properties.fittable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["persistentVolumes"]) -> typing.Union[MetaOapg.properties.persistentVolumes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataImageMounts"]) -> typing.Union[MetaOapg.properties.dataImageMounts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceGroup"]) -> typing.Union[MetaOapg.properties.resourceGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeouts"]) -> typing.Union['ModelTimeoutsData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceLimits"]) -> typing.Union['ModelLimitsData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retriesConfig"]) -> typing.Union['ModelRetriesData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batchesConfig"]) -> typing.Union['ModelBatchesData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["modelName", "imageId", "trainingModelAccountId", "trainingModelId", "trainingType", "trainingDatasetId", "trainingFitConfigId", "public", "config", "env", "fittable", "persistentVolumes", "dataImageMounts", "resourceGroup", "timeouts", "resourceLimits", "retriesConfig", "batchesConfig", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        modelName: typing.Union[MetaOapg.properties.modelName, str, ],
        imageId: typing.Union[MetaOapg.properties.imageId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingModelAccountId: typing.Union[MetaOapg.properties.trainingModelAccountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingModelId: typing.Union[MetaOapg.properties.trainingModelId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingType: typing.Union[MetaOapg.properties.trainingType, str, schemas.Unset] = schemas.unset,
        trainingDatasetId: typing.Union[MetaOapg.properties.trainingDatasetId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingFitConfigId: typing.Union[MetaOapg.properties.trainingFitConfigId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        public: typing.Union[MetaOapg.properties.public, bool, schemas.Unset] = schemas.unset,
        config: typing.Union[MetaOapg.properties.config, str, schemas.Unset] = schemas.unset,
        env: typing.Union[MetaOapg.properties.env, str, schemas.Unset] = schemas.unset,
        fittable: typing.Union[MetaOapg.properties.fittable, bool, schemas.Unset] = schemas.unset,
        persistentVolumes: typing.Union[MetaOapg.properties.persistentVolumes, list, tuple, schemas.Unset] = schemas.unset,
        dataImageMounts: typing.Union[MetaOapg.properties.dataImageMounts, list, tuple, schemas.Unset] = schemas.unset,
        resourceGroup: typing.Union[MetaOapg.properties.resourceGroup, str, schemas.Unset] = schemas.unset,
        timeouts: typing.Union['ModelTimeoutsData', schemas.Unset] = schemas.unset,
        resourceLimits: typing.Union['ModelLimitsData', schemas.Unset] = schemas.unset,
        retriesConfig: typing.Union['ModelRetriesData', schemas.Unset] = schemas.unset,
        batchesConfig: typing.Union['ModelBatchesData', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelCreateUpdateData':
        return super().__new__(
            cls,
            *_args,
            modelName=modelName,
            imageId=imageId,
            trainingModelAccountId=trainingModelAccountId,
            trainingModelId=trainingModelId,
            trainingType=trainingType,
            trainingDatasetId=trainingDatasetId,
            trainingFitConfigId=trainingFitConfigId,
            public=public,
            config=config,
            env=env,
            fittable=fittable,
            persistentVolumes=persistentVolumes,
            dataImageMounts=dataImageMounts,
            resourceGroup=resourceGroup,
            timeouts=timeouts,
            resourceLimits=resourceLimits,
            retriesConfig=retriesConfig,
            batchesConfig=batchesConfig,
            _configuration=_configuration,
            **kwargs,
        )

from caila_api.model.data_image_mount_data import DataImageMountData
from caila_api.model.model_batches_data import ModelBatchesData
from caila_api.model.model_limits_data import ModelLimitsData
from caila_api.model.model_retries_data import ModelRetriesData
from caila_api.model.model_timeouts_data import ModelTimeoutsData
from caila_api.model.persistent_volume_data import PersistentVolumeData
