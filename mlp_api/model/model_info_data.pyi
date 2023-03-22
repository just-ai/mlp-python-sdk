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


class ModelInfoData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "timeouts",
            "hostingType",
            "resourceLimits",
            "restrictedImageAccess",
            "modelName",
            "dataImageMounts",
            "fittable",
            "retriesConfig",
            "composite",
            "persistentVolumes",
            "publicSettings",
            "imageAccountId",
            "id",
            "favorite",
            "batchesConfig",
        }
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['ModelInfoPK']:
                return ModelInfoPK
            modelName = schemas.StrSchema
            imageAccountId = schemas.Int64Schema
            composite = schemas.BoolSchema
            fittable = schemas.BoolSchema
            
            
            class hostingType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EXTERNAL(cls):
                    return cls("EXTERNAL")
                
                @schemas.classproperty
                def INTERNAL(cls):
                    return cls("INTERNAL")
            
            
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
            def publicSettings() -> typing.Type['ModelPublicSettingsData']:
                return ModelPublicSettingsData
            restrictedImageAccess = schemas.BoolSchema
            favorite = schemas.BoolSchema
            modelAccountName = schemas.StrSchema
            modelAccountDisplayName = schemas.StrSchema
            imageId = schemas.Int64Schema
        
            @staticmethod
            def image() -> typing.Type['ImageInfoData']:
                return ImageInfoData
            modelGroupId = schemas.Int64Schema
            modelGroupName = schemas.StrSchema
            trainingDatasetAccountId = schemas.Int64Schema
            trainingDatasetId = schemas.Int64Schema
        
            @staticmethod
            def trainingDataset() -> typing.Type['DatasetInfoData']:
                return DatasetInfoData
            trainingDatasetType = schemas.StrSchema
            trainingFitConfigId = schemas.Int64Schema
        
            @staticmethod
            def trainingFitConfig() -> typing.Type['FitConfigData']:
                return FitConfigData
            fitTemplateModelId = schemas.Int64Schema
            taskType = schemas.StrSchema
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
            config = schemas.StrSchema
            env = schemas.StrSchema
            resourceGroup = schemas.StrSchema
            shortDescription = schemas.StrSchema
            
            
            class languages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
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
            lastActivity = schemas.Int64Schema
            
            
            class state(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def RUNNING(cls):
                    return cls("RUNNING")
                
                @schemas.classproperty
                def STARTING(cls):
                    return cls("STARTING")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
            __annotations__ = {
                "id": id,
                "modelName": modelName,
                "imageAccountId": imageAccountId,
                "composite": composite,
                "fittable": fittable,
                "hostingType": hostingType,
                "persistentVolumes": persistentVolumes,
                "dataImageMounts": dataImageMounts,
                "timeouts": timeouts,
                "resourceLimits": resourceLimits,
                "retriesConfig": retriesConfig,
                "batchesConfig": batchesConfig,
                "publicSettings": publicSettings,
                "restrictedImageAccess": restrictedImageAccess,
                "favorite": favorite,
                "modelAccountName": modelAccountName,
                "modelAccountDisplayName": modelAccountDisplayName,
                "imageId": imageId,
                "image": image,
                "modelGroupId": modelGroupId,
                "modelGroupName": modelGroupName,
                "trainingDatasetAccountId": trainingDatasetAccountId,
                "trainingDatasetId": trainingDatasetId,
                "trainingDataset": trainingDataset,
                "trainingDatasetType": trainingDatasetType,
                "trainingFitConfigId": trainingFitConfigId,
                "trainingFitConfig": trainingFitConfig,
                "fitTemplateModelId": fitTemplateModelId,
                "taskType": taskType,
                "trainingModelAccountId": trainingModelAccountId,
                "trainingModelId": trainingModelId,
                "trainingType": trainingType,
                "config": config,
                "env": env,
                "resourceGroup": resourceGroup,
                "shortDescription": shortDescription,
                "languages": languages,
                "lastActivity": lastActivity,
                "state": state,
            }
    
    timeouts: 'ModelTimeoutsData'
    hostingType: MetaOapg.properties.hostingType
    resourceLimits: 'ModelLimitsData'
    restrictedImageAccess: MetaOapg.properties.restrictedImageAccess
    modelName: MetaOapg.properties.modelName
    dataImageMounts: MetaOapg.properties.dataImageMounts
    fittable: MetaOapg.properties.fittable
    retriesConfig: 'ModelRetriesData'
    composite: MetaOapg.properties.composite
    persistentVolumes: MetaOapg.properties.persistentVolumes
    publicSettings: 'ModelPublicSettingsData'
    imageAccountId: MetaOapg.properties.imageAccountId
    id: 'ModelInfoPK'
    favorite: MetaOapg.properties.favorite
    batchesConfig: 'ModelBatchesData'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'ModelInfoPK': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelName"]) -> MetaOapg.properties.modelName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageAccountId"]) -> MetaOapg.properties.imageAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["composite"]) -> MetaOapg.properties.composite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fittable"]) -> MetaOapg.properties.fittable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostingType"]) -> MetaOapg.properties.hostingType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["persistentVolumes"]) -> MetaOapg.properties.persistentVolumes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataImageMounts"]) -> MetaOapg.properties.dataImageMounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeouts"]) -> 'ModelTimeoutsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceLimits"]) -> 'ModelLimitsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retriesConfig"]) -> 'ModelRetriesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batchesConfig"]) -> 'ModelBatchesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicSettings"]) -> 'ModelPublicSettingsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restrictedImageAccess"]) -> MetaOapg.properties.restrictedImageAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["favorite"]) -> MetaOapg.properties.favorite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelAccountName"]) -> MetaOapg.properties.modelAccountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelAccountDisplayName"]) -> MetaOapg.properties.modelAccountDisplayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageId"]) -> MetaOapg.properties.imageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> 'ImageInfoData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelGroupId"]) -> MetaOapg.properties.modelGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelGroupName"]) -> MetaOapg.properties.modelGroupName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDatasetAccountId"]) -> MetaOapg.properties.trainingDatasetAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDatasetId"]) -> MetaOapg.properties.trainingDatasetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDataset"]) -> 'DatasetInfoData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDatasetType"]) -> MetaOapg.properties.trainingDatasetType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingFitConfigId"]) -> MetaOapg.properties.trainingFitConfigId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingFitConfig"]) -> 'FitConfigData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fitTemplateModelId"]) -> MetaOapg.properties.fitTemplateModelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taskType"]) -> MetaOapg.properties.taskType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingModelAccountId"]) -> MetaOapg.properties.trainingModelAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingModelId"]) -> MetaOapg.properties.trainingModelId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingType"]) -> MetaOapg.properties.trainingType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["env"]) -> MetaOapg.properties.env: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceGroup"]) -> MetaOapg.properties.resourceGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shortDescription"]) -> MetaOapg.properties.shortDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["languages"]) -> MetaOapg.properties.languages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastActivity"]) -> MetaOapg.properties.lastActivity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "modelName", "imageAccountId", "composite", "fittable", "hostingType", "persistentVolumes", "dataImageMounts", "timeouts", "resourceLimits", "retriesConfig", "batchesConfig", "publicSettings", "restrictedImageAccess", "favorite", "modelAccountName", "modelAccountDisplayName", "imageId", "image", "modelGroupId", "modelGroupName", "trainingDatasetAccountId", "trainingDatasetId", "trainingDataset", "trainingDatasetType", "trainingFitConfigId", "trainingFitConfig", "fitTemplateModelId", "taskType", "trainingModelAccountId", "trainingModelId", "trainingType", "config", "env", "resourceGroup", "shortDescription", "languages", "lastActivity", "state", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'ModelInfoPK': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelName"]) -> MetaOapg.properties.modelName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageAccountId"]) -> MetaOapg.properties.imageAccountId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["composite"]) -> MetaOapg.properties.composite: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fittable"]) -> MetaOapg.properties.fittable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostingType"]) -> MetaOapg.properties.hostingType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["persistentVolumes"]) -> MetaOapg.properties.persistentVolumes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataImageMounts"]) -> MetaOapg.properties.dataImageMounts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeouts"]) -> 'ModelTimeoutsData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceLimits"]) -> 'ModelLimitsData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retriesConfig"]) -> 'ModelRetriesData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batchesConfig"]) -> 'ModelBatchesData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicSettings"]) -> 'ModelPublicSettingsData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restrictedImageAccess"]) -> MetaOapg.properties.restrictedImageAccess: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["favorite"]) -> MetaOapg.properties.favorite: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelAccountName"]) -> typing.Union[MetaOapg.properties.modelAccountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelAccountDisplayName"]) -> typing.Union[MetaOapg.properties.modelAccountDisplayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageId"]) -> typing.Union[MetaOapg.properties.imageId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> typing.Union['ImageInfoData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelGroupId"]) -> typing.Union[MetaOapg.properties.modelGroupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelGroupName"]) -> typing.Union[MetaOapg.properties.modelGroupName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDatasetAccountId"]) -> typing.Union[MetaOapg.properties.trainingDatasetAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDatasetId"]) -> typing.Union[MetaOapg.properties.trainingDatasetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDataset"]) -> typing.Union['DatasetInfoData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDatasetType"]) -> typing.Union[MetaOapg.properties.trainingDatasetType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingFitConfigId"]) -> typing.Union[MetaOapg.properties.trainingFitConfigId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingFitConfig"]) -> typing.Union['FitConfigData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fitTemplateModelId"]) -> typing.Union[MetaOapg.properties.fitTemplateModelId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taskType"]) -> typing.Union[MetaOapg.properties.taskType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingModelAccountId"]) -> typing.Union[MetaOapg.properties.trainingModelAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingModelId"]) -> typing.Union[MetaOapg.properties.trainingModelId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingType"]) -> typing.Union[MetaOapg.properties.trainingType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union[MetaOapg.properties.config, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["env"]) -> typing.Union[MetaOapg.properties.env, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceGroup"]) -> typing.Union[MetaOapg.properties.resourceGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shortDescription"]) -> typing.Union[MetaOapg.properties.shortDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["languages"]) -> typing.Union[MetaOapg.properties.languages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastActivity"]) -> typing.Union[MetaOapg.properties.lastActivity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "modelName", "imageAccountId", "composite", "fittable", "hostingType", "persistentVolumes", "dataImageMounts", "timeouts", "resourceLimits", "retriesConfig", "batchesConfig", "publicSettings", "restrictedImageAccess", "favorite", "modelAccountName", "modelAccountDisplayName", "imageId", "image", "modelGroupId", "modelGroupName", "trainingDatasetAccountId", "trainingDatasetId", "trainingDataset", "trainingDatasetType", "trainingFitConfigId", "trainingFitConfig", "fitTemplateModelId", "taskType", "trainingModelAccountId", "trainingModelId", "trainingType", "config", "env", "resourceGroup", "shortDescription", "languages", "lastActivity", "state", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        timeouts: 'ModelTimeoutsData',
        hostingType: typing.Union[MetaOapg.properties.hostingType, str, ],
        resourceLimits: 'ModelLimitsData',
        restrictedImageAccess: typing.Union[MetaOapg.properties.restrictedImageAccess, bool, ],
        modelName: typing.Union[MetaOapg.properties.modelName, str, ],
        dataImageMounts: typing.Union[MetaOapg.properties.dataImageMounts, list, tuple, ],
        fittable: typing.Union[MetaOapg.properties.fittable, bool, ],
        retriesConfig: 'ModelRetriesData',
        composite: typing.Union[MetaOapg.properties.composite, bool, ],
        persistentVolumes: typing.Union[MetaOapg.properties.persistentVolumes, list, tuple, ],
        publicSettings: 'ModelPublicSettingsData',
        imageAccountId: typing.Union[MetaOapg.properties.imageAccountId, decimal.Decimal, int, ],
        id: 'ModelInfoPK',
        favorite: typing.Union[MetaOapg.properties.favorite, bool, ],
        batchesConfig: 'ModelBatchesData',
        modelAccountName: typing.Union[MetaOapg.properties.modelAccountName, str, schemas.Unset] = schemas.unset,
        modelAccountDisplayName: typing.Union[MetaOapg.properties.modelAccountDisplayName, str, schemas.Unset] = schemas.unset,
        imageId: typing.Union[MetaOapg.properties.imageId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        image: typing.Union['ImageInfoData', schemas.Unset] = schemas.unset,
        modelGroupId: typing.Union[MetaOapg.properties.modelGroupId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        modelGroupName: typing.Union[MetaOapg.properties.modelGroupName, str, schemas.Unset] = schemas.unset,
        trainingDatasetAccountId: typing.Union[MetaOapg.properties.trainingDatasetAccountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingDatasetId: typing.Union[MetaOapg.properties.trainingDatasetId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingDataset: typing.Union['DatasetInfoData', schemas.Unset] = schemas.unset,
        trainingDatasetType: typing.Union[MetaOapg.properties.trainingDatasetType, str, schemas.Unset] = schemas.unset,
        trainingFitConfigId: typing.Union[MetaOapg.properties.trainingFitConfigId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingFitConfig: typing.Union['FitConfigData', schemas.Unset] = schemas.unset,
        fitTemplateModelId: typing.Union[MetaOapg.properties.fitTemplateModelId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        taskType: typing.Union[MetaOapg.properties.taskType, str, schemas.Unset] = schemas.unset,
        trainingModelAccountId: typing.Union[MetaOapg.properties.trainingModelAccountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingModelId: typing.Union[MetaOapg.properties.trainingModelId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        trainingType: typing.Union[MetaOapg.properties.trainingType, str, schemas.Unset] = schemas.unset,
        config: typing.Union[MetaOapg.properties.config, str, schemas.Unset] = schemas.unset,
        env: typing.Union[MetaOapg.properties.env, str, schemas.Unset] = schemas.unset,
        resourceGroup: typing.Union[MetaOapg.properties.resourceGroup, str, schemas.Unset] = schemas.unset,
        shortDescription: typing.Union[MetaOapg.properties.shortDescription, str, schemas.Unset] = schemas.unset,
        languages: typing.Union[MetaOapg.properties.languages, list, tuple, schemas.Unset] = schemas.unset,
        lastActivity: typing.Union[MetaOapg.properties.lastActivity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelInfoData':
        return super().__new__(
            cls,
            *_args,
            timeouts=timeouts,
            hostingType=hostingType,
            resourceLimits=resourceLimits,
            restrictedImageAccess=restrictedImageAccess,
            modelName=modelName,
            dataImageMounts=dataImageMounts,
            fittable=fittable,
            retriesConfig=retriesConfig,
            composite=composite,
            persistentVolumes=persistentVolumes,
            publicSettings=publicSettings,
            imageAccountId=imageAccountId,
            id=id,
            favorite=favorite,
            batchesConfig=batchesConfig,
            modelAccountName=modelAccountName,
            modelAccountDisplayName=modelAccountDisplayName,
            imageId=imageId,
            image=image,
            modelGroupId=modelGroupId,
            modelGroupName=modelGroupName,
            trainingDatasetAccountId=trainingDatasetAccountId,
            trainingDatasetId=trainingDatasetId,
            trainingDataset=trainingDataset,
            trainingDatasetType=trainingDatasetType,
            trainingFitConfigId=trainingFitConfigId,
            trainingFitConfig=trainingFitConfig,
            fitTemplateModelId=fitTemplateModelId,
            taskType=taskType,
            trainingModelAccountId=trainingModelAccountId,
            trainingModelId=trainingModelId,
            trainingType=trainingType,
            config=config,
            env=env,
            resourceGroup=resourceGroup,
            shortDescription=shortDescription,
            languages=languages,
            lastActivity=lastActivity,
            state=state,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.data_image_mount_data import DataImageMountData
from mlp_api.model.dataset_info_data import DatasetInfoData
from mlp_api.model.fit_config_data import FitConfigData
from mlp_api.model.image_info_data import ImageInfoData
from mlp_api.model.model_batches_data import ModelBatchesData
from mlp_api.model.model_info_pk import ModelInfoPK
from mlp_api.model.model_limits_data import ModelLimitsData
from mlp_api.model.model_public_settings_data import ModelPublicSettingsData
from mlp_api.model.model_retries_data import ModelRetriesData
from mlp_api.model.model_timeouts_data import ModelTimeoutsData
from mlp_api.model.persistent_volume_data import PersistentVolumeData
