#!/usr/bin/env python3
"""
Document Update Status Example

This example demonstrates how to batch update document status.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.update_document_status_request import UpdateDocumentStatusRequest
from dify_oapi.api.knowledge.v1.model.update_document_status_request_body import UpdateDocumentStatusRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_document_status_sync() -> None:
    """Update document status synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        document_ids = os.getenv("DOCUMENT_IDS")
        if not document_ids:
            raise ValueError("DOCUMENT_IDS environment variable is required (comma-separated list of document IDs)")

        # Parse comma-separated document IDs
        document_id_list = [doc_id.strip() for doc_id in document_ids.split(",")]

        # Action can be 'enable', 'disable', or 'archive'
        action = os.getenv("ACTION", "disable")
        if action not in ["enable", "disable", "archive"]:
            raise ValueError("ACTION must be one of: enable, disable, archive")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = UpdateDocumentStatusRequestBody.builder().document_ids(document_id_list).build()

        request = (
            UpdateDocumentStatusRequest.builder()
            .dataset_id(dataset_id)
            .action(action)
            .request_body(request_body)
            .build()
        )
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.document.update_status(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        print(f"Documents status updated with action '{action}': Success")

    except Exception as e:
        print(f"Error updating document status: {e}")


async def update_document_status_async() -> None:
    """Update document status asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        document_ids = os.getenv("DOCUMENT_IDS")
        if not document_ids:
            raise ValueError("DOCUMENT_IDS environment variable is required (comma-separated list of document IDs)")

        # Parse comma-separated document IDs
        document_id_list = [doc_id.strip() for doc_id in document_ids.split(",")]

        # Action can be 'enable', 'disable', or 'archive'
        action = os.getenv("ACTION", "enable")  # Default to enable for async example
        if action not in ["enable", "disable", "archive"]:
            raise ValueError("ACTION must be one of: enable, disable, archive")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request_body = UpdateDocumentStatusRequestBody.builder().document_ids(document_id_list).build()

        request = (
            UpdateDocumentStatusRequest.builder()
            .dataset_id(dataset_id)
            .action(action)
            .request_body(request_body)
            .build()
        )
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.document.aupdate_status(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print(f"Documents status updated asynchronously with action '{action}': Success")

    except Exception as e:
        print(f"Error updating document status asynchronously: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Document Update Status Examples ===\n")
    print("Note: This example requires:")
    print("  1. A dataset ID set in DATASET_ID environment variable")
    print("  2. A comma-separated list of document IDs in DOCUMENT_IDS environment variable")
    print("  3. Optional ACTION environment variable ('enable', 'disable', or 'archive', default is 'disable')\n")

    print("1. Updating document status synchronously...")
    update_document_status_sync()

    print("\n2. Updating document status asynchronously...")
    asyncio.run(update_document_status_async())


if __name__ == "__main__":
    main()
