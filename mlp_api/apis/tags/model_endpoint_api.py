# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_derived.post import CreateDerivedModel
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_external.post import CreateExternalConnection
from mlp_api.paths.api_mlpgate_account_account_id_model.post import CreateModel
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_external_instance_id.delete import DeleteExternalConnection
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id.delete import DeleteModel
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_external.get import GetExternalConnectionsInfo
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_instances.get import GetInstancesStatus
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_logs.get import GetLogsByModel
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id.get import GetModelInfo
from mlp_api.paths.api_mlpgate_account_account_id_model.get import GetPagedModels
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_action_descriptor.get import GetServiceDescriptor
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_simple_doc.get import GetSimpleDoc
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_last_job.get import LastJob
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_instances.post import SetRequestedInstancesCount
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_simple_doc.post import SetSimpleDoc
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_status.get import ShortModelStatus
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_instance_start.post import StartNewInstance
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id.post import UpdateModel


class ModelEndpointApi(
    CreateDerivedModel,
    CreateExternalConnection,
    CreateModel,
    DeleteExternalConnection,
    DeleteModel,
    GetExternalConnectionsInfo,
    GetInstancesStatus,
    GetLogsByModel,
    GetModelInfo,
    GetPagedModels,
    GetServiceDescriptor,
    GetSimpleDoc,
    LastJob,
    SetRequestedInstancesCount,
    SetSimpleDoc,
    ShortModelStatus,
    StartNewInstance,
    UpdateModel,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
