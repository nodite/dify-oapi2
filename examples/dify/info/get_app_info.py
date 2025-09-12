"""
Dify System API - Get App Info Example

Demonstrates how to retrieve basic application information.
"""

import os

from dify_oapi.api.dify.v1.model.get_info_request import GetInfoRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_app_info_sync():
    """Synchronous app info retrieval"""

    # Environment validation
    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    # Initialize client
    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    # Build request
    request = GetInfoRequest.builder().build()

    try:
        # Get app info
        response = client.dify.v1.info.get(request, request_option)

        print("Application information retrieved successfully:")
        print(f"App name: {response.name}")
        print(f"App description: {response.description}")
        print(f"App tags: {response.tags}")

        return response

    except Exception as e:
        print(f"Failed to get application info: {e}")
        raise


async def get_app_info_async():
    """Asynchronous app info retrieval"""

    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    request = GetInfoRequest.builder().build()

    try:
        response = await client.dify.v1.info.aget(request, request_option)

        print("Async application info retrieved successfully:")
        print(f"App name: {response.name}")
        print(f"App tags: {response.tags}")

        return response

    except Exception as e:
        print(f"Async app info retrieval failed: {e}")
        raise


if __name__ == "__main__":
    print("=== Dify System API - Get App Info Example ===")
    get_app_info_sync()
