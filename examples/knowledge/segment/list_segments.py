import os

from dify_oapi.api.knowledge.v1.model.list_segments_request import ListSegmentsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_segments_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        raise ValueError("DATASET_ID environment variable is required")

    document_id = os.getenv("DOCUMENT_ID")
    if not document_id:
        raise ValueError("DOCUMENT_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req = ListSegmentsRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.segment.list(req, req_option)
    print(f"Found {len(response.data)} segments")
    for segment in response.data:
        print(f"- Segment {segment.id}: {segment.content[:50]}...")
    return response


async def alist_segments_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        raise ValueError("DATASET_ID environment variable is required")

    document_id = os.getenv("DOCUMENT_ID")
    if not document_id:
        raise ValueError("DOCUMENT_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req = ListSegmentsRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.segment.alist(req, req_option)
    print(f"Found {len(response.data)} segments (async)")
    return response


if __name__ == "__main__":
    list_segments_example()
