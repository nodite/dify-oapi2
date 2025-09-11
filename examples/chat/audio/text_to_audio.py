import asyncio
import os

from dify_oapi.api.chat.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.chat.v1.model.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def text_to_audio():
    """Convert text to audio"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = TextToAudioRequestBody.builder().text("Hello, how are you today?").user("user-123").build()
    req = TextToAudioRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.audio.to_audio(req, req_option)
        print("Text-to-speech conversion successful!")
        print(f"Audio data length: {len(response)} bytes")

        # Save audio to file
        output_path = "output_audio.wav"
        with open(output_path, "wb") as f:
            f.write(response)
        print(f"Audio saved to: {output_path}")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def text_to_audio_from_message():
    """Convert message text to audio"""
    api_key = os.getenv("API_KEY")
    message_id = os.getenv("MESSAGE_ID")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")
    if not message_id:
        raise ValueError("MESSAGE_ID environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = TextToAudioRequestBody.builder().message_id(message_id).user("user-123").build()
    req = TextToAudioRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.audio.to_audio(req, req_option)
        print("Message text-to-speech conversion successful!")
        print(f"Audio data length: {len(response)} bytes")

        # Save audio to file
        output_path = f"message_{message_id}_audio.wav"
        with open(output_path, "wb") as f:
            f.write(response)
        print(f"Audio saved to: {output_path}")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def text_to_audio_async():
    """Convert text to audio asynchronously"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = TextToAudioRequestBody.builder().text("This is an async text-to-speech test.").user("user-123").build()
    req = TextToAudioRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.audio.ato_audio(req, req_option)
        print("Async text-to-speech conversion successful!")
        print(f"Audio data length: {len(response)} bytes")

        # Save audio to file
        output_path = "async_output_audio.wav"
        with open(output_path, "wb") as f:
            f.write(response)
        print(f"Audio saved to: {output_path}")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    text_to_audio()
    if os.getenv("MESSAGE_ID"):
        text_to_audio_from_message()
    asyncio.run(text_to_audio_async())
