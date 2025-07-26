#!/usr/bin/env python3
"""
Metadata Delete Example

This example demonstrates how to delete metadata configuration using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.metadata.delete_request import DeleteMetadataRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_metadata_sync() -> None:
    """Delete metadata synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build delete metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        metadata_id = os.getenv("METADATA_ID", "your-metadata-id-here")
        
        request = (
            DeleteMetadataRequest.builder()
            .dataset_id(dataset_id)
            .metadata_id(metadata_id)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Confirm deletion
        print(f"Are you sure you want to delete metadata {metadata_id}? (y/N): ", end="")
        confirmation = input().strip().lower()
        
        if confirmation != 'y':
            print("Deletion cancelled.")
            return
        
        # Delete metadata
        response = client.knowledge_base.v1.metadata.delete(request, request_option)
        
        print(f"Metadata {metadata_id} deleted successfully!")
        print("Note: This will remove the metadata field from all documents.")
        
    except Exception as e:
        print(f"Error deleting metadata: {e}")


async def delete_metadata_async() -> None:
    """Delete metadata asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build delete metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        metadata_id = os.getenv("METADATA_ID_ASYNC", "your-async-metadata-id-here")
        
        request = (
            DeleteMetadataRequest.builder()
            .dataset_id(dataset_id)
            .metadata_id(metadata_id)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Confirm deletion
        print(f"Are you sure you want to delete metadata {metadata_id} (async)? (y/N): ", end="")
        confirmation = input().strip().lower()
        
        if confirmation != 'y':
            print("Async deletion cancelled.")
            return
        
        # Delete metadata asynchronously
        response = await client.knowledge_base.v1.metadata.adelete(request, request_option)
        
        print(f"Metadata {metadata_id} deleted successfully (async)!")
        print("Note: This will remove the metadata field from all documents.")
        
    except Exception as e:
        print(f"Error deleting metadata (async): {e}")


def delete_multiple_metadata() -> None:
    """Delete multiple metadata fields with confirmation."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        
        # List of metadata IDs to delete
        metadata_ids = [
            os.getenv("METADATA_ID_1", "metadata-id-1"),
            os.getenv("METADATA_ID_2", "metadata-id-2"),
            os.getenv("METADATA_ID_3", "metadata-id-3")
        ]
        
        print(f"About to delete {len(metadata_ids)} metadata fields:")
        for metadata_id in metadata_ids:
            print(f"  - {metadata_id}")
        
        print(f"\nWARNING: This will remove these metadata fields from all documents!")
        print(f"Are you sure you want to delete all these metadata fields? (y/N): ", end="")
        confirmation = input().strip().lower()
        
        if confirmation != 'y':
            print("Bulk deletion cancelled.")
            return
        
        # Delete each metadata field
        deleted_count = 0
        failed_count = 0
        
        for metadata_id in metadata_ids:
            try:
                request = (
                    DeleteMetadataRequest.builder()
                    .dataset_id(dataset_id)
                    .metadata_id(metadata_id)
                    .build()
                )
                
                response = client.knowledge_base.v1.metadata.delete(request, request_option)
                print(f"✓ Deleted metadata: {metadata_id}")
                deleted_count += 1
                
            except Exception as e:
                print(f"✗ Failed to delete metadata {metadata_id}: {e}")
                failed_count += 1
        
        print(f"\nDeletion summary:")
        print(f"  Successfully deleted: {deleted_count}")
        print(f"  Failed to delete: {failed_count}")
        
    except Exception as e:
        print(f"Error in bulk deletion: {e}")


def delete_unused_metadata() -> None:
    """Delete metadata fields that are not being used."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        
        # Note: In a real implementation, you would first list metadata to find unused ones
        # For this example, we'll use predefined unused metadata IDs
        unused_metadata_ids = [
            os.getenv("UNUSED_METADATA_ID_1", "unused-metadata-1"),
            os.getenv("UNUSED_METADATA_ID_2", "unused-metadata-2")
        ]
        
        if not any(unused_metadata_ids):
            print("No unused metadata IDs provided in environment variables.")
            print("Set UNUSED_METADATA_ID_1, UNUSED_METADATA_ID_2, etc.")
            return
        
        print("Cleaning up unused metadata fields...")
        print("These metadata fields have 0 usage count and will be deleted:")
        
        for metadata_id in unused_metadata_ids:
            if metadata_id and metadata_id != f"unused-metadata-{unused_metadata_ids.index(metadata_id) + 1}":
                print(f"  - {metadata_id}")
        
        print(f"\nProceed with cleanup? (y/N): ", end="")
        confirmation = input().strip().lower()
        
        if confirmation != 'y':
            print("Cleanup cancelled.")
            return
        
        cleaned_count = 0
        
        for metadata_id in unused_metadata_ids:
            if not metadata_id or metadata_id.startswith("unused-metadata-"):
                continue
                
            try:
                request = (
                    DeleteMetadataRequest.builder()
                    .dataset_id(dataset_id)
                    .metadata_id(metadata_id)
                    .build()
                )
                
                response = client.knowledge_base.v1.metadata.delete(request, request_option)
                print(f"✓ Cleaned up unused metadata: {metadata_id}")
                cleaned_count += 1
                
            except Exception as e:
                print(f"✗ Failed to clean up metadata {metadata_id}: {e}")
        
        print(f"\nCleanup completed: {cleaned_count} unused metadata fields removed.")
        
    except Exception as e:
        print(f"Error during cleanup: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata Delete Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    print("WARNING: Metadata deletion is irreversible and affects all documents!")
    print("Make sure you have the correct metadata IDs set in environment variables.\n")
    
    if os.getenv("METADATA_ID"):
        print("1. Deleting metadata synchronously...")
        delete_metadata_sync()
    else:
        print("1. Skipping sync deletion (METADATA_ID not set)")
    
    if os.getenv("METADATA_ID_ASYNC"):
        print("\n2. Deleting metadata asynchronously...")
        asyncio.run(delete_metadata_async())
    else:
        print("\n2. Skipping async deletion (METADATA_ID_ASYNC not set)")
    
    if any(os.getenv(f"METADATA_ID_{i}") for i in range(1, 4)):
        print("\n3. Bulk deletion example...")
        delete_multiple_metadata()
    else:
        print("\n3. Skipping bulk deletion (METADATA_ID_1, METADATA_ID_2, METADATA_ID_3 not set)")
    
    print("\n4. Cleanup unused metadata...")
    delete_unused_metadata()


if __name__ == "__main__":
    main()