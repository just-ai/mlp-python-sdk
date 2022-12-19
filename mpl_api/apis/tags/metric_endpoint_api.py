# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from mpl_api.paths.api_mplgate_account_account_id_metric.get import GetAccountMetric
from mpl_api.paths.api_mplgate_account_account_id_metric_range.get import GetAccountMetricRange
from mpl_api.paths.api_mplgate_account_account_id_model_model_id_instance_instance_id_metric.get import GetInstanceMetric
from mpl_api.paths.api_mplgate_account_account_id_model_model_id_instance_instance_id_metric_range.get import GetInstanceMetricRange
from mpl_api.paths.api_mplgate_account_account_id_model_model_id_metric.get import GetModelMetric
from mpl_api.paths.api_mplgate_account_account_id_model_model_id_metric_range.get import GetModelMetricRange


class MetricEndpointApi(
    GetAccountMetric,
    GetAccountMetricRange,
    GetInstanceMetric,
    GetInstanceMetricRange,
    GetModelMetric,
    GetModelMetricRange,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
