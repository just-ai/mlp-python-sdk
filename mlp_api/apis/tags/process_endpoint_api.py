# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""

from mlp_api.paths.api_mlpgate_account_account_model_model_cross_validation.post import CrossValidation
from mlp_api.paths.api_mlpgate_account_account_model_model_ext.post import Ext
from mlp_api.paths.api_mlpgate_account_account_model_model_fit.post import Fit
from mlp_api.paths.api_mlpgate_account_account_model_model_fit_v2.post import FitV2
from mlp_api.paths.p_account_field_model_field.get import GetModelInfoOld
from mlp_api.paths.api_mlpgate_account_account_model_model_predict.post import Predict
from mlp_api.paths.api_mlpgate_account_account_model_model_predict_with_config.post import PredictWithConfig
from mlp_api.paths.api_mlpgate_account_account_model_model_predict_with_config_v2.post import PredictWithConfigV2
from mlp_api.paths.p_account_field_model_field.post import ServletPredict
from mlp_api.paths.api_mlpgate_account_account_model_model_tts.get import TtsStreamGet
from mlp_api.paths.api_mlpgate_account_account_model_model_tts.post import TtsStreamPost


class ProcessEndpointApi(
    CrossValidation,
    Ext,
    Fit,
    FitV2,
    GetModelInfoOld,
    Predict,
    PredictWithConfig,
    PredictWithConfigV2,
    ServletPredict,
    TtsStreamGet,
    TtsStreamPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
