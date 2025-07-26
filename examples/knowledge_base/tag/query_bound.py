#!/usr/bin/env python3
"""
Tag Query Bound Example

This example demonstrates how to query tags bound to a dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_request import QueryBoundTagsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def query_bound_tags_sync() -> None:
    """Query bound tags synchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request = (
            QueryBoundTagsRequest.builder()
            .dataset_id(os.getenv("DATASET_ID", "your-dataset-id-here"))
            .build()
        )
        
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        response = client.knowledge_base.v1.tag.query_bound(request, request_option)
        
        print(f"Found {response.total} bound tags:")
        for tag in response.data:
            print(f"  - {tag.name} (ID: {tag.id})")
        
    except Exception as e:
        print(f"Error querying bound tags: {e}")


async def query_bound_tags_async() -> None:
    """Query bound tags asynchronously."""
    try:
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request = (
            QueryBoundTagsRequest.builder()
            .dataset_id(os.getenv("DATASET_ID", "your-dataset-id-here"))
            .build()
        )
        
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        response = await client.knowledge_base.v1.tag.aquery_bound(request, request_option)
        
        print(f"Bound tags (async): {response.total} total")
        for tag in response.data:
            print(f"  • {tag.name}")
        
    except Exception as e:
        print(f"Error querying bound tags (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Query Bound Examples ===\n")
    
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    print("1. Querying bound tags synchronously...")
    query_bound_tags_sync()
    
    print("\n2. Querying bound tags asynchronously...")
    asyncio.run(query_bound_tags_async())


if __name__ == "__main__":
    main()