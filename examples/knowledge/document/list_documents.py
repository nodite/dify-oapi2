import os

from dify_oapi.api.knowledge.v1.model.list_documents_request import ListDocumentsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_documents_example():
    api_key = os.getenv("API_KEY")
    dataset_id = os.getenv("DATASET_ID")
    if not api_key or not dataset_id:
        raise ValueError("API_KEY and DATASET_ID environment variables are required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = ListDocumentsRequest.builder().dataset_id(dataset_id).page(1).limit(10).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.document.list(req, req_option)
    print(f"Found {len(response.data or [])} documents")
    for document in response.data or []:
        print(f"- {document.name} (ID: {document.id})")


if __name__ == "__main__":
    list_documents_example()
