#!/usr/bin/env python3
"""
Segment Delete Example

This example demonstrates how to delete a segment using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.segment.delete_request import DeleteRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_segment_sync() -> None:
    """Delete segment synchronously."""
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

        # Safety check: only delete segments with [Example] prefix
        if not segment_id.startswith("[Example]"):
            print("Safety check: Only segments with '[Example]' prefix can be deleted")
            return

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = DeleteRequest.builder().dataset_id(dataset_id).document_id(document_id).segment_id(segment_id).build()

        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.segment.delete(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Segment {segment_id} deleted successfully")

    except Exception as e:
        print(f"Error deleting segment: {e}")


async def delete_segment_async() -> None:
    """Delete segment asynchronously."""
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

        # Safety check: only delete segments with [Example] prefix
        if not segment_id.startswith("[Example]"):
            print("Safety check: Only segments with '[Example]' prefix can be deleted")
            return

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = DeleteRequest.builder().dataset_id(dataset_id).document_id(document_id).segment_id(segment_id).build()

        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.segment.adelete(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Segment {segment_id} deleted successfully (async)")

    except Exception as e:
        print(f"Error deleting segment (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Segment Delete Examples ===\n")

    print("1. Deleting segment synchronously...")
    delete_segment_sync()

    print("\n2. Deleting segment asynchronously...")
    asyncio.run(delete_segment_async())


if __name__ == "__main__":
    main()
