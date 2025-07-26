#!/usr/bin/env python3
"""
Tag Unbind Example

This example demonstrates how to unbind datasets from knowledge type tags using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request import UnbindTagRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def unbind_tag_sync() -> None:
    """Unbind tag from dataset synchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request = (
            UnbindTagRequest.builder()
            .target_id(os.getenv("DATASET_ID", "your-dataset-id-here"))
            .tag_id(os.getenv("TAG_ID", "your-tag-id-here"))
            .build()
        )
        
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        response = client.knowledge_base.v1.tag.unbind_tag(request, request_option)
        
        print(f"Tag unbound from dataset successfully!")
        print(f"Result: {response.result}")
        
    except Exception as e:
        print(f"Error unbinding tag: {e}")


async def unbind_tag_async() -> None:
    """Unbind tag from dataset asynchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request = (
            UnbindTagRequest.builder()
            .target_id(os.getenv("DATASET_ID", "your-dataset-id-here"))
            .tag_id(os.getenv("TAG_ID_ASYNC", "your-async-tag-id-here"))
            .build()
        )
        
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        response = await client.knowledge_base.v1.tag.aunbind_tag(request, request_option)
        
        print(f"Tag unbound from dataset successfully (async)!")
        print(f"Result: {response.result}")
        
    except Exception as e:
        print(f"Error unbinding tag (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Unbind Examples ===\n")
    
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    if os.getenv("TAG_ID"):
        print("1. Unbinding tag synchronously...")
        unbind_tag_sync()
    else:
        print("1. Skipping sync unbind (TAG_ID not set)")
    
    if os.getenv("TAG_ID_ASYNC"):
        print("\n2. Unbinding tag asynchronously...")
        asyncio.run(unbind_tag_async())
    else:
        print("\n2. Skipping async unbind (TAG_ID_ASYNC not set)")


if __name__ == "__main__":
    main()