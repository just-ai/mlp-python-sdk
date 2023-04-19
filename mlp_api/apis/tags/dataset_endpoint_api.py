# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from mlp_api.paths.api_mlpgate_account_account_dataset_form.post import CreateDatasetByForm
from mlp_api.paths.api_mlpgate_account_account_dataset.post import CreateEmptyDataset
from mlp_api.paths.api_mlpgate_account_account_dataset_dataset_id.delete import DeleteDataset
from mlp_api.paths.api_mlpgate_account_account_dataset_dataset_id_content.get import DownloadDatasetRawContent
from mlp_api.paths.api_mlpgate_account_account_dataset_dataset_id.get import GetDatasetInfo
from mlp_api.paths.api_mlpgate_account_account_dataset_original_dataset_id_paraphrase.get import GetParaphrasedDatasetStatus
from mlp_api.paths.api_mlpgate_account_account_dataset.get import ListDatasets
from mlp_api.paths.api_mlpgate_account_account_dataset_dataset_id_paraphrase.post import ParaphraseDataset
from mlp_api.paths.api_mlpgate_account_account_dataset_dataset_id.post import UpdateDataset
from mlp_api.paths.api_mlpgate_account_account_dataset_dataset_id_content.post import UploadDatasetContent


class DatasetEndpointApi(
    CreateDatasetByForm,
    CreateEmptyDataset,
    DeleteDataset,
    DownloadDatasetRawContent,
    GetDatasetInfo,
    GetParaphrasedDatasetStatus,
    ListDatasets,
    ParaphraseDataset,
    UpdateDataset,
    UploadDatasetContent,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
