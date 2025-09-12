#!/usr/bin/env python3
"""
Child Chunk Update Example

This example demonstrates how to update a child chunk using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.update_child_chunk_request import UpdateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.update_child_chunk_request_body import UpdateChildChunkRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_child_chunk_sync() -> None:
    """Update child chunk synchronously."""
    try:
        # Check required environment variables
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        document_id = os.getenv("DOCUMENT_ID")
        if not document_id:
            raise ValueError("DOCUMENT_ID environment variable is required")

        segment_id = os.getenv("SEGMENT_ID")
        if not segment_id:
            raise ValueError("SEGMENT_ID environment variable is required")

        child_chunk_id = os.getenv("CHILD_CHUNK_ID")
        if not child_chunk_id:
            raise ValueError("CHILD_CHUNK_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = (
            UpdateChildChunkRequestBody.builder()
            .content("[Example] Updated child chunk content with new information.")
            .build()
        )

        request = (
            UpdateChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .child_chunk_id(child_chunk_id)
            .request_body(request_body)
            .build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.chunk.update(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        child_chunk = response.data
        if child_chunk:
            print("Child chunk updated successfully:")
            print(f"  ID: {child_chunk.id}")
            print(f"  Segment ID: {child_chunk.segment_id}")
            print(f"  Content: {child_chunk.content}")
            print(f"  Position: {child_chunk.position}")

    except Exception as e:
        print(f"Error updating child chunk: {e}")


async def update_child_chunk_async() -> None:
    """Update child chunk asynchronously."""
    try:
        # Check required environment variables
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        document_id = os.getenv("DOCUMENT_ID")
        if not document_id:
            raise ValueError("DOCUMENT_ID environment variable is required")

        segment_id = os.getenv("SEGMENT_ID")
        if not segment_id:
            raise ValueError("SEGMENT_ID environment variable is required")

        child_chunk_id = os.getenv("CHILD_CHUNK_ID")
        if not child_chunk_id:
            raise ValueError("CHILD_CHUNK_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = (
            UpdateChildChunkRequestBody.builder().content("[Example] Async updated child chunk content.").build()
        )

        request = (
            UpdateChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .child_chunk_id(child_chunk_id)
            .request_body(request_body)
            .build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.chunk.aupdate(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        child_chunk = response.data
        if child_chunk:
            print("Child chunk updated successfully (async):")
            print(f"  ID: {child_chunk.id}")
            print(f"  Segment ID: {child_chunk.segment_id}")
            print(f"  Content: {child_chunk.content}")
            print(f"  Position: {child_chunk.position}")

    except Exception as e:
        print(f"Error updating child chunk (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Child Chunk Update Examples ===\n")

    print("1. Updating child chunk synchronously...")
    update_child_chunk_sync()

    print("\n2. Updating child chunk asynchronously...")
    asyncio.run(update_child_chunk_async())


if __name__ == "__main__":
    main()
