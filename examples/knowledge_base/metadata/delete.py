#!/usr/bin/env python3
"""
Metadata Delete Example

This example demonstrates how to delete metadata configuration using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.metadata.delete_request import DeleteRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_metadata_sync() -> None:
    """Delete metadata synchronously (only [Example] prefixed metadata)."""
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
        request_option = RequestOption.builder().api_key(api_key).build()

        from dify_oapi.api.knowledge_base.v1.model.metadata.list_request import ListRequest

        list_request = ListRequest.builder().dataset_id(dataset_id).build()
        list_response = client.knowledge_base.v1.metadata.list(list_request, request_option)

        target_metadata = None
        if list_response.doc_metadata:
            target_metadata = next((meta for meta in list_response.doc_metadata if meta.id == metadata_id), None)

        if not target_metadata:
            print(f"Metadata {metadata_id} not found")
            return

        if not target_metadata.name or not target_metadata.name.startswith("[Example]"):
            print(f"Skipping '{target_metadata.name}' - not an example metadata")
            return

        request = DeleteRequest.builder().dataset_id(dataset_id).metadata_id(metadata_id).build()
        client.knowledge_base.v1.metadata.delete(request, request_option)
        print(f"Deleted: {target_metadata.name}")

    except Exception as e:
        print(f"Error deleting metadata: {e}")


async def delete_metadata_async() -> None:
    """Delete metadata asynchronously (only [Example] prefixed metadata)."""
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
        request_option = RequestOption.builder().api_key(api_key).build()

        from dify_oapi.api.knowledge_base.v1.model.metadata.list_request import ListRequest

        list_request = ListRequest.builder().dataset_id(dataset_id).build()
        list_response = await client.knowledge_base.v1.metadata.alist(list_request, request_option)

        target_metadata = None
        if list_response.doc_metadata:
            target_metadata = next((meta for meta in list_response.doc_metadata if meta.id == metadata_id), None)

        if not target_metadata:
            print(f"Metadata {metadata_id} not found")
            return

        if not target_metadata.name or not target_metadata.name.startswith("[Example]"):
            print(f"Skipping '{target_metadata.name}' - not an example metadata")
            return

        request = DeleteRequest.builder().dataset_id(dataset_id).metadata_id(metadata_id).build()
        await client.knowledge_base.v1.metadata.adelete(request, request_option)
        print(f"Deleted (async): {target_metadata.name}")

    except Exception as e:
        print(f"Error deleting metadata (async): {e}")


def delete_example_metadata() -> None:
    """Delete all metadata with [Example] prefix."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        from dify_oapi.api.knowledge_base.v1.model.metadata.list_request import ListRequest

        list_request = ListRequest.builder().dataset_id(dataset_id).build()
        list_response = client.knowledge_base.v1.metadata.list(list_request, request_option)

        example_metadata = [m for m in list_response.doc_metadata if m.name and m.name.startswith("[Example]")]

        if not example_metadata:
            print("No example metadata found")
            return

        print(f"Deleting {len(example_metadata)} example metadata...")

        for metadata in example_metadata:
            try:
                request = DeleteRequest.builder().dataset_id(dataset_id).metadata_id(metadata.id).build()
                client.knowledge_base.v1.metadata.delete(request, request_option)
                print(f"✓ {metadata.name}")
            except Exception as e:
                print(f"✗ {metadata.name}: {e}")

    except Exception as e:
        print(f"Error in cleanup: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata Delete Examples ===\n")

    print("1. Deleting specific metadata synchronously...")
    delete_metadata_sync()

    print("\n2. Deleting specific metadata asynchronously...")
    asyncio.run(delete_metadata_async())

    print("\n3. Cleaning up all example metadata...")
    delete_example_metadata()


if __name__ == "__main__":
    main()
