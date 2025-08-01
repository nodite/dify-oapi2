#!/usr/bin/env python3
"""
Document Update by File Example

This example demonstrates how to update an existing document using file upload.
"""

import asyncio
import os
import tempfile

from dify_oapi.api.knowledge_base.v1.model.document.process_rule import ProcessRule
from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request import UpdateByFileRequest
from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request_body import UpdateByFileRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_sample_file() -> str:
    """Create a temporary sample file for upload."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("[Example] Updated document content for API testing.\n")
        f.write("This file was created programmatically to update an existing document.\n")
        f.write("It contains updated sample text to test document update via file upload.")
        return f.name


def update_document_by_file_sync() -> None:
    """Update a document by file synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        document_id = os.getenv("DOCUMENT_ID")
        if not document_id:
            raise ValueError("DOCUMENT_ID environment variable is required to update a document")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        file_path = create_sample_file()

        try:
            process_rule = ProcessRule.builder().mode("automatic").build()

            request_body = UpdateByFileRequestBody.builder().process_rule(process_rule).file(file_path).build()

            request = (
                UpdateByFileRequest.builder()
                .dataset_id(dataset_id)
                .document_id(document_id)
                .request_body(request_body)
                .build()
            )
            request_option = RequestOption.builder().api_key(api_key).build()

            response = client.knowledge_base.v1.document.update_by_file(request, request_option)

            if not response.success:
                print(f"API Error: {response.code} - {response.msg}")
                return

            if not response.success:
                print(f"API Error: {response.code} - {response.msg}")
                return

            if response.document:
                print(f"Document updated: {response.document.name} (ID: {response.document.id})")
            else:
                print(f"Document updated with batch: {response.batch}")

        finally:
            os.unlink(file_path)

    except Exception as e:
        print(f"Error updating document: {e}")


async def update_document_by_file_async() -> None:
    """Update a document by file asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        document_id = os.getenv("DOCUMENT_ID")
        if not document_id:
            raise ValueError("DOCUMENT_ID environment variable is required to update a document")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        file_path = create_sample_file()

        try:
            process_rule = ProcessRule.builder().mode("automatic").build()

            request_body = UpdateByFileRequestBody.builder().process_rule(process_rule).file(file_path).build()

            request = (
                UpdateByFileRequest.builder()
                .dataset_id(dataset_id)
                .document_id(document_id)
                .request_body(request_body)
                .build()
            )
            request_option = RequestOption.builder().api_key(api_key).build()

            response = await client.knowledge_base.v1.document.aupdate_by_file(request, request_option)

            if not response.success:
                print(f"API Error (async): {response.code} - {response.msg}")
                return

            if not response.success:
                print(f"API Error (async): {response.code} - {response.msg}")
                return

            if response.document:
                print(f"Document updated (async): {response.document.name} (ID: {response.document.id})")
            else:
                print(f"Document updated (async) with batch: {response.batch}")

        finally:
            os.unlink(file_path)

    except Exception as e:
        print(f"Error updating document (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Document Update by File Examples ===\n")
    print("Note: This example requires an existing document ID set in the DOCUMENT_ID environment variable.\n")

    print("1. Updating document by file synchronously...")
    update_document_by_file_sync()

    print("\n2. Updating document by file asynchronously...")
    asyncio.run(update_document_by_file_async())


if __name__ == "__main__":
    main()
