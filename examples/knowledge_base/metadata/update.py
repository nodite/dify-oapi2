#!/usr/bin/env python3
"""
Metadata Update Example

This example demonstrates how to update metadata configuration using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.metadata.update_request import UpdateMetadataRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_metadata_sync() -> None:
    """Update metadata synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build update metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        metadata_id = os.getenv("METADATA_ID", "your-metadata-id-here")
        
        request = (
            UpdateMetadataRequest.builder()
            .dataset_id(dataset_id)
            .metadata_id(metadata_id)
            .name("updated_category")
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Update metadata
        response = client.knowledge_base.v1.metadata.update(request, request_option)
        
        print(f"Metadata updated successfully!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Type: {response.type}")
        
    except Exception as e:
        print(f"Error updating metadata: {e}")


async def update_metadata_async() -> None:
    """Update metadata asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build update metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        metadata_id = os.getenv("METADATA_ID_ASYNC", "your-async-metadata-id-here")
        
        request = (
            UpdateMetadataRequest.builder()
            .dataset_id(dataset_id)
            .metadata_id(metadata_id)
            .name("async_updated_field")
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Update metadata asynchronously
        response = await client.knowledge_base.v1.metadata.aupdate(request, request_option)
        
        print(f"Metadata updated successfully (async)!")
        print(f"ID: {response.id}")
        print(f"Name: {response.name}")
        print(f"Type: {response.type}")
        
    except Exception as e:
        print(f"Error updating metadata (async): {e}")


def update_multiple_metadata() -> None:
    """Update multiple metadata fields."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        
        # Define metadata updates
        metadata_updates = [
            {"id": os.getenv("METADATA_ID_1", "metadata-id-1"), "new_name": "document_category"},
            {"id": os.getenv("METADATA_ID_2", "metadata-id-2"), "new_name": "importance_level"},
            {"id": os.getenv("METADATA_ID_3", "metadata-id-3"), "new_name": "last_modified"},
        ]
        
        updated_metadata = []
        
        print(f"Updating {len(metadata_updates)} metadata fields...")
        
        for update in metadata_updates:
            try:
                request = (
                    UpdateMetadataRequest.builder()
                    .dataset_id(dataset_id)
                    .metadata_id(update["id"])
                    .name(update["new_name"])
                    .build()
                )
                
                response = client.knowledge_base.v1.metadata.update(request, request_option)
                updated_metadata.append(response)
                print(f"✓ Updated metadata {update['id']} to '{update['new_name']}'")
                
            except Exception as e:
                print(f"✗ Failed to update metadata {update['id']}: {e}")
        
        print(f"\nUpdate Summary:")
        print(f"Successfully updated {len(updated_metadata)} metadata fields:")
        for metadata in updated_metadata:
            print(f"  - {metadata.name} (ID: {metadata.id}, Type: {metadata.type})")
        
    except Exception as e:
        print(f"Error updating multiple metadata: {e}")


def rename_metadata_with_validation() -> None:
    """Rename metadata with name validation."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        metadata_id = os.getenv("METADATA_ID", "your-metadata-id-here")
        
        # Get current name first (would need to implement get metadata or list)
        print("Current metadata configuration:")
        
        # For demonstration, we'll use a predefined new name
        new_name = "validated_field_name"
        
        # Validate new name (basic validation)
        if not new_name or len(new_name.strip()) == 0:
            print("Error: New name cannot be empty")
            return
        
        if len(new_name) > 50:
            print("Error: New name is too long (max 50 characters)")
            return
        
        if not new_name.replace('_', '').replace('-', '').isalnum():
            print("Error: New name should only contain alphanumeric characters, underscores, and hyphens")
            return
        
        # Build update request
        request = (
            UpdateMetadataRequest.builder()
            .dataset_id(dataset_id)
            .metadata_id(metadata_id)
            .name(new_name)
            .build()
        )
        
        # Update metadata
        response = client.knowledge_base.v1.metadata.update(request, request_option)
        
        print(f"Metadata renamed successfully!")
        print(f"ID: {response.id}")
        print(f"New name: {response.name}")
        print(f"Type: {response.type}")
        
    except Exception as e:
        print(f"Error renaming metadata: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata Update Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    if os.getenv("METADATA_ID"):
        print("1. Updating metadata synchronously...")
        update_metadata_sync()
    else:
        print("1. Skipping sync update (METADATA_ID not set)")
    
    if os.getenv("METADATA_ID_ASYNC"):
        print("\n2. Updating metadata asynchronously...")
        asyncio.run(update_metadata_async())
    else:
        print("\n2. Skipping async update (METADATA_ID_ASYNC not set)")
    
    if any(os.getenv(f"METADATA_ID_{i}") for i in range(1, 4)):
        print("\n3. Updating multiple metadata fields...")
        update_multiple_metadata()
    else:
        print("\n3. Skipping multiple updates (METADATA_ID_1, METADATA_ID_2, METADATA_ID_3 not set)")
    
    if os.getenv("METADATA_ID"):
        print("\n4. Renaming metadata with validation...")
        rename_metadata_with_validation()
    else:
        print("\n4. Skipping validation example (METADATA_ID not set)")


if __name__ == "__main__":
    main()