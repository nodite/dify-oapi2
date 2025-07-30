#!/usr/bin/env python3
"""
Document Delete Example

This example demonstrates how to delete documents.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.document.delete_request import DeleteRequest
from dify_oapi.api.knowledge_base.v1.model.document.list_request import ListRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_document_sync() -> None:
    """Delete a document synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        # First, get a document ID from the list
        list_request = ListRequest.builder().dataset_id(dataset_id).keyword("[Example]").limit("1").build()
        list_response = client.knowledge_base.v1.document.list(list_request, request_option)

        if not list_response.data or len(list_response.data) == 0:
            print("No [Example] documents found to delete.")
            return

        document_id = list_response.data[0].id
        document_name = list_response.data[0].name

        # Verify it's an example document before deleting
        if not document_name or not document_name.startswith("[Example]"):
            print(f"Skipping deletion of non-example document: {document_name}")
            return

        print(f"Deleting document: {document_name}")

        request = DeleteRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
        client.knowledge_base.v1.document.delete(request, request_option)

        print(f"Document deleted successfully: {document_name}")

    except Exception as e:
        print(f"Error deleting document: {e}")


async def delete_document_async() -> None:
    """Delete a document asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        # First, get a document ID from the list
        list_request = ListRequest.builder().dataset_id(dataset_id).keyword("[Example]").limit("1").build()
        list_response = await client.knowledge_base.v1.document.alist(list_request, request_option)

        if not list_response.data or len(list_response.data) == 0:
            print("No [Example] documents found to delete.")
            return

        document_id = list_response.data[0].id
        document_name = list_response.data[0].name

        # Verify it's an example document before deleting
        if not document_name or not document_name.startswith("[Example]"):
            print(f"Skipping deletion of non-example document: {document_name}")
            return

        print(f"Deleting document (async): {document_name}")

        request = DeleteRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
        await client.knowledge_base.v1.document.adelete(request, request_option)

        print(f"Document deleted successfully (async): {document_name}")

    except Exception as e:
        print(f"Error deleting document (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Document Delete Examples ===\n")

    print("1. Deleting document synchronously...")
    delete_document_sync()

    print("\n2. Deleting document asynchronously...")
    asyncio.run(delete_document_async())


if __name__ == "__main__":
    main()
