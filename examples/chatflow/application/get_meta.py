#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.get_meta_request import GetMetaRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_meta_sync():
    """Get application meta information synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = GetMetaRequest.builder().build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.application.meta(request, request_option)

        if response.success:
            if response.tool_icons:
                print(f"Tool Icons: {len(response.tool_icons)} tools configured")
                for tool_name, icon_info in response.tool_icons.items():
                    if isinstance(icon_info, str):
                        print(f"  {tool_name}: {icon_info}")
                    else:
                        print(f"  {tool_name}: background={icon_info.background}, content={icon_info.content}")
            else:
                print("No tool icons configured")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def get_meta_async():
    """Get application meta information asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = GetMetaRequest.builder().build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.application.ameta(request, request_option)

        if response.success:
            if response.tool_icons:
                print(f"Tool Icons (async): {len(response.tool_icons)} tools configured")
                for tool_name, icon_info in response.tool_icons.items():
                    print(f"  {tool_name}: {icon_info}")
            else:
                print("No tool icons configured")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Get Application Meta Examples ===")

    print("\n1. Sync Example:")
    get_meta_sync()

    print("\n2. Async Example:")
    asyncio.run(get_meta_async())
