import os
import time

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_dataset_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    timestamp = int(time.time())
    req_body = (
        CreateDatasetRequestBody.builder()
        .name(f"[Example] KB {timestamp}")
        .description("Example knowledge base")
        .type("knowledge_base")
        .indexing_technique("high_quality")
        .permission("only_me")
        .build()
    )

    req = CreateDatasetRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.dataset.create(req, req_option)
    if response.success:
        print(f"Dataset created: {response.name} (ID: {response.id})")
    else:
        print(f"Error creating dataset: {response.code} - {response.msg}")
    return response


async def acreate_dataset_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    timestamp = int(time.time())
    req_body = (
        CreateDatasetRequestBody.builder()
        .name(f"[Example] Async KB {timestamp}")
        .description("Example async knowledge base")
        .type("knowledge_base")
        .indexing_technique("high_quality")
        .permission("only_me")
        .build()
    )

    req = CreateDatasetRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.dataset.acreate(req, req_option)
    if response.success:
        print(f"Dataset created async: {response.name} (ID: {response.id})")
    else:
        print(f"Error creating dataset async: {response.code} - {response.msg}")
    return response


if __name__ == "__main__":
    create_dataset_example()
