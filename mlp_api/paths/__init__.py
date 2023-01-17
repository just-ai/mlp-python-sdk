# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from mlp_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_ID_LIMITS = "/api/mlpgate/admin/account/{accountId}/limits"
    API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_ID_FEATURES = "/api/mlpgate/admin/account/{accountId}/features"
    API_MLPGATE_ACCOUNT = "/api/mlpgate/account"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_TOKEN = "/api/mlpgate/account/{accountId}/token"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL = "/api/mlpgate/account/{accountId}/model"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID = "/api/mlpgate/account/{accountId}/model/{modelId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_SIMPLEDOC = "/api/mlpgate/account/{accountId}/model/{modelId}/simple-doc"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICT = "/api/mlpgate/account/{accountId}/model/{modelId}/predict"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICTWITHCONFIG = "/api/mlpgate/account/{accountId}/model/{modelId}/predict-with-config"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICTCONFIG = "/api/mlpgate/account/{accountId}/model/{modelId}/predict-config"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PREDICTCONFIG_CONFIG_ID = "/api/mlpgate/account/{accountId}/model/{modelId}/predict-config/{configId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCES = "/api/mlpgate/account/{accountId}/model/{modelId}/instances"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_TERMINATE = "/api/mlpgate/account/{accountId}/model/{modelId}/instance/{instanceId}/terminate"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_STOP = "/api/mlpgate/account/{accountId}/model/{modelId}/instance/{instanceId}/stop"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_START = "/api/mlpgate/account/{accountId}/model/{modelId}/instance/start"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_FIT = "/api/mlpgate/account/{accountId}/model/{modelId}/fit"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_FITCONFIG = "/api/mlpgate/account/{accountId}/model/{modelId}/fit-config"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_FITCONFIG_CONFIG_ID = "/api/mlpgate/account/{accountId}/model/{modelId}/fit-config/{configId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_EXTERNAL = "/api/mlpgate/account/{accountId}/model/{modelId}/external"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_EXT = "/api/mlpgate/account/{accountId}/model/{modelId}/ext"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_DERIVED = "/api/mlpgate/account/{accountId}/model/{modelId}/derived"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_CROSSVALIDATION = "/api/mlpgate/account/{accountId}/model/{modelId}/cross-validation"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MANAGEMENT_FEATURE_NAME = "/api/mlpgate/account/{accountId}/management/{featureName}"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_IMAGE = "/api/mlpgate/account/{accountId}/image"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_IMAGE_IMAGE_ID = "/api/mlpgate/account/{accountId}/image/{imageId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATASET = "/api/mlpgate/account/{accountId}/dataset"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATASET_DATASET_ID = "/api/mlpgate/account/{accountId}/dataset/{datasetId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATASET_DATASET_ID_CONTENT = "/api/mlpgate/account/{accountId}/dataset/{datasetId}/content"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATAIMAGE = "/api/mlpgate/account/{accountId}/data-image"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_DATAIMAGE_IMAGE_ID = "/api/mlpgate/account/{accountId}/data-image/{imageId}"
    API_MLPGATE_ACCOUNT_DUMP_ACCOUNT_ID = "/api/mlpgate/account/dump/{accountId}"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_UPDATELIMITS = "/api/mlpgate-internal/account/{accountId}/update-limits"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_NAMESPACE_ENSURE = "/api/mlpgate-internal/account/{accountId}/namespace/ensure"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_PATH = "/api/mlpgate-internal/account/{accountId}/model/{modelId}/path"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_DEACTIVATE = "/api/mlpgate-internal/account/{accountId}/model/{modelId}/instance/deactivate"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_FEATURES = "/api/mlpgate-internal/account/{accountId}/features"
    API_MLPGATEINTERNAL_ACCOUNT_DEACTIVATE = "/api/mlpgate-internal/account/deactivate"
    API_MLPGATE_ADMIN_RESOURCEGROUPS = "/api/mlpgate/admin/resource-groups"
    API_MLPGATEINTERNAL_RESOURCEGROUPS = "/api/mlpgate-internal/resource-groups"
    API_MLPGATE_VERSION = "/api/mlpgate/version"
    API_MLPGATE_SYSTEMCONFIG_TASKTYPES = "/api/mlpgate/system-config/task-types"
    API_MLPGATE_SYSTEMCONFIG_RESOURCEGROUPS = "/api/mlpgate/system-config/resource-groups"
    API_MLPGATE_SYSTEMCONFIG_MODELDEFAULTS = "/api/mlpgate/system-config/model-defaults"
    API_MLPGATE_SYSTEMCONFIG_DATASETDATATYPE = "/api/mlpgate/system-config/dataset-data-type"
    API_MLPGATE_HEALTH = "/api/mlpgate/health"
    API_MLPGATE_HEALTH_TEST = "/api/mlpgate/health/test"
    API_MLPGATE_ADMIN_ACCOUNT = "/api/mlpgate/admin/account"
    API_MLPGATE_ADMIN_ACCOUNT_ACCOUNT_ID = "/api/mlpgate/admin/account/{accountId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_TOKEN_TOKEN = "/api/mlpgate/account/{accountId}/token/{token}"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_STATLOG = "/api/mlpgate/account/{accountId}/stat-log"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_STATUS = "/api/mlpgate/account/{accountId}/model/{modelId}/status"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_METRIC = "/api/mlpgate/account/{accountId}/model/{modelId}/metric"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_METRICRANGE = "/api/mlpgate/account/{accountId}/model/{modelId}/metric-range"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_LOGS = "/api/mlpgate/account/{accountId}/model/{modelId}/logs"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_LASTJOB = "/api/mlpgate/account/{accountId}/model/{modelId}/last-job"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE = "/api/mlpgate/account/{accountId}/model/{modelId}/instance"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_METRIC = "/api/mlpgate/account/{accountId}/model/{modelId}/instance/{instanceId}/metric"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_METRICRANGE = "/api/mlpgate/account/{accountId}/model/{modelId}/instance/{instanceId}/metric-range"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_FILE = "/api/mlpgate/account/{accountId}/model/{modelId}/instance/{instanceId}/file"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_FILE_LOGS = "/api/mlpgate/account/{accountId}/model/{modelId}/instance/{instanceId}/file/logs"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_EVENTS = "/api/mlpgate/account/{accountId}/model/{modelId}/instance/{instanceId}/events"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCE_INSTANCE_ID_ENVIRONMENT = "/api/mlpgate/account/{accountId}/model/{modelId}/instance/{instanceId}/environment"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_ACTIONDESCRIPTOR = "/api/mlpgate/account/{accountId}/model/{modelId}/action-descriptor"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_METRIC = "/api/mlpgate/account/{accountId}/metric"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_METRICRANGE = "/api/mlpgate/account/{accountId}/metric-range"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_JOB = "/api/mlpgate/account/{accountId}/job"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_JOB_JOB_ID = "/api/mlpgate/account/{accountId}/job/{jobId}"
    API_MLPGATE_ACCOUNT_ACCOUNT_ID_IMAGE_IMAGE_ID_LOGS = "/api/mlpgate/account/{accountId}/image/{imageId}/logs"
    API_MLPGATE_ACCOUNT_S3_ACCOUNT_ID = "/api/mlpgate/account/s3/{accountId}"
    API_MLPGATEINTERNAL_TESTMAIL = "/api/mlpgate-internal/test-mail"
    API_MLPGATEINTERNAL_SERVICES = "/api/mlpgate-internal/services"
    API_MLPGATEINTERNAL_NOTIFY_ACCOUNT_ID_USER_USER_ID = "/api/mlpgate-internal/notify/{accountId}/user/{userId}"
    API_MLPGATEINTERNAL_CLUSTER = "/api/mlpgate-internal/cluster"
    API_MLPGATEINTERNAL_ACTIONS = "/api/mlpgate-internal/actions"
    API_MLPGATEINTERNAL_ACCOUNT = "/api/mlpgate-internal/account"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_INSTANCES = "/api/mlpgate-internal/account/{accountId}/model/{modelId}/instances"
    API_MLPGATEINTERNAL_ACCOUNT_ACCOUNT_ID_MODEL_MODEL_ID_ACTIONS = "/api/mlpgate-internal/account/{accountId}/model/{modelId}/actions"
    API_MLPGATEINTERNAL_INSTANCES_DELETE_BY_TIMESTAMP = "/api/mlpgate-internal/instances/deleteByTimestamp"
    P_ACCOUNT_MODEL = "/p/{account}/{model}"