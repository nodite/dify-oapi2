import asyncio
import os

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def send_blocking_chat():
    """Send a blocking chat message"""
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        ChatRequestBody.builder()
        .inputs({})
        .query("Hello, how are you? Please keep it brief. Please answer within 10 words. No thinking process.")
        .response_mode("blocking")
        .user("user-123")
        .build()
    )

    req = ChatRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.chat.chat(req, req_option, False)
        print(f"Response: {response.answer}")
        print(f"Message ID: {response.message_id}")
        print(f"Conversation ID: {response.conversation_id}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def send_streaming_chat():
    """Send a streaming chat message"""
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        ChatRequestBody.builder()
        .inputs({})
        .query("Tell me a very short story. Please answer within 10 words. No thinking process.")
        .response_mode("streaming")
        .user("user-123")
        .build()
    )

    req = ChatRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.chat.chat(req, req_option, True)

        print("Streaming response:")
        for chunk in response:
            print(chunk.decode("utf-8"), end="", flush=True)
        print()

    except Exception as e:
        print(f"Error: {e}")
        raise


async def send_async_chat():
    """Send an async chat message"""
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        ChatRequestBody.builder()
        .inputs({})
        .query("What's the weather like? Keep your answer short. Please answer within 10 words. No thinking process.")
        .response_mode("blocking")
        .user("user-123")
        .build()
    )

    req = ChatRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.chat.achat(req, req_option, False)
        print(f"Async Response: {response.answer}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    send_blocking_chat()
    send_streaming_chat()
    asyncio.run(send_async_chat())
