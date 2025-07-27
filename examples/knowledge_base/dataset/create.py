#!/usr/bin/env python3
"""
Dataset Creation Example

This example demonstrates how to create a new dataset (knowledge base) using the Dify API.
"""

import asyncio
import os
import time

from dify_oapi.api.knowledge_base.v1.model.dataset.create_request import CreateRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.create_request_body import CreateRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_dataset_sync() -> None:
    """Create a dataset synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = (
            CreateRequestBody.builder()
            .name(f"[Example] Test Dataset {int(time.time())}")
            .description("Test dataset created via API")
            .indexing_technique("economy")
            .permission("only_me")
            .build()
        )

        request = CreateRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.dataset.create(request, request_option)

        print(f"Dataset created: {response.name} (ID: {response.id})")

    except Exception as e:
        print(f"Error creating dataset: {e}")


async def create_dataset_async() -> None:
    """Create a dataset asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = (
            CreateRequestBody.builder()
            .name(f"[Example] Async Dataset {int(time.time())}")
            .description("Async test dataset")
            .indexing_technique("economy")
            .permission("only_me")
            .build()
        )

        request = CreateRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.dataset.acreate(request, request_option)

        print(f"Dataset created (async): {response.name} (ID: {response.id})")

    except Exception as e:
        print(f"Error creating dataset (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Creation Examples ===\n")

    print("1. Creating dataset synchronously...")
    create_dataset_sync()

    print("\n2. Creating dataset asynchronously...")
    asyncio.run(create_dataset_async())


if __name__ == "__main__":
    main()
