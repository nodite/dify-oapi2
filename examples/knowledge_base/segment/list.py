#!/usr/bin/env python3
"""
Segment List Example

This example demonstrates how to list segments from a document using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.segment.list_request import ListRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_segments_sync() -> None:
    """List segments synchronously."""
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

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = ListRequest.builder().dataset_id(dataset_id).document_id(document_id).limit(10).build()

        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.segment.list(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Found {response.total} segments (showing {len(response.data or [])})")
        for segment in response.data or []:
            print(f"  - ID: {segment.id}, Status: {segment.status}, Content: {segment.content[:50]}...")

    except Exception as e:
        print(f"Error listing segments: {e}")


async def list_segments_async() -> None:
    """List segments asynchronously."""
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

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = (
            ListRequest.builder().dataset_id(dataset_id).document_id(document_id).keyword("[Example]").limit(5).build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.segment.alist(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Found {response.total} segments with keyword '[Example]' (async)")
        for segment in response.data or []:
            print(f"  - ID: {segment.id}, Status: {segment.status}, Content: {segment.content[:50]}...")

    except Exception as e:
        print(f"Error listing segments (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Segment List Examples ===\n")

    print("1. Listing segments synchronously...")
    list_segments_sync()

    print("\n2. Listing segments with filter asynchronously...")
    asyncio.run(list_segments_async())


if __name__ == "__main__":
    main()
