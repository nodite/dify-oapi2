#!/usr/bin/env python3
"""
Metadata Update Example

This example demonstrates how to update metadata configuration using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.metadata.update_request import UpdateRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.update_request_body import UpdateRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_metadata_sync() -> None:
    """Update metadata synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        metadata_id = os.getenv("METADATA_ID")
        if not metadata_id:
            raise ValueError("METADATA_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = UpdateRequestBody.builder().name("[Example] updated_category").build()
        request = (
            UpdateRequest.builder().dataset_id(dataset_id).metadata_id(metadata_id).request_body(request_body).build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()
        response = client.knowledge_base.v1.metadata.update(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Metadata updated: {response.name} ({response.type})")

    except Exception as e:
        print(f"Error updating metadata: {e}")


async def update_metadata_async() -> None:
    """Update metadata asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        metadata_id = os.getenv("METADATA_ID")
        if not metadata_id:
            raise ValueError("METADATA_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = UpdateRequestBody.builder().name("[Example] async_updated_field").build()
        request = (
            UpdateRequest.builder().dataset_id(dataset_id).metadata_id(metadata_id).request_body(request_body).build()
        )

        request_option = RequestOption.builder().api_key(api_key).build()
        response = await client.knowledge_base.v1.metadata.aupdate(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Metadata updated (async): {response.name}")

    except Exception as e:
        print(f"Error updating metadata (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata Update Examples ===\n")

    print("1. Updating metadata synchronously...")
    update_metadata_sync()

    print("\n2. Updating metadata asynchronously...")
    asyncio.run(update_metadata_async())


if __name__ == "__main__":
    main()
