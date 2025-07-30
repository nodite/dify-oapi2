#!/usr/bin/env python3
"""
Document List Example

This example demonstrates how to list documents in a dataset.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.document.list_request import ListRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_documents_sync() -> None:
    """List documents synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = ListRequest.builder().dataset_id(dataset_id).keyword("[Example]").page("1").limit("10").build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.document.list(request, request_option)

        print(f"Found {response.total} documents (page {response.page}/{response.limit})")
        if response.data:
            for doc in response.data:
                print(f"- {doc.name} (ID: {doc.id}, Status: {doc.indexing_status})")
        else:
            print("No documents found")

    except Exception as e:
        print(f"Error listing documents: {e}")


async def list_documents_async() -> None:
    """List documents asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = ListRequest.builder().dataset_id(dataset_id).keyword("[Example]").page("1").limit("5").build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.document.alist(request, request_option)

        print(f"Found {response.total} documents (async, page {response.page}/{response.limit})")
        if response.data:
            for doc in response.data:
                print(f"- {doc.name} (ID: {doc.id}, Status: {doc.indexing_status})")
        else:
            print("No documents found")

    except Exception as e:
        print(f"Error listing documents (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Document List Examples ===\n")

    print("1. Listing documents synchronously...")
    list_documents_sync()

    print("\n2. Listing documents asynchronously...")
    asyncio.run(list_documents_async())


if __name__ == "__main__":
    main()
