#!/usr/bin/env python3
"""
Tag Update Example

This example demonstrates how to update knowledge type tag names using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.tag.update_request import UpdateTagRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_tag_sync() -> None:
    """Update tag synchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request = (
            UpdateTagRequest.builder()
            .tag_id(os.getenv("TAG_ID", "your-tag-id-here"))
            .name("Updated Tag Name")
            .build()
        )
        
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        response = client.knowledge_base.v1.tag.update(request, request_option)
        
        print(f"Tag updated successfully!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Binding count: {response.binding_count}")
        
    except Exception as e:
        print(f"Error updating tag: {e}")


async def update_tag_async() -> None:
    """Update tag asynchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request = (
            UpdateTagRequest.builder()
            .tag_id(os.getenv("TAG_ID_ASYNC", "your-async-tag-id-here"))
            .name("Async Updated Tag")
            .build()
        )
        
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        response = await client.knowledge_base.v1.tag.aupdate(request, request_option)
        
        print(f"Tag updated successfully (async)!")
        print(f"Name: {response.name}")
        
    except Exception as e:
        print(f"Error updating tag (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Update Examples ===\n")
    
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if os.getenv("TAG_ID"):
        print("1. Updating tag synchronously...")
        update_tag_sync()
    else:
        print("1. Skipping sync update (TAG_ID not set)")
    
    if os.getenv("TAG_ID_ASYNC"):
        print("\n2. Updating tag asynchronously...")
        asyncio.run(update_tag_async())
    else:
        print("\n2. Skipping async update (TAG_ID_ASYNC not set)")


if __name__ == "__main__":
    main()