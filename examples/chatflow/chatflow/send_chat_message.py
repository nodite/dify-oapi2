#!/usr/bin/env python3
"""
Send Chat Message Example

This example demonstrates how to send chat messages using the Chatflow API
with both streaming and blocking modes, sync and async operations.
"""

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.chat_file import ChatFile
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def validate_environment():
    """Validate required environment variables."""
    api_key = os.getenv("API_KEY")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")
    return api_key, domain


def send_chat_message_blocking():
    """Send chat message in blocking mode (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    req_body = (
        SendChatMessageRequestBody.builder()
        .query("What can Dify API do?")
        .response_mode("blocking")
        .user("user-123")
        .inputs({})
        .auto_generate_name(True)
        .build()
    )

    # Build request
    req = SendChatMessageRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.chatflow.send(req, req_option, False)

    if response.success:
        print("✅ Chat message sent successfully!")
        print(f"Message ID: {response.id}")
        print(f"Conversation ID: {response.conversation_id}")
        print(f"Answer: {response.answer}")
    else:
        print(f"❌ Error: {response.msg}")


def send_chat_message_streaming():
    """Send chat message in streaming mode (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body for streaming
    req_body = (
        SendChatMessageRequestBody.builder()
        .query("Tell me a story about AI")
        .response_mode("streaming")
        .user("user-123")
        .inputs({})
        .auto_generate_name(True)
        .build()
    )

    # Build request
    req = SendChatMessageRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute streaming request
    print("🔄 Streaming response:")
    response = client.chatflow.v1.chatflow.send(req, req_option, True)

    for chunk in response:
        print(chunk.decode("utf-8"), end="", flush=True)
    print("\n✅ Streaming completed!")


def send_chat_message_with_file():
    """Send chat message with file attachment (blocking mode)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Create a file attachment
    chat_file = (
        ChatFile.builder().type("document").transfer_method("remote_url").url("https://example.com/sample.pdf").build()
    )

    # Build request body with file
    req_body = (
        SendChatMessageRequestBody.builder()
        .query("Analyze this document and summarize its content")
        .response_mode("blocking")
        .user("user-123")
        .inputs({})
        .files([chat_file])
        .auto_generate_name(True)
        .build()
    )

    # Build request
    req = SendChatMessageRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.chatflow.send(req, req_option, False)

    if response.success:
        print("✅ Chat message with file sent successfully!")
        print(f"Message ID: {response.id}")
        print(f"Answer: {response.answer}")
        if response.message_files:
            print(f"Files processed: {len(response.message_files)}")
    else:
        print(f"❌ Error: {response.msg}")


async def send_chat_message_async_blocking():
    """Send chat message in blocking mode (async)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    req_body = (
        SendChatMessageRequestBody.builder()
        .query("What are the benefits of async programming?")
        .response_mode("blocking")
        .user("user-123")
        .inputs({})
        .auto_generate_name(True)
        .build()
    )

    # Build request
    req = SendChatMessageRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute async request
    response = await client.chatflow.v1.chatflow.asend(req, req_option, False)

    if response.success:
        print("✅ Async chat message sent successfully!")
        print(f"Message ID: {response.id}")
        print(f"Answer: {response.answer}")
    else:
        print(f"❌ Error: {response.msg}")


async def send_chat_message_async_streaming():
    """Send chat message in streaming mode (async)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body for streaming
    req_body = (
        SendChatMessageRequestBody.builder()
        .query("Explain machine learning in simple terms")
        .response_mode("streaming")
        .user("user-123")
        .inputs({})
        .auto_generate_name(True)
        .build()
    )

    # Build request
    req = SendChatMessageRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute async streaming request
    print("🔄 Async streaming response:")
    response = await client.chatflow.v1.chatflow.asend(req, req_option, True)

    async for chunk in response:
        print(chunk.decode("utf-8"), end="", flush=True)
    print("\n✅ Async streaming completed!")


def send_chat_message_with_conversation():
    """Send chat message continuing an existing conversation."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body with conversation ID
    req_body = (
        SendChatMessageRequestBody.builder()
        .query("Can you elaborate on that?")
        .response_mode("blocking")
        .user("user-123")
        .conversation_id("conv-12345")  # Use existing conversation ID
        .inputs({})
        .auto_generate_name(False)  # Don't auto-generate name for existing conversation
        .build()
    )

    # Build request
    req = SendChatMessageRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.chatflow.send(req, req_option, False)

    if response.success:
        print("✅ Conversation message sent successfully!")
        print(f"Message ID: {response.id}")
        print(f"Conversation ID: {response.conversation_id}")
        print(f"Answer: {response.answer}")
    else:
        print(f"❌ Error: {response.msg}")


def main():
    """Run all send chat message examples."""
    print("=== Send Chat Message Examples ===\n")

    try:
        # Sync examples
        print("1. Blocking Mode (Sync)")
        send_chat_message_blocking()
        print()

        print("2. Streaming Mode (Sync)")
        send_chat_message_streaming()
        print()

        print("3. With File Attachment")
        send_chat_message_with_file()
        print()

        print("4. Continue Conversation")
        send_chat_message_with_conversation()
        print()

        # Async examples
        print("5. Blocking Mode (Async)")
        asyncio.run(send_chat_message_async_blocking())
        print()

        print("6. Streaming Mode (Async)")
        asyncio.run(send_chat_message_async_streaming())
        print()

    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()
