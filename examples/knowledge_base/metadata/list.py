#!/usr/bin/env python3
"""
Metadata List Example

This example demonstrates how to list metadata for a dataset using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.metadata.list_request import ListMetadataRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_metadata_sync() -> None:
    """List metadata synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build list metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = ListMetadataRequest.builder().dataset_id(dataset_id).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # List metadata
        response = client.knowledge_base.v1.metadata.list(request, request_option)
        
        print(f"Metadata Configuration for Dataset {dataset_id}:")
        print(f"Built-in field enabled: {response.built_in_field_enabled}")
        print(f"Custom metadata count: {len(response.doc_metadata)}")
        
        if response.doc_metadata:
            print(f"\nCustom Metadata Fields:")
            for metadata in response.doc_metadata:
                print(f"  - Name: {metadata.name}")
                print(f"    ID: {metadata.id}")
                print(f"    Type: {metadata.type}")
                print(f"    Use count: {metadata.use_count}")
                print()
        else:
            print("\nNo custom metadata fields found.")
        
    except Exception as e:
        print(f"Error listing metadata: {e}")


async def list_metadata_async() -> None:
    """List metadata asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build list metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = ListMetadataRequest.builder().dataset_id(dataset_id).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # List metadata asynchronously
        response = await client.knowledge_base.v1.metadata.alist(request, request_option)
        
        print(f"Metadata Configuration (Async):")
        print(f"Built-in fields: {'Enabled' if response.built_in_field_enabled else 'Disabled'}")
        
        if response.doc_metadata:
            print(f"\nMetadata Fields Summary:")
            
            # Group by type
            by_type = {}
            for metadata in response.doc_metadata:
                if metadata.type not in by_type:
                    by_type[metadata.type] = []
                by_type[metadata.type].append(metadata)
            
            for metadata_type, fields in by_type.items():
                print(f"\n{metadata_type.upper()} fields:")
                for field in fields:
                    usage_info = f"(used {field.use_count} times)" if field.use_count > 0 else "(unused)"
                    print(f"  • {field.name} {usage_info}")
        else:
            print("\nNo custom metadata configured.")
        
    except Exception as e:
        print(f"Error listing metadata (async): {e}")


def analyze_metadata_usage() -> None:
    """Analyze metadata usage patterns."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build list metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = ListMetadataRequest.builder().dataset_id(dataset_id).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # List metadata
        response = client.knowledge_base.v1.metadata.list(request, request_option)
        
        print(f"Metadata Usage Analysis:")
        
        if not response.doc_metadata:
            print("No metadata fields to analyze.")
            return
        
        # Calculate statistics
        total_fields = len(response.doc_metadata)
        used_fields = [m for m in response.doc_metadata if m.use_count > 0]
        unused_fields = [m for m in response.doc_metadata if m.use_count == 0]
        
        total_usage = sum(m.use_count for m in response.doc_metadata)
        
        print(f"\nStatistics:")
        print(f"  Total metadata fields: {total_fields}")
        print(f"  Used fields: {len(used_fields)}")
        print(f"  Unused fields: {len(unused_fields)}")
        print(f"  Total usage count: {total_usage}")
        
        if used_fields:
            print(f"\nMost used fields:")
            sorted_fields = sorted(used_fields, key=lambda x: x.use_count, reverse=True)
            for field in sorted_fields[:5]:  # Top 5
                print(f"  • {field.name}: {field.use_count} uses")
        
        if unused_fields:
            print(f"\nUnused fields:")
            for field in unused_fields:
                print(f"  • {field.name} ({field.type})")
        
        # Type distribution
        type_counts = {}
        for metadata in response.doc_metadata:
            type_counts[metadata.type] = type_counts.get(metadata.type, 0) + 1
        
        print(f"\nType distribution:")
        for metadata_type, count in type_counts.items():
            print(f"  • {metadata_type}: {count} fields")
        
    except Exception as e:
        print(f"Error analyzing metadata usage: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata List Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    print("1. Listing metadata synchronously...")
    list_metadata_sync()
    
    print("\n2. Listing metadata asynchronously...")
    asyncio.run(list_metadata_async())
    
    print("\n3. Analyzing metadata usage...")
    analyze_metadata_usage()


if __name__ == "__main__":
    main()