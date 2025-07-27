#!/usr/bin/env python3
"""
Metadata Toggle Built-in Example

This example demonstrates how to enable or disable built-in metadata using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.metadata.toggle_builtin_request import ToggleBuiltinRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def enable_builtin_metadata_sync() -> None:
    """Enable built-in metadata synchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = ToggleBuiltinRequest.builder().dataset_id(dataset_id).action("enable").build()

        request_option = RequestOption.builder().api_key(api_key).build()
        client.knowledge_base.v1.metadata.toggle_builtin(request, request_option)

        print("Built-in metadata enabled")

    except Exception as e:
        print(f"Error enabling built-in metadata: {e}")


async def disable_builtin_metadata_async() -> None:
    """Disable built-in metadata asynchronously."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        request = ToggleBuiltinRequest.builder().dataset_id(dataset_id).action("disable").build()

        request_option = RequestOption.builder().api_key(api_key).build()
        await client.knowledge_base.v1.metadata.atoggle_builtin(request, request_option)

        print("Built-in metadata disabled (async)")

    except Exception as e:
        print(f"Error disabling built-in metadata (async): {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Metadata Toggle Built-in Examples ===\n")

    print("1. Enabling built-in metadata synchronously...")
    enable_builtin_metadata_sync()

    print("\n2. Disabling built-in metadata asynchronously...")
    asyncio.run(disable_builtin_metadata_async())


if __name__ == "__main__":
    main()
