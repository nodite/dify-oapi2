#!/usr/bin/env python3
"""
Child Chunk Delete Example

This example demonstrates how to delete a child chunk using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.delete_child_chunk_request import DeleteChildChunkRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_child_chunk_sync() -> None:
    """Delete child chunk synchronously."""
    try:
        # Check required environment variables
        api_key = os.getenv("KNOWLEDGE_API_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_API_KEY environment variable is required")

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
        request_option = RequestOption.builder().api_key(api_key).build()

        # First, get the child chunk to check its content for safety
        from dify_oapi.api.knowledge.v1.model.list_child_chunks_request import ListChildChunksRequest

        list_request = (
            ListChildChunksRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .build()
        )

        list_response = client.knowledge.v1.chunk.list(list_request, request_option)

        # Find the specific child chunk and check if it contains [Example]
        target_chunk = None
        if list_response.data:
            for chunk in list_response.data:
                if chunk.id == child_chunk_id:
                    target_chunk = chunk
                    break

        if not target_chunk:
            print(f"Child chunk {child_chunk_id} not found")
            return

        if not target_chunk.content or "[Example]" not in target_chunk.content:
            print("Safety check: Only child chunks with '[Example]' in content can be deleted")
            return

        request = (
            DeleteChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .child_chunk_id(child_chunk_id)
            .build()
        )

        response = client.knowledge.v1.chunk.delete(request, request_option)

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
        api_key = os.getenv("KNOWLEDGE_API_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_API_KEY environment variable is required")

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
        request_option = RequestOption.builder().api_key(api_key).build()

        # First, get the child chunk to check its content for safety
        from dify_oapi.api.knowledge.v1.model.list_child_chunks_request import ListChildChunksRequest

        list_request = (
            ListChildChunksRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .build()
        )

        list_response = await client.knowledge.v1.chunk.alist(list_request, request_option)

        # Find the specific child chunk and check if it contains [Example]
        target_chunk = None
        if list_response.data:
            for chunk in list_response.data:
                if chunk.id == child_chunk_id:
                    target_chunk = chunk
                    break

        if not target_chunk:
            print(f"Child chunk {child_chunk_id} not found (async)")
            return

        if not target_chunk.content or "[Example]" not in target_chunk.content:
            print("Safety check: Only child chunks with '[Example]' in content can be deleted (async)")
            return

        request = (
            DeleteChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .child_chunk_id(child_chunk_id)
            .build()
        )

        response = await client.knowledge.v1.chunk.adelete(request, request_option)

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
