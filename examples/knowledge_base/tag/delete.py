#!/usr/bin/env python3
"""
Tag Delete Example

This example demonstrates how to delete knowledge type tags using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.tag.delete_request import DeleteTagRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_tag_sync() -> None:
    """Delete tag synchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        tag_id = os.getenv("TAG_ID", "your-tag-id-here")
        request = DeleteTagRequest.builder().tag_id(tag_id).build()
        
        print(f"Are you sure you want to delete tag {tag_id}? (y/N): ", end="")
        if input().strip().lower() != 'y':
            print("Deletion cancelled.")
            return
        
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        response = client.knowledge_base.v1.tag.delete(request, request_option)
        
        print(f"Tag {tag_id} deleted successfully!")
        print(f"Result: {response.result}")
        
    except Exception as e:
        print(f"Error deleting tag: {e}")


async def delete_tag_async() -> None:
    """Delete tag asynchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        tag_id = os.getenv("TAG_ID_ASYNC", "your-async-tag-id-here")
        request = DeleteTagRequest.builder().tag_id(tag_id).build()
        
        print(f"Are you sure you want to delete tag {tag_id} (async)? (y/N): ", end="")
        if input().strip().lower() != 'y':
            print("Async deletion cancelled.")
            return
        
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        response = await client.knowledge_base.v1.tag.adelete(request, request_option)
        
        print(f"Tag {tag_id} deleted successfully (async)!")
        print(f"Result: {response.result}")
        
    except Exception as e:
        print(f"Error deleting tag (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Delete Examples ===\n")
    
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    print("WARNING: Tag deletion is irreversible!")
    
    if os.getenv("TAG_ID"):
        print("1. Deleting tag synchronously...")
        delete_tag_sync()
    else:
        print("1. Skipping sync deletion (TAG_ID not set)")
    
    if os.getenv("TAG_ID_ASYNC"):
        print("\n2. Deleting tag asynchronously...")
        asyncio.run(delete_tag_async())
    else:
        print("\n2. Skipping async deletion (TAG_ID_ASYNC not set)")


if __name__ == "__main__":
    main()