#!/usr/bin/env python3
"""
Segment Creation Example

This example demonstrates how to create new segments in a document using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.segment.create_request import CreateRequest
from dify_oapi.api.knowledge_base.v1.model.segment.create_request_body import CreateRequestBody
from dify_oapi.api.knowledge_base.v1.model.segment.segment_info import SegmentInfo
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_segment_sync() -> None:
    """Create segments synchronously."""
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

        # Create segment info
        segment = (
            SegmentInfo.builder()
            .content("[Example] This is a test segment content for demonstration purposes.")
            .keywords(["example", "test", "segment"])
            .build()
        )

        request_body = CreateRequestBody.builder().segments([segment]).build()

        request = (
            CreateRequest.builder().dataset_id(dataset_id).document_id(document_id).request_body(request_body).build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.segment.create(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Created {len(response.data or [])} segment(s)")
        for segment in response.data or []:
            print(f"  - Segment ID: {segment.id}, Content: {segment.content[:50]}...")

    except Exception as e:
        print(f"Error creating segment: {e}")


async def create_segment_async() -> None:
    """Create segments asynchronously."""
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

        # Create segment info
        segment = (
            SegmentInfo.builder()
            .content("[Example] This is an async test segment content.")
            .keywords(["example", "async", "segment"])
            .build()
        )

        request_body = CreateRequestBody.builder().segments([segment]).build()

        request = (
            CreateRequest.builder().dataset_id(dataset_id).document_id(document_id).request_body(request_body).build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.segment.acreate(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Created {len(response.data or [])} segment(s) (async)")
        for segment in response.data or []:
            print(f"  - Segment ID: {segment.id}, Content: {segment.content[:50]}...")

    except Exception as e:
        print(f"Error creating segment (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Segment Creation Examples ===\n")

    print("1. Creating segments synchronously...")
    create_segment_sync()

    print("\n2. Creating segments asynchronously...")
    asyncio.run(create_segment_async())


if __name__ == "__main__":
    main()
