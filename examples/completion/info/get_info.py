#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.info.get_info_request import GetInfoRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_info_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req = GetInfoRequest.builder().build()
        response = client.completion.v1.info.get_info(req, req_option)

        if response.success:
            print(f"App Name: {response.name}")
            print(f"Description: {response.description}")
            print(f"Mode: {response.mode}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def get_info_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req = GetInfoRequest.builder().build()
        response = await client.completion.v1.info.aget_info(req, req_option)

        if response.success:
            print(f"App Name (async): {response.name}")
            print(f"Description (async): {response.description}")
            print(f"Mode (async): {response.mode}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Get Info Examples ===")

    print("\n1. Sync get info:")
    get_info_sync()

    print("\n2. Async get info:")
    asyncio.run(get_info_async())


if __name__ == "__main__":
    main()
