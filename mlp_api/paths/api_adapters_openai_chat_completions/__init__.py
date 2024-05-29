# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from mlp_api.paths.api_adapters_openai_chat_completions import Api

from mlp_api.paths import PathValues

path = PathValues.API_ADAPTERS_OPENAI_CHAT_COMPLETIONS