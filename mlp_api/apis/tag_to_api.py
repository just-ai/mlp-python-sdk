import typing_extensions

from mlp_api.apis.tags import TagValues
from mlp_api.apis.tags.access_token_endpoint_api import AccessTokenEndpointApi
from mlp_api.apis.tags.account_endpoint_api import AccountEndpointApi
from mlp_api.apis.tags.admin_endpoint_api import AdminEndpointApi
from mlp_api.apis.tags.application_endpoint_api import ApplicationEndpointApi
from mlp_api.apis.tags.data_image_endpoint_api import DataImageEndpointApi
from mlp_api.apis.tags.dataset_endpoint_api import DatasetEndpointApi
from mlp_api.apis.tags.fit_config_endpoint_api import FitConfigEndpointApi
from mlp_api.apis.tags.image_endpoint_api import ImageEndpointApi
from mlp_api.apis.tags.internal_endpoint_api import InternalEndpointApi
from mlp_api.apis.tags.job_endpoint_api import JobEndpointApi
from mlp_api.apis.tags.manual_management_endpoint_api import ManualManagementEndpointApi
from mlp_api.apis.tags.metric_endpoint_api import MetricEndpointApi
from mlp_api.apis.tags.model_endpoint_api import ModelEndpointApi
from mlp_api.apis.tags.model_group_endpoint_api import ModelGroupEndpointApi
from mlp_api.apis.tags.model_instance_endpoint_api import ModelInstanceEndpointApi
from mlp_api.apis.tags.predict_config_endpoint_api import PredictConfigEndpointApi
from mlp_api.apis.tags.process_endpoint_api import ProcessEndpointApi
from mlp_api.apis.tags.resource_group_endpoint_api import ResourceGroupEndpointApi
from mlp_api.apis.tags.resource_group_quota_endpoint_api import ResourceGroupQuotaEndpointApi
from mlp_api.apis.tags.resource_group_servers_endpoint_api import ResourceGroupServersEndpointApi
from mlp_api.apis.tags.stat_log_endpoint_api import StatLogEndpointApi
from mlp_api.apis.tags.system_config_endpoint_api import SystemConfigEndpointApi
from mlp_api.apis.tags.system_endpoint_api import SystemEndpointApi
from mlp_api.apis.tags.task_endpoint_api import TaskEndpointApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCESSTOKENENDPOINT: AccessTokenEndpointApi,
        TagValues.ACCOUNTENDPOINT: AccountEndpointApi,
        TagValues.ADMINENDPOINT: AdminEndpointApi,
        TagValues.APPLICATIONENDPOINT: ApplicationEndpointApi,
        TagValues.DATAIMAGEENDPOINT: DataImageEndpointApi,
        TagValues.DATASETENDPOINT: DatasetEndpointApi,
        TagValues.FITCONFIGENDPOINT: FitConfigEndpointApi,
        TagValues.IMAGEENDPOINT: ImageEndpointApi,
        TagValues.INTERNALENDPOINT: InternalEndpointApi,
        TagValues.JOBENDPOINT: JobEndpointApi,
        TagValues.MANUALMANAGEMENTENDPOINT: ManualManagementEndpointApi,
        TagValues.METRICENDPOINT: MetricEndpointApi,
        TagValues.MODELENDPOINT: ModelEndpointApi,
        TagValues.MODELGROUPENDPOINT: ModelGroupEndpointApi,
        TagValues.MODELINSTANCEENDPOINT: ModelInstanceEndpointApi,
        TagValues.PREDICTCONFIGENDPOINT: PredictConfigEndpointApi,
        TagValues.PROCESSENDPOINT: ProcessEndpointApi,
        TagValues.RESOURCEGROUPENDPOINT: ResourceGroupEndpointApi,
        TagValues.RESOURCEGROUPQUOTAENDPOINT: ResourceGroupQuotaEndpointApi,
        TagValues.RESOURCEGROUPSERVERSENDPOINT: ResourceGroupServersEndpointApi,
        TagValues.STATLOGENDPOINT: StatLogEndpointApi,
        TagValues.SYSTEMCONFIGENDPOINT: SystemConfigEndpointApi,
        TagValues.SYSTEMENDPOINT: SystemEndpointApi,
        TagValues.TASKENDPOINT: TaskEndpointApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCESSTOKENENDPOINT: AccessTokenEndpointApi,
        TagValues.ACCOUNTENDPOINT: AccountEndpointApi,
        TagValues.ADMINENDPOINT: AdminEndpointApi,
        TagValues.APPLICATIONENDPOINT: ApplicationEndpointApi,
        TagValues.DATAIMAGEENDPOINT: DataImageEndpointApi,
        TagValues.DATASETENDPOINT: DatasetEndpointApi,
        TagValues.FITCONFIGENDPOINT: FitConfigEndpointApi,
        TagValues.IMAGEENDPOINT: ImageEndpointApi,
        TagValues.INTERNALENDPOINT: InternalEndpointApi,
        TagValues.JOBENDPOINT: JobEndpointApi,
        TagValues.MANUALMANAGEMENTENDPOINT: ManualManagementEndpointApi,
        TagValues.METRICENDPOINT: MetricEndpointApi,
        TagValues.MODELENDPOINT: ModelEndpointApi,
        TagValues.MODELGROUPENDPOINT: ModelGroupEndpointApi,
        TagValues.MODELINSTANCEENDPOINT: ModelInstanceEndpointApi,
        TagValues.PREDICTCONFIGENDPOINT: PredictConfigEndpointApi,
        TagValues.PROCESSENDPOINT: ProcessEndpointApi,
        TagValues.RESOURCEGROUPENDPOINT: ResourceGroupEndpointApi,
        TagValues.RESOURCEGROUPQUOTAENDPOINT: ResourceGroupQuotaEndpointApi,
        TagValues.RESOURCEGROUPSERVERSENDPOINT: ResourceGroupServersEndpointApi,
        TagValues.STATLOGENDPOINT: StatLogEndpointApi,
        TagValues.SYSTEMCONFIGENDPOINT: SystemConfigEndpointApi,
        TagValues.SYSTEMENDPOINT: SystemEndpointApi,
        TagValues.TASKENDPOINT: TaskEndpointApi,
    }
)
