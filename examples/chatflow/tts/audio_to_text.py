#!/usr/bin/env python3

import asyncio
import os
from io import BytesIO

from dify_oapi.api.chatflow.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def audio_to_text_sync():
    """Convert audio to text synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Create sample audio file (in real usage, load from file)
    audio_data = b"fake_audio_data_for_example"
    audio_file = BytesIO(audio_data)

    # Build request
    request = AudioToTextRequest.builder().file(audio_file, "example_audio.mp3").user("user-123").build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.tts.speech_to_text(request, request_option)

        if response.success:
            print(f"Transcribed text: {response.text}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def audio_to_text_async():
    """Convert audio to text asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Create sample audio file (in real usage, load from file)
    audio_data = b"fake_audio_data_for_example"
    audio_file = BytesIO(audio_data)

    # Build request
    request = AudioToTextRequest.builder().file(audio_file, "example_audio.wav").user("user-123").build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.tts.aspeech_to_text(request, request_option)

        if response.success:
            print(f"Transcribed text (async): {response.text}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def audio_to_text_with_different_formats():
    """Convert audio to text with different audio formats."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    # Test different audio formats
    formats = ["mp3", "wav", "m4a", "webm"]

    for format_type in formats:
        try:
            # Create sample audio file
            audio_data = f"fake_audio_data_for_{format_type}".encode()
            audio_file = BytesIO(audio_data)

            # Build request
            request = (
                AudioToTextRequest.builder().file(audio_file, f"example_audio.{format_type}").user("user-123").build()
            )

            # Execute request
            response = client.chatflow.v1.tts.speech_to_text(request, request_option)

            if response.success:
                print(f"Format {format_type}: {response.text}")
            else:
                print(f"Format {format_type} error: {response.msg}")

        except Exception as e:
            print(f"Format {format_type} exception: {e}")


if __name__ == "__main__":
    print("=== Audio to Text Examples ===")

    print("\n1. Sync Example:")
    audio_to_text_sync()

    print("\n2. Async Example:")
    asyncio.run(audio_to_text_async())

    print("\n3. Different Formats Example:")
    audio_to_text_with_different_formats()
