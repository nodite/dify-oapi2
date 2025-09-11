#!/usr/bin/env python3
"""
Stop Chat Message Example

This example demonstrates how to stop chat message generation using the Chatflow API
with both sync and async operations.
"""

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.stop_chat_message_request import StopChatMessageRequest
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request_body import StopChatMessageRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def validate_environment():
    """Validate required environment variables."""
    api_key = os.getenv("CHATFLOW_API_KEY")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    if not api_key:
        raise ValueError("CHATFLOW_API_KEY environment variable is required")
    return api_key, domain


def stop_chat_message():
    """Stop chat message generation (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Example task ID from a streaming chat message
    task_id = "task-12345"  # Replace with actual task ID from streaming response

    # Build request body
    req_body = StopChatMessageRequestBody.builder().user("user-123").build()

    # Build request
    req = StopChatMessageRequest.builder().task_id(task_id).request_body(req_body).build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.chatflow.stop(req, req_option)

    if response.success:
        print("✅ Chat message generation stopped successfully!")
        print(f"Result: {response.result}")
    else:
        print(f"❌ Error: {response.msg}")


async def stop_chat_message_async():
    """Stop chat message generation (async)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Example task ID from a streaming chat message
    task_id = "task-67890"  # Replace with actual task ID from streaming response

    # Build request body
    req_body = StopChatMessageRequestBody.builder().user("user-123").build()

    # Build request
    req = StopChatMessageRequest.builder().task_id(task_id).request_body(req_body).build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute async request
    response = await client.chatflow.v1.chatflow.astop(req, req_option)

    if response.success:
        print("✅ Async chat message generation stopped successfully!")
        print(f"Result: {response.result}")
    else:
        print(f"❌ Error: {response.msg}")


def stop_multiple_tasks():
    """Stop multiple chat message generation tasks."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Example task IDs from multiple streaming chat messages
    task_ids = ["task-111", "task-222", "task-333"]

    for task_id in task_ids:
        print(f"🛑 Stopping task: {task_id}")

        # Build request body
        req_body = StopChatMessageRequestBody.builder().user("user-123").build()

        # Build request
        req = StopChatMessageRequest.builder().task_id(task_id).request_body(req_body).build()

        req_option = RequestOption.builder().api_key(api_key).build()

        # Execute request
        response = client.chatflow.v1.chatflow.stop(req, req_option)

        if response.success:
            print(f"  ✅ Task {task_id} stopped successfully!")
        else:
            print(f"  ❌ Failed to stop task {task_id}: {response.msg}")


def demonstrate_streaming_with_stop():
    """Demonstrate starting a streaming chat and then stopping it."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    print("🔄 This example shows how to stop a streaming chat message.")
    print("In a real scenario, you would:")
    print("1. Start a streaming chat message")
    print("2. Extract the task_id from the streaming response")
    print("3. Use that task_id to stop the generation")
    print()

    # Example of what the task_id extraction would look like:
    print("Example streaming response parsing:")
    print('{"event": "message", "task_id": "task-abc123", "message_id": "msg-xyz789", ...}')
    print("Extract task_id: task-abc123")
    print()

    # Simulate stopping with the extracted task_id
    task_id = "task-abc123"

    # Build request body
    req_body = StopChatMessageRequestBody.builder().user("user-123").build()

    # Build request
    req = StopChatMessageRequest.builder().task_id(task_id).request_body(req_body).build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.chatflow.stop(req, req_option)

    if response.success:
        print("✅ Streaming chat stopped successfully!")
        print(f"Result: {response.result}")
    else:
        print(f"❌ Error: {response.msg}")


def main():
    """Run all stop chat message examples."""
    print("=== Stop Chat Message Examples ===\n")

    try:
        print("1. Stop Chat Message (Sync)")
        stop_chat_message()
        print()

        print("2. Stop Chat Message (Async)")
        asyncio.run(stop_chat_message_async())
        print()

        print("3. Stop Multiple Tasks")
        stop_multiple_tasks()
        print()

        print("4. Streaming with Stop Demonstration")
        demonstrate_streaming_with_stop()
        print()

    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()
