# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from mlp_api.paths.api_mlpgate_health.get import HealthCheck
from mlp_api.paths.api_mlpgate_health_test.get import HealthCheckForTests
from mlp_api.paths.api_mlpgate_version.get import Version


class SystemEndpointApi(
    HealthCheck,
    HealthCheckForTests,
    Version,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass