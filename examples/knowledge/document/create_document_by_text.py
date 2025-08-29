import os

from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import CreateDocumentByTextRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_document_by_text_example():
    api_key = os.getenv("API_KEY")
    dataset_id = os.getenv("DATASET_ID")
    if not api_key or not dataset_id:
        raise ValueError("API_KEY and DATASET_ID environment variables are required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = (
        CreateDocumentByTextRequestBody.builder()
        .name("[Example] Product Manual")
        .text("This is an example product manual content for testing purposes.")
        .indexing_technique("high_quality")
        .build()
    )

    req = CreateDocumentByTextRequest.builder().dataset_id(dataset_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.document.create_by_text(req, req_option)
    print(f"Document created: {response.document.name} (ID: {response.document.id})")
    return response


if __name__ == "__main__":
    create_document_by_text_example()
