#!/usr/bin/env python3
"""
Document Get Upload File Example

This example demonstrates how to get upload file information for a document.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.get_upload_file_info_request import GetUploadFileInfoRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_document_upload_file_sync() -> None:
    """Get document upload file information synchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        document_id = os.getenv("DOCUMENT_ID")
        if not document_id:
            raise ValueError("DOCUMENT_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = GetUploadFileInfoRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.document.file_info(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        if response.id:
            print("Upload File Information:")
            print(f"  ID: {response.id}")
            print(f"  Name: {response.name}")
            print(f"  Size: {response.size} bytes")
            print(f"  Extension: {response.extension}")
            print(f"  MIME Type: {response.mime_type}")
            print(f"  Created By: {response.created_by}")
            print(f"  Created At: {response.created_at}")
        else:
            print("No upload file information available or document was not created from a file upload")

    except Exception as e:
        print(f"Error getting upload file information: {e}")


async def get_document_upload_file_async() -> None:
    """Get document upload file information asynchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        document_id = os.getenv("DOCUMENT_ID")
        if not document_id:
            raise ValueError("DOCUMENT_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = GetUploadFileInfoRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.document.afile_info(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        print("\nAsync Upload File Information:")
        if response.id:
            print(f"  ID: {response.id}")
            print(f"  Name: {response.name}")
            print(f"  Size: {response.size} bytes")
            print(f"  Extension: {response.extension}")
        else:
            print("No upload file information available (async) or document was not created from a file upload")

    except Exception as e:
        print(f"Error getting upload file information asynchronously: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Document Get Upload File Examples ===\n")
    print("Note: This example requires a document ID set in the DOCUMENT_ID environment variable.\n")

    print("1. Getting upload file information synchronously...")
    get_document_upload_file_sync()

    print("\n2. Getting upload file information asynchronously...")
    asyncio.run(get_document_upload_file_async())


if __name__ == "__main__":
    main()
