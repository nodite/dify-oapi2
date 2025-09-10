#!/usr/bin/env python3
"""
Message Feedback Example

This example demonstrates how to provide feedback for messages using the Chatflow Feedback API
with both sync and async operations, supporting different feedback types.
"""

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.message_feedback_request import MessageFeedbackRequest
from dify_oapi.api.chatflow.v1.model.message_feedback_request_body import MessageFeedbackRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def validate_environment():
    """Validate required environment variables."""
    api_key = os.getenv("API_KEY")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")
    return api_key, domain


def provide_like_feedback():
    """Provide like feedback for a message (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    req_body = (
        MessageFeedbackRequestBody.builder()
        .rating("like")
        .user("user-123")
        .content("This response was very helpful and accurate!")
        .build()
    )

    # Build request
    req = MessageFeedbackRequest.builder().message_id("[Example]_message_12345").request_body(req_body).build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.feedback.message(req, req_option)

    if response.success:
        print("✅ Like feedback submitted successfully!")
        print(f"Result: {response.result}")
    else:
        print(f"❌ Error: {response.msg}")


def provide_dislike_feedback():
    """Provide dislike feedback for a message (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    req_body = (
        MessageFeedbackRequestBody.builder()
        .rating("dislike")
        .user("user-123")
        .content("The response was not accurate and didn't address my question properly.")
        .build()
    )

    # Build request
    req = MessageFeedbackRequest.builder().message_id("[Example]_message_67890").request_body(req_body).build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.feedback.message(req, req_option)

    if response.success:
        print("✅ Dislike feedback submitted successfully!")
        print(f"Result: {response.result}")
    else:
        print(f"❌ Error: {response.msg}")


async def provide_feedback_async():
    """Provide feedback for a message (async)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    req_body = (
        MessageFeedbackRequestBody.builder()
        .rating("like")
        .user("user-123")
        .content("Async feedback: This was a great response!")
        .build()
    )

    # Build request
    req = MessageFeedbackRequest.builder().message_id("[Example]_async_message_99999").request_body(req_body).build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute async request
    response = await client.chatflow.v1.feedback.amessage(req, req_option)

    if response.success:
        print("✅ Async feedback submitted successfully!")
        print(f"Result: {response.result}")
    else:
        print(f"❌ Error: {response.msg}")


if __name__ == "__main__":
    print("🔄 Running Message Feedback Examples...")
    print()

    # Run sync examples
    print("=== Sync Examples ===")
    provide_like_feedback()
    print()
    provide_dislike_feedback()
    print()

    # Run async example
    print("=== Async Examples ===")
    asyncio.run(provide_feedback_async())
    print()

    print("✅ All Message Feedback examples completed!")
