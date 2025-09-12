import os

from dify_oapi.api.knowledge.v1.model.delete_document_request import DeleteDocumentRequest
from dify_oapi.api.knowledge.v1.model.list_documents_request import ListDocumentsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_example_documents():
    api_key = os.getenv("KNOWLEDGE_KEY")
    dataset_id = os.getenv("DATASET_ID")
    if not api_key or not dataset_id:
        print("Note: KNOWLEDGE_KEY and DATASET_ID environment variables are required for this example.")
        print("This example demonstrates the API structure but needs real IDs to execute.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # List documents to find example ones
    list_req = ListDocumentsRequest.builder().dataset_id(dataset_id).build()
    list_response = client.knowledge.v1.document.list(list_req, req_option)

    deleted_count = 0
    for document in list_response.data or []:
        if document.name and document.name.startswith("[Example]"):
            delete_req = DeleteDocumentRequest.builder().dataset_id(dataset_id).document_id(document.id).build()
            client.knowledge.v1.document.delete(delete_req, req_option)
            print(f"Deleted document: {document.name}")
            deleted_count += 1

    print(f"Deleted {deleted_count} example documents")


if __name__ == "__main__":
    delete_example_documents()
