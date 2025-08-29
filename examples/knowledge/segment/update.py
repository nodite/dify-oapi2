#!/usr/bin/env python3
"""
Segment Update Example

This example demonstrates how to update a segment using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.segment.segment_data import SegmentData
from dify_oapi.api.knowledge.v1.model.segment.update_request import UpdateRequest
from dify_oapi.api.knowledge.v1.model.segment.update_request_body import UpdateRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_segment_sync() -> None:
    """Update segment synchronously."""
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

        # Create segment data for update
        segment_data = (
            SegmentData.builder()
            .content("[Example] Updated segment content with new information.")
            .keywords(["example", "updated", "segment"])
            .enabled(True)
            .build()
        )

        request_body = UpdateRequestBody.builder().segment(segment_data).build()

        request = (
            UpdateRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .request_body(request_body)
            .build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.segment.update(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        segment = response.data
        if segment:
            print("Segment updated successfully:")
            print(f"  ID: {segment.id}")
            print(f"  Status: {segment.status}")
            print(f"  Content: {segment.content}")

    except Exception as e:
        print(f"Error updating segment: {e}")


async def update_segment_async() -> None:
    """Update segment asynchronously."""
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

        # Create segment data for async update
        segment_data = (
            SegmentData.builder()
            .content("[Example] Async updated segment content.")
            .keywords(["example", "async", "updated"])
            .enabled(True)
            .build()
        )

        request_body = UpdateRequestBody.builder().segment(segment_data).build()

        request = (
            UpdateRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .request_body(request_body)
            .build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.segment.aupdate(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        segment = response.data
        if segment:
            print("Segment updated successfully (async):")
            print(f"  ID: {segment.id}")
            print(f"  Status: {segment.status}")
            print(f"  Content: {segment.content}")

    except Exception as e:
        print(f"Error updating segment (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Segment Update Examples ===\n")

    print("1. Updating segment synchronously...")
    update_segment_sync()

    print("\n2. Updating segment asynchronously...")
    asyncio.run(update_segment_async())


if __name__ == "__main__":
    main()
