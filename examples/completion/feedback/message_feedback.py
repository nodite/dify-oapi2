#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.feedback.message_feedback_request import MessageFeedbackRequest
from dify_oapi.api.completion.v1.model.feedback.message_feedback_request_body import MessageFeedbackRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def message_feedback_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        message_id = os.getenv("MESSAGE_ID")
        if not message_id:
            raise ValueError("MESSAGE_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req_body = (
            MessageFeedbackRequestBody.builder()
            .rating("like")
            .user("[Example] User")
            .content("[Example] This response was helpful")
            .build()
        )

        req = MessageFeedbackRequest.builder().message_id(message_id).request_body(req_body).build()

        response = client.completion.v1.feedback.message_feedback(req, req_option)

        if response.success:
            print(f"Feedback submitted: {response.result}")
        else:
            print(f"Feedback failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def message_feedback_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        message_id = os.getenv("MESSAGE_ID")
        if not message_id:
            raise ValueError("MESSAGE_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req_body = (
            MessageFeedbackRequestBody.builder()
            .rating("like")
            .user("[Example] User")
            .content("[Example] This response was helpful")
            .build()
        )

        req = MessageFeedbackRequest.builder().message_id(message_id).request_body(req_body).build()

        response = await client.completion.v1.feedback.amessage_feedback(req, req_option)

        if response.success:
            print(f"Feedback submitted: {response.result}")
        else:
            print(f"Feedback failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Message Feedback Examples ===")

    print("\n1. Sync Feedback:")
    message_feedback_sync()

    print("\n2. Async Feedback:")
    asyncio.run(message_feedback_async())


if __name__ == "__main__":
    main()
