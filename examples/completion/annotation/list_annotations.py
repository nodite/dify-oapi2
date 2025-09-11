#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.annotation.list_annotations_request import ListAnnotationsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_annotations_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_API_KEY")
        if not api_key:
            raise ValueError("COMPLETION_API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req = ListAnnotationsRequest.builder().page("1").limit("10").build()
        response = client.completion.v1.annotation.list_annotations(req, req_option)

        if response.success:
            print(f"Total annotations: {response.total}")
            print(f"Current page: {response.page}")
            print(f"Annotations count: {len(response.data or [])}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def list_annotations_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_API_KEY")
        if not api_key:
            raise ValueError("COMPLETION_API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req = ListAnnotationsRequest.builder().page("1").limit("10").build()
        response = await client.completion.v1.annotation.alist_annotations(req, req_option)

        if response.success:
            print(f"Total annotations (async): {response.total}")
            print(f"Current page (async): {response.page}")
            print(f"Annotations count (async): {len(response.data or [])}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== List Annotations Examples ===")

    print("\n1. Sync list annotations:")
    list_annotations_sync()

    print("\n2. Async list annotations:")
    asyncio.run(list_annotations_async())


if __name__ == "__main__":
    main()
