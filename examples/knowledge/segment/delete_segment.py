import os

from dify_oapi.api.knowledge.v1.model.delete_segment_request import DeleteSegmentRequest
from dify_oapi.api.knowledge.v1.model.list_segments_request import ListSegmentsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_example_segments():
    api_key = os.getenv("KNOWLEDGE_API_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_API_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        print("Note: DATASET_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real dataset id to execute.")
        print("Set DATASET_ID environment variable with a valid ID to test this functionality.")
        return

    document_id = os.getenv("DOCUMENT_ID")
    if not document_id:
        raise ValueError("DOCUMENT_ID environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # List segments to find example ones
    list_req = ListSegmentsRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
    list_response = client.knowledge.v1.segment.list(list_req, req_option)

    deleted_count = 0
    for segment in list_response.data or []:
        if segment.content and "[Example]" in segment.content:
            delete_req = (
                DeleteSegmentRequest.builder()
                .dataset_id(dataset_id)
                .document_id(document_id)
                .segment_id(segment.id)
                .build()
            )
            client.knowledge.v1.segment.delete(delete_req, req_option)
            print(f"Deleted segment: {segment.content[:50]}...")
            deleted_count += 1

    print(f"Deleted {deleted_count} example segments")


async def adelete_example_segments():
    api_key = os.getenv("KNOWLEDGE_API_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_API_KEY environment variable is required")

    dataset_id = os.getenv("DATASET_ID")
    if not dataset_id:
        print("Note: DATASET_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real dataset id to execute.")
        print("Set DATASET_ID environment variable with a valid ID to test this functionality.")
        return

    document_id = os.getenv("DOCUMENT_ID")
    if not document_id:
        raise ValueError("DOCUMENT_ID environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # List segments to find example ones
    list_req = ListSegmentsRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
    list_response = await client.knowledge.v1.segment.alist(list_req, req_option)

    deleted_count = 0
    for segment in list_response.data or []:
        if segment.content and "[Example]" in segment.content:
            delete_req = (
                DeleteSegmentRequest.builder()
                .dataset_id(dataset_id)
                .document_id(document_id)
                .segment_id(segment.id)
                .build()
            )
            await client.knowledge.v1.segment.adelete(delete_req, req_option)
            print(f"Deleted segment (async): {segment.content[:50]}...")
            deleted_count += 1

    print(f"Deleted {deleted_count} example segments (async)")


if __name__ == "__main__":
    delete_example_segments()
