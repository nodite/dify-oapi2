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
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build create metadata request body
        request_body = (
            CreateRequestBody.builder()
            .type("string")
            .name("category")
            .build()
        )
        
        # Build create metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            CreateRequest.builder()
            .dataset_id(dataset_id)
            .request_body(request_body)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Create metadata
        response = client.knowledge_base.v1.metadata.create(request, request_option)
        
        print(f"Metadata created successfully!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Type: {response.type}")
        
    except Exception as e:
        print(f"Error creating metadata: {e}")


async def create_metadata_async() -> None:
    """Create metadata asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build create metadata request body for number type
        request_body = (
            CreateRequestBody.builder()
            .type("number")
            .name("priority")
            .build()
        )
        
        # Build create metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            CreateRequest.builder()
            .dataset_id(dataset_id)
            .request_body(request_body)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Create metadata asynchronously
        response = await client.knowledge_base.v1.metadata.acreate(request, request_option)
        
        print(f"Metadata created successfully (async)!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Type: {response.type}")
        
    except Exception as e:
        print(f"Error creating metadata (async): {e}")


def create_multiple_metadata() -> None:
    """Create multiple metadata fields."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        
        # Define metadata fields to create
        metadata_fields = [
            {"name": "author", "type": "string"},
            {"name": "created_date", "type": "date"},
            {"name": "version", "type": "number"},
            {"name": "tags", "type": "string"},
            {"name": "status", "type": "string"}
        ]
        
        created_metadata = []
        
        print(f"Creating {len(metadata_fields)} metadata fields...")
        
        for field in metadata_fields:
            try:
                request_body = (
                    CreateRequestBody.builder()
                    .type(field["type"])
                    .name(field["name"])
                    .build()
                )
                
                request = (
                    CreateRequest.builder()
                    .dataset_id(dataset_id)
                    .request_body(request_body)
                    .build()
                )
                
                response = client.knowledge_base.v1.metadata.create(request, request_option)
                created_metadata.append(response)
                print(f"✓ Created {field['name']} ({field['type']})")
                
            except Exception as e:
                print(f"✗ Failed to create {field['name']}: {e}")
        
        print(f"\nSummary:")
        print(f"Successfully created {len(created_metadata)} metadata fields:")
        for metadata in created_metadata:
            print(f"  - {metadata.name} (ID: {metadata.id}, Type: {metadata.type})")
        
    except Exception as e:
        print(f"Error creating multiple metadata: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata Create Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    print("1. Creating metadata synchronously...")
    create_metadata_sync()
    
    print("\n2. Creating metadata asynchronously...")
    asyncio.run(create_metadata_async())
    
    print("\n3. Creating multiple metadata fields...")
    create_multiple_metadata()


if __name__ == "__main__":
    main()