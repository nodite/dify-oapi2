#!/usr/bin/env python3
"""
Tag Update Example

This example demonstrates how to update knowledge type tag names using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.tag.update_request import UpdateRequest
from dify_oapi.api.knowledge_base.v1.model.tag.update_request_body import UpdateRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_tag_sync() -> None:
    """Update tag synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        tag_id = os.getenv("TAG_ID")
        if not tag_id:
            raise ValueError("TAG_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = UpdateRequestBody.builder().tag_id(tag_id).name("[Example] Updated Tag Name").build()

        request = UpdateRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()
        response = client.knowledge_base.v1.tag.update(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Tag updated: {response.name} (Bindings: {response.binding_count})")

    except Exception as e:
        print(f"Error updating tag: {e}")


async def update_tag_async() -> None:
    """Update tag asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        tag_id = os.getenv("TAG_ID")
        if not tag_id:
            raise ValueError("TAG_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = UpdateRequestBody.builder().tag_id(tag_id).name("[Example] Async Updated Tag").build()

        request = UpdateRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()
        response = await client.knowledge_base.v1.tag.aupdate(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Tag updated (async): {response.name}")

    except Exception as e:
        print(f"Error updating tag (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Update Examples ===\n")

    print("1. Updating tag synchronously...")
    update_tag_sync()

    print("\n2. Updating tag asynchronously...")
    asyncio.run(update_tag_async())


if __name__ == "__main__":
    main()
