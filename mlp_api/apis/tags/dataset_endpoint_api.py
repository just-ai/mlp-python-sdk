# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from mlp_api.paths.api_mlpgate_account_account_id_dataset.post import CreateDataset
from mlp_api.paths.api_mlpgate_account_account_id_dataset_dataset_id.delete import DeleteDataset
from mlp_api.paths.api_mlpgate_account_account_id_dataset_dataset_id_content.get import DownloadDatasetContent
from mlp_api.paths.api_mlpgate_account_account_id_dataset_dataset_id.get import GetDatasetInfo
from mlp_api.paths.api_mlpgate_account_account_id_dataset.get import ListDatasets
from mlp_api.paths.api_mlpgate_account_account_id_dataset_dataset_id.post import UpdateDataset
from mlp_api.paths.api_mlpgate_account_account_id_dataset_dataset_id_content.post import UploadDatasetContent


class DatasetEndpointApi(
    CreateDataset,
    DeleteDataset,
    DownloadDatasetContent,
    GetDatasetInfo,
    ListDatasets,
    UpdateDataset,
    UploadDatasetContent,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
