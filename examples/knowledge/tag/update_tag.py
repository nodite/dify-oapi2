import os

from dify_oapi.api.knowledge.v1.model.update_tag_request import UpdateTagRequest
from dify_oapi.api.knowledge.v1.model.update_tag_request_body import UpdateTagRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_tag_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    tag_id = os.getenv("TAG_ID")
    if not tag_id:
        raise ValueError("TAG_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = UpdateTagRequestBody.builder().tag_id(tag_id).name("[Example] Updated Tag Name").build()

    req = UpdateTagRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.tag.update(req, req_option)
    print(f"Tag updated: {response.name} (ID: {response.id})")
    return response


async def aupdate_tag_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    tag_id = os.getenv("TAG_ID")
    if not tag_id:
        raise ValueError("TAG_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = UpdateTagRequestBody.builder().tag_id(tag_id).name("[Example] Updated Tag Name (Async)").build()

    req = UpdateTagRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.tag.aupdate(req, req_option)
    print(f"Tag updated (async): {response.name} (ID: {response.id})")
    return response


if __name__ == "__main__":
    update_tag_example()
