#!/usr/bin/env python3
"""
Tag Bind Example

This example demonstrates how to bind datasets to knowledge type tags using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.tag.bind_request import BindTagsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def bind_tags_sync() -> None:
    """Bind tags to dataset synchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request = (
            BindTagsRequest.builder()
            .target_id(os.getenv("DATASET_ID", "your-dataset-id-here"))
            .tag_ids([
                os.getenv("TAG_ID_1", "tag-id-1"),
                os.getenv("TAG_ID_2", "tag-id-2")
            ])
            .build()
        )
        
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        response = client.knowledge_base.v1.tag.bind_tags(request, request_option)
        
        print(f"Tags bound to dataset successfully!")
        print(f"Result: {response.result}")
        
    except Exception as e:
        print(f"Error binding tags: {e}")


async def bind_tags_async() -> None:
    """Bind tags to dataset asynchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request = (
            BindTagsRequest.builder()
            .target_id(os.getenv("DATASET_ID", "your-dataset-id-here"))
            .tag_ids([os.getenv("TAG_ID_3", "tag-id-3")])
            .build()
        )
        
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        response = await client.knowledge_base.v1.tag.abind_tags(request, request_option)
        
        print(f"Tags bound to dataset successfully (async)!")
        print(f"Result: {response.result}")
        
    except Exception as e:
        print(f"Error binding tags (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Bind Examples ===\n")
    
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    print("1. Binding tags synchronously...")
    bind_tags_sync()
    
    print("\n2. Binding tags asynchronously...")
    asyncio.run(bind_tags_async())


if __name__ == "__main__":
    main()