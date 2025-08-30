import os

from dify_oapi.api.knowledge.v1.model.get_dataset_request import GetDatasetRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_dataset_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        raise ValueError("DATASET_ID environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetDatasetRequest.builder().dataset_id(dataset_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.dataset.get(req, req_option)
    print(f"Dataset: {response.name} (ID: {response.id})")
    print(f"Documents: {response.document_count}, Words: {response.word_count}")
    return response


async def aget_dataset_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        raise ValueError("DATASET_ID environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetDatasetRequest.builder().dataset_id(dataset_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.dataset.aget(req, req_option)
    print(f"Dataset (async): {response.name} (ID: {response.id})")
    return response


if __name__ == "__main__":
    get_dataset_example()
