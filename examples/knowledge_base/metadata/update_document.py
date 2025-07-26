#!/usr/bin/env python3
"""
Metadata Update Document Example

This example demonstrates how to update document metadata values using the Dify API.
"""

import asyncio
import os
from typing import List, Dict, Any

from dify_oapi.api.knowledge_base.v1.model.metadata.update_document_request import UpdateDocumentMetadataRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_document_metadata_sync() -> None:
    """Update document metadata synchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build operation data for updating document metadata
        operation_data = [
            {
                "document_id": os.getenv("DOCUMENT_ID_1", "doc-id-1"),
                "metadata_list": [
                    {
                        "id": os.getenv("METADATA_ID_1", "metadata-id-1"),
                        "value": "Technical Documentation",
                        "name": "category"
                    },
                    {
                        "id": os.getenv("METADATA_ID_2", "metadata-id-2"),
                        "value": "5",
                        "name": "priority"
                    }
                ]
            }
        ]
        
        # Build update document metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            UpdateDocumentMetadataRequest.builder()
            .dataset_id(dataset_id)
            .operation_data(operation_data)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Update document metadata
        response = client.knowledge_base.v1.metadata.update_document(request, request_option)
        
        print(f"Document metadata updated successfully!")
        print(f"Result: {response.result}")
        print(f"Updated metadata for {len(operation_data)} document(s)")
        
    except Exception as e:
        print(f"Error updating document metadata: {e}")


async def update_document_metadata_async() -> None:
    """Update document metadata asynchronously."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Build operation data for multiple documents
        operation_data = [
            {
                "document_id": os.getenv("DOCUMENT_ID_2", "doc-id-2"),
                "metadata_list": [
                    {
                        "id": os.getenv("METADATA_ID_1", "metadata-id-1"),
                        "value": "User Guide",
                        "name": "category"
                    },
                    {
                        "id": os.getenv("METADATA_ID_3", "metadata-id-3"),
                        "value": "John Doe",
                        "name": "author"
                    }
                ]
            },
            {
                "document_id": os.getenv("DOCUMENT_ID_3", "doc-id-3"),
                "metadata_list": [
                    {
                        "id": os.getenv("METADATA_ID_1", "metadata-id-1"),
                        "value": "API Reference",
                        "name": "category"
                    },
                    {
                        "id": os.getenv("METADATA_ID_2", "metadata-id-2"),
                        "value": "8",
                        "name": "priority"
                    }
                ]
            }
        ]
        
        # Build update document metadata request
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        request = (
            UpdateDocumentMetadataRequest.builder()
            .dataset_id(dataset_id)
            .operation_data(operation_data)
            .build()
        )
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        
        # Update document metadata asynchronously
        response = await client.knowledge_base.v1.metadata.aupdate_document(request, request_option)
        
        print(f"Document metadata updated successfully (async)!")
        print(f"Result: {response.result}")
        print(f"Updated metadata for {len(operation_data)} documents")
        
        # Show what was updated
        for i, doc_data in enumerate(operation_data, 1):
            print(f"\nDocument {i} ({doc_data['document_id']}):")
            for metadata in doc_data['metadata_list']:
                print(f"  • {metadata['name']}: {metadata['value']}")
        
    except Exception as e:
        print(f"Error updating document metadata (async): {e}")


def bulk_update_document_metadata() -> None:
    """Bulk update metadata for multiple documents."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        
        # Define bulk update data
        documents_to_update = [
            {
                "document_id": "doc-1",
                "updates": {"category": "Manual", "status": "Published", "version": "1.0"}
            },
            {
                "document_id": "doc-2", 
                "updates": {"category": "Tutorial", "status": "Draft", "author": "Jane Smith"}
            },
            {
                "document_id": "doc-3",
                "updates": {"category": "FAQ", "status": "Published", "priority": "3"}
            }
        ]
        
        # Convert to operation data format
        operation_data = []
        
        for doc_info in documents_to_update:
            metadata_list = []
            for field_name, field_value in doc_info["updates"].items():
                # In a real implementation, you'd need to map field names to metadata IDs
                metadata_list.append({
                    "id": f"metadata-{field_name}-id",  # Placeholder ID
                    "value": str(field_value),
                    "name": field_name
                })
            
            operation_data.append({
                "document_id": doc_info["document_id"],
                "metadata_list": metadata_list
            })
        
        print(f"Preparing to update metadata for {len(operation_data)} documents...")
        
        # Show what will be updated
        for i, doc_data in enumerate(operation_data, 1):
            print(f"\nDocument {i} ({doc_data['document_id']}):")
            for metadata in doc_data['metadata_list']:
                print(f"  • {metadata['name']}: {metadata['value']}")
        
        print(f"\nProceed with bulk update? (y/N): ", end="")
        confirmation = input().strip().lower()
        
        if confirmation != 'y':
            print("Bulk update cancelled.")
            return
        
        # Build request
        request = (
            UpdateDocumentMetadataRequest.builder()
            .dataset_id(dataset_id)
            .operation_data(operation_data)
            .build()
        )
        
        # Execute bulk update
        response = client.knowledge_base.v1.metadata.update_document(request, request_option)
        
        print(f"\nBulk update completed successfully!")
        print(f"Result: {response.result}")
        print(f"Updated metadata for {len(operation_data)} documents")
        
    except Exception as e:
        print(f"Error in bulk update: {e}")


def update_document_with_validation() -> None:
    """Update document metadata with value validation."""
    try:
        # Initialize client
        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        
        # Set up request options
        request_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()
        dataset_id = os.getenv("DATASET_ID", "your-dataset-id-here")
        document_id = os.getenv("DOCUMENT_ID", "your-document-id-here")
        
        # Define metadata updates with validation
        metadata_updates = [
            {
                "id": "category-metadata-id",
                "name": "category",
                "value": "Technical",
                "validation": lambda x: x in ["Technical", "User Guide", "FAQ", "Tutorial"]
            },
            {
                "id": "priority-metadata-id", 
                "name": "priority",
                "value": "7",
                "validation": lambda x: x.isdigit() and 1 <= int(x) <= 10
            },
            {
                "id": "status-metadata-id",
                "name": "status", 
                "value": "Published",
                "validation": lambda x: x in ["Draft", "Review", "Published", "Archived"]
            }
        ]
        
        # Validate all values
        validated_metadata = []
        validation_errors = []
        
        for metadata in metadata_updates:
            if metadata["validation"](metadata["value"]):
                validated_metadata.append({
                    "id": metadata["id"],
                    "value": metadata["value"],
                    "name": metadata["name"]
                })
                print(f"✓ {metadata['name']}: {metadata['value']} (valid)")
            else:
                validation_errors.append(f"✗ {metadata['name']}: {metadata['value']} (invalid)")
        
        if validation_errors:
            print("\nValidation errors:")
            for error in validation_errors:
                print(f"  {error}")
            print("\nPlease fix validation errors before proceeding.")
            return
        
        # Build operation data
        operation_data = [{
            "document_id": document_id,
            "metadata_list": validated_metadata
        }]
        
        # Build request
        request = (
            UpdateDocumentMetadataRequest.builder()
            .dataset_id(dataset_id)
            .operation_data(operation_data)
            .build()
        )
        
        # Update document metadata
        response = client.knowledge_base.v1.metadata.update_document(request, request_option)
        
        print(f"\nDocument metadata updated with validation!")
        print(f"Result: {response.result}")
        print(f"Updated {len(validated_metadata)} metadata fields")
        
    except Exception as e:
        print(f"Error updating document metadata with validation: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata Update Document Examples ===\n")
    
    # Check for required environment variables
    if not os.getenv("API_KEY"):
        print("Please set the API_KEY environment variable")
        return
    
    if not os.getenv("DATASET_ID"):
        print("Please set the DATASET_ID environment variable")
        return
    
    print("1. Updating document metadata synchronously...")
    update_document_metadata_sync()
    
    print("\n2. Updating document metadata asynchronously...")
    asyncio.run(update_document_metadata_async())
    
    print("\n3. Bulk update document metadata...")
    bulk_update_document_metadata()
    
    print("\n4. Update document metadata with validation...")
    update_document_with_validation()


if __name__ == "__main__":
    main()