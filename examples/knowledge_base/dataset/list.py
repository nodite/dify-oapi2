#!/usr/bin/env python3
"""
Dataset List Example

This example demonstrates how to list datasets (knowledge bases) using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.dataset.list_request import ListRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_datasets_sync() -> None:
    """List datasets synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request = ListRequest.builder().page(1).limit(10).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.dataset.list(request, request_option)

        print(f"Found {response.total} datasets:")
        for dataset in response.data:
            print(f"  - {dataset.name} (ID: {dataset.id}, Docs: {dataset.document_count})")

    except Exception as e:
        print(f"Error listing datasets: {e}")


async def list_datasets_async() -> None:
    """List datasets asynchronously with search."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request = ListRequest.builder().keyword("test").limit(5).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.dataset.alist(request, request_option)

        print(f"Search 'test': {len(response.data)} datasets found")
        for dataset in response.data:
            print(f"  - {dataset.name} (ID: {dataset.id})")

    except Exception as e:
        print(f"Error listing datasets (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset List Examples ===\n")

    print("1. Listing datasets synchronously...")
    list_datasets_sync()

    print("\n2. Searching datasets asynchronously...")
    asyncio.run(list_datasets_async())


if __name__ == "__main__":
    main()
