"""
Blocking Completion Example

This example demonstrates blocking completion requests.
"""

import os

from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def main():
    """Demonstrate blocking completion."""
    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        SendMessageRequestBody.builder()
        .inputs({})
        .query("Write a very short story about AI. Please answer within 10 words. No thinking process.")
        .response_mode("blocking")
        .user("user-123")
        .build()
    )

    req = SendMessageRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(os.getenv("COMPLETION_KEY", "<your-api-key>")).build()

    try:
        response = client.completion.v1.completion.send_message(req, req_option, False)
        print(f"Response: {response.answer}")
        print(f"Message ID: {response.message_id}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
