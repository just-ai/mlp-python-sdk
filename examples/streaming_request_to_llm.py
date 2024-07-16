import requests

if __name__ == "__main__":
    mlp_api_key = ""
    account_id = "just-ai"
    model_name = "openai-proxy"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "hello"}],
        "stream": True,
    }
    session = requests.Session()
    with session.post(
        f"https://caila.io/catalog/{account_id}/{model_name}",
        data=payload,
        headers={"MLP-API-KEY": mlp_api_key},
        stream=True,
    ) as resp:
        for chunk in resp.iter_content(chunk_size=None):
            print(chunk)
