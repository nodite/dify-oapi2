#!/usr/bin/env python3
"""
Tag Create Example

This example demonstrates how to create knowledge type tags using the Dify API.
"""

import asyncio
import os
import time

from dify_oapi.api.knowledge_base.v1.model.tag.create_request import CreateRequest
from dify_oapi.api.knowledge_base.v1.model.tag.create_request_body import CreateRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_tag_sync() -> None:
    """Create tag synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = CreateRequestBody.builder().name(f"[Example] Technical Docs {int(time.time())}").build()

        request = CreateRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.tag.create(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Tag created: {response.name} (Bindings: {response.binding_count})")

    except Exception as e:
        print(f"Error creating tag: {e}")


async def create_tag_async() -> None:
    """Create tag asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = CreateRequestBody.builder().name(f"[Example] User Guides {int(time.time())}").build()

        request = CreateRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.tag.acreate(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Tag created (async): {response.name}")

    except Exception as e:
        print(f"Error creating tag (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Create Examples ===\n")

    print("1. Creating tag synchronously...")
    create_tag_sync()

    print("\n2. Creating tag asynchronously...")
    asyncio.run(create_tag_async())


if __name__ == "__main__":
    main()
