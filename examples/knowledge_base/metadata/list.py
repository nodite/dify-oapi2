#!/usr/bin/env python3
"""
Metadata List Example

This example demonstrates how to list metadata for a dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.metadata.list_request import ListRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_metadata_sync() -> None:
    """List metadata synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request = ListRequest.builder().dataset_id(dataset_id).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.metadata.list(request, request_option)

        print(f"Built-in fields: {'Enabled' if response.built_in_field_enabled else 'Disabled'}")
        metadata_list = response.doc_metadata or []
        print(f"Custom metadata: {len(metadata_list)} fields")

        for metadata in metadata_list:
            print(f"  - {metadata.name} ({metadata.type}, ID: {metadata.id}, used: {metadata.use_count or 0})")

    except Exception as e:
        print(f"Error listing metadata: {e}")


async def list_metadata_async() -> None:
    """List metadata asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request = ListRequest.builder().dataset_id(dataset_id).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.metadata.alist(request, request_option)

        metadata_list = response.doc_metadata or []
        print(f"Metadata (async): {len(metadata_list)} fields")

        by_type = {}
        for metadata in metadata_list:
            if metadata.type not in by_type:
                by_type[metadata.type] = []
            by_type[metadata.type].append(metadata)

        for metadata_type, fields in by_type.items():
            print(f"  {metadata_type}: {', '.join(f.name for f in fields)}")

    except Exception as e:
        print(f"Error listing metadata (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata List Examples ===\n")

    print("1. Listing metadata synchronously...")
    list_metadata_sync()

    print("\n2. Listing metadata asynchronously...")
    asyncio.run(list_metadata_async())


if __name__ == "__main__":
    main()
