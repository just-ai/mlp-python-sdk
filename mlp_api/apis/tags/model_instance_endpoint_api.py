# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from mlp_api.paths.api_mlpgate_account_account_model_model_instance_instance_id_events.get import GetInstanceEvents
from mlp_api.paths.api_mlpgate_account_account_model_model_instance_instance_id_file_logs.get import GetInstanceLogFile
from mlp_api.paths.api_mlpgate_account_account_model_model_instance_instance_id_file.get import GetInstancePodFile
from mlp_api.paths.api_mlpgate_account_account_model_model_instance_instance_id_environment.get import GetModelInstanceEnvironment
from mlp_api.paths.api_mlpgate_account_account_model_model_instance_instance_id_timing.get import GetModelInstanceStartTime
from mlp_api.paths.api_mlpgate_account_account_model_model_instance.get import GetModelInstances
from mlp_api.paths.api_mlpgate_account_account_model_model_instance_instance_id_stop.post import StopInstance
from mlp_api.paths.api_mlpgate_account_account_model_model_instance_instance_id_terminate.post import TerminateInstance


class ModelInstanceEndpointApi(
    GetInstanceEvents,
    GetInstanceLogFile,
    GetInstancePodFile,
    GetModelInstanceEnvironment,
    GetModelInstanceStartTime,
    GetModelInstances,
    StopInstance,
    TerminateInstance,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
