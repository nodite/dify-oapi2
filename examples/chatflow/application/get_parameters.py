#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.get_parameters_request import GetParametersRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_parameters_sync():
    """Get application parameters synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request
    request = GetParametersRequest.builder().build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.application.parameters(request, request_option)

        if response.success:
            print(f"Opening Statement: {response.opening_statement}")
            print(f"Suggested Questions: {response.suggested_questions}")

            if response.suggested_questions_after_answer:
                print(f"Suggested Questions After Answer Enabled: {response.suggested_questions_after_answer.enabled}")

            if response.speech_to_text:
                print(f"Speech to Text Enabled: {response.speech_to_text.enabled}")

            if response.text_to_speech:
                print(f"Text to Speech Enabled: {response.text_to_speech.enabled}")
                print(f"TTS Voice: {response.text_to_speech.voice}")
                print(f"TTS Language: {response.text_to_speech.language}")
                print(f"TTS AutoPlay: {response.text_to_speech.auto_play}")

            if response.retriever_resource:
                print(f"Retriever Resource Enabled: {response.retriever_resource.enabled}")

            if response.annotation_reply:
                print(f"Annotation Reply Enabled: {response.annotation_reply.enabled}")

            if response.user_input_form:
                print(f"User Input Forms: {len(response.user_input_form)} forms configured")
                for i, form in enumerate(response.user_input_form):
                    print(f"  Form {i + 1}: {form}")

            if response.file_upload:
                print(f"File Upload Configuration: {response.file_upload}")

            if response.system_parameters:
                print(f"System Parameters: {response.system_parameters}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def get_parameters_async():
    """Get application parameters asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request
    request = GetParametersRequest.builder().build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.application.aparameters(request, request_option)

        if response.success:
            print(f"Opening Statement: {response.opening_statement}")

            if response.file_upload and response.file_upload.image:
                print(f"Image Upload Enabled: {response.file_upload.image.enabled}")
                print(f"Image Number Limits: {response.file_upload.image.number_limits}")
                print(f"Image Detail: {response.file_upload.image.detail}")
                print(f"Transfer Methods: {response.file_upload.image.transfer_methods}")

            if response.system_parameters:
                print(f"File Size Limit: {response.system_parameters.file_size_limit}")
                print(f"Image File Size Limit: {response.system_parameters.image_file_size_limit}")
                print(f"Audio File Size Limit: {response.system_parameters.audio_file_size_limit}")
                print(f"Video File Size Limit: {response.system_parameters.video_file_size_limit}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Get Application Parameters Examples ===")

    print("\n1. Sync Example:")
    get_parameters_sync()

    print("\n2. Async Example:")
    asyncio.run(get_parameters_async())
