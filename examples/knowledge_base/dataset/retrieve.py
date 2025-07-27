#!/usr/bin/env python3
"""
Dataset Retrieve Example

This example demonstrates how to perform retrieval search in a dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_request import RetrieveRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_request_body import RetrieveRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def retrieve_basic_sync() -> None:
    """Perform basic retrieval synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = RetrieveRequestBody.builder().query("What is artificial intelligence?").build()
        request = RetrieveRequest.builder().dataset_id(dataset_id).request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.dataset.retrieve(request, request_option)

        if response.raw.status_code != 200:
            print(f"Retrieval failed: {getattr(response, 'message_', 'Unknown error')}")
            return

        print(f"Query: {response.query.content if response.query else 'N/A'}")
        print(f"Found {len(response.records) if response.records else 0} records")

        if response.records:
            for i, record in enumerate(response.records[:3], 1):
                segment = record.segment
                print(f"  {i}. {segment.document.name} (Score: {record.score:.4f})")
                print(f"     {segment.content[:100]}...")

    except Exception as e:
        print(f"Error performing retrieval: {e}")


async def retrieve_async() -> None:
    """Perform retrieval asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = RetrieveRequestBody.builder().query("machine learning").build()
        request = RetrieveRequest.builder().dataset_id(dataset_id).request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.dataset.aretrieve(request, request_option)

        if response.raw.status_code != 200:
            print(f"Retrieval failed (async): {getattr(response, 'message_', 'Unknown error')}")
            return

        print(f"Query (async): {response.query.content if response.query else 'N/A'}")
        print(f"Found {len(response.records) if response.records else 0} records")

        if response.records:
            for i, record in enumerate(response.records[:2], 1):
                segment = record.segment
                print(f"  {i}. {segment.document.name}")

    except Exception as e:
        print(f"Error performing retrieval (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Retrieve Examples ===\n")

    print("1. Basic retrieval synchronously...")
    retrieve_basic_sync()

    print("\n2. Retrieval asynchronously...")
    asyncio.run(retrieve_async())


if __name__ == "__main__":
    main()
