#!/usr/bin/env python3
"""
Tag Bind Example

This example demonstrates how to bind datasets to knowledge type tags using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request_body import BindTagsToDatasetRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def bind_tags_sync() -> None:
    """Bind tags to dataset synchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_API_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        tag_ids = os.getenv("TAG_IDS")
        if not tag_ids:
            raise ValueError("TAG_IDS environment variable is required (comma-separated list of tag IDs)")

        # Parse comma-separated tag IDs
        tag_id_list = [tag_id.strip() for tag_id in tag_ids.split(",")]

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = BindTagsToDatasetRequestBody.builder().target_id(dataset_id).tag_ids(tag_id_list).build()

        request = BindTagsToDatasetRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.tag.bind(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print("Tags bound to dataset successfully")

    except Exception as e:
        print(f"Error binding tags: {e}")


async def bind_tags_async() -> None:
    """Bind tags to dataset asynchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_API_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        tag_ids = os.getenv("TAG_IDS")
        if not tag_ids:
            raise ValueError("TAG_IDS environment variable is required (comma-separated list of tag IDs)")

        # Parse comma-separated tag IDs
        tag_id_list = [tag_id.strip() for tag_id in tag_ids.split(",")]

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = BindTagsToDatasetRequestBody.builder().target_id(dataset_id).tag_ids(tag_id_list).build()

        request = BindTagsToDatasetRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.tag.abind(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print("Tags bound to dataset successfully (async)")

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
