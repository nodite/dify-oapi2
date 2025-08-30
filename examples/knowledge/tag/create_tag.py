import os

from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_tag_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = CreateTagRequestBody.builder().name("[Example] Test Tag").type("knowledge").build()

    req = CreateTagRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.tag.create(req, req_option)
    print(f"Tag created: {response.name} (ID: {response.id})")
    return response


if __name__ == "__main__":
    create_tag_example()
