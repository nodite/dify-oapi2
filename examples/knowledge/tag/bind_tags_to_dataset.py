#!/usr/bin/env python3
"""
Tag Bind Example

This example demonstrates how to bind datasets to knowledge type tags using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.tag.bind_request import BindRequest
from dify_oapi.api.knowledge.v1.model.tag.bind_request_body import BindRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def bind_tags_sync() -> None:
    """Bind tags to dataset synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = (
            BindRequestBody.builder().target_id(dataset_id).tag_ids([os.getenv("TAG_ID", "tag-id-1")]).build()
        )

        request = BindRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()
        client.knowledge.v1.tag.bind_tags(request, request_option)

        print("Tags bound to dataset")

    except Exception as e:
        print(f"Error binding tags: {e}")


async def bind_tags_async() -> None:
    """Bind tags to dataset asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = (
            BindRequestBody.builder().target_id(dataset_id).tag_ids([os.getenv("TAG_ID", "tag-id-1")]).build()
        )

        request = BindRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()
        await client.knowledge.v1.tag.abind_tags(request, request_option)

        print("Tags bound to dataset (async)")

    except Exception as e:
        print(f"Error binding tags (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Bind Examples ===\n")

    print("1. Binding tags synchronously...")
    bind_tags_sync()

    print("\n2. Binding tags asynchronously...")
    asyncio.run(bind_tags_async())


if __name__ == "__main__":
    main()
