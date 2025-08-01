#!/usr/bin/env python3
"""
Dataset Update Example

This example demonstrates how to update dataset configuration using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.dataset.update_request import UpdateRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.update_request_body import UpdateRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_dataset_sync() -> None:
    """Update dataset synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = (
            UpdateRequestBody.builder().name("[Example] Updated Dataset").permission("all_team_members").build()
        )

        request = UpdateRequest.builder().dataset_id(dataset_id).request_body(request_body).build()

        request_option = RequestOption.builder().api_key(api_key).build()
        response = client.knowledge_base.v1.dataset.update(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Dataset updated: {response.name} (Permission: {response.permission})")

    except Exception as e:
        print(f"Error updating dataset: {e}")


async def update_dataset_async() -> None:
    """Update dataset asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = UpdateRequestBody.builder().name("[Example] Async Updated Dataset").permission("only_me").build()

        request = UpdateRequest.builder().dataset_id(dataset_id).request_body(request_body).build()

        request_option = RequestOption.builder().api_key(api_key).build()
        response = await client.knowledge_base.v1.dataset.aupdate(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Dataset updated (async): {response.name}")

    except Exception as e:
        print(f"Error updating dataset (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Update Examples ===\n")

    print("1. Updating dataset synchronously...")
    update_dataset_sync()

    print("\n2. Updating dataset asynchronously...")
    asyncio.run(update_dataset_async())


if __name__ == "__main__":
    main()
