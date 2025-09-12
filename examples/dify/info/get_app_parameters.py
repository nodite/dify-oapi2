"""
Dify System API - Get App Parameters Example

Demonstrates how to retrieve application configuration parameters.
"""

import os

from dify_oapi.api.dify.v1.model.get_parameters_request import GetParametersRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_app_parameters_sync():
    """Synchronous app parameters retrieval"""

    # Environment validation
    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    user_id = os.getenv("USER_ID", "user-123")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    # Initialize client
    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    # Build request
    request = GetParametersRequest.builder().user(user_id).build()

    try:
        # Get app parameters
        response = client.dify.v1.info.parameters(request, request_option)

        print("Application parameters retrieved successfully:")
        print(f"Opening statement: {response.opening_statement}")
        print(f"Suggested questions: {response.suggested_questions}")
        print(f"Speech to text enabled: {response.speech_to_text}")
        print(f"File upload enabled: {response.file_upload}")
        print(f"System parameters: {response.system_parameters}")

        if hasattr(response, "user_input_form"):
            print(f"User input form: {response.user_input_form}")

        return response

    except Exception as e:
        print(f"Failed to get application parameters: {e}")
        raise


async def get_app_parameters_async():
    """Asynchronous app parameters retrieval"""

    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    user_id = os.getenv("USER_ID", "user-123")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    request = GetParametersRequest.builder().user(user_id).build()

    try:
        response = await client.dify.v1.info.aparameters(request, request_option)

        print("Async application parameters retrieved successfully:")
        print(f"Opening statement: {response.opening_statement}")
        print(f"File upload enabled: {response.file_upload}")

        return response

    except Exception as e:
        print(f"Async app parameters retrieval failed: {e}")
        raise


if __name__ == "__main__":
    print("=== Dify System API - Get App Parameters Example ===")
    get_app_parameters_sync()
