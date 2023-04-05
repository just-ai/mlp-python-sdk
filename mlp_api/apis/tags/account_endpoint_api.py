# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from mlp_api.paths.api_mlpgate_account_account_dump.get import DumpConfig
from mlp_api.paths.api_mlpgate_account.get import EnsureAccount
from mlp_api.paths.api_mlpgate_account_account_s3.get import GetS3Credentials
from mlp_api.paths.api_mlpgate_account_account_dump.post import RestoreConfig
from mlp_api.paths.api_mlpgate_account.post import UpdateAccountData


class AccountEndpointApi(
    DumpConfig,
    EnsureAccount,
    GetS3Credentials,
    RestoreConfig,
    UpdateAccountData,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
