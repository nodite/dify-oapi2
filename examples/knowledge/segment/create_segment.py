import os

from dify_oapi.api.knowledge.v1.model.create_segment_request import CreateSegmentRequest
from dify_oapi.api.knowledge.v1.model.create_segment_request_body import CreateSegmentRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_segment_example():
    api_key = os.getenv("API_KEY")
    dataset_id = os.getenv("DATASET_ID")
    document_id = os.getenv("DOCUMENT_ID")
    if not api_key or not dataset_id or not document_id:
        raise ValueError("API_KEY, DATASET_ID, and DOCUMENT_ID environment variables are required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = (
        CreateSegmentRequestBody.builder()
        .content("[Example] This is a sample segment content for testing.")
        .answer("This is an example answer for the segment.")
        .keywords(["example", "test", "segment"])
        .build()
    )

    req = CreateSegmentRequest.builder().dataset_id(dataset_id).document_id(document_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.segment.create(req, req_option)
    print(f"Segment created: ID {response.id}")
    return response


if __name__ == "__main__":
    create_segment_example()
