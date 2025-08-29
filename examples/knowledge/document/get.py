#!/usr/bin/env python3
"""
Document Get Example

This example demonstrates how to get document details.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.document.get_request import GetRequest
from dify_oapi.api.knowledge.v1.model.document.list_request import ListRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_document_sync() -> None:
    """Get document details synchronously."""
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
        list_response = client.knowledge.v1.document.list(list_request, request_option)

        if not list_response.success:
            print(f"API Error: {list_response.code} - {list_response.msg}")
            return

        if not list_response.data or len(list_response.data) == 0:
            print("No [Example] documents found. Please create one first.")
            return

        document_id = list_response.data[0].id
        if not document_id:
            print("Document ID is None")
            return
        print(f"Getting details for document: {list_response.data[0].name}")

        request = GetRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
        response = client.knowledge.v1.document.get(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Document: {response.name}")
        print(f"ID: {response.id}")
        print(f"Status: {response.indexing_status}")
        print(f"Tokens: {response.tokens}")
        print(f"Word Count: {response.word_count}")
        print(f"Created: {response.created_at}")

    except Exception as e:
        print(f"Error getting document: {e}")


async def get_document_async() -> None:
    """Get document details asynchronously."""
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
        list_response = await client.knowledge.v1.document.alist(list_request, request_option)

        if not list_response.success:
            print(f"API Error (async): {list_response.code} - {list_response.msg}")
            return

        if not list_response.data or len(list_response.data) == 0:
            print("No [Example] documents found. Please create one first.")
            return

        document_id = list_response.data[0].id
        if not document_id:
            print("Document ID is None")
            return
        print(f"Getting details for document (async): {list_response.data[0].name}")

        request = GetRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
        response = await client.knowledge.v1.document.aget(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Document: {response.name}")
        print(f"ID: {response.id}")
        print(f"Status: {response.indexing_status}")
        print(f"Tokens: {response.tokens}")
        print(f"Word Count: {response.word_count}")
        print(f"Created: {response.created_at}")

    except Exception as e:
        print(f"Error getting document (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Document Get Examples ===\n")

    print("1. Getting document details synchronously...")
    get_document_sync()

    print("\n2. Getting document details asynchronously...")
    asyncio.run(get_document_async())


if __name__ == "__main__":
    main()
