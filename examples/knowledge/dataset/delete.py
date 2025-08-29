#!/usr/bin/env python3
"""
Dataset Delete Example

This example demonstrates how to delete datasets using the Dify API.
Only deletes datasets with "[Example]" prefix for safety.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.dataset.delete_request import DeleteRequest
from dify_oapi.api.knowledge.v1.model.dataset.get_request import GetRequest
from dify_oapi.api.knowledge.v1.model.dataset.list_request import ListRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_dataset_sync() -> None:
    """Delete dataset synchronously (only [Example] prefixed datasets)."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        get_request = GetRequest.builder().dataset_id(dataset_id).build()
        dataset_info = client.knowledge.v1.dataset.get(get_request, request_option)

        if not dataset_info.name or not dataset_info.name.startswith("[Example]"):
            print(f"Skipping '{dataset_info.name}' - not an example dataset")
            return

        request = DeleteRequest.builder().dataset_id(dataset_id).build()
        client.knowledge.v1.dataset.delete(request, request_option)
        print(f"Deleted: {dataset_info.name}")

    except Exception as e:
        print(f"Error deleting dataset: {e}")


async def delete_dataset_async() -> None:
    """Delete dataset asynchronously (only [Example] prefixed datasets)."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        get_request = GetRequest.builder().dataset_id(dataset_id).build()
        dataset_info = await client.knowledge.v1.dataset.aget(get_request, request_option)

        if not dataset_info.name or not dataset_info.name.startswith("[Example]"):
            print(f"Skipping '{dataset_info.name}' - not an example dataset")
            return

        request = DeleteRequest.builder().dataset_id(dataset_id).build()
        await client.knowledge.v1.dataset.adelete(request, request_option)
        print(f"Deleted (async): {dataset_info.name}")

    except Exception as e:
        print(f"Error deleting dataset (async): {e}")


def delete_example_datasets() -> None:
    """Delete all datasets with [Example] prefix."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        list_request = ListRequest.builder().limit("100").build()
        list_response = client.knowledge.v1.dataset.list(list_request, request_option)

        if not list_response.success:
            print(f"API Error: {list_response.code} - {list_response.msg}")
            return

        if not list_response.data:
            print("No datasets found")
            return

        example_datasets = [d for d in list_response.data if d.name and d.name.startswith("[Example]")]

        if not example_datasets:
            print("No example datasets found")
            return

        print(f"Deleting {len(example_datasets)} example datasets...")

        for dataset in example_datasets:
            try:
                if not dataset.id:
                    print(f"✗ {dataset.name}: Dataset ID is None")
                    continue
                request = DeleteRequest.builder().dataset_id(dataset.id).build()
                client.knowledge.v1.dataset.delete(request, request_option)
                print(f"✓ {dataset.name}")
            except Exception as e:
                print(f"✗ {dataset.name}: {e}")

    except Exception as e:
        print(f"Error in cleanup: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Delete Examples ===\n")

    print("1. Deleting specific dataset synchronously...")
    delete_dataset_sync()

    print("\n2. Deleting specific dataset asynchronously...")
    asyncio.run(delete_dataset_async())

    print("\n3. Cleaning up all example datasets...")
    delete_example_datasets()


if __name__ == "__main__":
    main()
