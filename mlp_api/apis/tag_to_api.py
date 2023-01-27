import typing_extensions

from mlp_api.apis.tags import TagValues
from mlp_api.apis.tags.access_token_endpoint_api import AccessTokenEndpointApi
from mlp_api.apis.tags.account_endpoint_api import AccountEndpointApi
from mlp_api.apis.tags.admin_endpoint_api import AdminEndpointApi
from mlp_api.apis.tags.data_image_endpoint_api import DataImageEndpointApi
from mlp_api.apis.tags.dataset_endpoint_api import DatasetEndpointApi
from mlp_api.apis.tags.fit_config_endpoint_api import FitConfigEndpointApi
from mlp_api.apis.tags.image_endpoint_api import ImageEndpointApi
from mlp_api.apis.tags.internal_endpoint_api import InternalEndpointApi
from mlp_api.apis.tags.job_endpoint_api import JobEndpointApi
from mlp_api.apis.tags.manual_management_endpoint_api import ManualManagementEndpointApi
from mlp_api.apis.tags.metric_endpoint_api import MetricEndpointApi
from mlp_api.apis.tags.model_endpoint_api import ModelEndpointApi
from mlp_api.apis.tags.model_instance_endpoint_api import ModelInstanceEndpointApi
from mlp_api.apis.tags.predict_config_endpoint_api import PredictConfigEndpointApi
from mlp_api.apis.tags.process_endpoint_api import ProcessEndpointApi
from mlp_api.apis.tags.process_servlet_api import ProcessServletApi
from mlp_api.apis.tags.stat_log_endpoint_api import StatLogEndpointApi
from mlp_api.apis.tags.system_config_endpoint_api import SystemConfigEndpointApi
from mlp_api.apis.tags.system_endpoint_api import SystemEndpointApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCESSTOKENENDPOINT: AccessTokenEndpointApi,
        TagValues.ACCOUNTENDPOINT: AccountEndpointApi,
        TagValues.ADMINENDPOINT: AdminEndpointApi,
        TagValues.DATAIMAGEENDPOINT: DataImageEndpointApi,
        TagValues.DATASETENDPOINT: DatasetEndpointApi,
        TagValues.FITCONFIGENDPOINT: FitConfigEndpointApi,
        TagValues.IMAGEENDPOINT: ImageEndpointApi,
        TagValues.INTERNALENDPOINT: InternalEndpointApi,
        TagValues.JOBENDPOINT: JobEndpointApi,
        TagValues.MANUALMANAGEMENTENDPOINT: ManualManagementEndpointApi,
        TagValues.METRICENDPOINT: MetricEndpointApi,
        TagValues.MODELENDPOINT: ModelEndpointApi,
        TagValues.MODELINSTANCEENDPOINT: ModelInstanceEndpointApi,
        TagValues.PREDICTCONFIGENDPOINT: PredictConfigEndpointApi,
        TagValues.PROCESSENDPOINT: ProcessEndpointApi,
        TagValues.PROCESSSERVLET: ProcessServletApi,
        TagValues.STATLOGENDPOINT: StatLogEndpointApi,
        TagValues.SYSTEMCONFIGENDPOINT: SystemConfigEndpointApi,
        TagValues.SYSTEMENDPOINT: SystemEndpointApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCESSTOKENENDPOINT: AccessTokenEndpointApi,
        TagValues.ACCOUNTENDPOINT: AccountEndpointApi,
        TagValues.ADMINENDPOINT: AdminEndpointApi,
        TagValues.DATAIMAGEENDPOINT: DataImageEndpointApi,
        TagValues.DATASETENDPOINT: DatasetEndpointApi,
        TagValues.FITCONFIGENDPOINT: FitConfigEndpointApi,
        TagValues.IMAGEENDPOINT: ImageEndpointApi,
        TagValues.INTERNALENDPOINT: InternalEndpointApi,
        TagValues.JOBENDPOINT: JobEndpointApi,
        TagValues.MANUALMANAGEMENTENDPOINT: ManualManagementEndpointApi,
        TagValues.METRICENDPOINT: MetricEndpointApi,
        TagValues.MODELENDPOINT: ModelEndpointApi,
        TagValues.MODELINSTANCEENDPOINT: ModelInstanceEndpointApi,
        TagValues.PREDICTCONFIGENDPOINT: PredictConfigEndpointApi,
        TagValues.PROCESSENDPOINT: ProcessEndpointApi,
        TagValues.PROCESSSERVLET: ProcessServletApi,
        TagValues.STATLOGENDPOINT: StatLogEndpointApi,
        TagValues.SYSTEMCONFIGENDPOINT: SystemConfigEndpointApi,
        TagValues.SYSTEMENDPOINT: SystemEndpointApi,
    }
)
