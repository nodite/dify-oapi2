#!/usr/bin/env python3
"""
Dataset List Example

This example demonstrates how to list datasets (knowledge bases) using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.dataset.list_request import ListDatasetsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_datasets_sync() -> None:
    """List datasets synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build list request with pagination
        request = (
            ListDatasetsRequest.builder()
            .page(1)
            .limit(10)
            .include_all(False)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # List datasets
        response = client.knowledge_base.v1.dataset.list(request, request_option)
        
        print(f"Found {response.total} datasets (showing page {response.page})")
        print(f"Has more: {response.has_more}")
        print("\nDatasets:")
        
        for dataset in response.data:
            print(f"  - ID: {dataset.id}")
            print(f"    Name: {dataset.name}")
            print(f"    Description: {dataset.description}")
            print(f"    Permission: {dataset.permission}")
            print(f"    Document count: {dataset.document_count}")
            print(f"    Word count: {dataset.word_count}")
            print(f"    Created at: {dataset.created_at}")
            print()
        
    except Exception as e:
        print(f"Error listing datasets: {e}")


async def list_datasets_async() -> None:
    """List datasets asynchronously with search."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build list request with keyword search
        request = (
            ListDatasetsRequest.builder()
            .keyword("test")
            .page(1)
            .limit(5)
            .include_all(True)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # List datasets asynchronously
        response = await client.knowledge_base.v1.dataset.alist(request, request_option)
        
        print(f"Search results for 'test': {len(response.data)} datasets found")
        print(f"Total: {response.total}, Page: {response.page}, Limit: {response.limit}")
        
        if response.data:
            print("\nMatching datasets:")
            for dataset in response.data:
                print(f"  - {dataset.name} (ID: {dataset.id})")
                print(f"    Description: {dataset.description}")
                print(f"    App count: {dataset.app_count}")
                print()
        else:
            print("No datasets found matching the search criteria.")
        
    except Exception as e:
        print(f"Error listing datasets (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset List Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    print("1. Listing datasets synchronously...")
    list_datasets_sync()
    
    print("\n2. Searching datasets asynchronously...")
    asyncio.run(list_datasets_async())


if __name__ == "__main__":
    main()