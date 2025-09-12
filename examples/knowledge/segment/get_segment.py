import os

from dify_oapi.api.knowledge.v1.model.get_segment_request import GetSegmentRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_segment_example():
    api_key = os.getenv("KNOWLEDGE_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        print("Note: DATASET_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real dataset id to execute.")
        print("Set DATASET_ID environment variable with a valid ID to test this functionality.")
        return

    document_id = os.getenv("DOCUMENT_ID")
    if not document_id:
        raise ValueError("DOCUMENT_ID environment variable is required")

    segment_id = os.getenv("SEGMENT_ID")
    if not segment_id:
        raise ValueError("SEGMENT_ID environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetSegmentRequest.builder().dataset_id(dataset_id).document_id(document_id).segment_id(segment_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.segment.get(req, req_option)
    if response.success and response.data:
        segment = response.data
        content_preview = segment.content[:100] if segment.content and len(segment.content) > 100 else segment.content
        print(f"Segment: {content_preview}... (ID: {segment.id})")
    else:
        print(f"Error getting segment: {response.code} - {response.msg}")
    return response


async def aget_segment_example():
    api_key = os.getenv("KNOWLEDGE_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        print("Note: DATASET_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real dataset id to execute.")
        print("Set DATASET_ID environment variable with a valid ID to test this functionality.")
        return

    document_id = os.getenv("DOCUMENT_ID")
    if not document_id:
        raise ValueError("DOCUMENT_ID environment variable is required")

    segment_id = os.getenv("SEGMENT_ID")
    if not segment_id:
        raise ValueError("SEGMENT_ID environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetSegmentRequest.builder().dataset_id(dataset_id).document_id(document_id).segment_id(segment_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.segment.aget(req, req_option)
    if response.success and response.data:
        segment = response.data
        content_preview = segment.content[:100] if segment.content and len(segment.content) > 100 else segment.content
        print(f"Segment (async): {content_preview}... (ID: {segment.id})")
    else:
        print(f"Error getting segment (async): {response.code} - {response.msg}")
    return response


if __name__ == "__main__":
    get_segment_example()
