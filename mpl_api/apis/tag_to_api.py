import typing_extensions

from mpl_api.apis.tags import TagValues
from mpl_api.apis.tags.access_token_endpoint_api import AccessTokenEndpointApi
from mpl_api.apis.tags.account_endpoint_api import AccountEndpointApi
from mpl_api.apis.tags.admin_endpoint_api import AdminEndpointApi
from mpl_api.apis.tags.data_image_endpoint_api import DataImageEndpointApi
from mpl_api.apis.tags.dataset_endpoint_api import DatasetEndpointApi
from mpl_api.apis.tags.fit_config_endpoint_api import FitConfigEndpointApi
from mpl_api.apis.tags.image_endpoint_api import ImageEndpointApi
from mpl_api.apis.tags.internal_endpoint_api import InternalEndpointApi
from mpl_api.apis.tags.job_endpoint_api import JobEndpointApi
from mpl_api.apis.tags.manual_management_endpoint_api import ManualManagementEndpointApi
from mpl_api.apis.tags.metric_endpoint_api import MetricEndpointApi
from mpl_api.apis.tags.model_endpoint_api import ModelEndpointApi
from mpl_api.apis.tags.model_instance_endpoint_api import ModelInstanceEndpointApi
from mpl_api.apis.tags.predict_config_endpoint_api import PredictConfigEndpointApi
from mpl_api.apis.tags.process_endpoint_api import ProcessEndpointApi
from mpl_api.apis.tags.process_servlet_api import ProcessServletApi
from mpl_api.apis.tags.stat_log_endpoint_api import StatLogEndpointApi
from mpl_api.apis.tags.system_config_endpoint_api import SystemConfigEndpointApi
from mpl_api.apis.tags.system_endpoint_api import SystemEndpointApi

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
