#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.workflow.v1.model.info.get_info_request import GetInfoRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_info_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = GetInfoRequest.builder().build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.info.get_info(req, req_option)

        if response.success:
            print(f"App info: {response.name} - {response.mode}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def get_info_async() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = GetInfoRequest.builder().build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.workflow.v1.info.aget_info(req, req_option)

        if response.success:
            print(f"App info: {response.name} - {response.mode}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Get Info Sync ===")
    get_info_sync()

    print("\n=== Get Info Async ===")
    asyncio.run(get_info_async())
