#!/usr/bin/env python3
"""
Child Chunks List Example

This example demonstrates how to list child chunks from a segment using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.segment.list_child_chunks_request import ListChildChunksRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_child_chunks_sync() -> None:
    """List child chunks synchronously."""
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

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

        request = (
            ListChildChunksRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .limit(10)
            .build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.segment.list_child_chunks(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Found {response.total} child chunks (showing {len(response.data or [])})")
        for chunk in response.data or []:
            print(f"  - ID: {chunk.id}, Status: {chunk.status}, Content: {chunk.content[:50]}...")

    except Exception as e:
        print(f"Error listing child chunks: {e}")


async def list_child_chunks_async() -> None:
    """List child chunks asynchronously."""
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

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

        request = (
            ListChildChunksRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .keyword("example")
            .limit(5)
            .build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.segment.alist_child_chunks(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Found {response.total} child chunks with keyword 'example' (async)")
        for chunk in response.data or []:
            print(f"  - ID: {chunk.id}, Status: {chunk.status}, Content: {chunk.content[:50]}...")

    except Exception as e:
        print(f"Error listing child chunks (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Child Chunks List Examples ===\n")

    print("1. Listing child chunks synchronously...")
    list_child_chunks_sync()

    print("\n2. Listing child chunks with filter asynchronously...")
    asyncio.run(list_child_chunks_async())


if __name__ == "__main__":
    main()
