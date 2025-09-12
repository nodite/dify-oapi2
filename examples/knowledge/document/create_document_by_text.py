#!/usr/bin/env python3
"""
Document Create by Text Example

This example demonstrates how to create a document using text content.
"""

import asyncio
import os

from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import CreateDocumentByTextRequestBody
from dify_oapi.api.knowledge.v1.model.process_rule import ProcessRule
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_document_by_text_sync() -> None:
    """Create a document by text synchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        process_rule = ProcessRule.builder().mode("automatic").build()

        request_body = (
            CreateDocumentByTextRequestBody.builder()
            .name("[Example] API Documentation")
            .text(
                "[Example] This is sample text content for API testing. It demonstrates how to create documents programmatically using the Dify API."
            )
            .indexing_technique("economy")
            .process_rule(process_rule)
            .build()
        )

        request = CreateDocumentByTextRequest.builder().dataset_id(dataset_id).request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge.v1.document.create_by_text(request, request_option)

        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return

        if response.document:
            print(f"Document created: {response.document.name} (ID: {response.document.id})")
        else:
            print(f"Document created with batch: {response.batch}")

    except Exception as e:
        print(f"Error creating document: {e}")


async def create_document_by_text_async() -> None:
    """Create a document by text asynchronously."""
    try:
        api_key = os.getenv("KNOWLEDGE_KEY")
        if not api_key:
            raise ValueError("KNOWLEDGE_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        process_rule = ProcessRule.builder().mode("automatic").build()

        request_body = (
            CreateDocumentByTextRequestBody.builder()
            .name("[Example] API Guide (Async)")
            .text(
                "[Example] This is sample text content created asynchronously. It shows how to use async operations with the Dify API."
            )
            .indexing_technique("economy")
            .process_rule(process_rule)
            .build()
        )

        request = CreateDocumentByTextRequest.builder().dataset_id(dataset_id).request_body(request_body).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge.v1.document.acreate_by_text(request, request_option)

        if not response.success:
            print(f"API Error (async): {response.code} - {response.msg}")
            return

        if response.document:
            print(f"Document created (async): {response.document.name} (ID: {response.document.id})")
        else:
            print(f"Document created (async) with batch: {response.batch}")

    except Exception as e:
        print(f"Error creating document (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Document Create by Text Examples ===\n")

    print("1. Creating document by text synchronously...")
    create_document_by_text_sync()

    print("\n2. Creating document by text asynchronously...")
    asyncio.run(create_document_by_text_async())


if __name__ == "__main__":
    main()
