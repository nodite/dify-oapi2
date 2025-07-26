#!/usr/bin/env python3
"""
Metadata Toggle Built-in Example

This example demonstrates how to enable or disable built-in metadata using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.metadata.toggle_builtin_request import ToggleBuiltinMetadataRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def enable_builtin_metadata_sync() -> None:
    """Enable built-in metadata synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build enable built-in metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            ToggleBuiltinMetadataRequest.builder()
            .dataset_id(dataset_id)
            .action("enable")
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Enable built-in metadata
        response = client.knowledge_base.v1.metadata.toggle_builtin(request, request_option)
        
        print(f"Built-in metadata enabled successfully!")
        print(f"Result: {response.result}")
        print("\nBuilt-in metadata fields are now available for use in documents.")
        print("These typically include fields like file name, creation date, etc.")
        
    except Exception as e:
        print(f"Error enabling built-in metadata: {e}")


async def disable_builtin_metadata_async() -> None:
    """Disable built-in metadata asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build disable built-in metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            ToggleBuiltinMetadataRequest.builder()
            .dataset_id(dataset_id)
            .action("disable")
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Disable built-in metadata asynchronously
        response = await client.knowledge_base.v1.metadata.atoggle_builtin(request, request_option)
        
        print(f"Built-in metadata disabled successfully (async)!")
        print(f"Result: {response.result}")
        print("\nBuilt-in metadata fields are no longer available.")
        print("Only custom metadata fields will be accessible.")
        
    except Exception as e:
        print(f"Error disabling built-in metadata (async): {e}")


def toggle_builtin_with_confirmation() -> None:
    """Toggle built-in metadata with user confirmation."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        
        # Ask user for action
        print("Built-in Metadata Toggle Options:")
        print("1. Enable built-in metadata")
        print("2. Disable built-in metadata")
        print("3. Cancel")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            action = "enable"
            action_desc = "enable"
        elif choice == "2":
            action = "disable"
            action_desc = "disable"
        elif choice == "3":
            print("Operation cancelled.")
            return
        else:
            print("Invalid choice. Operation cancelled.")
            return
        
        # Confirm action
        print(f"\nThis will {action_desc} built-in metadata for dataset {dataset_id}")
        print(f"Are you sure you want to {action_desc} built-in metadata? (y/N): ", end="")
        confirmation = input().strip().lower()
        
        if confirmation != 'y':
            print("Operation cancelled.")
            return
        
        # Build request
        request = (
            ToggleBuiltinMetadataRequest.builder()
            .dataset_id(dataset_id)
            .action(action)
            .build()
        )
        
        # Execute toggle
        response = client.knowledge_base.v1.metadata.toggle_builtin(request, request_option)
        
        print(f"\nBuilt-in metadata {action}d successfully!")
        print(f"Result: {response.result}")
        
        if action == "enable":
            print("\nBuilt-in metadata fields are now available:")
            print("  • Document name")
            print("  • File type")
            print("  • Creation date")
            print("  • File size")
            print("  • And other system-generated metadata")
        else:
            print("\nBuilt-in metadata fields are now disabled.")
            print("Only custom metadata fields will be available for filtering and search.")
        
    except Exception as e:
        print(f"Error toggling built-in metadata: {e}")


def check_builtin_status() -> None:
    """Check current built-in metadata status."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        
        # Note: This would typically use the list metadata endpoint to check status
        # For demonstration, we'll show how to interpret the response
        
        print("Checking built-in metadata status...")
        print("(In a real implementation, this would call the list metadata endpoint)")
        
        # Simulated status check
        print(f"\nDataset: {dataset_id}")
        print("Built-in metadata status: Unknown (would be determined by list metadata call)")
        print("\nTo check the actual status, use the list metadata example which shows:")
        print("  response.built_in_field_enabled")
        
    except Exception as e:
        print(f"Error checking built-in status: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata Toggle Built-in Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    print("1. Enabling built-in metadata synchronously...")
    enable_builtin_metadata_sync()
    
    print("\n2. Disabling built-in metadata asynchronously...")
    asyncio.run(disable_builtin_metadata_async())
    
    print("\n3. Interactive toggle with confirmation...")
    toggle_builtin_with_confirmation()
    
    print("\n4. Checking built-in metadata status...")
    check_builtin_status()


if __name__ == "__main__":
    main()