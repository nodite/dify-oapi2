import os

from dify_oapi.api.knowledge.v1.model.update_dataset_request import UpdateDatasetRequest
from dify_oapi.api.knowledge.v1.model.update_dataset_request_body import UpdateDatasetRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_dataset_example():
    api_key = os.getenv("KNOWLEDGE_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        print("Note: DATASET_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real dataset id to execute.")
        print("Set DATASET_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        UpdateDatasetRequestBody.builder()
        .name("[Example] Updated Dataset Name")
        .description("Updated description for example dataset")
        .build()
    )

    req = UpdateDatasetRequest.builder().dataset_id(dataset_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.dataset.update(req, req_option)
    print(f"Dataset updated: {response.name} (ID: {response.id})")
    return response


async def aupdate_dataset_example():
    api_key = os.getenv("KNOWLEDGE_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        print("Note: DATASET_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real dataset id to execute.")
        print("Set DATASET_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        UpdateDatasetRequestBody.builder()
        .name("[Example] Async Updated Dataset")
        .description("Async updated description")
        .build()
    )

    req = UpdateDatasetRequest.builder().dataset_id(dataset_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.dataset.aupdate(req, req_option)
    print(f"Dataset updated (async): {response.name} (ID: {response.id})")
    return response


if __name__ == "__main__":
    update_dataset_example()
