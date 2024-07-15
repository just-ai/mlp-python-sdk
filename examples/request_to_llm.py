import ast
from pprint import pprint

from mlp_api.api.process_endpoint_api import ProcessEndpointApi
from mlp_api.models.predict_request_data import PredictRequestData
from mlp_sdk.transport.MlpClientSDK import MlpRestClient

if __name__ == "__main__":
    mlp_api_key = ""
    account_id = "just-ai"
    model_name = "openai-proxy"
    rest_client = MlpRestClient(url="https://caila.io", token=mlp_api_key)
    model = ProcessEndpointApi(rest_client)

    request = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "hello"}],
    }
    response = model.predict_with_config(
        account_id,
        model_name,
        predict_request_data=PredictRequestData(data=request),
    )
    result = ast.literal_eval(response)
    pprint(result)
