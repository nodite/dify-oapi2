#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.completion.completion_inputs import CompletionInputs
from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def send_message_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Send completion message
        inputs = CompletionInputs.builder().query("[Example] What is artificial intelligence?").build()
        req_body = SendMessageRequestBody.builder().inputs(inputs).response_mode("blocking").user("user-123").build()

        req = SendMessageRequest.builder().request_body(req_body).build()
        response = client.completion.v1.completion.send_message(req, req_option, False)

        if response.success:
            print(f"Message sent successfully: {response.answer}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def send_message_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Send completion message
        inputs = CompletionInputs.builder().query("[Example] Explain machine learning in simple terms").build()
        req_body = SendMessageRequestBody.builder().inputs(inputs).response_mode("blocking").user("user-123").build()

        req = SendMessageRequest.builder().request_body(req_body).build()
        response = await client.completion.v1.completion.asend_message(req, req_option, False)

        if response.success:
            print(f"Message sent successfully: {response.answer}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def send_message_streaming_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Send streaming completion message
        inputs = CompletionInputs.builder().query("[Example] Write a short story about AI").build()
        req_body = SendMessageRequestBody.builder().inputs(inputs).response_mode("streaming").user("user-123").build()

        req = SendMessageRequest.builder().request_body(req_body).build()
        response = client.completion.v1.completion.send_message(req, req_option, True)

        print("Streaming response:")
        for chunk in response:
            print(chunk, end="", flush=True)
        print()

    except Exception as e:
        print(f"Error: {e}")


async def send_message_streaming_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Send streaming completion message
        inputs = CompletionInputs.builder().query("[Example] Describe the future of technology").build()
        req_body = SendMessageRequestBody.builder().inputs(inputs).response_mode("streaming").user("user-123").build()

        req = SendMessageRequest.builder().request_body(req_body).build()
        response = await client.completion.v1.completion.asend_message(req, req_option, True)

        print("Streaming response:")
        async for chunk in response:
            print(chunk, end="", flush=True)
        print()

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Send Message Examples ===")

    print("\n1. Sync send message:")
    send_message_sync()

    print("\n2. Async send message:")
    asyncio.run(send_message_async())

    print("\n3. Sync streaming send message:")
    send_message_streaming_sync()

    print("\n4. Async streaming send message:")
    asyncio.run(send_message_streaming_async())


if __name__ == "__main__":
    main()
