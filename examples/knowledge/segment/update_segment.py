import asyncio
import os

from dify_oapi.api.knowledge.v1.model.segment_content import SegmentContent
from dify_oapi.api.knowledge.v1.model.update_segment_request import UpdateSegmentRequest
from dify_oapi.api.knowledge.v1.model.update_segment_request_body import UpdateSegmentRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_segment_example():
    api_key = os.getenv("KNOWLEDGE_API_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_API_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        raise ValueError("DATASET_ID environment variable is required")

    document_id = os.getenv("DOCUMENT_ID")
    if not document_id:
        raise ValueError("DOCUMENT_ID environment variable is required")

    segment_id = os.getenv("SEGMENT_ID")
    if not segment_id:
        raise ValueError("SEGMENT_ID environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    segment_content = (
        SegmentContent.builder()
        .content("[Example] Updated segment content for testing purposes")
        .keywords(["example", "updated", "testing"])
        .build()
    )

    req_body = UpdateSegmentRequestBody.builder().segment(segment_content).build()

    req = (
        UpdateSegmentRequest.builder()
        .dataset_id(dataset_id)
        .document_id(document_id)
        .segment_id(segment_id)
        .request_body(req_body)
        .build()
    )
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.segment.update(req, req_option)

    if not response.success:
        print(f"API Error: {response.code} - {response.msg}")
        return response

    if response.data:
        content_preview = response.data.content[:100] if response.data.content else "No content"
        segment_id = response.data.id if response.data.id else "No ID"
        print(f"Segment updated: {content_preview}... (ID: {segment_id})")
    else:
        print("Segment updated but no data returned")
    return response


async def aupdate_segment_example():
    api_key = os.getenv("KNOWLEDGE_API_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_API_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        raise ValueError("DATASET_ID environment variable is required")

    document_id = os.getenv("DOCUMENT_ID")
    if not document_id:
        raise ValueError("DOCUMENT_ID environment variable is required")

    segment_id = os.getenv("SEGMENT_ID")
    if not segment_id:
        raise ValueError("SEGMENT_ID environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    segment_content = (
        SegmentContent.builder()
        .content("[Example] Updated segment content for async testing")
        .keywords(["example", "async", "updated"])
        .build()
    )

    req_body = UpdateSegmentRequestBody.builder().segment(segment_content).build()

    req = (
        UpdateSegmentRequest.builder()
        .dataset_id(dataset_id)
        .document_id(document_id)
        .segment_id(segment_id)
        .request_body(req_body)
        .build()
    )
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.segment.aupdate(req, req_option)

    if not response.success:
        print(f"API Error (async): {response.code} - {response.msg}")
        return response

    if response.data:
        content_preview = response.data.content[:100] if response.data.content else "No content"
        segment_id = response.data.id if response.data.id else "No ID"
        print(f"Segment updated (async): {content_preview}... (ID: {segment_id})")
    else:
        print("Segment updated (async) but no data returned")
    return response


def main():
    """Main function to run examples."""
    print("=== Segment Update Examples ===\n")

    print("1. Updating segment synchronously...")
    try:
        update_segment_example()
    except Exception as e:
        print(f"Error updating segment: {e}")

    print("\n2. Updating segment asynchronously...")
    try:
        asyncio.run(aupdate_segment_example())
    except Exception as e:
        print(f"Error updating segment asynchronously: {e}")


if __name__ == "__main__":
    main()
