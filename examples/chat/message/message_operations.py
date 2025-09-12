"""
Chat Message Operations Example

This example demonstrates basic message operations in the Chat API.
"""

import os

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def main():
    """Demonstrate basic message operations."""
    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    # Basic message sending
    req_body = (
        ChatRequestBody.builder()
        .inputs({})
        .query("Hello, how are you? Please keep it brief. Please answer within 10 words. No thinking process.")
        .response_mode("blocking")
        .user("user-123")
        .build()
    )

    req = ChatRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(os.getenv("CHAT_KEY", "<your-api-key>")).build()

    try:
        response = client.chat.v1.chat.chat(req, req_option, False)
        print(f"Response: {response.answer}")
        print(f"Message ID: {response.message_id}")
        print(f"Conversation ID: {response.conversation_id}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
