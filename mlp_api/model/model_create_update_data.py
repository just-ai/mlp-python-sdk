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
            imageAccountId = schemas.Int64Schema
            imageId = schemas.Int64Schema
            trainingModelAccountId = schemas.Int64Schema
            trainingModelId = schemas.Int64Schema
            
            
            class trainingType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "singleContainer": "SINGLE_CONTAINER",
                        "multipleFit": "MULTIPLE_FIT",
                    }
                
                @schemas.classproperty
                def SINGLE_CONTAINER(cls):
                    return cls("singleContainer")
                
                @schemas.classproperty
                def MULTIPLE_FIT(cls):
                    return cls("multipleFit")
            trainingDatasetAccountId = schemas.Int64Schema
            trainingDatasetId = schemas.Int64Schema
            trainingFitConfigId = schemas.Int64Schema
            taskType = schemas.StrSchema
            trainingDatasetType = schemas.StrSchema
            fitTemplateModelId = schemas.Int64Schema
            composite = schemas.BoolSchema
            config = schemas.StrSchema
            env = schemas.StrSchema
            fittable = schemas.BoolSchema
            
            
            class hostingType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EXTERNAL": "EXTERNAL",
                        "INTERNAL": "INTERNAL",
                        "HOSTING_SERVER": "HOSTING_SERVER",
                    }
                
                @schemas.classproperty
                def EXTERNAL(cls):
                    return cls("EXTERNAL")
                
                @schemas.classproperty
                def INTERNAL(cls):
                    return cls("INTERNAL")
                
                @schemas.classproperty
                def HOSTING_SERVER(cls):
                    return cls("HOSTING_SERVER")
            
            
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
        
            @staticmethod
            def caching() -> typing.Type['ModelCachingData']:
                return ModelCachingData
        
            @staticmethod
            def priorityQueue() -> typing.Type['ModelPriorityQueueData']:
                return ModelPriorityQueueData
            shortDescription = schemas.StrSchema
            
            
            class languages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'languages':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            minInstancesCount = schemas.Int32Schema
            startTimeSec = schemas.Float32Schema
            __annotations__ = {
                "modelName": modelName,
                "imageAccountId": imageAccountId,
                "imageId": imageId,
                "trainingModelAccountId": trainingModelAccountId,
                "trainingModelId": trainingModelId,
                "trainingType": trainingType,
                "trainingDatasetAccountId": trainingDatasetAccountId,
                "trainingDatasetId": trainingDatasetId,
                "trainingFitConfigId": trainingFitConfigId,
                "taskType": taskType,
                "trainingDatasetType": trainingDatasetType,
                "fitTemplateModelId": fitTemplateModelId,
                "composite": composite,
                "config": config,
                "env": env,
                "fittable": fittable,
                "hostingType": hostingType,
                "persistentVolumes": persistentVolumes,
                "dataImageMounts": dataImageMounts,
                "resourceGroup": resourceGroup,
                "timeouts": timeouts,
                "resourceLimits": resourceLimits,
                "retriesConfig": retriesConfig,
                "batchesConfig": batchesConfig,
                "caching": caching,
                "priorityQueue": priorityQueue,
                "shortDescription": shortDescription,
                "languages": languages,
                "minInstancesCount": minInstancesCount,
                "startTimeSec": startTimeSec,
            }
    
    modelName: MetaOapg.properties.modelName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelName"]) -> MetaOapg.properties.modelName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageAccountId"]) -> MetaOapg.properties.imageAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageId"]) -> MetaOapg.properties.imageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingModelAccountId"]) -> MetaOapg.properties.trainingModelAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingModelId"]) -> MetaOapg.properties.trainingModelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingType"]) -> MetaOapg.properties.trainingType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDatasetAccountId"]) -> MetaOapg.properties.trainingDatasetAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDatasetId"]) -> MetaOapg.properties.trainingDatasetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingFitConfigId"]) -> MetaOapg.properties.trainingFitConfigId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taskType"]) -> MetaOapg.properties.taskType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDatasetType"]) -> MetaOapg.properties.trainingDatasetType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fitTemplateModelId"]) -> MetaOapg.properties.fitTemplateModelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["composite"]) -> MetaOapg.properties.composite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["env"]) -> MetaOapg.properties.env: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fittable"]) -> MetaOapg.properties.fittable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostingType"]) -> MetaOapg.properties.hostingType: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["caching"]) -> 'ModelCachingData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priorityQueue"]) -> 'ModelPriorityQueueData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shortDescription"]) -> MetaOapg.properties.shortDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["languages"]) -> MetaOapg.properties.languages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minInstancesCount"]) -> MetaOapg.properties.minInstancesCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTimeSec"]) -> MetaOapg.properties.startTimeSec: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["modelName", "imageAccountId", "imageId", "trainingModelAccountId", "trainingModelId", "trainingType", "trainingDatasetAccountId", "trainingDatasetId", "trainingFitConfigId", "taskType", "trainingDatasetType", "fitTemplateModelId", "composite", "config", "env", "fittable", "hostingType", "persistentVolumes", "dataImageMounts", "resourceGroup", "timeouts", "resourceLimits", "retriesConfig", "batchesConfig", "caching", "priorityQueue", "shortDescription", "languages", "minInstancesCount", "startTimeSec", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelName"]) -> MetaOapg.properties.modelName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageAccountId"]) -> typing.Union[MetaOapg.properties.imageAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageId"]) -> typing.Union[MetaOapg.properties.imageId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingModelAccountId"]) -> typing.Union[MetaOapg.properties.trainingModelAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingModelId"]) -> typing.Union[MetaOapg.properties.trainingModelId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingType"]) -> typing.Union[MetaOapg.properties.trainingType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDatasetAccountId"]) -> typing.Union[MetaOapg.properties.trainingDatasetAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDatasetId"]) -> typing.Union[MetaOapg.properties.trainingDatasetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingFitConfigId"]) -> typing.Union[MetaOapg.properties.trainingFitConfigId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taskType"]) -> typing.Union[MetaOapg.properties.taskType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDatasetType"]) -> typing.Union[MetaOapg.properties.trainingDatasetType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fitTemplateModelId"]) -> typing.Union[MetaOapg.properties.fitTemplateModelId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["composite"]) -> typing.Union[MetaOapg.properties.composite, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union[MetaOapg.properties.config, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["env"]) -> typing.Union[MetaOapg.properties.env, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fittable"]) -> typing.Union[MetaOapg.properties.fittable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostingType"]) -> typing.Union[MetaOapg.properties.hostingType, schemas.Unset]: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["caching"]) -> typing.Union['ModelCachingData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priorityQueue"]) -> typing.Union['ModelPriorityQueueData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shortDescription"]) -> typing.Union[MetaOapg.properties.shortDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["languages"]) -> typing.Union[MetaOapg.properties.languages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minInstancesCount"]) -> typing.Union[MetaOapg.properties.minInstancesCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTimeSec"]) -> typing.Union[MetaOapg.properties.startTimeSec, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["modelName", "imageAccountId", "imageId", "trainingModelAccountId", "trainingModelId", "trainingType", "trainingDatasetAccountId", "trainingDatasetId", "trainingFitConfigId", "taskType", "trainingDatasetType", "fitTemplateModelId", "composite", "config", "env", "fittable", "hostingType", "persistentVolumes", "dataImageMounts", "resourceGroup", "timeouts", "resourceLimits", "retriesConfig", "batchesConfig", "caching", "priorityQueue", "shortDescription", "languages", "minInstancesCount", "startTimeSec", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        modelName: typing.Union[MetaOapg.properties.modelName, str, ],
        imageAccountId: typing.Union[MetaOapg.properties.imageAccountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        imageId: typing.Union[MetaOapg.properties.imageId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingModelAccountId: typing.Union[MetaOapg.properties.trainingModelAccountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingModelId: typing.Union[MetaOapg.properties.trainingModelId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingType: typing.Union[MetaOapg.properties.trainingType, str, schemas.Unset] = schemas.unset,
        trainingDatasetAccountId: typing.Union[MetaOapg.properties.trainingDatasetAccountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingDatasetId: typing.Union[MetaOapg.properties.trainingDatasetId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingFitConfigId: typing.Union[MetaOapg.properties.trainingFitConfigId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        taskType: typing.Union[MetaOapg.properties.taskType, str, schemas.Unset] = schemas.unset,
        trainingDatasetType: typing.Union[MetaOapg.properties.trainingDatasetType, str, schemas.Unset] = schemas.unset,
        fitTemplateModelId: typing.Union[MetaOapg.properties.fitTemplateModelId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        composite: typing.Union[MetaOapg.properties.composite, bool, schemas.Unset] = schemas.unset,
        config: typing.Union[MetaOapg.properties.config, str, schemas.Unset] = schemas.unset,
        env: typing.Union[MetaOapg.properties.env, str, schemas.Unset] = schemas.unset,
        fittable: typing.Union[MetaOapg.properties.fittable, bool, schemas.Unset] = schemas.unset,
        hostingType: typing.Union[MetaOapg.properties.hostingType, str, schemas.Unset] = schemas.unset,
        persistentVolumes: typing.Union[MetaOapg.properties.persistentVolumes, list, tuple, schemas.Unset] = schemas.unset,
        dataImageMounts: typing.Union[MetaOapg.properties.dataImageMounts, list, tuple, schemas.Unset] = schemas.unset,
        resourceGroup: typing.Union[MetaOapg.properties.resourceGroup, str, schemas.Unset] = schemas.unset,
        timeouts: typing.Union['ModelTimeoutsData', schemas.Unset] = schemas.unset,
        resourceLimits: typing.Union['ModelLimitsData', schemas.Unset] = schemas.unset,
        retriesConfig: typing.Union['ModelRetriesData', schemas.Unset] = schemas.unset,
        batchesConfig: typing.Union['ModelBatchesData', schemas.Unset] = schemas.unset,
        caching: typing.Union['ModelCachingData', schemas.Unset] = schemas.unset,
        priorityQueue: typing.Union['ModelPriorityQueueData', schemas.Unset] = schemas.unset,
        shortDescription: typing.Union[MetaOapg.properties.shortDescription, str, schemas.Unset] = schemas.unset,
        languages: typing.Union[MetaOapg.properties.languages, list, tuple, schemas.Unset] = schemas.unset,
        minInstancesCount: typing.Union[MetaOapg.properties.minInstancesCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        startTimeSec: typing.Union[MetaOapg.properties.startTimeSec, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelCreateUpdateData':
        return super().__new__(
            cls,
            *_args,
            modelName=modelName,
            imageAccountId=imageAccountId,
            imageId=imageId,
            trainingModelAccountId=trainingModelAccountId,
            trainingModelId=trainingModelId,
            trainingType=trainingType,
            trainingDatasetAccountId=trainingDatasetAccountId,
            trainingDatasetId=trainingDatasetId,
            trainingFitConfigId=trainingFitConfigId,
            taskType=taskType,
            trainingDatasetType=trainingDatasetType,
            fitTemplateModelId=fitTemplateModelId,
            composite=composite,
            config=config,
            env=env,
            fittable=fittable,
            hostingType=hostingType,
            persistentVolumes=persistentVolumes,
            dataImageMounts=dataImageMounts,
            resourceGroup=resourceGroup,
            timeouts=timeouts,
            resourceLimits=resourceLimits,
            retriesConfig=retriesConfig,
            batchesConfig=batchesConfig,
            caching=caching,
            priorityQueue=priorityQueue,
            shortDescription=shortDescription,
            languages=languages,
            minInstancesCount=minInstancesCount,
            startTimeSec=startTimeSec,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.data_image_mount_data import DataImageMountData
from mlp_api.model.model_batches_data import ModelBatchesData
from mlp_api.model.model_caching_data import ModelCachingData
from mlp_api.model.model_limits_data import ModelLimitsData
from mlp_api.model.model_priority_queue_data import ModelPriorityQueueData
from mlp_api.model.model_retries_data import ModelRetriesData
from mlp_api.model.model_timeouts_data import ModelTimeoutsData
from mlp_api.model.persistent_volume_data import PersistentVolumeData
