#!/usr/bin/env python3
"""
Tag Query Bound Example

This example demonstrates how to query tags bound to a dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.get_dataset_tags_request import GetDatasetTagsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def query_bound_tags_sync() -> None:
    """Query bound tags synchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_API_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = GetDatasetTagsRequest.builder().dataset_id(dataset_id).build()
        request_option = RequestOption.builder().api_key(api_key).build()
        response = client.knowledge.v1.tag.get_dataset_tags(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Found {response.total or 0} bound tags:")
        if response.data:
            if response.data:
                for tag in response.data:
                    print(f"  - {tag.name}")

            else:
                print("  No items found")

        else:
            print("  No items found")

    except Exception as e:
        print(f"Error querying bound tags: {e}")


async def query_bound_tags_async() -> None:
    """Query bound tags asynchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_API_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = GetDatasetTagsRequest.builder().dataset_id(dataset_id).build()
        request_option = RequestOption.builder().api_key(api_key).build()
        response = await client.knowledge.v1.tag.aget_dataset_tags(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Bound tags (async): {response.total or 0} total")
        if response.data:
            if response.data:
                for tag in response.data:
                    print(f"  • {tag.name}")

            else:
                print("  No items found")

        else:
            print("  No items found")

    except Exception as e:
        print(f"Error querying bound tags (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Query Bound Examples ===\n")

    print("1. Querying bound tags synchronously...")
    query_bound_tags_sync()

    print("\n2. Querying bound tags asynchronously...")
    asyncio.run(query_bound_tags_async())


if __name__ == "__main__":
    main()
