import typing_extensions

from mlp_api.paths import PathValues
from mlp_api.apis.paths.api_mlpgate_admin_account_account_id_limits import ApiMlpgateAdminAccountAccountIdLimits
from mlp_api.apis.paths.api_mlpgate_admin_account_account_id_features import ApiMlpgateAdminAccountAccountIdFeatures
from mlp_api.apis.paths.api_mlpgate_account import ApiMlpgateAccount
from mlp_api.apis.paths.api_mlpgate_account_account_id_token import ApiMlpgateAccountAccountIdToken
from mlp_api.apis.paths.api_mlpgate_account_account_id_model import ApiMlpgateAccountAccountIdModel
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id import ApiMlpgateAccountAccountIdModelModelId
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_simple_doc import ApiMlpgateAccountAccountIdModelModelIdSimpleDoc
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_public_settings import ApiMlpgateAccountAccountIdModelModelIdPublicSettings
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_predict import ApiMlpgateAccountAccountIdModelModelIdPredict
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_predict_with_config import ApiMlpgateAccountAccountIdModelModelIdPredictWithConfig
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_predict_config import ApiMlpgateAccountAccountIdModelModelIdPredictConfig
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_predict_config_config_id import ApiMlpgateAccountAccountIdModelModelIdPredictConfigConfigId
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instances import ApiMlpgateAccountAccountIdModelModelIdInstances
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instance_instance_id_terminate import ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdTerminate
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instance_instance_id_stop import ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdStop
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instance_start import ApiMlpgateAccountAccountIdModelModelIdInstanceStart
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_fit import ApiMlpgateAccountAccountIdModelModelIdFit
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_fit_config import ApiMlpgateAccountAccountIdModelModelIdFitConfig
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_fit_config_config_id import ApiMlpgateAccountAccountIdModelModelIdFitConfigConfigId
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_external import ApiMlpgateAccountAccountIdModelModelIdExternal
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_ext import ApiMlpgateAccountAccountIdModelModelIdExt
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_derived import ApiMlpgateAccountAccountIdModelModelIdDerived
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_cross_validation import ApiMlpgateAccountAccountIdModelModelIdCrossValidation
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_clone import ApiMlpgateAccountAccountIdModelModelIdClone
from mlp_api.apis.paths.api_mlpgate_account_account_id_management_feature_name import ApiMlpgateAccountAccountIdManagementFeatureName
from mlp_api.apis.paths.api_mlpgate_account_account_id_image import ApiMlpgateAccountAccountIdImage
from mlp_api.apis.paths.api_mlpgate_account_account_id_image_image_id import ApiMlpgateAccountAccountIdImageImageId
from mlp_api.apis.paths.api_mlpgate_account_account_id_dump import ApiMlpgateAccountAccountIdDump
from mlp_api.apis.paths.api_mlpgate_account_account_id_dataset import ApiMlpgateAccountAccountIdDataset
from mlp_api.apis.paths.api_mlpgate_account_account_id_dataset_dataset_id import ApiMlpgateAccountAccountIdDatasetDatasetId
from mlp_api.apis.paths.api_mlpgate_account_account_id_dataset_dataset_id_content import ApiMlpgateAccountAccountIdDatasetDatasetIdContent
from mlp_api.apis.paths.api_mlpgate_account_account_id_data_image import ApiMlpgateAccountAccountIdDataImage
from mlp_api.apis.paths.api_mlpgate_account_account_id_data_image_image_id import ApiMlpgateAccountAccountIdDataImageImageId
from mlp_api.apis.paths.api_mlpgate_internal_account_account_id_update_limits import ApiMlpgateInternalAccountAccountIdUpdateLimits
from mlp_api.apis.paths.api_mlpgate_internal_account_account_id_namespace_ensure import ApiMlpgateInternalAccountAccountIdNamespaceEnsure
from mlp_api.apis.paths.api_mlpgate_internal_account_account_id_model_model_id_path import ApiMlpgateInternalAccountAccountIdModelModelIdPath
from mlp_api.apis.paths.api_mlpgate_internal_account_account_id_model_model_id_instance_deactivate import ApiMlpgateInternalAccountAccountIdModelModelIdInstanceDeactivate
from mlp_api.apis.paths.api_mlpgate_internal_account_account_id_features import ApiMlpgateInternalAccountAccountIdFeatures
from mlp_api.apis.paths.api_mlpgate_internal_account_deactivate import ApiMlpgateInternalAccountDeactivate
from mlp_api.apis.paths.api_mlpgate_admin_resource_groups import ApiMlpgateAdminResourceGroups
from mlp_api.apis.paths.api_mlpgate_internal_resource_groups import ApiMlpgateInternalResourceGroups
from mlp_api.apis.paths.api_mlpgate_version import ApiMlpgateVersion
from mlp_api.apis.paths.api_mlpgate_system_config_task_types import ApiMlpgateSystemConfigTaskTypes
from mlp_api.apis.paths.api_mlpgate_system_config_resource_groups import ApiMlpgateSystemConfigResourceGroups
from mlp_api.apis.paths.api_mlpgate_system_config_model_defaults import ApiMlpgateSystemConfigModelDefaults
from mlp_api.apis.paths.api_mlpgate_system_config_dataset_data_type import ApiMlpgateSystemConfigDatasetDataType
from mlp_api.apis.paths.api_mlpgate_model import ApiMlpgateModel
from mlp_api.apis.paths.api_mlpgate_model_featured import ApiMlpgateModelFeatured
from mlp_api.apis.paths.api_mlpgate_health import ApiMlpgateHealth
from mlp_api.apis.paths.api_mlpgate_health_test import ApiMlpgateHealthTest
from mlp_api.apis.paths.api_mlpgate_admin_account import ApiMlpgateAdminAccount
from mlp_api.apis.paths.api_mlpgate_admin_account_account_id import ApiMlpgateAdminAccountAccountId
from mlp_api.apis.paths.api_mlpgate_account_account_id_token_token import ApiMlpgateAccountAccountIdTokenToken
from mlp_api.apis.paths.api_mlpgate_account_account_id_stat_log import ApiMlpgateAccountAccountIdStatLog
from mlp_api.apis.paths.api_mlpgate_account_account_id_s3 import ApiMlpgateAccountAccountIdS3
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_status import ApiMlpgateAccountAccountIdModelModelIdStatus
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_metric import ApiMlpgateAccountAccountIdModelModelIdMetric
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_metric_range import ApiMlpgateAccountAccountIdModelModelIdMetricRange
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_logs import ApiMlpgateAccountAccountIdModelModelIdLogs
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_last_job import ApiMlpgateAccountAccountIdModelModelIdLastJob
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instance import ApiMlpgateAccountAccountIdModelModelIdInstance
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instance_instance_id_metric import ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdMetric
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instance_instance_id_metric_range import ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdMetricRange
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instance_instance_id_file import ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdFile
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instance_instance_id_file_logs import ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdFileLogs
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instance_instance_id_events import ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdEvents
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_instance_instance_id_environment import ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdEnvironment
from mlp_api.apis.paths.api_mlpgate_account_account_id_model_model_id_action_descriptor import ApiMlpgateAccountAccountIdModelModelIdActionDescriptor
from mlp_api.apis.paths.api_mlpgate_account_account_id_metric import ApiMlpgateAccountAccountIdMetric
from mlp_api.apis.paths.api_mlpgate_account_account_id_metric_range import ApiMlpgateAccountAccountIdMetricRange
from mlp_api.apis.paths.api_mlpgate_account_account_id_job import ApiMlpgateAccountAccountIdJob
from mlp_api.apis.paths.api_mlpgate_account_account_id_job_job_id import ApiMlpgateAccountAccountIdJobJobId
from mlp_api.apis.paths.api_mlpgate_account_account_id_image_image_id_logs import ApiMlpgateAccountAccountIdImageImageIdLogs
from mlp_api.apis.paths.api_mlpgate_internal_test_mail import ApiMlpgateInternalTestMail
from mlp_api.apis.paths.api_mlpgate_internal_start_one_instance import ApiMlpgateInternalStartOneInstance
from mlp_api.apis.paths.api_mlpgate_internal_set_public_for_all import ApiMlpgateInternalSetPublicForAll
from mlp_api.apis.paths.api_mlpgate_internal_services import ApiMlpgateInternalServices
from mlp_api.apis.paths.api_mlpgate_internal_notify_account_id_user_user_id import ApiMlpgateInternalNotifyAccountIdUserUserId
from mlp_api.apis.paths.api_mlpgate_internal_cluster import ApiMlpgateInternalCluster
from mlp_api.apis.paths.api_mlpgate_internal_clear_public_for_all import ApiMlpgateInternalClearPublicForAll
from mlp_api.apis.paths.api_mlpgate_internal_clear_instances import ApiMlpgateInternalClearInstances
from mlp_api.apis.paths.api_mlpgate_internal_clear_account import ApiMlpgateInternalClearAccount
from mlp_api.apis.paths.api_mlpgate_internal_actions import ApiMlpgateInternalActions
from mlp_api.apis.paths.api_mlpgate_internal_account import ApiMlpgateInternalAccount
from mlp_api.apis.paths.api_mlpgate_internal_account_account_id_model_model_id_instances import ApiMlpgateInternalAccountAccountIdModelModelIdInstances
from mlp_api.apis.paths.api_mlpgate_internal_account_account_id_model_model_id_actions import ApiMlpgateInternalAccountAccountIdModelModelIdActions
from mlp_api.apis.paths.api_mlpgate_internal_instances_delete_by_timestamp import ApiMlpgateInternalInstancesDeleteByTimestamp
from mlp_api.apis.paths.p_account_model import PAccountModel

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_ID_LIMITS: ApiMlpgateAdminAccountAccountIdLimits,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_ID_FEATURES: ApiMlpgateAdminAccountAccountIdFeatures,
        PathValues.API_MLPGATE_ACCOUNT: ApiMlpgateAccount,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_TOKEN: ApiMlpgateAccountAccountIdToken,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL: ApiMlpgateAccountAccountIdModel,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID: ApiMlpgateAccountAccountIdModelModelId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_SIMPLEDOC: ApiMlpgateAccountAccountIdModelModelIdSimpleDoc,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PUBLICSETTINGS: ApiMlpgateAccountAccountIdModelModelIdPublicSettings,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICT: ApiMlpgateAccountAccountIdModelModelIdPredict,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICTWITHCONFIG: ApiMlpgateAccountAccountIdModelModelIdPredictWithConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICTCONFIG: ApiMlpgateAccountAccountIdModelModelIdPredictConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICTCONFIG_CONFIG_ID: ApiMlpgateAccountAccountIdModelModelIdPredictConfigConfigId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCES: ApiMlpgateAccountAccountIdModelModelIdInstances,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_TERMINATE: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdTerminate,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_STOP: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdStop,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_START: ApiMlpgateAccountAccountIdModelModelIdInstanceStart,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_FIT: ApiMlpgateAccountAccountIdModelModelIdFit,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_FITCONFIG: ApiMlpgateAccountAccountIdModelModelIdFitConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_FITCONFIG_CONFIG_ID: ApiMlpgateAccountAccountIdModelModelIdFitConfigConfigId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_EXTERNAL: ApiMlpgateAccountAccountIdModelModelIdExternal,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_EXT: ApiMlpgateAccountAccountIdModelModelIdExt,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_DERIVED: ApiMlpgateAccountAccountIdModelModelIdDerived,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_CROSSVALIDATION: ApiMlpgateAccountAccountIdModelModelIdCrossValidation,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_CLONE: ApiMlpgateAccountAccountIdModelModelIdClone,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MANAGEMENT_FEATURE_NAME: ApiMlpgateAccountAccountIdManagementFeatureName,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_IMAGE: ApiMlpgateAccountAccountIdImage,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_IMAGE_IMAGE_ID: ApiMlpgateAccountAccountIdImageImageId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DUMP: ApiMlpgateAccountAccountIdDump,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATASET: ApiMlpgateAccountAccountIdDataset,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATASET_DATASET_ID: ApiMlpgateAccountAccountIdDatasetDatasetId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATASET_DATASET_ID_CONTENT: ApiMlpgateAccountAccountIdDatasetDatasetIdContent,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATAIMAGE: ApiMlpgateAccountAccountIdDataImage,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATAIMAGE_IMAGE_ID: ApiMlpgateAccountAccountIdDataImageImageId,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_UPDATELIMITS: ApiMlpgateInternalAccountAccountIdUpdateLimits,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_NAMESPACE_ENSURE: ApiMlpgateInternalAccountAccountIdNamespaceEnsure,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PATH: ApiMlpgateInternalAccountAccountIdModelModelIdPath,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_DEACTIVATE: ApiMlpgateInternalAccountAccountIdModelModelIdInstanceDeactivate,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_FEATURES: ApiMlpgateInternalAccountAccountIdFeatures,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_DEACTIVATE: ApiMlpgateInternalAccountDeactivate,
        PathValues.API_MLPGATE_ADMIN_RESOURCEGROUPS: ApiMlpgateAdminResourceGroups,
        PathValues.API_MLPGATEINTERNAL_RESOURCEGROUPS: ApiMlpgateInternalResourceGroups,
        PathValues.API_MLPGATE_VERSION: ApiMlpgateVersion,
        PathValues.API_MLPGATE_SYSTEMCONFIG_TASKTYPES: ApiMlpgateSystemConfigTaskTypes,
        PathValues.API_MLPGATE_SYSTEMCONFIG_RESOURCEGROUPS: ApiMlpgateSystemConfigResourceGroups,
        PathValues.API_MLPGATE_SYSTEMCONFIG_MODELDEFAULTS: ApiMlpgateSystemConfigModelDefaults,
        PathValues.API_MLPGATE_SYSTEMCONFIG_DATASETDATATYPE: ApiMlpgateSystemConfigDatasetDataType,
        PathValues.API_MLPGATE_MODEL: ApiMlpgateModel,
        PathValues.API_MLPGATE_MODEL_FEATURED: ApiMlpgateModelFeatured,
        PathValues.API_MLPGATE_HEALTH: ApiMlpgateHealth,
        PathValues.API_MLPGATE_HEALTH_TEST: ApiMlpgateHealthTest,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT: ApiMlpgateAdminAccount,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_ID: ApiMlpgateAdminAccountAccountId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_TOKEN_TOKEN: ApiMlpgateAccountAccountIdTokenToken,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_STATLOG: ApiMlpgateAccountAccountIdStatLog,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_S3: ApiMlpgateAccountAccountIdS3,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_STATUS: ApiMlpgateAccountAccountIdModelModelIdStatus,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_METRIC: ApiMlpgateAccountAccountIdModelModelIdMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_METRICRANGE: ApiMlpgateAccountAccountIdModelModelIdMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_LOGS: ApiMlpgateAccountAccountIdModelModelIdLogs,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_LASTJOB: ApiMlpgateAccountAccountIdModelModelIdLastJob,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE: ApiMlpgateAccountAccountIdModelModelIdInstance,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_METRIC: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_METRICRANGE: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_FILE: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdFile,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_FILE_LOGS: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdFileLogs,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_EVENTS: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdEvents,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_ENVIRONMENT: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdEnvironment,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_ACTIONDESCRIPTOR: ApiMlpgateAccountAccountIdModelModelIdActionDescriptor,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_METRIC: ApiMlpgateAccountAccountIdMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_METRICRANGE: ApiMlpgateAccountAccountIdMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_JOB: ApiMlpgateAccountAccountIdJob,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_JOB_JOB_ID: ApiMlpgateAccountAccountIdJobJobId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_IMAGE_IMAGE_ID_LOGS: ApiMlpgateAccountAccountIdImageImageIdLogs,
        PathValues.API_MLPGATEINTERNAL_TESTMAIL: ApiMlpgateInternalTestMail,
        PathValues.API_MLPGATEINTERNAL_STARTONEINSTANCE: ApiMlpgateInternalStartOneInstance,
        PathValues.API_MLPGATEINTERNAL_SETPUBLICFORALL: ApiMlpgateInternalSetPublicForAll,
        PathValues.API_MLPGATEINTERNAL_SERVICES: ApiMlpgateInternalServices,
        PathValues.API_MLPGATEINTERNAL_NOTIFY_ACCOUNT_ID_USER_USER_ID: ApiMlpgateInternalNotifyAccountIdUserUserId,
        PathValues.API_MLPGATEINTERNAL_CLUSTER: ApiMlpgateInternalCluster,
        PathValues.API_MLPGATEINTERNAL_CLEARPUBLICFORALL: ApiMlpgateInternalClearPublicForAll,
        PathValues.API_MLPGATEINTERNAL_CLEARINSTANCES: ApiMlpgateInternalClearInstances,
        PathValues.API_MLPGATEINTERNAL_CLEARACCOUNT: ApiMlpgateInternalClearAccount,
        PathValues.API_MLPGATEINTERNAL_ACTIONS: ApiMlpgateInternalActions,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT: ApiMlpgateInternalAccount,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCES: ApiMlpgateInternalAccountAccountIdModelModelIdInstances,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_ACTIONS: ApiMlpgateInternalAccountAccountIdModelModelIdActions,
        PathValues.API_MLPGATEINTERNAL_INSTANCES_DELETE_BY_TIMESTAMP: ApiMlpgateInternalInstancesDeleteByTimestamp,
        PathValues.P_ACCOUNT_MODEL: PAccountModel,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_ID_LIMITS: ApiMlpgateAdminAccountAccountIdLimits,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_ID_FEATURES: ApiMlpgateAdminAccountAccountIdFeatures,
        PathValues.API_MLPGATE_ACCOUNT: ApiMlpgateAccount,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_TOKEN: ApiMlpgateAccountAccountIdToken,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL: ApiMlpgateAccountAccountIdModel,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID: ApiMlpgateAccountAccountIdModelModelId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_SIMPLEDOC: ApiMlpgateAccountAccountIdModelModelIdSimpleDoc,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PUBLICSETTINGS: ApiMlpgateAccountAccountIdModelModelIdPublicSettings,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICT: ApiMlpgateAccountAccountIdModelModelIdPredict,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICTWITHCONFIG: ApiMlpgateAccountAccountIdModelModelIdPredictWithConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICTCONFIG: ApiMlpgateAccountAccountIdModelModelIdPredictConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICTCONFIG_CONFIG_ID: ApiMlpgateAccountAccountIdModelModelIdPredictConfigConfigId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCES: ApiMlpgateAccountAccountIdModelModelIdInstances,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_TERMINATE: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdTerminate,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_STOP: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdStop,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_START: ApiMlpgateAccountAccountIdModelModelIdInstanceStart,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_FIT: ApiMlpgateAccountAccountIdModelModelIdFit,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_FITCONFIG: ApiMlpgateAccountAccountIdModelModelIdFitConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_FITCONFIG_CONFIG_ID: ApiMlpgateAccountAccountIdModelModelIdFitConfigConfigId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_EXTERNAL: ApiMlpgateAccountAccountIdModelModelIdExternal,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_EXT: ApiMlpgateAccountAccountIdModelModelIdExt,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_DERIVED: ApiMlpgateAccountAccountIdModelModelIdDerived,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_CROSSVALIDATION: ApiMlpgateAccountAccountIdModelModelIdCrossValidation,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_CLONE: ApiMlpgateAccountAccountIdModelModelIdClone,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MANAGEMENT_FEATURE_NAME: ApiMlpgateAccountAccountIdManagementFeatureName,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_IMAGE: ApiMlpgateAccountAccountIdImage,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_IMAGE_IMAGE_ID: ApiMlpgateAccountAccountIdImageImageId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DUMP: ApiMlpgateAccountAccountIdDump,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATASET: ApiMlpgateAccountAccountIdDataset,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATASET_DATASET_ID: ApiMlpgateAccountAccountIdDatasetDatasetId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATASET_DATASET_ID_CONTENT: ApiMlpgateAccountAccountIdDatasetDatasetIdContent,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATAIMAGE: ApiMlpgateAccountAccountIdDataImage,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATAIMAGE_IMAGE_ID: ApiMlpgateAccountAccountIdDataImageImageId,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_UPDATELIMITS: ApiMlpgateInternalAccountAccountIdUpdateLimits,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_NAMESPACE_ENSURE: ApiMlpgateInternalAccountAccountIdNamespaceEnsure,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PATH: ApiMlpgateInternalAccountAccountIdModelModelIdPath,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_DEACTIVATE: ApiMlpgateInternalAccountAccountIdModelModelIdInstanceDeactivate,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_FEATURES: ApiMlpgateInternalAccountAccountIdFeatures,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_DEACTIVATE: ApiMlpgateInternalAccountDeactivate,
        PathValues.API_MLPGATE_ADMIN_RESOURCEGROUPS: ApiMlpgateAdminResourceGroups,
        PathValues.API_MLPGATEINTERNAL_RESOURCEGROUPS: ApiMlpgateInternalResourceGroups,
        PathValues.API_MLPGATE_VERSION: ApiMlpgateVersion,
        PathValues.API_MLPGATE_SYSTEMCONFIG_TASKTYPES: ApiMlpgateSystemConfigTaskTypes,
        PathValues.API_MLPGATE_SYSTEMCONFIG_RESOURCEGROUPS: ApiMlpgateSystemConfigResourceGroups,
        PathValues.API_MLPGATE_SYSTEMCONFIG_MODELDEFAULTS: ApiMlpgateSystemConfigModelDefaults,
        PathValues.API_MLPGATE_SYSTEMCONFIG_DATASETDATATYPE: ApiMlpgateSystemConfigDatasetDataType,
        PathValues.API_MLPGATE_MODEL: ApiMlpgateModel,
        PathValues.API_MLPGATE_MODEL_FEATURED: ApiMlpgateModelFeatured,
        PathValues.API_MLPGATE_HEALTH: ApiMlpgateHealth,
        PathValues.API_MLPGATE_HEALTH_TEST: ApiMlpgateHealthTest,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT: ApiMlpgateAdminAccount,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_ID: ApiMlpgateAdminAccountAccountId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_TOKEN_TOKEN: ApiMlpgateAccountAccountIdTokenToken,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_STATLOG: ApiMlpgateAccountAccountIdStatLog,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_S3: ApiMlpgateAccountAccountIdS3,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_STATUS: ApiMlpgateAccountAccountIdModelModelIdStatus,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_METRIC: ApiMlpgateAccountAccountIdModelModelIdMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_METRICRANGE: ApiMlpgateAccountAccountIdModelModelIdMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_LOGS: ApiMlpgateAccountAccountIdModelModelIdLogs,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_LASTJOB: ApiMlpgateAccountAccountIdModelModelIdLastJob,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE: ApiMlpgateAccountAccountIdModelModelIdInstance,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_METRIC: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_METRICRANGE: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_FILE: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdFile,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_FILE_LOGS: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdFileLogs,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_EVENTS: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdEvents,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_ENVIRONMENT: ApiMlpgateAccountAccountIdModelModelIdInstanceInstanceIdEnvironment,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_ACTIONDESCRIPTOR: ApiMlpgateAccountAccountIdModelModelIdActionDescriptor,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_METRIC: ApiMlpgateAccountAccountIdMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_METRICRANGE: ApiMlpgateAccountAccountIdMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_JOB: ApiMlpgateAccountAccountIdJob,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_JOB_JOB_ID: ApiMlpgateAccountAccountIdJobJobId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_ID_IMAGE_IMAGE_ID_LOGS: ApiMlpgateAccountAccountIdImageImageIdLogs,
        PathValues.API_MLPGATEINTERNAL_TESTMAIL: ApiMlpgateInternalTestMail,
        PathValues.API_MLPGATEINTERNAL_STARTONEINSTANCE: ApiMlpgateInternalStartOneInstance,
        PathValues.API_MLPGATEINTERNAL_SETPUBLICFORALL: ApiMlpgateInternalSetPublicForAll,
        PathValues.API_MLPGATEINTERNAL_SERVICES: ApiMlpgateInternalServices,
        PathValues.API_MLPGATEINTERNAL_NOTIFY_ACCOUNT_ID_USER_USER_ID: ApiMlpgateInternalNotifyAccountIdUserUserId,
        PathValues.API_MLPGATEINTERNAL_CLUSTER: ApiMlpgateInternalCluster,
        PathValues.API_MLPGATEINTERNAL_CLEARPUBLICFORALL: ApiMlpgateInternalClearPublicForAll,
        PathValues.API_MLPGATEINTERNAL_CLEARINSTANCES: ApiMlpgateInternalClearInstances,
        PathValues.API_MLPGATEINTERNAL_CLEARACCOUNT: ApiMlpgateInternalClearAccount,
        PathValues.API_MLPGATEINTERNAL_ACTIONS: ApiMlpgateInternalActions,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT: ApiMlpgateInternalAccount,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCES: ApiMlpgateInternalAccountAccountIdModelModelIdInstances,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_ACTIONS: ApiMlpgateInternalAccountAccountIdModelModelIdActions,
        PathValues.API_MLPGATEINTERNAL_INSTANCES_DELETE_BY_TIMESTAMP: ApiMlpgateInternalInstancesDeleteByTimestamp,
        PathValues.P_ACCOUNT_MODEL: PAccountModel,
    }
)
