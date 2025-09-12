#!/usr/bin/env python3
"""
Dataset Retrieve Example

This example demonstrates how to perform retrieval search in a dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request_body import RetrieveFromDatasetRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def retrieve_basic_sync() -> None:
    """Perform basic retrieval synchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = RetrieveFromDatasetRequestBody.builder().query("What is artificial intelligence?").build()
        request = RetrieveFromDatasetRequest.builder().dataset_id(dataset_id).request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.dataset.retrieve(request, request_option)

        if not response.success:
            # Handle specific error cases
            if "no graphql provider present" in str(response.msg):
                print("Dataset is empty - no documents available for retrieval")
                print("Please add documents to the dataset first")
            else:
                print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Query: {response.query.content if response.query else 'N/A'}")
        print(f"Found {len(response.records) if response.records else 0} records")

        if response.records:
            for i, record in enumerate(response.records[:3], 1):
                segment = record.segment
                print(f"  {i}. {segment.document.name} (Score: {record.score:.4f})")
                print(f"     {segment.content[:100]}...")
        else:
            print("No matching records found for the query")

    except Exception as e:
        print(f"Error performing retrieval: {e}")


async def retrieve_async() -> None:
    """Perform retrieval asynchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = RetrieveFromDatasetRequestBody.builder().query("machine learning").build()
        request = RetrieveFromDatasetRequest.builder().dataset_id(dataset_id).request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.dataset.aretrieve(request, request_option)

        if not response.success:
            # Handle specific error cases
            if "no graphql provider present" in str(response.msg):
                print("Dataset is empty - no documents available for retrieval (async)")
                print("Please add documents to the dataset first")
            else:
                print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Query (async): {response.query.content if response.query else 'N/A'}")
        print(f"Found {len(response.records) if response.records else 0} records")

        if response.records:
            for i, record in enumerate(response.records[:2], 1):
                segment = record.segment
                print(f"  {i}. {segment.document.name}")
        else:
            print("No matching records found for the query (async)")

    except Exception as e:
        print(f"Error performing retrieval (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Retrieve Examples ===\n")
    print("Note: Retrieval requires documents to be indexed in the dataset.")
    print("If the dataset is empty, you'll see a message about no documents available.\n")

    print("1. Basic retrieval synchronously...")
    retrieve_basic_sync()

    print("\n2. Retrieval asynchronously...")
    asyncio.run(retrieve_async())


if __name__ == "__main__":
    main()
