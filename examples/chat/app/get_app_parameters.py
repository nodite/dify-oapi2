import asyncio
import os

from dify_oapi.api.chat.v1.model.get_app_parameters_request import GetAppParametersRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_app_parameters():
    """Get application parameters"""
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req = GetAppParametersRequest.builder().user("user-123").build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.app.parameters(req, req_option)
        print("Application Parameters:")
        print(f"Opening Statement: {response.opening_statement}")
        print(f"Suggested Questions: {response.suggested_questions}")
        print(f"Speech to Text Enabled: {response.speech_to_text.enabled if response.speech_to_text else 'N/A'}")
        print(f"Text to Speech Enabled: {response.text_to_speech.enabled if response.text_to_speech else 'N/A'}")
        print(
            f"Retriever Resource Enabled: {response.retriever_resource.enabled if response.retriever_resource else 'N/A'}"
        )
        print(f"Annotation Reply Enabled: {response.annotation_reply.enabled if response.annotation_reply else 'N/A'}")

        if response.file_upload and response.file_upload.image:
            print(f"Image Upload Enabled: {response.file_upload.image.enabled}")
            print(f"Image Number Limits: {response.file_upload.image.number_limits}")

        if response.user_input_form:
            print(f"User Input Form Fields: {len(response.user_input_form)}")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def get_app_parameters_async():
    """Get application parameters asynchronously"""
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req = GetAppParametersRequest.builder().user("user-123").build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.app.aparameters(req, req_option)
        print("Async Application Parameters:")
        print(f"Opening Statement: {response.opening_statement}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    get_app_parameters()
    asyncio.run(get_app_parameters_async())
