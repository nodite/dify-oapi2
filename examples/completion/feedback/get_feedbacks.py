#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.feedback.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_feedbacks_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req = GetFeedbacksRequest.builder().page("1").limit("10").build()

        response = client.completion.v1.feedback.get_feedbacks(req, req_option)

        if response.success:
            print(f"Found {len(response.data or [])} feedbacks")
            for feedback in response.data or []:
                print(f"- {feedback.rating}: {feedback.content}")
        else:
            print(f"Get feedbacks failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def get_feedbacks_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req = GetFeedbacksRequest.builder().page("1").limit("10").build()

        response = await client.completion.v1.feedback.aget_feedbacks(req, req_option)

        if response.success:
            print(f"Found {len(response.data or [])} feedbacks")
            for feedback in response.data or []:
                print(f"- {feedback.rating}: {feedback.content}")
        else:
            print(f"Get feedbacks failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Get Feedbacks Examples ===")

    print("\n1. Sync Get Feedbacks:")
    get_feedbacks_sync()

    print("\n2. Async Get Feedbacks:")
    asyncio.run(get_feedbacks_async())


if __name__ == "__main__":
    main()
