# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from mlp_api.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCESSTOKENENDPOINT = "access-token-endpoint"
    ACCOUNTENDPOINT = "account-endpoint"
    ADMINENDPOINT = "admin-endpoint"
    APPLICATIONENDPOINT = "application-endpoint"
    ARCHIVEENDPOINT = "archive-endpoint"
    CHATGPTENDPOINT = "chat-gpt-endpoint"
    DATAIMAGEENDPOINT = "data-image-endpoint"
    DATASETENDPOINT = "dataset-endpoint"
    FITCONFIGENDPOINT = "fit-config-endpoint"
    IMAGEENDPOINT = "image-endpoint"
    INTERNALENDPOINT = "internal-endpoint"
    JOBENDPOINT = "job-endpoint"
    MANUALMANAGEMENTENDPOINT = "manual-management-endpoint"
    METRICENDPOINT = "metric-endpoint"
    MODELENDPOINT = "model-endpoint"
    MODELGROUPENDPOINT = "model-group-endpoint"
    MODELINSTANCEENDPOINT = "model-instance-endpoint"
    PREDICTCONFIGENDPOINT = "predict-config-endpoint"
    PROCESSENDPOINT = "process-endpoint"
    RESOURCEGROUPENDPOINT = "resource-group-endpoint"
    RESOURCEGROUPQUOTAENDPOINT = "resource-group-quota-endpoint"
    RESOURCEGROUPSERVERSENDPOINT = "resource-group-servers-endpoint"
    STATLOGENDPOINT = "stat-log-endpoint"
    SYSTEMCONFIGENDPOINT = "system-config-endpoint"
    SYSTEMENDPOINT = "system-endpoint"
    TASKENDPOINT = "task-endpoint"
    TTSENDPOINT = "tts-endpoint"
