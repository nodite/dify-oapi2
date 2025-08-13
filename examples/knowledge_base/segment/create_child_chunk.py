#!/usr/bin/env python3
"""
Child Chunk Creation Example

This example demonstrates how to create child chunks for a segment using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.segment.create_child_chunk_request import CreateChildChunkRequest
from dify_oapi.api.knowledge_base.v1.model.segment.create_child_chunk_request_body import CreateChildChunkRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_child_chunk_sync() -> None:
    """Create child chunk synchronously."""
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

        request_body = (
            CreateChildChunkRequestBody.builder()
            .content("[Example] This is a test child chunk content for demonstration.")
            .build()
        )

        request = (
            CreateChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .request_body(request_body)
            .build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.segment.create_child_chunk(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        child_chunk = response.data
        if child_chunk:
            print("Child chunk created successfully:")
            print(f"  ID: {child_chunk.id}")
            print(f"  Segment ID: {child_chunk.segment_id}")
            print(f"  Status: {child_chunk.status}")
            print(f"  Content: {child_chunk.content}")

    except Exception as e:
        print(f"Error creating child chunk: {e}")


async def create_child_chunk_async() -> None:
    """Create child chunk asynchronously."""
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

        request_body = (
            CreateChildChunkRequestBody.builder()
            .content("[Example] This is an async test child chunk content.")
            .build()
        )

        request = (
            CreateChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .request_body(request_body)
            .build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.segment.acreate_child_chunk(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        child_chunk = response.data
        if child_chunk:
            print("Child chunk created successfully (async):")
            print(f"  ID: {child_chunk.id}")
            print(f"  Segment ID: {child_chunk.segment_id}")
            print(f"  Content: {child_chunk.content}")

    except Exception as e:
        print(f"Error creating child chunk (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Child Chunk Creation Examples ===\n")

    print("1. Creating child chunk synchronously...")
    create_child_chunk_sync()

    print("\n2. Creating child chunk asynchronously...")
    asyncio.run(create_child_chunk_async())


if __name__ == "__main__":
    main()
