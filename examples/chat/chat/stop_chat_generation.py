import asyncio
import os

from dify_oapi.api.chat.v1.model.stop_chat_request import StopChatRequest
from dify_oapi.api.chat.v1.model.stop_chat_request_body import StopChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def stop_chat_generation():
    """Stop a chat generation task"""
    api_key = os.getenv("CHAT_API_KEY")
    task_id = os.getenv("TASK_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not task_id:
        raise ValueError("TASK_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = StopChatRequestBody.builder().user("user-123").build()
    req = StopChatRequest.builder().task_id(task_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.chat.stop(req, req_option)
        print(f"Stop result: {response.result}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def stop_chat_generation_async():
    """Stop a chat generation task asynchronously"""
    api_key = os.getenv("CHAT_API_KEY")
    task_id = os.getenv("TASK_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not task_id:
        raise ValueError("TASK_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = StopChatRequestBody.builder().user("user-123").build()
    req = StopChatRequest.builder().task_id(task_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.chat.astop(req, req_option)
        print(f"Async stop result: {response.result}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    stop_chat_generation()
    asyncio.run(stop_chat_generation_async())
