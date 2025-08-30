#!/usr/bin/env python3
"""
Child Chunk Delete Example

This example demonstrates how to delete a child chunk using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.segment.delete_child_chunk_request import DeleteChildChunkRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_child_chunk_sync() -> None:
    """Delete child chunk synchronously."""
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

        child_chunk_id = os.getenv("CHILD_CHUNK_ID")
        if not child_chunk_id:
            raise ValueError("CHILD_CHUNK_ID environment variable is required")

        # Safety check: only delete child chunks with [Example] prefix
        if not child_chunk_id.startswith("[Example]"):
            print("Safety check: Only child chunks with '[Example]' prefix can be deleted")
            return

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = (
            DeleteChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .child_chunk_id(child_chunk_id)
            .build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.segment.delete_child_chunk(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Child chunk {child_chunk_id} deleted successfully")

    except Exception as e:
        print(f"Error deleting child chunk: {e}")


async def delete_child_chunk_async() -> None:
    """Delete child chunk asynchronously."""
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

        child_chunk_id = os.getenv("CHILD_CHUNK_ID")
        if not child_chunk_id:
            raise ValueError("CHILD_CHUNK_ID environment variable is required")

        # Safety check: only delete child chunks with [Example] prefix
        if not child_chunk_id.startswith("[Example]"):
            print("Safety check: Only child chunks with '[Example]' prefix can be deleted")
            return

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = (
            DeleteChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .child_chunk_id(child_chunk_id)
            .build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.segment.adelete_child_chunk(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Child chunk {child_chunk_id} deleted successfully (async)")

    except Exception as e:
        print(f"Error deleting child chunk (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Child Chunk Delete Examples ===\n")

    print("1. Deleting child chunk synchronously...")
    delete_child_chunk_sync()

    print("\n2. Deleting child chunk asynchronously...")
    asyncio.run(delete_child_chunk_async())


if __name__ == "__main__":
    main()
