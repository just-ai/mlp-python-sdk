# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from mlp_api.paths.api_mlpgate_server_heartbeat import Api

from mlp_api.paths import PathValues

path = PathValues.API_MLPGATE_SERVERHEARTBEAT