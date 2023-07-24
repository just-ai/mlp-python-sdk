import typing_extensions

from mlp_api.paths import PathValues
from mlp_api.apis.paths.p_account_field_model_field import PAccountFieldModelField
from mlp_api.apis.paths.api_mlpgate_admin_system_config_account_account_data import ApiMlpgateAdminSystemConfigAccountAccountData
from mlp_api.apis.paths.api_mlpgate_admin_system_config_account_account_config import ApiMlpgateAdminSystemConfigAccountAccountConfig
from mlp_api.apis.paths.api_mlpgate_admin_account_account_limits import ApiMlpgateAdminAccountAccountLimits
from mlp_api.apis.paths.api_mlpgate_admin_account_account_features import ApiMlpgateAdminAccountAccountFeatures
from mlp_api.apis.paths.api_mlpgate_account import ApiMlpgateAccount
from mlp_api.apis.paths.api_mlpgate_account_account_token import ApiMlpgateAccountAccountToken
from mlp_api.apis.paths.api_mlpgate_account_account_model import ApiMlpgateAccountAccountModel
from mlp_api.apis.paths.api_mlpgate_account_account_model_model import ApiMlpgateAccountAccountModelModel
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_tts_stream import ApiMlpgateAccountAccountModelModelTtsStream
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_simple_doc import ApiMlpgateAccountAccountModelModelSimpleDoc
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_public_settings import ApiMlpgateAccountAccountModelModelPublicSettings
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_predict import ApiMlpgateAccountAccountModelModelPredict
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_predict_with_config import ApiMlpgateAccountAccountModelModelPredictWithConfig
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_predict_with_config_v2 import ApiMlpgateAccountAccountModelModelPredictWithConfigV2
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_predict_config import ApiMlpgateAccountAccountModelModelPredictConfig
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_predict_config_config_id import ApiMlpgateAccountAccountModelModelPredictConfigConfigId
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instances import ApiMlpgateAccountAccountModelModelInstances
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instance_instance_id_terminate import ApiMlpgateAccountAccountModelModelInstanceInstanceIdTerminate
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instance_instance_id_stop import ApiMlpgateAccountAccountModelModelInstanceInstanceIdStop
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instance_start import ApiMlpgateAccountAccountModelModelInstanceStart
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_fit import ApiMlpgateAccountAccountModelModelFit
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_fit_v2 import ApiMlpgateAccountAccountModelModelFitV2
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_fit_config import ApiMlpgateAccountAccountModelModelFitConfig
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_fit_config_config_id import ApiMlpgateAccountAccountModelModelFitConfigConfigId
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_favorite import ApiMlpgateAccountAccountModelModelFavorite
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_external import ApiMlpgateAccountAccountModelModelExternal
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_ext import ApiMlpgateAccountAccountModelModelExt
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_derived import ApiMlpgateAccountAccountModelModelDerived
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_cross_validation import ApiMlpgateAccountAccountModelModelCrossValidation
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_clone import ApiMlpgateAccountAccountModelModelClone
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_billing import ApiMlpgateAccountAccountModelModelBilling
from mlp_api.apis.paths.api_mlpgate_account_account_model_group import ApiMlpgateAccountAccountModelGroup
from mlp_api.apis.paths.api_mlpgate_account_account_management_feature_name import ApiMlpgateAccountAccountManagementFeatureName
from mlp_api.apis.paths.api_mlpgate_account_account_image import ApiMlpgateAccountAccountImage
from mlp_api.apis.paths.api_mlpgate_account_account_image_image_id import ApiMlpgateAccountAccountImageImageId
from mlp_api.apis.paths.api_mlpgate_account_account_dump import ApiMlpgateAccountAccountDump
from mlp_api.apis.paths.api_mlpgate_account_account_dataset import ApiMlpgateAccountAccountDataset
from mlp_api.apis.paths.api_mlpgate_account_account_dataset_dataset_id import ApiMlpgateAccountAccountDatasetDatasetId
from mlp_api.apis.paths.api_mlpgate_account_account_dataset_dataset_id_raw import ApiMlpgateAccountAccountDatasetDatasetIdRaw
from mlp_api.apis.paths.api_mlpgate_account_account_dataset_dataset_id_paraphrase import ApiMlpgateAccountAccountDatasetDatasetIdParaphrase
from mlp_api.apis.paths.api_mlpgate_account_account_dataset_dataset_id_content import ApiMlpgateAccountAccountDatasetDatasetIdContent
from mlp_api.apis.paths.api_mlpgate_account_account_dataset_raw import ApiMlpgateAccountAccountDatasetRaw
from mlp_api.apis.paths.api_mlpgate_account_account_dataset_empty import ApiMlpgateAccountAccountDatasetEmpty
from mlp_api.apis.paths.api_mlpgate_account_account_data_image import ApiMlpgateAccountAccountDataImage
from mlp_api.apis.paths.api_mlpgate_account_account_data_image_image_id import ApiMlpgateAccountAccountDataImageImageId
from mlp_api.apis.paths.api_mlpgate_internal_accounts_deactivate import ApiMlpgateInternalAccountsDeactivate
from mlp_api.apis.paths.api_mlpgate_internal_account_account_update_limits import ApiMlpgateInternalAccountAccountUpdateLimits
from mlp_api.apis.paths.api_mlpgate_internal_account_account_namespace_ensure import ApiMlpgateInternalAccountAccountNamespaceEnsure
from mlp_api.apis.paths.api_mlpgate_internal_account_account_model_model_path import ApiMlpgateInternalAccountAccountModelModelPath
from mlp_api.apis.paths.api_mlpgate_internal_account_account_model_model_instance_deactivate import ApiMlpgateInternalAccountAccountModelModelInstanceDeactivate
from mlp_api.apis.paths.api_mlpgate_internal_account_account_features import ApiMlpgateInternalAccountAccountFeatures
from mlp_api.apis.paths.api_mlpgate_internal_account_account_bucket_deny import ApiMlpgateInternalAccountAccountBucketDeny
from mlp_api.apis.paths.api_mlpgate_internal_account_account_bucket_access import ApiMlpgateInternalAccountAccountBucketAccess
from mlp_api.apis.paths.api_mlpgate_admin_resource_groups import ApiMlpgateAdminResourceGroups
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_model_group_group_id import ApiMlpgateAccountAccountModelModelModelGroupGroupId
from mlp_api.apis.paths.api_mlpgate_internal_resource_groups import ApiMlpgateInternalResourceGroups
from mlp_api.apis.paths.api_mlpgate_version import ApiMlpgateVersion
from mlp_api.apis.paths.api_mlpgate_system_config_task_types import ApiMlpgateSystemConfigTaskTypes
from mlp_api.apis.paths.api_mlpgate_system_config_resource_groups import ApiMlpgateSystemConfigResourceGroups
from mlp_api.apis.paths.api_mlpgate_system_config_model_defaults import ApiMlpgateSystemConfigModelDefaults
from mlp_api.apis.paths.api_mlpgate_system_config_dataset_data_type import ApiMlpgateSystemConfigDatasetDataType
from mlp_api.apis.paths.api_mlpgate_models import ApiMlpgateModels
from mlp_api.apis.paths.api_mlpgate_models_featured import ApiMlpgateModelsFeatured
from mlp_api.apis.paths.api_mlpgate_health import ApiMlpgateHealth
from mlp_api.apis.paths.api_mlpgate_health_test import ApiMlpgateHealthTest
from mlp_api.apis.paths.api_mlpgate_health_history import ApiMlpgateHealthHistory
from mlp_api.apis.paths.api_mlpgate_admin_accounts import ApiMlpgateAdminAccounts
from mlp_api.apis.paths.api_mlpgate_admin_account_account import ApiMlpgateAdminAccountAccount
from mlp_api.apis.paths.api_mlpgate_account_account_token_token import ApiMlpgateAccountAccountTokenToken
from mlp_api.apis.paths.api_mlpgate_account_account_stat_log import ApiMlpgateAccountAccountStatLog
from mlp_api.apis.paths.api_mlpgate_account_account_s3 import ApiMlpgateAccountAccountS3
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_status import ApiMlpgateAccountAccountModelModelStatus
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_metric import ApiMlpgateAccountAccountModelModelMetric
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_metric_range import ApiMlpgateAccountAccountModelModelMetricRange
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_logs import ApiMlpgateAccountAccountModelModelLogs
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_last_job import ApiMlpgateAccountAccountModelModelLastJob
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instance import ApiMlpgateAccountAccountModelModelInstance
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instance_instance_id_metric import ApiMlpgateAccountAccountModelModelInstanceInstanceIdMetric
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instance_instance_id_metric_range import ApiMlpgateAccountAccountModelModelInstanceInstanceIdMetricRange
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instance_instance_id_file import ApiMlpgateAccountAccountModelModelInstanceInstanceIdFile
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instance_instance_id_file_logs import ApiMlpgateAccountAccountModelModelInstanceInstanceIdFileLogs
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instance_instance_id_events import ApiMlpgateAccountAccountModelModelInstanceInstanceIdEvents
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_instance_instance_id_environment import ApiMlpgateAccountAccountModelModelInstanceInstanceIdEnvironment
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_action_descriptor import ApiMlpgateAccountAccountModelModelActionDescriptor
from mlp_api.apis.paths.api_mlpgate_account_account_metric import ApiMlpgateAccountAccountMetric
from mlp_api.apis.paths.api_mlpgate_account_account_metric_range import ApiMlpgateAccountAccountMetricRange
from mlp_api.apis.paths.api_mlpgate_account_account_job import ApiMlpgateAccountAccountJob
from mlp_api.apis.paths.api_mlpgate_account_account_job_job_id import ApiMlpgateAccountAccountJobJobId
from mlp_api.apis.paths.api_mlpgate_account_account_image_image_id_logs import ApiMlpgateAccountAccountImageImageIdLogs
from mlp_api.apis.paths.api_mlpgate_account_account_dataset_original_dataset_id_paraphrase import ApiMlpgateAccountAccountDatasetOriginalDatasetIdParaphrase
from mlp_api.apis.paths.api_mlpgate_internal_test_mail import ApiMlpgateInternalTestMail
from mlp_api.apis.paths.api_mlpgate_internal_start_one_instance import ApiMlpgateInternalStartOneInstance
from mlp_api.apis.paths.api_mlpgate_internal_set_public_for_all import ApiMlpgateInternalSetPublicForAll
from mlp_api.apis.paths.api_mlpgate_internal_services import ApiMlpgateInternalServices
from mlp_api.apis.paths.api_mlpgate_internal_pg_test_account import ApiMlpgateInternalPgTestAccount
from mlp_api.apis.paths.api_mlpgate_internal_notify_account_user_user_id import ApiMlpgateInternalNotifyAccountUserUserId
from mlp_api.apis.paths.api_mlpgate_internal_empty_test import ApiMlpgateInternalEmptyTest
from mlp_api.apis.paths.api_mlpgate_internal_cluster import ApiMlpgateInternalCluster
from mlp_api.apis.paths.api_mlpgate_internal_clear_public_for_all import ApiMlpgateInternalClearPublicForAll
from mlp_api.apis.paths.api_mlpgate_internal_clear_instances import ApiMlpgateInternalClearInstances
from mlp_api.apis.paths.api_mlpgate_internal_clear_account import ApiMlpgateInternalClearAccount
from mlp_api.apis.paths.api_mlpgate_internal_actions import ApiMlpgateInternalActions
from mlp_api.apis.paths.api_mlpgate_internal_account import ApiMlpgateInternalAccount
from mlp_api.apis.paths.api_mlpgate_internal_account_account_model_model_instances import ApiMlpgateInternalAccountAccountModelModelInstances
from mlp_api.apis.paths.api_mlpgate_internal_account_account_model_model_actions import ApiMlpgateInternalAccountAccountModelModelActions
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_model_group import ApiMlpgateAccountAccountModelModelModelGroup
from mlp_api.apis.paths.api_mlpgate_account_account_model_model_external_instance_id import ApiMlpgateAccountAccountModelModelExternalInstanceId
from mlp_api.apis.paths.api_mlpgate_account_account_model_group_group_id import ApiMlpgateAccountAccountModelGroupGroupId
from mlp_api.apis.paths.api_mlpgate_internal_instances_delete_by_timestamp import ApiMlpgateInternalInstancesDeleteByTimestamp

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.P_ACCOUNT_FIELD_MODEL_FIELD: PAccountFieldModelField,
        PathValues.API_MLPGATE_ADMIN_SYSTEMCONFIG_ACCOUNT_ACCOUNT_DATA: ApiMlpgateAdminSystemConfigAccountAccountData,
        PathValues.API_MLPGATE_ADMIN_SYSTEMCONFIG_ACCOUNT_ACCOUNT_CONFIG: ApiMlpgateAdminSystemConfigAccountAccountConfig,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_LIMITS: ApiMlpgateAdminAccountAccountLimits,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_FEATURES: ApiMlpgateAdminAccountAccountFeatures,
        PathValues.API_MLPGATE_ACCOUNT: ApiMlpgateAccount,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_TOKEN: ApiMlpgateAccountAccountToken,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL: ApiMlpgateAccountAccountModel,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL: ApiMlpgateAccountAccountModelModel,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_TTSSTREAM: ApiMlpgateAccountAccountModelModelTtsStream,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_SIMPLEDOC: ApiMlpgateAccountAccountModelModelSimpleDoc,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PUBLICSETTINGS: ApiMlpgateAccountAccountModelModelPublicSettings,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICT: ApiMlpgateAccountAccountModelModelPredict,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTWITHCONFIG: ApiMlpgateAccountAccountModelModelPredictWithConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTWITHCONFIGV2: ApiMlpgateAccountAccountModelModelPredictWithConfigV2,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTCONFIG: ApiMlpgateAccountAccountModelModelPredictConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTCONFIG_CONFIG_ID: ApiMlpgateAccountAccountModelModelPredictConfigConfigId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCES: ApiMlpgateAccountAccountModelModelInstances,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_TERMINATE: ApiMlpgateAccountAccountModelModelInstanceInstanceIdTerminate,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_STOP: ApiMlpgateAccountAccountModelModelInstanceInstanceIdStop,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_START: ApiMlpgateAccountAccountModelModelInstanceStart,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FIT: ApiMlpgateAccountAccountModelModelFit,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FITV2: ApiMlpgateAccountAccountModelModelFitV2,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FITCONFIG: ApiMlpgateAccountAccountModelModelFitConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FITCONFIG_CONFIG_ID: ApiMlpgateAccountAccountModelModelFitConfigConfigId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FAVORITE: ApiMlpgateAccountAccountModelModelFavorite,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_EXTERNAL: ApiMlpgateAccountAccountModelModelExternal,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_EXT: ApiMlpgateAccountAccountModelModelExt,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_DERIVED: ApiMlpgateAccountAccountModelModelDerived,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_CROSSVALIDATION: ApiMlpgateAccountAccountModelModelCrossValidation,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_CLONE: ApiMlpgateAccountAccountModelModelClone,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_BILLING: ApiMlpgateAccountAccountModelModelBilling,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODELGROUP: ApiMlpgateAccountAccountModelGroup,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MANAGEMENT_FEATURE_NAME: ApiMlpgateAccountAccountManagementFeatureName,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_IMAGE: ApiMlpgateAccountAccountImage,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_IMAGE_IMAGE_ID: ApiMlpgateAccountAccountImageImageId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DUMP: ApiMlpgateAccountAccountDump,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET: ApiMlpgateAccountAccountDataset,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID: ApiMlpgateAccountAccountDatasetDatasetId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID_RAW: ApiMlpgateAccountAccountDatasetDatasetIdRaw,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID_PARAPHRASE: ApiMlpgateAccountAccountDatasetDatasetIdParaphrase,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID_CONTENT: ApiMlpgateAccountAccountDatasetDatasetIdContent,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_RAW: ApiMlpgateAccountAccountDatasetRaw,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_EMPTY: ApiMlpgateAccountAccountDatasetEmpty,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATAIMAGE: ApiMlpgateAccountAccountDataImage,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATAIMAGE_IMAGE_ID: ApiMlpgateAccountAccountDataImageImageId,
        PathValues.API_MLPGATEINTERNAL_ACCOUNTS_DEACTIVATE: ApiMlpgateInternalAccountsDeactivate,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_UPDATELIMITS: ApiMlpgateInternalAccountAccountUpdateLimits,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_NAMESPACE_ENSURE: ApiMlpgateInternalAccountAccountNamespaceEnsure,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_PATH: ApiMlpgateInternalAccountAccountModelModelPath,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_DEACTIVATE: ApiMlpgateInternalAccountAccountModelModelInstanceDeactivate,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_FEATURES: ApiMlpgateInternalAccountAccountFeatures,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_BUCKET_DENY: ApiMlpgateInternalAccountAccountBucketDeny,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_BUCKET_ACCESS: ApiMlpgateInternalAccountAccountBucketAccess,
        PathValues.API_MLPGATE_ADMIN_RESOURCEGROUPS: ApiMlpgateAdminResourceGroups,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_MODELGROUP_GROUP_ID: ApiMlpgateAccountAccountModelModelModelGroupGroupId,
        PathValues.API_MLPGATEINTERNAL_RESOURCEGROUPS: ApiMlpgateInternalResourceGroups,
        PathValues.API_MLPGATE_VERSION: ApiMlpgateVersion,
        PathValues.API_MLPGATE_SYSTEMCONFIG_TASKTYPES: ApiMlpgateSystemConfigTaskTypes,
        PathValues.API_MLPGATE_SYSTEMCONFIG_RESOURCEGROUPS: ApiMlpgateSystemConfigResourceGroups,
        PathValues.API_MLPGATE_SYSTEMCONFIG_MODELDEFAULTS: ApiMlpgateSystemConfigModelDefaults,
        PathValues.API_MLPGATE_SYSTEMCONFIG_DATASETDATATYPE: ApiMlpgateSystemConfigDatasetDataType,
        PathValues.API_MLPGATE_MODELS: ApiMlpgateModels,
        PathValues.API_MLPGATE_MODELS_FEATURED: ApiMlpgateModelsFeatured,
        PathValues.API_MLPGATE_HEALTH: ApiMlpgateHealth,
        PathValues.API_MLPGATE_HEALTH_TEST: ApiMlpgateHealthTest,
        PathValues.API_MLPGATE_HEALTH_HISTORY: ApiMlpgateHealthHistory,
        PathValues.API_MLPGATE_ADMIN_ACCOUNTS: ApiMlpgateAdminAccounts,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT: ApiMlpgateAdminAccountAccount,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_TOKEN_TOKEN: ApiMlpgateAccountAccountTokenToken,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_STATLOG: ApiMlpgateAccountAccountStatLog,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_S3: ApiMlpgateAccountAccountS3,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_STATUS: ApiMlpgateAccountAccountModelModelStatus,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_METRIC: ApiMlpgateAccountAccountModelModelMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_METRICRANGE: ApiMlpgateAccountAccountModelModelMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_LOGS: ApiMlpgateAccountAccountModelModelLogs,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_LASTJOB: ApiMlpgateAccountAccountModelModelLastJob,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE: ApiMlpgateAccountAccountModelModelInstance,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_METRIC: ApiMlpgateAccountAccountModelModelInstanceInstanceIdMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_METRICRANGE: ApiMlpgateAccountAccountModelModelInstanceInstanceIdMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_FILE: ApiMlpgateAccountAccountModelModelInstanceInstanceIdFile,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_FILE_LOGS: ApiMlpgateAccountAccountModelModelInstanceInstanceIdFileLogs,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_EVENTS: ApiMlpgateAccountAccountModelModelInstanceInstanceIdEvents,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_ENVIRONMENT: ApiMlpgateAccountAccountModelModelInstanceInstanceIdEnvironment,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_ACTIONDESCRIPTOR: ApiMlpgateAccountAccountModelModelActionDescriptor,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_METRIC: ApiMlpgateAccountAccountMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_METRICRANGE: ApiMlpgateAccountAccountMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_JOB: ApiMlpgateAccountAccountJob,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_JOB_JOB_ID: ApiMlpgateAccountAccountJobJobId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_IMAGE_IMAGE_ID_LOGS: ApiMlpgateAccountAccountImageImageIdLogs,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_ORIGINAL_DATASET_ID_PARAPHRASE: ApiMlpgateAccountAccountDatasetOriginalDatasetIdParaphrase,
        PathValues.API_MLPGATEINTERNAL_TESTMAIL: ApiMlpgateInternalTestMail,
        PathValues.API_MLPGATEINTERNAL_STARTONEINSTANCE: ApiMlpgateInternalStartOneInstance,
        PathValues.API_MLPGATEINTERNAL_SETPUBLICFORALL: ApiMlpgateInternalSetPublicForAll,
        PathValues.API_MLPGATEINTERNAL_SERVICES: ApiMlpgateInternalServices,
        PathValues.API_MLPGATEINTERNAL_PGTEST_ACCOUNT: ApiMlpgateInternalPgTestAccount,
        PathValues.API_MLPGATEINTERNAL_NOTIFY_ACCOUNT_USER_USER_ID: ApiMlpgateInternalNotifyAccountUserUserId,
        PathValues.API_MLPGATEINTERNAL_EMPTYTEST: ApiMlpgateInternalEmptyTest,
        PathValues.API_MLPGATEINTERNAL_CLUSTER: ApiMlpgateInternalCluster,
        PathValues.API_MLPGATEINTERNAL_CLEARPUBLICFORALL: ApiMlpgateInternalClearPublicForAll,
        PathValues.API_MLPGATEINTERNAL_CLEARINSTANCES: ApiMlpgateInternalClearInstances,
        PathValues.API_MLPGATEINTERNAL_CLEARACCOUNT: ApiMlpgateInternalClearAccount,
        PathValues.API_MLPGATEINTERNAL_ACTIONS: ApiMlpgateInternalActions,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT: ApiMlpgateInternalAccount,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCES: ApiMlpgateInternalAccountAccountModelModelInstances,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_ACTIONS: ApiMlpgateInternalAccountAccountModelModelActions,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_MODELGROUP: ApiMlpgateAccountAccountModelModelModelGroup,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_EXTERNAL_INSTANCE_ID: ApiMlpgateAccountAccountModelModelExternalInstanceId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODELGROUP_GROUP_ID: ApiMlpgateAccountAccountModelGroupGroupId,
        PathValues.API_MLPGATEINTERNAL_INSTANCES_DELETE_BY_TIMESTAMP: ApiMlpgateInternalInstancesDeleteByTimestamp,
    }
)

path_to_api = PathToApi(
    {
        PathValues.P_ACCOUNT_FIELD_MODEL_FIELD: PAccountFieldModelField,
        PathValues.API_MLPGATE_ADMIN_SYSTEMCONFIG_ACCOUNT_ACCOUNT_DATA: ApiMlpgateAdminSystemConfigAccountAccountData,
        PathValues.API_MLPGATE_ADMIN_SYSTEMCONFIG_ACCOUNT_ACCOUNT_CONFIG: ApiMlpgateAdminSystemConfigAccountAccountConfig,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_LIMITS: ApiMlpgateAdminAccountAccountLimits,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_FEATURES: ApiMlpgateAdminAccountAccountFeatures,
        PathValues.API_MLPGATE_ACCOUNT: ApiMlpgateAccount,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_TOKEN: ApiMlpgateAccountAccountToken,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL: ApiMlpgateAccountAccountModel,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL: ApiMlpgateAccountAccountModelModel,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_TTSSTREAM: ApiMlpgateAccountAccountModelModelTtsStream,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_SIMPLEDOC: ApiMlpgateAccountAccountModelModelSimpleDoc,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PUBLICSETTINGS: ApiMlpgateAccountAccountModelModelPublicSettings,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICT: ApiMlpgateAccountAccountModelModelPredict,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTWITHCONFIG: ApiMlpgateAccountAccountModelModelPredictWithConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTWITHCONFIGV2: ApiMlpgateAccountAccountModelModelPredictWithConfigV2,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTCONFIG: ApiMlpgateAccountAccountModelModelPredictConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTCONFIG_CONFIG_ID: ApiMlpgateAccountAccountModelModelPredictConfigConfigId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCES: ApiMlpgateAccountAccountModelModelInstances,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_TERMINATE: ApiMlpgateAccountAccountModelModelInstanceInstanceIdTerminate,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_STOP: ApiMlpgateAccountAccountModelModelInstanceInstanceIdStop,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_START: ApiMlpgateAccountAccountModelModelInstanceStart,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FIT: ApiMlpgateAccountAccountModelModelFit,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FITV2: ApiMlpgateAccountAccountModelModelFitV2,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FITCONFIG: ApiMlpgateAccountAccountModelModelFitConfig,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FITCONFIG_CONFIG_ID: ApiMlpgateAccountAccountModelModelFitConfigConfigId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FAVORITE: ApiMlpgateAccountAccountModelModelFavorite,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_EXTERNAL: ApiMlpgateAccountAccountModelModelExternal,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_EXT: ApiMlpgateAccountAccountModelModelExt,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_DERIVED: ApiMlpgateAccountAccountModelModelDerived,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_CROSSVALIDATION: ApiMlpgateAccountAccountModelModelCrossValidation,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_CLONE: ApiMlpgateAccountAccountModelModelClone,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_BILLING: ApiMlpgateAccountAccountModelModelBilling,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODELGROUP: ApiMlpgateAccountAccountModelGroup,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MANAGEMENT_FEATURE_NAME: ApiMlpgateAccountAccountManagementFeatureName,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_IMAGE: ApiMlpgateAccountAccountImage,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_IMAGE_IMAGE_ID: ApiMlpgateAccountAccountImageImageId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DUMP: ApiMlpgateAccountAccountDump,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET: ApiMlpgateAccountAccountDataset,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID: ApiMlpgateAccountAccountDatasetDatasetId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID_RAW: ApiMlpgateAccountAccountDatasetDatasetIdRaw,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID_PARAPHRASE: ApiMlpgateAccountAccountDatasetDatasetIdParaphrase,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID_CONTENT: ApiMlpgateAccountAccountDatasetDatasetIdContent,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_RAW: ApiMlpgateAccountAccountDatasetRaw,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_EMPTY: ApiMlpgateAccountAccountDatasetEmpty,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATAIMAGE: ApiMlpgateAccountAccountDataImage,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATAIMAGE_IMAGE_ID: ApiMlpgateAccountAccountDataImageImageId,
        PathValues.API_MLPGATEINTERNAL_ACCOUNTS_DEACTIVATE: ApiMlpgateInternalAccountsDeactivate,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_UPDATELIMITS: ApiMlpgateInternalAccountAccountUpdateLimits,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_NAMESPACE_ENSURE: ApiMlpgateInternalAccountAccountNamespaceEnsure,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_PATH: ApiMlpgateInternalAccountAccountModelModelPath,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_DEACTIVATE: ApiMlpgateInternalAccountAccountModelModelInstanceDeactivate,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_FEATURES: ApiMlpgateInternalAccountAccountFeatures,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_BUCKET_DENY: ApiMlpgateInternalAccountAccountBucketDeny,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_BUCKET_ACCESS: ApiMlpgateInternalAccountAccountBucketAccess,
        PathValues.API_MLPGATE_ADMIN_RESOURCEGROUPS: ApiMlpgateAdminResourceGroups,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_MODELGROUP_GROUP_ID: ApiMlpgateAccountAccountModelModelModelGroupGroupId,
        PathValues.API_MLPGATEINTERNAL_RESOURCEGROUPS: ApiMlpgateInternalResourceGroups,
        PathValues.API_MLPGATE_VERSION: ApiMlpgateVersion,
        PathValues.API_MLPGATE_SYSTEMCONFIG_TASKTYPES: ApiMlpgateSystemConfigTaskTypes,
        PathValues.API_MLPGATE_SYSTEMCONFIG_RESOURCEGROUPS: ApiMlpgateSystemConfigResourceGroups,
        PathValues.API_MLPGATE_SYSTEMCONFIG_MODELDEFAULTS: ApiMlpgateSystemConfigModelDefaults,
        PathValues.API_MLPGATE_SYSTEMCONFIG_DATASETDATATYPE: ApiMlpgateSystemConfigDatasetDataType,
        PathValues.API_MLPGATE_MODELS: ApiMlpgateModels,
        PathValues.API_MLPGATE_MODELS_FEATURED: ApiMlpgateModelsFeatured,
        PathValues.API_MLPGATE_HEALTH: ApiMlpgateHealth,
        PathValues.API_MLPGATE_HEALTH_TEST: ApiMlpgateHealthTest,
        PathValues.API_MLPGATE_HEALTH_HISTORY: ApiMlpgateHealthHistory,
        PathValues.API_MLPGATE_ADMIN_ACCOUNTS: ApiMlpgateAdminAccounts,
        PathValues.API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT: ApiMlpgateAdminAccountAccount,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_TOKEN_TOKEN: ApiMlpgateAccountAccountTokenToken,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_STATLOG: ApiMlpgateAccountAccountStatLog,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_S3: ApiMlpgateAccountAccountS3,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_STATUS: ApiMlpgateAccountAccountModelModelStatus,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_METRIC: ApiMlpgateAccountAccountModelModelMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_METRICRANGE: ApiMlpgateAccountAccountModelModelMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_LOGS: ApiMlpgateAccountAccountModelModelLogs,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_LASTJOB: ApiMlpgateAccountAccountModelModelLastJob,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE: ApiMlpgateAccountAccountModelModelInstance,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_METRIC: ApiMlpgateAccountAccountModelModelInstanceInstanceIdMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_METRICRANGE: ApiMlpgateAccountAccountModelModelInstanceInstanceIdMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_FILE: ApiMlpgateAccountAccountModelModelInstanceInstanceIdFile,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_FILE_LOGS: ApiMlpgateAccountAccountModelModelInstanceInstanceIdFileLogs,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_EVENTS: ApiMlpgateAccountAccountModelModelInstanceInstanceIdEvents,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_ENVIRONMENT: ApiMlpgateAccountAccountModelModelInstanceInstanceIdEnvironment,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_ACTIONDESCRIPTOR: ApiMlpgateAccountAccountModelModelActionDescriptor,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_METRIC: ApiMlpgateAccountAccountMetric,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_METRICRANGE: ApiMlpgateAccountAccountMetricRange,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_JOB: ApiMlpgateAccountAccountJob,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_JOB_JOB_ID: ApiMlpgateAccountAccountJobJobId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_IMAGE_IMAGE_ID_LOGS: ApiMlpgateAccountAccountImageImageIdLogs,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_ORIGINAL_DATASET_ID_PARAPHRASE: ApiMlpgateAccountAccountDatasetOriginalDatasetIdParaphrase,
        PathValues.API_MLPGATEINTERNAL_TESTMAIL: ApiMlpgateInternalTestMail,
        PathValues.API_MLPGATEINTERNAL_STARTONEINSTANCE: ApiMlpgateInternalStartOneInstance,
        PathValues.API_MLPGATEINTERNAL_SETPUBLICFORALL: ApiMlpgateInternalSetPublicForAll,
        PathValues.API_MLPGATEINTERNAL_SERVICES: ApiMlpgateInternalServices,
        PathValues.API_MLPGATEINTERNAL_PGTEST_ACCOUNT: ApiMlpgateInternalPgTestAccount,
        PathValues.API_MLPGATEINTERNAL_NOTIFY_ACCOUNT_USER_USER_ID: ApiMlpgateInternalNotifyAccountUserUserId,
        PathValues.API_MLPGATEINTERNAL_EMPTYTEST: ApiMlpgateInternalEmptyTest,
        PathValues.API_MLPGATEINTERNAL_CLUSTER: ApiMlpgateInternalCluster,
        PathValues.API_MLPGATEINTERNAL_CLEARPUBLICFORALL: ApiMlpgateInternalClearPublicForAll,
        PathValues.API_MLPGATEINTERNAL_CLEARINSTANCES: ApiMlpgateInternalClearInstances,
        PathValues.API_MLPGATEINTERNAL_CLEARACCOUNT: ApiMlpgateInternalClearAccount,
        PathValues.API_MLPGATEINTERNAL_ACTIONS: ApiMlpgateInternalActions,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT: ApiMlpgateInternalAccount,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCES: ApiMlpgateInternalAccountAccountModelModelInstances,
        PathValues.API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_ACTIONS: ApiMlpgateInternalAccountAccountModelModelActions,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_MODELGROUP: ApiMlpgateAccountAccountModelModelModelGroup,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_EXTERNAL_INSTANCE_ID: ApiMlpgateAccountAccountModelModelExternalInstanceId,
        PathValues.API_MLPGATE_ACCOUNT_ACCOUNT_MODELGROUP_GROUP_ID: ApiMlpgateAccountAccountModelGroupGroupId,
        PathValues.API_MLPGATEINTERNAL_INSTANCES_DELETE_BY_TIMESTAMP: ApiMlpgateInternalInstancesDeleteByTimestamp,
    }
)
