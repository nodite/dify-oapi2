#!/usr/bin/env python3
"""
Metadata Create Example

This example demonstrates how to create metadata for a dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.metadata.create_request import CreateRequest
from dify_oapi.api.knowledge_base.v1.model.metadata.create_request_body import CreateRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_metadata_sync() -> None:
    """Create metadata synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")
        
        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")
        
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request_body = (
            CreateRequestBody.builder()
            .type("string")
            .name("[Example] category")
            .build()
        )
        
        request = (
            CreateRequest.builder()
            .dataset_id(dataset_id)
            .request_body(request_body)
            .build()
        )
        
        request_option = RequestOption.builder().api_key(api_key).build()
        response = client.knowledge_base.v1.metadata.create(request, request_option)
        
        print(f"Metadata created: {response.name} ({response.type})")
        
    except Exception as e:
        print(f"Error creating metadata: {e}")


async def create_metadata_async() -> None:
    """Create metadata asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")
        
        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")
        
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        request_body = (
            CreateRequestBody.builder()
            .type("number")
            .name("[Example] priority")
            .build()
        )
        
        request = (
            CreateRequest.builder()
            .dataset_id(dataset_id)
            .request_body(request_body)
            .build()
        )
        
        request_option = RequestOption.builder().api_key(api_key).build()
        response = await client.knowledge_base.v1.metadata.acreate(request, request_option)
        
        print(f"Metadata created (async): {response.name} ({response.type})")
        
    except Exception as e:
        print(f"Error creating metadata (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata Create Examples ===\n")
    
    print("1. Creating metadata synchronously...")
    create_metadata_sync()
    
    print("\n2. Creating metadata asynchronously...")
    asyncio.run(create_metadata_async())


if __name__ == "__main__":
    main()