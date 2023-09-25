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


class ModelDump(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "image",
            "docs",
            "asPublicSettingsData",
            "fitConfigs",
            "name",
            "asBillingSettingsData",
            "predictConfigs",
        }
        
        class properties:
            name = schemas.StrSchema
            image = schemas.StrSchema
            
            
            class docs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DocumentDump']:
                        return DocumentDump
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DocumentDump'], typing.List['DocumentDump']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'docs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DocumentDump':
                    return super().__getitem__(i)
            
            
            class predictConfigs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PredictConfigDump']:
                        return PredictConfigDump
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['PredictConfigDump'], typing.List['PredictConfigDump']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'predictConfigs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PredictConfigDump':
                    return super().__getitem__(i)
            
            
            class fitConfigs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FitConfigDump']:
                        return FitConfigDump
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['FitConfigDump'], typing.List['FitConfigDump']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fitConfigs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FitConfigDump':
                    return super().__getitem__(i)
        
            @staticmethod
            def asBillingSettingsData() -> typing.Type['ModelBillingSettingsData']:
                return ModelBillingSettingsData
        
            @staticmethod
            def asPublicSettingsData() -> typing.Type['ModelPublicSettingsData']:
                return ModelPublicSettingsData
            imageAccount = schemas.StrSchema
            modelGroup = schemas.StrSchema
            isPublic = schemas.BoolSchema
            config = schemas.DictSchema
            env = schemas.DictSchema
            trainingModelAccount = schemas.StrSchema
            trainingModelName = schemas.StrSchema
            trainingDatasetAccount = schemas.StrSchema
            trainingDatasetName = schemas.StrSchema
            trainingFitConfigName = schemas.StrSchema
            taskType = schemas.StrSchema
            trainingDatasetType = schemas.StrSchema
            fitTemplateModelName = schemas.StrSchema
            composite = schemas.BoolSchema
            fittable = schemas.BoolSchema
            
            
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
            
            
            class dataImageMounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DataImageMountDump']:
                        return DataImageMountDump
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DataImageMountDump'], typing.List['DataImageMountDump']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dataImageMounts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DataImageMountDump':
                    return super().__getitem__(i)
        
            @staticmethod
            def timeouts() -> typing.Type['ModelTimeoutsData']:
                return ModelTimeoutsData
        
            @staticmethod
            def limits() -> typing.Type['ModelLimitsData']:
                return ModelLimitsData
        
            @staticmethod
            def retries() -> typing.Type['ModelRetriesData']:
                return ModelRetriesData
        
            @staticmethod
            def batches() -> typing.Type['ModelBatchesData']:
                return ModelBatchesData
        
            @staticmethod
            def caching() -> typing.Type['ModelCachingData']:
                return ModelCachingData
        
            @staticmethod
            def priorityQueue() -> typing.Type['ModelPriorityQueueData']:
                return ModelPriorityQueueData
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
            availableInJaicp = schemas.BoolSchema
            featured = schemas.BoolSchema
            featuredListOrder = schemas.Int32Schema
            minInstancesCount = schemas.Int32Schema
            startTimeSec = schemas.Float32Schema
            hidden = schemas.BoolSchema
            publicTestingAllowed = schemas.BoolSchema
            isBillingEnabled = schemas.BoolSchema
            
            
            class billingUnit(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CALLS(cls):
                    return cls("calls")
                
                @schemas.classproperty
                def BYTES(cls):
                    return cls("bytes")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("custom")
            billingUnitPriceInNanoToken = schemas.Int64Schema
            freeUnitQuota = schemas.Int32Schema
            __annotations__ = {
                "name": name,
                "image": image,
                "docs": docs,
                "predictConfigs": predictConfigs,
                "fitConfigs": fitConfigs,
                "asBillingSettingsData": asBillingSettingsData,
                "asPublicSettingsData": asPublicSettingsData,
                "imageAccount": imageAccount,
                "modelGroup": modelGroup,
                "isPublic": isPublic,
                "config": config,
                "env": env,
                "trainingModelAccount": trainingModelAccount,
                "trainingModelName": trainingModelName,
                "trainingDatasetAccount": trainingDatasetAccount,
                "trainingDatasetName": trainingDatasetName,
                "trainingFitConfigName": trainingFitConfigName,
                "taskType": taskType,
                "trainingDatasetType": trainingDatasetType,
                "fitTemplateModelName": fitTemplateModelName,
                "composite": composite,
                "fittable": fittable,
                "trainingType": trainingType,
                "hostingType": hostingType,
                "dataImageMounts": dataImageMounts,
                "timeouts": timeouts,
                "limits": limits,
                "retries": retries,
                "batches": batches,
                "caching": caching,
                "priorityQueue": priorityQueue,
                "resourceGroup": resourceGroup,
                "shortDescription": shortDescription,
                "languages": languages,
                "availableInJaicp": availableInJaicp,
                "featured": featured,
                "featuredListOrder": featuredListOrder,
                "minInstancesCount": minInstancesCount,
                "startTimeSec": startTimeSec,
                "hidden": hidden,
                "publicTestingAllowed": publicTestingAllowed,
                "isBillingEnabled": isBillingEnabled,
                "billingUnit": billingUnit,
                "billingUnitPriceInNanoToken": billingUnitPriceInNanoToken,
                "freeUnitQuota": freeUnitQuota,
            }
    
    image: MetaOapg.properties.image
    docs: MetaOapg.properties.docs
    asPublicSettingsData: 'ModelPublicSettingsData'
    fitConfigs: MetaOapg.properties.fitConfigs
    name: MetaOapg.properties.name
    asBillingSettingsData: 'ModelBillingSettingsData'
    predictConfigs: MetaOapg.properties.predictConfigs
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["docs"]) -> MetaOapg.properties.docs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["predictConfigs"]) -> MetaOapg.properties.predictConfigs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fitConfigs"]) -> MetaOapg.properties.fitConfigs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asBillingSettingsData"]) -> 'ModelBillingSettingsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asPublicSettingsData"]) -> 'ModelPublicSettingsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageAccount"]) -> MetaOapg.properties.imageAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modelGroup"]) -> MetaOapg.properties.modelGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPublic"]) -> MetaOapg.properties.isPublic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["env"]) -> MetaOapg.properties.env: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingModelAccount"]) -> MetaOapg.properties.trainingModelAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingModelName"]) -> MetaOapg.properties.trainingModelName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDatasetAccount"]) -> MetaOapg.properties.trainingDatasetAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDatasetName"]) -> MetaOapg.properties.trainingDatasetName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingFitConfigName"]) -> MetaOapg.properties.trainingFitConfigName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taskType"]) -> MetaOapg.properties.taskType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingDatasetType"]) -> MetaOapg.properties.trainingDatasetType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fitTemplateModelName"]) -> MetaOapg.properties.fitTemplateModelName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["composite"]) -> MetaOapg.properties.composite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fittable"]) -> MetaOapg.properties.fittable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trainingType"]) -> MetaOapg.properties.trainingType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostingType"]) -> MetaOapg.properties.hostingType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataImageMounts"]) -> MetaOapg.properties.dataImageMounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeouts"]) -> 'ModelTimeoutsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limits"]) -> 'ModelLimitsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retries"]) -> 'ModelRetriesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batches"]) -> 'ModelBatchesData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caching"]) -> 'ModelCachingData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priorityQueue"]) -> 'ModelPriorityQueueData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceGroup"]) -> MetaOapg.properties.resourceGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shortDescription"]) -> MetaOapg.properties.shortDescription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["languages"]) -> MetaOapg.properties.languages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availableInJaicp"]) -> MetaOapg.properties.availableInJaicp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["featured"]) -> MetaOapg.properties.featured: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["featuredListOrder"]) -> MetaOapg.properties.featuredListOrder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minInstancesCount"]) -> MetaOapg.properties.minInstancesCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTimeSec"]) -> MetaOapg.properties.startTimeSec: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hidden"]) -> MetaOapg.properties.hidden: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicTestingAllowed"]) -> MetaOapg.properties.publicTestingAllowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isBillingEnabled"]) -> MetaOapg.properties.isBillingEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingUnit"]) -> MetaOapg.properties.billingUnit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingUnitPriceInNanoToken"]) -> MetaOapg.properties.billingUnitPriceInNanoToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["freeUnitQuota"]) -> MetaOapg.properties.freeUnitQuota: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "image", "docs", "predictConfigs", "fitConfigs", "asBillingSettingsData", "asPublicSettingsData", "imageAccount", "modelGroup", "isPublic", "config", "env", "trainingModelAccount", "trainingModelName", "trainingDatasetAccount", "trainingDatasetName", "trainingFitConfigName", "taskType", "trainingDatasetType", "fitTemplateModelName", "composite", "fittable", "trainingType", "hostingType", "dataImageMounts", "timeouts", "limits", "retries", "batches", "caching", "priorityQueue", "resourceGroup", "shortDescription", "languages", "availableInJaicp", "featured", "featuredListOrder", "minInstancesCount", "startTimeSec", "hidden", "publicTestingAllowed", "isBillingEnabled", "billingUnit", "billingUnitPriceInNanoToken", "freeUnitQuota", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["docs"]) -> MetaOapg.properties.docs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["predictConfigs"]) -> MetaOapg.properties.predictConfigs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fitConfigs"]) -> MetaOapg.properties.fitConfigs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asBillingSettingsData"]) -> 'ModelBillingSettingsData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asPublicSettingsData"]) -> 'ModelPublicSettingsData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageAccount"]) -> typing.Union[MetaOapg.properties.imageAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modelGroup"]) -> typing.Union[MetaOapg.properties.modelGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPublic"]) -> typing.Union[MetaOapg.properties.isPublic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union[MetaOapg.properties.config, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["env"]) -> typing.Union[MetaOapg.properties.env, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingModelAccount"]) -> typing.Union[MetaOapg.properties.trainingModelAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingModelName"]) -> typing.Union[MetaOapg.properties.trainingModelName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDatasetAccount"]) -> typing.Union[MetaOapg.properties.trainingDatasetAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDatasetName"]) -> typing.Union[MetaOapg.properties.trainingDatasetName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingFitConfigName"]) -> typing.Union[MetaOapg.properties.trainingFitConfigName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taskType"]) -> typing.Union[MetaOapg.properties.taskType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingDatasetType"]) -> typing.Union[MetaOapg.properties.trainingDatasetType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fitTemplateModelName"]) -> typing.Union[MetaOapg.properties.fitTemplateModelName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["composite"]) -> typing.Union[MetaOapg.properties.composite, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fittable"]) -> typing.Union[MetaOapg.properties.fittable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trainingType"]) -> typing.Union[MetaOapg.properties.trainingType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostingType"]) -> typing.Union[MetaOapg.properties.hostingType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataImageMounts"]) -> typing.Union[MetaOapg.properties.dataImageMounts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeouts"]) -> typing.Union['ModelTimeoutsData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limits"]) -> typing.Union['ModelLimitsData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retries"]) -> typing.Union['ModelRetriesData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batches"]) -> typing.Union['ModelBatchesData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caching"]) -> typing.Union['ModelCachingData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priorityQueue"]) -> typing.Union['ModelPriorityQueueData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceGroup"]) -> typing.Union[MetaOapg.properties.resourceGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shortDescription"]) -> typing.Union[MetaOapg.properties.shortDescription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["languages"]) -> typing.Union[MetaOapg.properties.languages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availableInJaicp"]) -> typing.Union[MetaOapg.properties.availableInJaicp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["featured"]) -> typing.Union[MetaOapg.properties.featured, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["featuredListOrder"]) -> typing.Union[MetaOapg.properties.featuredListOrder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minInstancesCount"]) -> typing.Union[MetaOapg.properties.minInstancesCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTimeSec"]) -> typing.Union[MetaOapg.properties.startTimeSec, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hidden"]) -> typing.Union[MetaOapg.properties.hidden, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicTestingAllowed"]) -> typing.Union[MetaOapg.properties.publicTestingAllowed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isBillingEnabled"]) -> typing.Union[MetaOapg.properties.isBillingEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingUnit"]) -> typing.Union[MetaOapg.properties.billingUnit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingUnitPriceInNanoToken"]) -> typing.Union[MetaOapg.properties.billingUnitPriceInNanoToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["freeUnitQuota"]) -> typing.Union[MetaOapg.properties.freeUnitQuota, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "image", "docs", "predictConfigs", "fitConfigs", "asBillingSettingsData", "asPublicSettingsData", "imageAccount", "modelGroup", "isPublic", "config", "env", "trainingModelAccount", "trainingModelName", "trainingDatasetAccount", "trainingDatasetName", "trainingFitConfigName", "taskType", "trainingDatasetType", "fitTemplateModelName", "composite", "fittable", "trainingType", "hostingType", "dataImageMounts", "timeouts", "limits", "retries", "batches", "caching", "priorityQueue", "resourceGroup", "shortDescription", "languages", "availableInJaicp", "featured", "featuredListOrder", "minInstancesCount", "startTimeSec", "hidden", "publicTestingAllowed", "isBillingEnabled", "billingUnit", "billingUnitPriceInNanoToken", "freeUnitQuota", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        image: typing.Union[MetaOapg.properties.image, str, ],
        docs: typing.Union[MetaOapg.properties.docs, list, tuple, ],
        asPublicSettingsData: 'ModelPublicSettingsData',
        fitConfigs: typing.Union[MetaOapg.properties.fitConfigs, list, tuple, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        asBillingSettingsData: 'ModelBillingSettingsData',
        predictConfigs: typing.Union[MetaOapg.properties.predictConfigs, list, tuple, ],
        imageAccount: typing.Union[MetaOapg.properties.imageAccount, str, schemas.Unset] = schemas.unset,
        modelGroup: typing.Union[MetaOapg.properties.modelGroup, str, schemas.Unset] = schemas.unset,
        isPublic: typing.Union[MetaOapg.properties.isPublic, bool, schemas.Unset] = schemas.unset,
        config: typing.Union[MetaOapg.properties.config, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        env: typing.Union[MetaOapg.properties.env, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        trainingModelAccount: typing.Union[MetaOapg.properties.trainingModelAccount, str, schemas.Unset] = schemas.unset,
        trainingModelName: typing.Union[MetaOapg.properties.trainingModelName, str, schemas.Unset] = schemas.unset,
        trainingDatasetAccount: typing.Union[MetaOapg.properties.trainingDatasetAccount, str, schemas.Unset] = schemas.unset,
        trainingDatasetName: typing.Union[MetaOapg.properties.trainingDatasetName, str, schemas.Unset] = schemas.unset,
        trainingFitConfigName: typing.Union[MetaOapg.properties.trainingFitConfigName, str, schemas.Unset] = schemas.unset,
        taskType: typing.Union[MetaOapg.properties.taskType, str, schemas.Unset] = schemas.unset,
        trainingDatasetType: typing.Union[MetaOapg.properties.trainingDatasetType, str, schemas.Unset] = schemas.unset,
        fitTemplateModelName: typing.Union[MetaOapg.properties.fitTemplateModelName, str, schemas.Unset] = schemas.unset,
        composite: typing.Union[MetaOapg.properties.composite, bool, schemas.Unset] = schemas.unset,
        fittable: typing.Union[MetaOapg.properties.fittable, bool, schemas.Unset] = schemas.unset,
        trainingType: typing.Union[MetaOapg.properties.trainingType, str, schemas.Unset] = schemas.unset,
        hostingType: typing.Union[MetaOapg.properties.hostingType, str, schemas.Unset] = schemas.unset,
        dataImageMounts: typing.Union[MetaOapg.properties.dataImageMounts, list, tuple, schemas.Unset] = schemas.unset,
        timeouts: typing.Union['ModelTimeoutsData', schemas.Unset] = schemas.unset,
        limits: typing.Union['ModelLimitsData', schemas.Unset] = schemas.unset,
        retries: typing.Union['ModelRetriesData', schemas.Unset] = schemas.unset,
        batches: typing.Union['ModelBatchesData', schemas.Unset] = schemas.unset,
        caching: typing.Union['ModelCachingData', schemas.Unset] = schemas.unset,
        priorityQueue: typing.Union['ModelPriorityQueueData', schemas.Unset] = schemas.unset,
        resourceGroup: typing.Union[MetaOapg.properties.resourceGroup, str, schemas.Unset] = schemas.unset,
        shortDescription: typing.Union[MetaOapg.properties.shortDescription, str, schemas.Unset] = schemas.unset,
        languages: typing.Union[MetaOapg.properties.languages, list, tuple, schemas.Unset] = schemas.unset,
        availableInJaicp: typing.Union[MetaOapg.properties.availableInJaicp, bool, schemas.Unset] = schemas.unset,
        featured: typing.Union[MetaOapg.properties.featured, bool, schemas.Unset] = schemas.unset,
        featuredListOrder: typing.Union[MetaOapg.properties.featuredListOrder, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        minInstancesCount: typing.Union[MetaOapg.properties.minInstancesCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        startTimeSec: typing.Union[MetaOapg.properties.startTimeSec, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        hidden: typing.Union[MetaOapg.properties.hidden, bool, schemas.Unset] = schemas.unset,
        publicTestingAllowed: typing.Union[MetaOapg.properties.publicTestingAllowed, bool, schemas.Unset] = schemas.unset,
        isBillingEnabled: typing.Union[MetaOapg.properties.isBillingEnabled, bool, schemas.Unset] = schemas.unset,
        billingUnit: typing.Union[MetaOapg.properties.billingUnit, str, schemas.Unset] = schemas.unset,
        billingUnitPriceInNanoToken: typing.Union[MetaOapg.properties.billingUnitPriceInNanoToken, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        freeUnitQuota: typing.Union[MetaOapg.properties.freeUnitQuota, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelDump':
        return super().__new__(
            cls,
            *_args,
            image=image,
            docs=docs,
            asPublicSettingsData=asPublicSettingsData,
            fitConfigs=fitConfigs,
            name=name,
            asBillingSettingsData=asBillingSettingsData,
            predictConfigs=predictConfigs,
            imageAccount=imageAccount,
            modelGroup=modelGroup,
            isPublic=isPublic,
            config=config,
            env=env,
            trainingModelAccount=trainingModelAccount,
            trainingModelName=trainingModelName,
            trainingDatasetAccount=trainingDatasetAccount,
            trainingDatasetName=trainingDatasetName,
            trainingFitConfigName=trainingFitConfigName,
            taskType=taskType,
            trainingDatasetType=trainingDatasetType,
            fitTemplateModelName=fitTemplateModelName,
            composite=composite,
            fittable=fittable,
            trainingType=trainingType,
            hostingType=hostingType,
            dataImageMounts=dataImageMounts,
            timeouts=timeouts,
            limits=limits,
            retries=retries,
            batches=batches,
            caching=caching,
            priorityQueue=priorityQueue,
            resourceGroup=resourceGroup,
            shortDescription=shortDescription,
            languages=languages,
            availableInJaicp=availableInJaicp,
            featured=featured,
            featuredListOrder=featuredListOrder,
            minInstancesCount=minInstancesCount,
            startTimeSec=startTimeSec,
            hidden=hidden,
            publicTestingAllowed=publicTestingAllowed,
            isBillingEnabled=isBillingEnabled,
            billingUnit=billingUnit,
            billingUnitPriceInNanoToken=billingUnitPriceInNanoToken,
            freeUnitQuota=freeUnitQuota,
            _configuration=_configuration,
            **kwargs,
        )

from mlp_api.model.data_image_mount_dump import DataImageMountDump
from mlp_api.model.document_dump import DocumentDump
from mlp_api.model.fit_config_dump import FitConfigDump
from mlp_api.model.model_batches_data import ModelBatchesData
from mlp_api.model.model_billing_settings_data import ModelBillingSettingsData
from mlp_api.model.model_caching_data import ModelCachingData
from mlp_api.model.model_limits_data import ModelLimitsData
from mlp_api.model.model_priority_queue_data import ModelPriorityQueueData
from mlp_api.model.model_public_settings_data import ModelPublicSettingsData
from mlp_api.model.model_retries_data import ModelRetriesData
from mlp_api.model.model_timeouts_data import ModelTimeoutsData
from mlp_api.model.predict_config_dump import PredictConfigDump
