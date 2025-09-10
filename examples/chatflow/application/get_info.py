#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.get_info_request import GetInfoRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_info_sync():
    """Get application basic information synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = GetInfoRequest.builder().build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.application.info(request, request_option)

        if response.success:
            print(f"Application Name: {response.name}")
            print(f"Description: {response.description}")
            print(f"Tags: {', '.join(response.tags) if response.tags else 'None'}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def get_info_async():
    """Get application basic information asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = GetInfoRequest.builder().build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.application.ainfo(request, request_option)

        if response.success:
            print(f"Application Name: {response.name}")
            print(f"Description: {response.description}")
            print(f"Tags: {', '.join(response.tags) if response.tags else 'None'}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Get Application Info Examples ===")

    print("\n1. Sync Example:")
    get_info_sync()

    print("\n2. Async Example:")
    asyncio.run(get_info_async())
