import os

from dify_oapi.api.knowledge.v1.model.delete_tag_request import DeleteTagRequest
from dify_oapi.api.knowledge.v1.model.delete_tag_request_body import DeleteTagRequestBody
from dify_oapi.api.knowledge.v1.model.list_tags_request import ListTagsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_example_tags():
    api_key = os.getenv("KNOWLEDGE_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # List tags to find example ones
    list_req = ListTagsRequest.builder().build()
    list_response = client.knowledge.v1.tag.list(list_req, req_option)

    deleted_count = 0
    for tag in list_response.data or []:
        if tag.name and tag.name.startswith("[Example]"):
            req_body = DeleteTagRequestBody.builder().tag_id(tag.id).build()
            delete_req = DeleteTagRequest.builder().request_body(req_body).build()
            client.knowledge.v1.tag.delete(delete_req, req_option)
            print(f"Deleted tag: {tag.name}")
            deleted_count += 1

    print(f"Deleted {deleted_count} example tags")


async def adelete_example_tags():
    api_key = os.getenv("KNOWLEDGE_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # List tags to find example ones
    list_req = ListTagsRequest.builder().build()
    list_response = await client.knowledge.v1.tag.alist(list_req, req_option)

    deleted_count = 0
    for tag in list_response.data or []:
        if tag.name and tag.name.startswith("[Example]"):
            req_body = DeleteTagRequestBody.builder().tag_id(tag.id).build()
            delete_req = DeleteTagRequest.builder().request_body(req_body).build()
            await client.knowledge.v1.tag.adelete(delete_req, req_option)
            print(f"Deleted tag (async): {tag.name}")
            deleted_count += 1

    print(f"Deleted {deleted_count} example tags (async)")


if __name__ == "__main__":
    delete_example_tags()
