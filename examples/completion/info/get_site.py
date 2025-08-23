#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.info.get_site_request import GetSiteRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_site_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req = GetSiteRequest.builder().build()
        response = client.completion.v1.info.get_site(req, req_option)

        if response.success:
            print(f"Title: {response.title}")
            print(f"Description: {response.description}")
            print(f"Icon Type: {response.icon_type}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def get_site_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req = GetSiteRequest.builder().build()
        response = await client.completion.v1.info.aget_site(req, req_option)

        if response.success:
            print(f"Title (async): {response.title}")
            print(f"Description (async): {response.description}")
            print(f"Icon Type (async): {response.icon_type}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Get Site Examples ===")

    print("\n1. Sync get site:")
    get_site_sync()

    print("\n2. Async get site:")
    asyncio.run(get_site_async())


if __name__ == "__main__":
    main()
