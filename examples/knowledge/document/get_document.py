import os

from dify_oapi.api.knowledge.v1.model.get_document_request import GetDocumentRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_document_example():
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

    req = GetDocumentRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = client.knowledge.v1.document.get(req, req_option)
    print(f"Document: {response.name} (ID: {response.id})")
    print(f"Status: {response.indexing_status}, Tokens: {response.tokens}")
    return response


async def aget_document_example():
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

    req = GetDocumentRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    response = await client.knowledge.v1.document.aget(req, req_option)
    print(f"Document (async): {response.name} (ID: {response.id})")
    print(f"Status: {response.indexing_status}, Tokens: {response.tokens}")
    return response


if __name__ == "__main__":
    get_document_example()
