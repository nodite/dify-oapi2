#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.info.get_parameters_request import GetParametersRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_parameters_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req = GetParametersRequest.builder().build()
        response = client.completion.v1.info.get_parameters(req, req_option)

        if response.success:
            print(f"Opening Statement: {response.opening_statement}")
            print(f"Suggested Questions: {len(response.suggested_questions or [])}")
            print(f"User Input Form: {len(response.user_input_form or [])}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def get_parameters_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req = GetParametersRequest.builder().build()
        response = await client.completion.v1.info.aget_parameters(req, req_option)

        if response.success:
            print(f"Opening Statement (async): {response.opening_statement}")
            print(f"Suggested Questions (async): {len(response.suggested_questions or [])}")
            print(f"User Input Form (async): {len(response.user_input_form or [])}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Get Parameters Examples ===")

    print("\n1. Sync get parameters:")
    get_parameters_sync()

    print("\n2. Async get parameters:")
    asyncio.run(get_parameters_async())


if __name__ == "__main__":
    main()
