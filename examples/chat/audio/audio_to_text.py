import asyncio
import os
from io import BytesIO

from dify_oapi.api.chat.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def audio_to_text():
    """Convert audio file to text"""
    api_key = os.getenv("CHAT_API_KEY")
    audio_path = os.getenv("AUDIO_PATH")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not audio_path:
        raise ValueError("AUDIO_PATH environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    try:
        with open(audio_path, "rb") as f:
            audio_data = BytesIO(f.read())

        req = AudioToTextRequest.builder().file(audio_data, os.path.basename(audio_path)).user("user-123").build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.chat.v1.audio.to_text(req, req_option)
        print("Audio transcription successful!")
        print(f"Text: {response.text}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def audio_to_text_async():
    """Convert audio file to text asynchronously"""
    api_key = os.getenv("CHAT_API_KEY")
    audio_path = os.getenv("AUDIO_PATH")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not audio_path:
        raise ValueError("AUDIO_PATH environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    try:
        with open(audio_path, "rb") as f:
            audio_data = BytesIO(f.read())

        req = AudioToTextRequest.builder().file(audio_data, os.path.basename(audio_path)).user("user-123").build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.chat.v1.audio.ato_text(req, req_option)
        print("Audio transcription completed asynchronously!")
        print(f"Text: {response.text}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    if os.getenv("AUDIO_PATH"):
        audio_to_text()
        asyncio.run(audio_to_text_async())
    else:
        print("AUDIO_PATH environment variable not set. Skipping audio transcription example.")
