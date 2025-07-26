#!/usr/bin/env python3
"""
Tag List Example

This example demonstrates how to list knowledge type tags using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.tag.list_request import ListTagsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_tags_sync() -> None:
    """List tags synchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request = ListTagsRequest.builder().build()
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        response = client.knowledge_base.v1.tag.list(request, request_option)
        
        print(f"Found {len(response.data)} tags:")
        for tag in response.data:
            print(f"  - {tag.name} (ID: {tag.id}, Bindings: {tag.binding_count})")
        
    except Exception as e:
        print(f"Error listing tags: {e}")


async def list_tags_async() -> None:
    """List tags asynchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request = ListTagsRequest.builder().build()
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        response = await client.knowledge_base.v1.tag.alist(request, request_option)
        
        print(f"Tags (async): {len(response.data)} found")
        for tag in response.data:
            print(f"  • {tag.name} - {tag.binding_count} bindings")
        
    except Exception as e:
        print(f"Error listing tags (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag List Examples ===\n")
    
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    print("1. Listing tags synchronously...")
    list_tags_sync()
    
    print("\n2. Listing tags asynchronously...")
    asyncio.run(list_tags_async())


if __name__ == "__main__":
    main()