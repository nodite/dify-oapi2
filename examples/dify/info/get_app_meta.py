"""
Dify System API - Get App Meta Example

Demonstrates how to retrieve application metadata and tool icons.
"""

import os

from dify_oapi.api.dify.v1.model.get_meta_request import GetMetaRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_app_meta_sync():
    """Synchronous app metadata retrieval"""

    # Environment validation
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    user_id = os.getenv("USER_ID", "user-123")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    # Initialize client
    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    # Build request
    request = GetMetaRequest.builder().user(user_id).build()

    try:
        # Get app metadata
        response = client.dify.v1.info.meta(request, request_option)

        print("Application metadata retrieved successfully:")
        print(f"Tool icons: {response.tool_icons}")

        if hasattr(response, "tool_labels"):
            print(f"Tool labels: {response.tool_labels}")

        return response

    except Exception as e:
        print(f"Failed to get application metadata: {e}")
        raise


async def get_app_meta_async():
    """Asynchronous app metadata retrieval"""

    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    user_id = os.getenv("USER_ID", "user-123")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    request = GetMetaRequest.builder().user(user_id).build()

    try:
        response = await client.dify.v1.info.ameta(request, request_option)

        print("Async application metadata retrieved successfully:")
        print(f"Tool icons: {response.tool_icons}")

        return response

    except Exception as e:
        print(f"Async app metadata retrieval failed: {e}")
        raise


if __name__ == "__main__":
    print("=== Dify System API - Get App Meta Example ===")
    get_app_meta_sync()
