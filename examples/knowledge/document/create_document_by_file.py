#!/usr/bin/env python3
"""
Document Create by File Example

This example demonstrates how to create a document using file upload.
"""

import asyncio
import os
import tempfile

from dify_oapi.api.knowledge.v1.model.create_document_by_file_request import CreateDocumentByFileRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_file_request_body import CreateDocumentByFileRequestBody
from dify_oapi.api.knowledge.v1.model.create_document_by_file_request_body_data import (
    CreateDocumentByFileRequestBodyData,
)
from dify_oapi.api.knowledge.v1.model.process_rule import ProcessRule
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_sample_file() -> str:
    """Create a temporary sample file for upload."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("[Example] Sample document content for API testing.\n")
        f.write("This file was created programmatically for demonstration purposes.\n")
        f.write("It contains sample text to test document creation via file upload.")
        return f.name


def create_document_by_file_sync() -> None:
    """Create a document by file synchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        file_path = create_sample_file()

        try:
            from io import BytesIO

            # Read file content
            with open(file_path, "rb") as f:
                file_content = f.read()
            file_io = BytesIO(file_content)

            # Create process rule
            process_rule = ProcessRule.builder().mode("automatic").build()

            # Create data object
            data = (
                CreateDocumentByFileRequestBodyData.builder()
                .indexing_technique("economy")
                .process_rule(process_rule)
                .build()
            )

            request_body = CreateDocumentByFileRequestBody.builder().data(data).build()

            request = (
                CreateDocumentByFileRequest.builder()
                .dataset_id(dataset_id)
                .request_body(request_body)
                .file(file_io, os.path.basename(file_path))
                .build()
            )
            request_option = RequestOption.builder().api_key(api_key).build()

            response = client.knowledge.v1.document.create_by_file(request, request_option)

            if not response.success:
                print(f"API Error: {response.code} - {response.msg}")
                return

            if response.document:
                print(f"Document created: {response.document.name} (ID: {response.document.id})")
            else:
                print(f"Document created with batch: {response.batch}")

        finally:
            os.unlink(file_path)

    except Exception as e:
        print(f"Error creating document: {e}")


async def create_document_by_file_async() -> None:
    """Create a document by file asynchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        file_path = create_sample_file()

        try:
            from io import BytesIO

            # Read file content
            with open(file_path, "rb") as f:
                file_content = f.read()
            file_io = BytesIO(file_content)

            # Create process rule
            process_rule = ProcessRule.builder().mode("automatic").build()

            # Create data object
            data = (
                CreateDocumentByFileRequestBodyData.builder()
                .indexing_technique("economy")
                .process_rule(process_rule)
                .build()
            )

            request_body = CreateDocumentByFileRequestBody.builder().data(data).build()

            request = (
                CreateDocumentByFileRequest.builder()
                .dataset_id(dataset_id)
                .request_body(request_body)
                .file(file_io, os.path.basename(file_path))
                .build()
            )
            request_option = RequestOption.builder().api_key(api_key).build()

            response = await client.knowledge.v1.document.acreate_by_file(request, request_option)

            if not response.success:
                print(f"API Error (async): {response.code} - {response.msg}")
                return

            if response.document:
                print(f"Document created (async): {response.document.name} (ID: {response.document.id})")
            else:
                print(f"Document created (async) with batch: {response.batch}")

        finally:
            os.unlink(file_path)

    except Exception as e:
        print(f"Error creating document (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Document Create by File Examples ===\n")

    print("1. Creating document by file synchronously...")
    create_document_by_file_sync()

    print("\n2. Creating document by file asynchronously...")
    asyncio.run(create_document_by_file_async())


if __name__ == "__main__":
    main()
