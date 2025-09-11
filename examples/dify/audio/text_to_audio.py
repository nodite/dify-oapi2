"""
Dify System API - Text to Audio Example

Demonstrates how to convert text to audio using text-to-speech synthesis.
"""

import os

from dify_oapi.api.dify.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.dify.v1.model.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def text_to_audio_sync():
    """Synchronous text to audio conversion"""

    # Environment validation
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    text_content = os.getenv("TEXT_CONTENT", "Hello, this is a text to speech example.")
    user_id = os.getenv("USER_ID", "user-123")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    # Initialize client
    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    # Build request
    request_body = TextToAudioRequestBody.builder().text(text_content).user(user_id).build()

    request = TextToAudioRequest.builder().request_body(request_body).build()

    try:
        # Execute request
        response = client.dify.v1.audio.from_text(request, request_option)

        print("Text to audio conversion successful:")
        if response.raw and response.raw.content:
            print(f"Audio data length: {len(response.raw.content)} bytes")

            # Save audio file
            output_file = "output_audio.mp3"
            with open(output_file, "wb") as f:
                f.write(response.raw.content)
            print(f"Audio file saved as {output_file}")
        else:
            print("No audio content received")

        return response

    except Exception as e:
        print(f"Text to audio conversion failed: {e}")
        raise


async def text_to_audio_async():
    """Asynchronous text to audio conversion"""

    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    text_content = os.getenv("TEXT_CONTENT", "Hello, this is an async text to speech example.")
    user_id = os.getenv("USER_ID", "user-123")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    request_body = TextToAudioRequestBody.builder().text(text_content).user(user_id).build()

    request = TextToAudioRequest.builder().request_body(request_body).build()

    try:
        response = await client.dify.v1.audio.afrom_text(request, request_option)

        print("Async text to audio conversion successful:")
        if response.raw and response.raw.content:
            print(f"Audio data length: {len(response.raw.content)} bytes")

            output_file = "async_output_audio.mp3"
            with open(output_file, "wb") as f:
                f.write(response.raw.content)
            print(f"Audio file saved as {output_file}")
        else:
            print("No audio content received")

        return response

    except Exception as e:
        print(f"Async text to audio failed: {e}")
        raise


if __name__ == "__main__":
    print("=== Dify System API - Text to Audio Example ===")
    text_to_audio_sync()
