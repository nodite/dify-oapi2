import os

from dify_oapi.api.knowledge.v1.model.get_segment_request import GetSegmentRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_segment_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        raise ValueError("DATASET_ID environment variable is required")

    document_id = os.getenv("DOCUMENT_ID")
    if not document_id:
        raise ValueError("DOCUMENT_ID environment variable is required")

    segment_id = os.getenv("SEGMENT_ID")
    if not segment_id:
        raise ValueError("SEGMENT_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req = GetSegmentRequest.builder().dataset_id(dataset_id).document_id(document_id).segment_id(segment_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.segment.get(req, req_option)
    print(f"Segment: {response.content[:100]}... (ID: {response.id})")
    return response


async def aget_segment_example():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        raise ValueError("DATASET_ID environment variable is required")

    document_id = os.getenv("DOCUMENT_ID")
    if not document_id:
        raise ValueError("DOCUMENT_ID environment variable is required")

    segment_id = os.getenv("SEGMENT_ID")
    if not segment_id:
        raise ValueError("SEGMENT_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req = GetSegmentRequest.builder().dataset_id(dataset_id).document_id(document_id).segment_id(segment_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.segment.aget(req, req_option)
    print(f"Segment (async): {response.content[:100]}... (ID: {response.id})")
    return response


if __name__ == "__main__":
    get_segment_example()
