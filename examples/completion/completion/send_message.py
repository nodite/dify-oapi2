#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def send_message_sync() -> str | None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_KEY")
        if not api_key:
            raise ValueError("COMPLETION_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Send completion message
        req_body = (
            SendMessageRequestBody.builder()
            .query(
                "[Example] What is artificial intelligence? Please be concise. Please answer within 10 words. No thinking process."
            )
            .response_mode("blocking")
            .user("user-123")
            .build()
        )

        req = SendMessageRequest.builder().request_body(req_body).build()
        response = client.completion.v1.completion.send_message(req, req_option, False)

        if response.success:
            print(f"Message sent successfully: {response.answer}")
            print(f"Message ID: {response.message_id}")
            return response.message_id
        else:
            print(f"Error: {response.msg}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


async def send_message_async() -> str | None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_KEY")
        if not api_key:
            raise ValueError("COMPLETION_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Send completion message
        req_body = (
            SendMessageRequestBody.builder()
            .query(
                "[Example] Briefly explain machine learning in simple terms. Please answer within 10 words. No thinking process."
            )
            .response_mode("blocking")
            .user("user-123")
            .build()
        )

        req = SendMessageRequest.builder().request_body(req_body).build()
        response = await client.completion.v1.completion.asend_message(req, req_option, False)

        if response.success:
            print(f"Message sent successfully: {response.answer}")
            print(f"Message ID: {response.message_id}")
            return response.message_id
        else:
            print(f"Error: {response.msg}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def send_message_streaming_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_KEY")
        if not api_key:
            raise ValueError("COMPLETION_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Send streaming completion message
        req_body = (
            SendMessageRequestBody.builder()
            .query("[Example] Write a very short story about AI. Please answer within 10 words. No thinking process.")
            .response_mode("streaming")
            .user("user-123")
            .build()
        )

        req = SendMessageRequest.builder().request_body(req_body).build()
        response = client.completion.v1.completion.send_message(req, req_option, True)

        print("Streaming response:")
        line_count = 0
        for chunk in response:
            chunk_str = chunk.decode("utf-8") if isinstance(chunk, bytes) else str(chunk)
            if "\n" in chunk_str:
                line_count += chunk_str.count("\n")
            print(chunk_str, end="", flush=True)
            if line_count >= 10:
                break
        print()

    except Exception as e:
        print(f"Error: {e}")


async def send_message_streaming_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_KEY")
        if not api_key:
            raise ValueError("COMPLETION_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Send streaming completion message
        req_body = (
            SendMessageRequestBody.builder()
            .query(
                "[Example] Briefly describe the future of technology. Please answer within 10 words. No thinking process."
            )
            .response_mode("streaming")
            .user("user-123")
            .build()
        )

        req = SendMessageRequest.builder().request_body(req_body).build()
        response = await client.completion.v1.completion.asend_message(req, req_option, True)

        print("Streaming response:")
        line_count = 0
        async for chunk in response:
            chunk_str = chunk.decode("utf-8") if isinstance(chunk, bytes) else str(chunk)
            if "\n" in chunk_str:
                line_count += chunk_str.count("\n")
            print(chunk_str, end="", flush=True)
            if line_count >= 10:
                break
        print()

    except Exception as e:
        print(f"Error: {e}")


async def async_main() -> None:
    print("=== Send Message Examples ===")

    print("\n1. Sync send message:")
    message_id = send_message_sync()
    if message_id:
        print(f"MESSAGE_ID for testing: {message_id}")

    print("\n2. Async send message:")
    await send_message_async()

    print("\n3. Sync streaming send message:")
    send_message_streaming_sync()

    print("\n4. Async streaming send message:")
    await send_message_streaming_async()


def main() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
