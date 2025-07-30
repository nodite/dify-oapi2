#!/usr/bin/env python3
"""
Document Update by Text Example

This example demonstrates how to update an existing document using text content.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.document.process_rule import ProcessRule
from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_request import UpdateByTextRequest
from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_request_body import UpdateByTextRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_document_by_text_sync() -> None:
    """Update a document by text synchronously."""
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

        process_rule = ProcessRule.builder().mode("automatic").build()

        request_body = (
            UpdateByTextRequestBody.builder()
            .name("[Example] Updated API Documentation")
            .text(
                "[Example] This is updated text content. The document has been modified with new information through the Dify API."
            )
            .process_rule(process_rule)
            .build()
        )

        request = (
            UpdateByTextRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .request_body(request_body)
            .build()
        )
        request_option = RequestOption.builder().api_key(api_key).build()

        response = client.knowledge_base.v1.document.update_by_text(request, request_option)

        if response.document:
            print(f"Document updated: {response.document.name} (ID: {response.document.id})")
        else:
            print(f"Document updated with batch: {response.batch}")

    except Exception as e:
        print(f"Error updating document: {e}")


async def update_document_by_text_async() -> None:
    """Update a document by text asynchronously."""
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

        process_rule = ProcessRule.builder().mode("automatic").build()

        request_body = (
            UpdateByTextRequestBody.builder()
            .name("[Example] Updated API Documentation (Async)")
            .text(
                "[Example] This is updated text content using async methods. The document has been modified asynchronously through the Dify API."
            )
            .process_rule(process_rule)
            .build()
        )

        request = (
            UpdateByTextRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .request_body(request_body)
            .build()
        )
        request_option = RequestOption.builder().api_key(api_key).build()

        response = await client.knowledge_base.v1.document.aupdate_by_text(request, request_option)

        if response.document:
            print(f"Document updated (async): {response.document.name} (ID: {response.document.id})")
        else:
            print(f"Document updated (async) with batch: {response.batch}")

    except Exception as e:
        print(f"Error updating document (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Document Update by Text Examples ===\n")
    print("Note: This example requires an existing document ID set in the DOCUMENT_ID environment variable.\n")

    print("1. Updating document by text synchronously...")
    update_document_by_text_sync()

    print("\n2. Updating document by text asynchronously...")
    asyncio.run(update_document_by_text_async())


if __name__ == "__main__":
    main()
