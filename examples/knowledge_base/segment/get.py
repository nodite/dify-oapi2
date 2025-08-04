#!/usr/bin/env python3
"""
Segment Get Example

This example demonstrates how to get detailed information about a specific segment using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.segment.get_request import GetRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_segment_sync() -> None:
    """Get segment details synchronously."""
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

        request = GetRequest.builder().dataset_id(dataset_id).document_id(document_id).segment_id(segment_id).build()

        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.segment.get(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        segment = response.data
        if segment:
            print("Segment Details:")
            print(f"  ID: {segment.id}")
            print(f"  Position: {segment.position}")
            print(f"  Status: {segment.status}")
            print(f"  Word Count: {segment.word_count}")
            print(f"  Tokens: {segment.tokens}")
            print(f"  Enabled: {segment.enabled}")
            print(f"  Keywords: {segment.keywords}")
            print(f"  Content: {segment.content}")

    except Exception as e:
        print(f"Error getting segment: {e}")


async def get_segment_async() -> None:
    """Get segment details asynchronously."""
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

        request = GetRequest.builder().dataset_id(dataset_id).document_id(document_id).segment_id(segment_id).build()

        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.segment.aget(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        segment = response.data
        if segment:
            print("Segment Details (async):")
            print(f"  ID: {segment.id}")
            print(f"  Position: {segment.position}")
            print(f"  Status: {segment.status}")
            print(f"  Content: {segment.content}")

    except Exception as e:
        print(f"Error getting segment (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Segment Get Examples ===\n")

    print("1. Getting segment details synchronously...")
    get_segment_sync()

    print("\n2. Getting segment details asynchronously...")
    asyncio.run(get_segment_async())


if __name__ == "__main__":
    main()
