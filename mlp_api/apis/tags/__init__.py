# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from mlp_api.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCESSTOKENENDPOINT = "access-token-endpoint"
    ACCOUNTENDPOINT = "account-endpoint"
    ADMINENDPOINT = "admin-endpoint"
    DATAIMAGEENDPOINT = "data-image-endpoint"
    DATASETENDPOINT = "dataset-endpoint"
    FITCONFIGENDPOINT = "fit-config-endpoint"
    IMAGEENDPOINT = "image-endpoint"
    INTERNALENDPOINT = "internal-endpoint"
    JOBENDPOINT = "job-endpoint"
    MANUALMANAGEMENTENDPOINT = "manual-management-endpoint"
    METRICENDPOINT = "metric-endpoint"
    MODELENDPOINT = "model-endpoint"
    MODELINSTANCEENDPOINT = "model-instance-endpoint"
    PREDICTCONFIGENDPOINT = "predict-config-endpoint"
    PROCESSENDPOINT = "process-endpoint"
    PROCESSSERVLET = "process-servlet"
    STATLOGENDPOINT = "stat-log-endpoint"
    SYSTEMCONFIGENDPOINT = "system-config-endpoint"
    SYSTEMENDPOINT = "system-endpoint"
