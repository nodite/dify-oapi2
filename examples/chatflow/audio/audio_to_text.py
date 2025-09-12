"""
Dify System API - Audio to Text Example

Demonstrates how to convert audio files to text using speech recognition.
"""

import os

from dify_oapi.api.dify.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.dify.v1.model.audio_to_text_request_body import AudioToTextRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def audio_to_text_sync():
    """Synchronous audio to text conversion"""

    # Environment validation
    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    audio_path = os.getenv("AUDIO_PATH", "path/to/audio.mp3")
    user_id = os.getenv("USER_ID", "user-123")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    # Initialize client
    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    # Build request
    if not os.path.exists(audio_path):
        print(f"Audio file not found: {audio_path}")
        print("Please set AUDIO_PATH environment variable to a valid audio file")
        return

    request_body = AudioToTextRequestBody.builder().user(user_id).build()

    request = (
        AudioToTextRequest.builder()
        .file(open(audio_path, "rb"), os.path.basename(audio_path))
        .request_body(request_body)
        .build()
    )

    try:
        # Execute request
        response = client.dify.v1.audio.to_text(request, request_option)

        print("Audio to text conversion successful:")
        print(f"Recognized text: {response.text}")
        return response

    except Exception as e:
        print(f"Audio to text conversion failed: {e}")
        raise


async def audio_to_text_async():
    """Asynchronous audio to text conversion"""

    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    audio_path = os.getenv("AUDIO_PATH", "path/to/audio.mp3")
    user_id = os.getenv("USER_ID", "user-123")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    if not os.path.exists(audio_path):
        print(f"Audio file not found: {audio_path}")
        print("Please set AUDIO_PATH environment variable to a valid audio file")
        return

    request_body = AudioToTextRequestBody.builder().user(user_id).build()

    request = (
        AudioToTextRequest.builder()
        .file(open(audio_path, "rb"), os.path.basename(audio_path))
        .request_body(request_body)
        .build()
    )

    try:
        response = await client.dify.v1.audio.ato_text(request, request_option)
        print(f"Async audio to text successful: {response.text}")
        return response

    except Exception as e:
        print(f"Async audio to text failed: {e}")
        raise


if __name__ == "__main__":
    print("=== Dify System API - Audio to Text Example ===")
    audio_to_text_sync()
