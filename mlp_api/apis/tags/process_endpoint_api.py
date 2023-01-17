# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_cross_validation.post import CrossValidation
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_ext.post import Ext
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_fit.post import Fit
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_predict.post import Predict
from mlp_api.paths.api_mlpgate_account_account_id_model_model_id_predict_with_config.post import PredictWithConfig


class ProcessEndpointApi(
    CrossValidation,
    Ext,
    Fit,
    Predict,
    PredictWithConfig,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass