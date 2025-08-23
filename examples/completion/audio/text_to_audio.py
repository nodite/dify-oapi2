#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.audio.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.completion.v1.model.audio.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def text_to_audio_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Create text-to-audio request
        req_body = (
            TextToAudioRequestBody.builder()
            .text("[Example] Hello, this is a test audio message.")
            .user("user-123")
            .build()
        )

        req = TextToAudioRequest.builder().request_body(req_body).build()
        response = client.completion.v1.audio.text_to_audio(req, req_option)

        if response.success:
            print(f"Audio generated successfully, size: {len(response.data) if response.data else 0} bytes")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def text_to_audio_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Create text-to-audio request
        req_body = (
            TextToAudioRequestBody.builder()
            .text("[Example] Hello, this is an async test audio message.")
            .user("user-123")
            .build()
        )

        req = TextToAudioRequest.builder().request_body(req_body).build()
        response = await client.completion.v1.audio.atext_to_audio(req, req_option)

        if response.success:
            print(f"Audio generated successfully (async), size: {len(response.data) if response.data else 0} bytes")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Text to Audio Examples ===")

    print("\n1. Sync text-to-audio:")
    text_to_audio_sync()

    print("\n2. Async text-to-audio:")
    asyncio.run(text_to_audio_async())


if __name__ == "__main__":
    main()
