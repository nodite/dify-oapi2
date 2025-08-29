#!/usr/bin/env python3
"""
Metadata Update Document Example

This example demonstrates how to update document metadata values using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.metadata.update_document_request import (
    UpdateDocumentRequest,
)
from dify_oapi.api.knowledge.v1.model.metadata.update_document_request_body import (
    DocumentMetadata,
    OperationData,
    UpdateDocumentRequestBody,
)
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_document_metadata_sync() -> None:
    """Update document metadata synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        metadata_list = [
            DocumentMetadata.builder()
            .id(os.getenv("METADATA_ID_1", "metadata-id-1"))
            .value("Technical Documentation")
            .name("category")
            .build(),
        ]

        operation_data = [
            OperationData.builder()
            .document_id(os.getenv("DOCUMENT_ID", "doc-id-1"))
            .metadata_list(metadata_list)
            .build()
        ]

        request_body = UpdateDocumentRequestBody.builder().operation_data(operation_data).build()
        request = UpdateDocumentRequest.builder().dataset_id(dataset_id).request_body(request_body).build()

        request_option = RequestOption.builder().api_key(api_key).build()
        client.knowledge.v1.metadata.update_document(request, request_option)

        print(f"Document metadata updated for {len(operation_data)} document(s)")

    except Exception as e:
        print(f"Error updating document metadata: {e}")


async def update_document_metadata_async() -> None:
    """Update document metadata asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        operation_data = [
            OperationData.builder()
            .document_id(os.getenv("DOCUMENT_ID", "doc-id-1"))
            .metadata_list(
                [
                    DocumentMetadata.builder()
                    .id(os.getenv("METADATA_ID_1", "metadata-id-1"))
                    .value("User Guide")
                    .name("category")
                    .build(),
                ]
            )
            .build(),
        ]

        request_body = UpdateDocumentRequestBody.builder().operation_data(operation_data).build()
        request = UpdateDocumentRequest.builder().dataset_id(dataset_id).request_body(request_body).build()

        request_option = RequestOption.builder().api_key(api_key).build()
        await client.knowledge.v1.metadata.aupdate_document(request, request_option)

        print(f"Document metadata updated (async) for {len(operation_data)} documents")

    except Exception as e:
        print(f"Error updating document metadata (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata Update Document Examples ===\n")

    print("1. Updating document metadata synchronously...")
    update_document_metadata_sync()

    print("\n2. Updating document metadata asynchronously...")
    asyncio.run(update_document_metadata_async())


if __name__ == "__main__":
    main()
