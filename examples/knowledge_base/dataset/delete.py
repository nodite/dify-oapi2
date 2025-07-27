#!/usr/bin/env python3
"""
Dataset Delete Example

This example demonstrates how to delete a dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.dataset.delete_request import DeleteRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_dataset_sync() -> None:
    """Delete dataset synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build delete request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = DeleteRequest.builder().dataset_id(dataset_id).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Confirm deletion
        print(f"Are you sure you want to delete dataset {dataset_id}? (y/N): ", end="")
        confirmation = input().strip().lower()
        
        if confirmation != 'y':
            print("Deletion cancelled.")
            return
        
        # Delete dataset
        response = client.knowledge_base.v1.dataset.delete(request, request_option)
        
        print(f"Dataset {dataset_id} deleted successfully!")
        print("Note: This operation is irreversible.")
        
    except Exception as e:
        print(f"Error deleting dataset: {e}")


async def delete_dataset_async() -> None:
    """Delete dataset asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build delete request
        dataset_id = os.getenv("DATASET_ID_ASYNC", "your-async-dataset-id-here")
        request = DeleteRequest.builder().dataset_id(dataset_id).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Confirm deletion
        print(f"Are you sure you want to delete dataset {dataset_id} (async)? (y/N): ", end="")
        confirmation = input().strip().lower()
        
        if confirmation != 'y':
            print("Async deletion cancelled.")
            return
        
        # Delete dataset asynchronously
        response = await client.knowledge_base.v1.dataset.adelete(request, request_option)
        
        print(f"Dataset {dataset_id} deleted successfully (async)!")
        print("Note: This operation is irreversible.")
        
    except Exception as e:
        print(f"Error deleting dataset (async): {e}")


def delete_multiple_datasets() -> None:
    """Delete multiple datasets with confirmation."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # List of dataset IDs to delete
        dataset_ids = [
            os.getenv("DATASET_ID_1", "dataset-id-1"),
            os.getenv("DATASET_ID_2", "dataset-id-2"),
            os.getenv("DATASET_ID_3", "dataset-id-3")
        ]
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        print(f"About to delete {len(dataset_ids)} datasets:")
        for dataset_id in dataset_ids:
            print(f"  - {dataset_id}")
        
        print(f"\nAre you sure you want to delete all these datasets? (y/N): ", end="")
        confirmation = input().strip().lower()
        
        if confirmation != 'y':
            print("Bulk deletion cancelled.")
            return
        
        # Delete each dataset
        deleted_count = 0
        failed_count = 0
        
        for dataset_id in dataset_ids:
            try:
                request = DeleteRequest.builder().dataset_id(dataset_id).build()
                response = client.knowledge_base.v1.dataset.delete(request, request_option)
                print(f"✓ Deleted dataset: {dataset_id}")
                deleted_count += 1
            except Exception as e:
                print(f"✗ Failed to delete dataset {dataset_id}: {e}")
                failed_count += 1
        
        print(f"\nDeletion summary:")
        print(f"  Successfully deleted: {deleted_count}")
        print(f"  Failed to delete: {failed_count}")
        
    except Exception as e:
        print(f"Error in bulk deletion: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Dataset Delete Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    print("WARNING: Dataset deletion is irreversible!")
    print("Make sure you have the correct dataset IDs set in environment variables.\n")
    
    if os.getenv("DATASET_ID"):
        print("1. Deleting dataset synchronously...")
        delete_dataset_sync()
    else:
        print("1. Skipping sync deletion (DATASET_ID not set)")
    
    if os.getenv("DATASET_ID_ASYNC"):
        print("\n2. Deleting dataset asynchronously...")
        asyncio.run(delete_dataset_async())
    else:
        print("\n2. Skipping async deletion (DATASET_ID_ASYNC not set)")
    
    if any(os.getenv(f"DATASET_ID_{i}") for i in range(1, 4)):
        print("\n3. Bulk deletion example...")
        delete_multiple_datasets()
    else:
        print("\n3. Skipping bulk deletion (DATASET_ID_1, DATASET_ID_2, DATASET_ID_3 not set)")


if __name__ == "__main__":
    main()