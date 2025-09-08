import asyncio
import os

from dify_oapi.api.chat.v1.model.get_app_info_request import GetAppInfoRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_app_info():
    """Get application basic information"""
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req = GetAppInfoRequest.builder().build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.app.info(req, req_option)
        print("Application Information:")
        print(f"Name: {response.name}")
        print(f"Description: {response.description}")
        print(f"Tags: {', '.join(response.tags) if response.tags else 'None'}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def get_app_info_async():
    """Get application basic information asynchronously"""
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req = GetAppInfoRequest.builder().build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.app.ainfo(req, req_option)
        print("Async Application Information:")
        print(f"Name: {response.name}")
        print(f"Description: {response.description}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    get_app_info()
    asyncio.run(get_app_info_async())
