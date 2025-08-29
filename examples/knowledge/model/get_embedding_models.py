import os

from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_embedding_models_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req = GetTextEmbeddingModelsRequest.builder().build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.model.embedding_models(req, req_option)
    print(f"Found {len(response.data or [])} embedding models")
    for model in response.data or []:
        print(f"- {model.model_name} ({model.model_type})")


if __name__ == "__main__":
    get_embedding_models_example()
