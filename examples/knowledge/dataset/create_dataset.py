import os

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_dataset_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = (
        CreateDatasetRequestBody.builder()
        .name("[Example] Product Documentation")
        .description("Example knowledge base for product documentation")
        .indexing_technique("high_quality")
        .permission("only_me")
        .build()
    )

    req = CreateDatasetRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.dataset.create(req, req_option)
    print(f"Dataset created: {response.name} (ID: {response.id})")
    return response


async def acreate_dataset_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = (
        CreateDatasetRequestBody.builder()
        .name("[Example] Async Product Documentation")
        .description("Example async knowledge base")
        .indexing_technique("high_quality")
        .permission("only_me")
        .build()
    )

    req = CreateDatasetRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.dataset.acreate(req, req_option)
    print(f"Dataset created async: {response.name} (ID: {response.id})")
    return response


if __name__ == "__main__":
    create_dataset_example()
