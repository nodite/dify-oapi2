#!/usr/bin/env python3
"""
Tag Unbind Example

This example demonstrates how to unbind datasets from knowledge type tags using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request import UnbindRequest
from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request_body import UnbindRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def unbind_tag_sync() -> None:
    """Unbind tag from dataset synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")
        
        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")
        
        tag_id = os.getenv("TAG_ID")
        if not tag_id:
            raise ValueError("TAG_ID environment variable is required")
        
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request_body = (
            UnbindRequestBody.builder()
            .target_id(dataset_id)
            .tag_id(tag_id)
            .build()
        )
        
        request = UnbindRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()
        response = client.knowledge_base.v1.tag.unbind_tag(request, request_option)
        
        print(f"Tag unbound from dataset")
        
    except Exception as e:
        print(f"Error unbinding tag: {e}")


async def unbind_tag_async() -> None:
    """Unbind tag from dataset asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")
        
        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")
        
        tag_id = os.getenv("TAG_ID")
        if not tag_id:
            raise ValueError("TAG_ID environment variable is required")
        
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request_body = (
            UnbindRequestBody.builder()
            .target_id(dataset_id)
            .tag_id(tag_id)
            .build()
        )
        
        request = UnbindRequest.builder().request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()
        response = await client.knowledge_base.v1.tag.aunbind_tag(request, request_option)
        
        print(f"Tag unbound from dataset (async)")
        
    except Exception as e:
        print(f"Error unbinding tag (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Unbind Examples ===\n")
    
    print("1. Unbinding tag synchronously...")
    unbind_tag_sync()
    
    print("\n2. Unbinding tag asynchronously...")
    asyncio.run(unbind_tag_async())


if __name__ == "__main__":
    main()