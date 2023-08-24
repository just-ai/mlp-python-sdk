# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from mlp_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    P_ACCOUNT_FIELD_MODEL_FIELD = "/p/{accountField}/{modelField}"
    API_MLPGATE_ADMIN_SYSTEMCONFIG_ACCOUNT_ACCOUNT_DATA = "/api/mlpgate/admin/system-config/account/{account}/data"
    API_MLPGATE_ADMIN_SYSTEMCONFIG_ACCOUNT_ACCOUNT_CONFIG = "/api/mlpgate/admin/system-config/account/{account}/config"
    API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_LIMITS = "/api/mlpgate/admin/account/{account}/limits"
    API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_FEATURES = "/api/mlpgate/admin/account/{account}/features"
    API_MLPGATE_ACCOUNT = "/api/mlpgate/account"
    API_MLPGATE_ACCOUNT_ACCOUNT_TOKEN = "/api/mlpgate/account/{account}/token"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL = "/api/mlpgate/account/{account}/model"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL = "/api/mlpgate/account/{account}/model/{model}"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_TTSSTREAM = "/api/mlpgate/account/{account}/model/{model}/tts-stream"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_SIMPLEDOC = "/api/mlpgate/account/{account}/model/{model}/simple-doc"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PUBLICSETTINGS = "/api/mlpgate/account/{account}/model/{model}/public-settings"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICT = "/api/mlpgate/account/{account}/model/{model}/predict"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTWITHCONFIG = "/api/mlpgate/account/{account}/model/{model}/predict-with-config"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTWITHCONFIGV2 = "/api/mlpgate/account/{account}/model/{model}/predict-with-config-v2"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTCONFIG = "/api/mlpgate/account/{account}/model/{model}/predict-config"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_PREDICTCONFIG_CONFIG_ID = "/api/mlpgate/account/{account}/model/{model}/predict-config/{configId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCES = "/api/mlpgate/account/{account}/model/{model}/instances"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_TERMINATE = "/api/mlpgate/account/{account}/model/{model}/instance/{instanceId}/terminate"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_STOP = "/api/mlpgate/account/{account}/model/{model}/instance/{instanceId}/stop"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_START = "/api/mlpgate/account/{account}/model/{model}/instance/start"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FIT = "/api/mlpgate/account/{account}/model/{model}/fit"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FITV2 = "/api/mlpgate/account/{account}/model/{model}/fit-v2"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FITCONFIG = "/api/mlpgate/account/{account}/model/{model}/fit-config"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FITCONFIG_CONFIG_ID = "/api/mlpgate/account/{account}/model/{model}/fit-config/{configId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_FAVORITE = "/api/mlpgate/account/{account}/model/{model}/favorite"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_EXTERNAL = "/api/mlpgate/account/{account}/model/{model}/external"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_EXT = "/api/mlpgate/account/{account}/model/{model}/ext"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_DERIVED = "/api/mlpgate/account/{account}/model/{model}/derived"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_CROSSVALIDATION = "/api/mlpgate/account/{account}/model/{model}/cross-validation"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_CLONE = "/api/mlpgate/account/{account}/model/{model}/clone"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_BILLING = "/api/mlpgate/account/{account}/model/{model}/billing"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODELGROUP = "/api/mlpgate/account/{account}/model-group"
    API_MLPGATE_ACCOUNT_ACCOUNT_MANAGEMENT_FEATURE_NAME = "/api/mlpgate/account/{account}/management/{featureName}"
    API_MLPGATE_ACCOUNT_ACCOUNT_IMAGE = "/api/mlpgate/account/{account}/image"
    API_MLPGATE_ACCOUNT_ACCOUNT_IMAGE_IMAGE_ID = "/api/mlpgate/account/{account}/image/{imageId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_DUMP = "/api/mlpgate/account/{account}/dump"
    API_MLPGATE_ACCOUNT_ACCOUNT_DATASET = "/api/mlpgate/account/{account}/dataset"
    API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID = "/api/mlpgate/account/{account}/dataset/{datasetId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID_RAW = "/api/mlpgate/account/{account}/dataset/{datasetId}/raw"
    API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID_PARAPHRASE = "/api/mlpgate/account/{account}/dataset/{datasetId}/paraphrase"
    API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_DATASET_ID_CONTENT = "/api/mlpgate/account/{account}/dataset/{datasetId}/content"
    API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_RAW = "/api/mlpgate/account/{account}/dataset/raw"
    API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_EMPTY = "/api/mlpgate/account/{account}/dataset/empty"
    API_MLPGATE_ACCOUNT_ACCOUNT_DATAIMAGE = "/api/mlpgate/account/{account}/data-image"
    API_MLPGATE_ACCOUNT_ACCOUNT_DATAIMAGE_IMAGE_ID = "/api/mlpgate/account/{account}/data-image/{imageId}"
    API_MLPGATEINTERNAL_ACCOUNTS_DEACTIVATE = "/api/mlpgate-internal/accounts/deactivate"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_UPDATELIMITS = "/api/mlpgate-internal/account/{account}/update-limits"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_NAMESPACE_ENSURE = "/api/mlpgate-internal/account/{account}/namespace/ensure"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_PATH = "/api/mlpgate-internal/account/{account}/model/{model}/path"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_DEACTIVATE = "/api/mlpgate-internal/account/{account}/model/{model}/instance/deactivate"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_FEATURES = "/api/mlpgate-internal/account/{account}/features"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_BUCKET_DENY = "/api/mlpgate-internal/account/{account}/bucket/deny"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_BUCKET_ACCESS = "/api/mlpgate-internal/account/{account}/bucket/access"
    API_MLPGATE_ADMIN_RESOURCEGROUPS = "/api/mlpgate/admin/resource-groups"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_MODELGROUP_GROUP_ID = "/api/mlpgate/account/{account}/model/{model}/model-group/{groupId}"
    API_MLPGATEINTERNAL_RESOURCEGROUPS = "/api/mlpgate-internal/resource-groups"
    API_MLPGATE_VERSION = "/api/mlpgate/version"
    API_MLPGATE_SYSTEMCONFIG_TASKTYPES = "/api/mlpgate/system-config/task-types"
    API_MLPGATE_SYSTEMCONFIG_RESOURCEGROUPS = "/api/mlpgate/system-config/resource-groups"
    API_MLPGATE_SYSTEMCONFIG_MODELDEFAULTS = "/api/mlpgate/system-config/model-defaults"
    API_MLPGATE_SYSTEMCONFIG_DATASETDATATYPE = "/api/mlpgate/system-config/dataset-data-type"
    API_MLPGATE_MODELS = "/api/mlpgate/models"
    API_MLPGATE_MODELS_FEATURED = "/api/mlpgate/models/featured"
    API_MLPGATE_HEALTH = "/api/mlpgate/health"
    API_MLPGATE_HEALTH_TEST = "/api/mlpgate/health/test"
    API_MLPGATE_HEALTH_HISTORY = "/api/mlpgate/health/history"
    API_MLPGATE_ADMIN_ACCOUNTS = "/api/mlpgate/admin/accounts"
    API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT = "/api/mlpgate/admin/account/{account}"
    API_MLPGATE_ACCOUNT_ACCOUNT_TOKEN_TOKEN = "/api/mlpgate/account/{account}/token/{token}"
    API_MLPGATE_ACCOUNT_ACCOUNT_STATLOG = "/api/mlpgate/account/{account}/stat-log"
    API_MLPGATE_ACCOUNT_ACCOUNT_S3 = "/api/mlpgate/account/{account}/s3"
    API_MLPGATE_ACCOUNT_ACCOUNT_RESOURCEGROUPS = "/api/mlpgate/account/{account}/resource-groups"
    API_MLPGATE_ACCOUNT_ACCOUNT_RESOURCEGROUPS_GROUP_NAME_SERVICES = "/api/mlpgate/account/{account}/resource-groups/{groupName}/services"
    API_MLPGATE_ACCOUNT_ACCOUNT_RESOURCEGROUPS_GROUP_NAME_METRIC = "/api/mlpgate/account/{account}/resource-groups/{groupName}/metric"
    API_MLPGATE_ACCOUNT_ACCOUNT_RESOURCEGROUPS_GROUP_NAME_METRICRANGE = "/api/mlpgate/account/{account}/resource-groups/{groupName}/metric-range"
    API_MLPGATE_ACCOUNT_ACCOUNT_RESOURCEGROUPS_GROUP_NAME_LOGS = "/api/mlpgate/account/{account}/resource-groups/{groupName}/logs"
    API_MLPGATE_ACCOUNT_ACCOUNT_RESOURCEGROUPS_GROUP_NAME_CAPACITY = "/api/mlpgate/account/{account}/resource-groups/{groupName}/capacity"
    API_MLPGATE_ACCOUNT_ACCOUNT_RESOURCEGROUPS_GROUP_NAME_CAPACITY_LOGS = "/api/mlpgate/account/{account}/resource-groups/{groupName}/capacity/logs"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_STATUS = "/api/mlpgate/account/{account}/model/{model}/status"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_METRIC = "/api/mlpgate/account/{account}/model/{model}/metric"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_METRICRANGE = "/api/mlpgate/account/{account}/model/{model}/metric-range"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_LOGS = "/api/mlpgate/account/{account}/model/{model}/logs"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_LASTJOB = "/api/mlpgate/account/{account}/model/{model}/last-job"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE = "/api/mlpgate/account/{account}/model/{model}/instance"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_METRIC = "/api/mlpgate/account/{account}/model/{model}/instance/{instanceId}/metric"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_METRICRANGE = "/api/mlpgate/account/{account}/model/{model}/instance/{instanceId}/metric-range"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_FILE = "/api/mlpgate/account/{account}/model/{model}/instance/{instanceId}/file"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_FILE_LOGS = "/api/mlpgate/account/{account}/model/{model}/instance/{instanceId}/file/logs"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_EVENTS = "/api/mlpgate/account/{account}/model/{model}/instance/{instanceId}/events"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCE_INSTANCE_ID_ENVIRONMENT = "/api/mlpgate/account/{account}/model/{model}/instance/{instanceId}/environment"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_DATASET_ALLOWED = "/api/mlpgate/account/{account}/model/{model}/dataset/allowed"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_DATASET_ALLOWEDTYPES = "/api/mlpgate/account/{account}/model/{model}/dataset/allowed-types"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_ACTIONDESCRIPTOR = "/api/mlpgate/account/{account}/model/{model}/action-descriptor"
    API_MLPGATE_ACCOUNT_ACCOUNT_METRIC = "/api/mlpgate/account/{account}/metric"
    API_MLPGATE_ACCOUNT_ACCOUNT_METRICRANGE = "/api/mlpgate/account/{account}/metric-range"
    API_MLPGATE_ACCOUNT_ACCOUNT_JOB = "/api/mlpgate/account/{account}/job"
    API_MLPGATE_ACCOUNT_ACCOUNT_JOB_JOB_ID = "/api/mlpgate/account/{account}/job/{jobId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_IMAGE_IMAGE_ID_LOGS = "/api/mlpgate/account/{account}/image/{imageId}/logs"
    API_MLPGATE_ACCOUNT_ACCOUNT_DATASET_ORIGINAL_DATASET_ID_PARAPHRASE = "/api/mlpgate/account/{account}/dataset/{originalDatasetId}/paraphrase"
    API_MLPGATEINTERNAL_TESTMAIL = "/api/mlpgate-internal/test-mail"
    API_MLPGATEINTERNAL_STARTONEINSTANCE = "/api/mlpgate-internal/start-one-instance"
    API_MLPGATEINTERNAL_SETPUBLICFORALL = "/api/mlpgate-internal/set-public-for-all"
    API_MLPGATEINTERNAL_SERVICES = "/api/mlpgate-internal/services"
    API_MLPGATEINTERNAL_PGTEST_ACCOUNT = "/api/mlpgate-internal/pg-test/{account}"
    API_MLPGATEINTERNAL_NOTIFY_ACCOUNT_USER_USER_ID = "/api/mlpgate-internal/notify/{account}/user/{userId}"
    API_MLPGATEINTERNAL_EMPTYTEST = "/api/mlpgate-internal/empty-test"
    API_MLPGATEINTERNAL_CLUSTER = "/api/mlpgate-internal/cluster"
    API_MLPGATEINTERNAL_CLEARPUBLICFORALL = "/api/mlpgate-internal/clear-public-for-all"
    API_MLPGATEINTERNAL_CLEARINSTANCES = "/api/mlpgate-internal/clear-instances"
    API_MLPGATEINTERNAL_CLEARACCOUNT = "/api/mlpgate-internal/clear-account"
    API_MLPGATEINTERNAL_ACTIONS = "/api/mlpgate-internal/actions"
    API_MLPGATEINTERNAL_ACCOUNT = "/api/mlpgate-internal/account"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_INSTANCES = "/api/mlpgate-internal/account/{account}/model/{model}/instances"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_MODEL_MODEL_ACTIONS = "/api/mlpgate-internal/account/{account}/model/{model}/actions"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_MODELGROUP = "/api/mlpgate/account/{account}/model/{model}/model-group"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODEL_MODEL_EXTERNAL_INSTANCE_ID = "/api/mlpgate/account/{account}/model/{model}/external/{instanceId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_MODELGROUP_GROUP_ID = "/api/mlpgate/account/{account}/model-group/{groupId}"
    API_MLPGATEINTERNAL_INSTANCES_DELETE_BY_TIMESTAMP = "/api/mlpgate-internal/instances/deleteByTimestamp"
