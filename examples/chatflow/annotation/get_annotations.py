#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.get_annotations_request import GetAnnotationsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_annotations_sync():
    """Get annotation list synchronously with pagination."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = GetAnnotationsRequest.builder().page(1).limit(20).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.annotation.list(request, request_option)

        if response.success:
            print(f"Retrieved {len(response.data)} annotations")
            print(f"Page: {response.page}")
            print(f"Limit: {response.limit}")
            print(f"Total: {response.total}")
            print(f"Has more: {response.has_more}")

            for annotation in response.data:
                print(f"Annotation ID: {annotation.id}")
                print(f"Question: {annotation.question}")
                print(f"Answer: {annotation.answer[:100]}...")
                print(f"Hit Count: {annotation.hit_count}")
                print(f"Created at: {annotation.created_at}")
                print("---")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def get_annotations_async():
    """Get annotation list asynchronously with pagination."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request with different pagination
    request = GetAnnotationsRequest.builder().page(1).limit(10).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.annotation.alist(request, request_option)

        if response.success:
            print(f"Retrieved {len(response.data)} annotations (async)")
            print(f"Total annotations: {response.total}")

            for annotation in response.data:
                print(f"ID: {annotation.id}")
                print(f"Q: {annotation.question[:50]}...")
                print(f"A: {annotation.answer[:50]}...")
                print(f"Hits: {annotation.hit_count}")
                print("---")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def get_annotations_with_pagination():
    """Get all annotations with pagination example."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        page = 1
        all_annotations = []

        while True:
            # Build request for current page
            request = GetAnnotationsRequest.builder().page(page).limit(5).build()

            # Execute request
            response = client.chatflow.v1.annotation.list(request, request_option)

            if response.success:
                print(f"Page {page}: Retrieved {len(response.data)} annotations")
                all_annotations.extend(response.data)

                if not response.has_more:
                    print("Reached end of annotations")
                    break

                page += 1
            else:
                print(f"Error: {response.msg}")
                break

        print(f"Total annotations retrieved: {len(all_annotations)}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Get Annotations Examples ===")

    print("\n1. Sync Example:")
    get_annotations_sync()

    print("\n2. Async Example:")
    asyncio.run(get_annotations_async())

    print("\n3. Pagination Example:")
    get_annotations_with_pagination()
