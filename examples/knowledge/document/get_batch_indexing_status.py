#!/usr/bin/env python3
"""
Document Indexing Status Example

This example demonstrates how to check the indexing status of a document batch.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.document.indexing_status_request import IndexingStatusRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def check_indexing_status_sync() -> None:
    """Check document indexing status synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        batch_id = os.getenv("BATCH_ID")
        if not batch_id:
            raise ValueError("BATCH_ID environment variable is required for checking indexing status")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = IndexingStatusRequest.builder().dataset_id(dataset_id).batch(batch_id).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.document.indexing_status(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Indexing Status for Batch: {batch_id}")
        if response.data:
            for idx, status_info in enumerate(response.data, 1):
                print(f"\nDocument {idx}:")
                print(f"  ID: {status_info.id}")
                print(f"  Status: {status_info.indexing_status}")

                if status_info.processing_started_at:
                    print(f"  Processing Started: {status_info.processing_started_at}")

                if status_info.parsing_completed_at:
                    print(f"  Parsing Completed: {status_info.parsing_completed_at}")

                if status_info.cleaning_completed_at:
                    print(f"  Cleaning Completed: {status_info.cleaning_completed_at}")

                if status_info.splitting_completed_at:
                    print(f"  Splitting Completed: {status_info.splitting_completed_at}")

                if status_info.completed_at:
                    print(f"  Indexing Completed: {status_info.completed_at}")

                if status_info.error:
                    print(f"  Error: {status_info.error}")

                if status_info.completed_segments is not None and status_info.total_segments is not None:
                    progress = (
                        (status_info.completed_segments / status_info.total_segments * 100)
                        if status_info.total_segments > 0
                        else 0
                    )
                    print(
                        f"  Progress: {status_info.completed_segments}/{status_info.total_segments} segments ({progress:.1f}%)"
                    )
        else:
            print("No indexing status information available")

    except Exception as e:
        print(f"Error checking indexing status: {e}")


async def check_indexing_status_async() -> None:
    """Check document indexing status asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        batch_id = os.getenv("BATCH_ID")
        if not batch_id:
            raise ValueError("BATCH_ID environment variable is required for checking indexing status")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = IndexingStatusRequest.builder().dataset_id(dataset_id).batch(batch_id).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.document.aindexing_status(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"\nAsync Indexing Status for Batch: {batch_id}")
        if response.data:
            for idx, status_info in enumerate(response.data, 1):
                print(f"\nDocument {idx} (Async):")
                print(f"  ID: {status_info.id}")
                print(f"  Status: {status_info.indexing_status}")

                if status_info.completed_segments is not None and status_info.total_segments is not None:
                    progress = (
                        (status_info.completed_segments / status_info.total_segments * 100)
                        if status_info.total_segments > 0
                        else 0
                    )
                    print(
                        f"  Progress: {status_info.completed_segments}/{status_info.total_segments} segments ({progress:.1f}%)"
                    )
        else:
            print("No indexing status information available (async)")

    except Exception as e:
        print(f"Error checking indexing status asynchronously: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Document Indexing Status Examples ===\n")
    print("Note: This example requires a batch ID set in the BATCH_ID environment variable.\n")

    print("1. Checking indexing status synchronously...")
    check_indexing_status_sync()

    print("\n2. Checking indexing status asynchronously...")
    asyncio.run(check_indexing_status_async())


if __name__ == "__main__":
    main()
