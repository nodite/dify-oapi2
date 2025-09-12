import os

from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_datasets_example():
    api_key = os.getenv("KNOWLEDGE_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = ListDatasetsRequest.builder().page(1).limit(10).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.dataset.list(req, req_option)
    print(f"Found {len(response.data or [])} datasets")
    for dataset in response.data or []:
        print(f"- {dataset.name} (ID: {dataset.id})")


async def alist_datasets_example():
    api_key = os.getenv("KNOWLEDGE_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = ListDatasetsRequest.builder().page(1).limit(10).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.dataset.alist(req, req_option)
    print(f"Found {len(response.data or [])} datasets (async)")


if __name__ == "__main__":
    list_datasets_example()
