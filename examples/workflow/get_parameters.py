#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.workflow.v1.model.get_parameters_request import GetParametersRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_parameters_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = GetParametersRequest.builder().build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.workflow.parameters(req, req_option)

        if response.success:
            print(f"Parameters retrieved: {len(response.user_input_form or [])} input forms")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def get_parameters_async() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = GetParametersRequest.builder().build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.workflow.v1.workflow.aparameters(req, req_option)

        if response.success:
            print(f"Parameters retrieved: {len(response.user_input_form or [])} input forms")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Get Parameters Sync ===")
    get_parameters_sync()

    print("\n=== Get Parameters Async ===")
    asyncio.run(get_parameters_async())
