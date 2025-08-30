import os

from dify_oapi.api.knowledge.v1.model.list_tags_request import ListTagsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_tags_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = ListTagsRequest.builder().build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.tag.list(req, req_option)
    print(f"Found {len(response.data or [])} tags")
    for tag in response.data or []:
        print(f"- {tag.name} ({tag.type}) - {tag.binding_count} bindings")
    return response


async def alist_tags_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = ListTagsRequest.builder().build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.tag.alist(req, req_option)
    print(f"Found {len(response.data or [])} tags (async)")
    for tag in response.data or []:
        print(f"- {tag.name} ({tag.type}) - {tag.binding_count} bindings")
    return response


def list_knowledge_type_tags_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = ListTagsRequest.builder().type("knowledge_type").build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.tag.list(req, req_option)
    print(f"Found {len(response.data or [])} knowledge type tags")
    for tag in response.data or []:
        print(f"- {tag.name}")
    return response


if __name__ == "__main__":
    list_tags_example()
