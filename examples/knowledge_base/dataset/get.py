#!/usr/bin/env python3
"""
Dataset Get Example

This example demonstrates how to get detailed information about a specific dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.dataset.get_request import GetRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_dataset_sync() -> None:
    """Get dataset details synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request = GetRequest.builder().dataset_id(dataset_id).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.dataset.get(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Dataset: {response.name} (ID: {response.id})")
        print(f"  Permission: {response.permission}")
        print(f"  Documents: {response.document_count}, Words: {response.word_count}")
        print(f"  Indexing: {response.indexing_technique}")

        if response.tags:
            print(f"  Tags: {', '.join(tag.name for tag in response.tags)}")

    except Exception as e:
        print(f"Error getting dataset: {e}")


async def get_dataset_async() -> None:
    """Get dataset details asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request = GetRequest.builder().dataset_id(dataset_id).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.dataset.aget(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Dataset (async): {response.name}")
        print(f"  Documents: {response.document_count}")
        print(f"  Embedding: {response.embedding_model or 'None'}")

    except Exception as e:
        print(f"Error getting dataset (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Get Examples ===\n")

    print("1. Getting dataset details synchronously...")
    get_dataset_sync()

    print("\n2. Getting dataset details asynchronously...")
    asyncio.run(get_dataset_async())


if __name__ == "__main__":
    main()
