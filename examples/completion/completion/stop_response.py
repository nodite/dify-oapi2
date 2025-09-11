#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.completion.stop_response_request import StopResponseRequest
from dify_oapi.api.completion.v1.model.completion.stop_response_request_body import StopResponseRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def stop_response_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_API_KEY")
        if not api_key:
            raise ValueError("COMPLETION_API_KEY environment variable is required")

        task_id = os.getenv("TASK_ID")
        if not task_id:
            raise ValueError("TASK_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Stop streaming response
        req_body = StopResponseRequestBody.builder().user("user-123").build()

        req = StopResponseRequest.builder().task_id(task_id).request_body(req_body).build()

        response = client.completion.v1.completion.stop_response(req, req_option)

        if response.success:
            print(f"Response stopped: {response.result}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def stop_response_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_API_KEY")
        if not api_key:
            raise ValueError("COMPLETION_API_KEY environment variable is required")

        task_id = os.getenv("TASK_ID")
        if not task_id:
            raise ValueError("TASK_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Stop streaming response
        req_body = StopResponseRequestBody.builder().user("user-123").build()

        req = StopResponseRequest.builder().task_id(task_id).request_body(req_body).build()

        response = await client.completion.v1.completion.astop_response(req, req_option)

        if response.success:
            print(f"Response stopped: {response.result}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Stop Response Examples ===")
    print("Note: Set TASK_ID environment variable from a streaming response")

    print("\n1. Sync stop response:")
    stop_response_sync()

    print("\n2. Async stop response:")
    asyncio.run(stop_response_async())


if __name__ == "__main__":
    main()
