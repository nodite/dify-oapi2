#!/usr/bin/env python3
"""
Tag Unbind Example

This example demonstrates how to unbind datasets from knowledge type tags using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_request import UnbindTagsFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_request_body import UnbindTagsFromDatasetRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def unbind_tags_sync() -> None:
    """Unbind tags from dataset synchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        tag_ids = os.getenv("TAG_IDS")
        if not tag_ids:
            raise ValueError("TAG_IDS environment variable is required (comma-separated list of tag IDs)")

        # Use first tag ID (unbind API only supports single tag)
        tag_id = tag_ids.split(",")[0].strip()

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = UnbindTagsFromDatasetRequestBody.builder().target_id(dataset_id).tag_id(tag_id).build()

        request = UnbindTagsFromDatasetRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()
        response = client.knowledge.v1.tag.unbind(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print("Tags unbound from dataset successfully")

    except Exception as e:
        print(f"Error unbinding tags: {e}")


async def unbind_tags_async() -> None:
    """Unbind tags from dataset asynchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        tag_ids = os.getenv("TAG_IDS")
        if not tag_ids:
            raise ValueError("TAG_IDS environment variable is required (comma-separated list of tag IDs)")

        # Use first tag ID (unbind API only supports single tag)
        tag_id = tag_ids.split(",")[0].strip()

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = UnbindTagsFromDatasetRequestBody.builder().target_id(dataset_id).tag_id(tag_id).build()

        request = UnbindTagsFromDatasetRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()
        response = await client.knowledge.v1.tag.aunbind(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print("Tags unbound from dataset successfully (async)")

    except Exception as e:
        print(f"Error unbinding tags (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Unbind Examples ===\n")

    print("1. Unbinding tags synchronously...")
    unbind_tags_sync()

    print("\n2. Unbinding tags asynchronously...")
    asyncio.run(unbind_tags_async())


if __name__ == "__main__":
    main()
