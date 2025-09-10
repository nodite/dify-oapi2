#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.chatflow.v1.model.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def text_to_audio_sync():
    """Convert text to audio synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request body
    req_body = (
        TextToAudioRequestBody.builder()
        .text("Hello, this is a text-to-speech example.")
        .user("user-123")
        .streaming(False)
        .build()
    )

    # Build request
    request = TextToAudioRequest.builder().request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.tts.text_to_audio(request, request_option)

        if response.success:
            print(f"Audio generated successfully, size: {len(response.raw)} bytes")
            # In real usage, save to file:
            # with open("output.wav", "wb") as f:
            #     f.write(response.raw)
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def text_to_audio_async():
    """Convert text to audio asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request body
    req_body = (
        TextToAudioRequestBody.builder()
        .text("This is an async text-to-speech example.")
        .user("user-123")
        .streaming(False)
        .build()
    )

    # Build request
    request = TextToAudioRequest.builder().request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.tts.atext_to_audio(request, request_option)

        if response.success:
            print(f"Audio generated (async), size: {len(response.raw)} bytes")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def text_to_audio_with_message_id():
    """Convert text to audio using message ID."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    message_id = os.getenv("MESSAGE_ID")
    if not message_id:
        print("MESSAGE_ID not provided, using text input instead")
        return text_to_audio_sync()

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request body with message_id
    req_body = TextToAudioRequestBody.builder().message_id(message_id).user("user-123").streaming(False).build()

    # Build request
    request = TextToAudioRequest.builder().request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.tts.text_to_audio(request, request_option)

        if response.success:
            print(f"Audio from message generated, size: {len(response.raw)} bytes")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def text_to_audio_streaming():
    """Convert text to audio with streaming."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request body with streaming enabled
    req_body = (
        TextToAudioRequestBody.builder()
        .text("This is a streaming text-to-speech example.")
        .user("user-123")
        .streaming(True)
        .build()
    )

    # Build request
    request = TextToAudioRequest.builder().request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request with streaming
        response = client.chatflow.v1.tts.text_to_audio(request, request_option)

        if response.success:
            print("Streaming audio generated successfully")
            # Handle streaming audio chunks here
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Text to Audio Examples ===")

    print("\n1. Sync Example:")
    text_to_audio_sync()

    print("\n2. Async Example:")
    asyncio.run(text_to_audio_async())

    print("\n3. Message ID Example:")
    text_to_audio_with_message_id()

    print("\n4. Streaming Example:")
    text_to_audio_streaming()
