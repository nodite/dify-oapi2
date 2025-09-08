import asyncio
import os

from dify_oapi.api.chat.v1.model.get_app_meta_request import GetAppMetaRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_app_meta():
    """Get application meta information"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetAppMetaRequest.builder().build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.app.meta(req, req_option)
        print("Application Meta Information:")

        if response.tool_icons:
            print("Tool Icons:")
            for tool_name, icon_info in response.tool_icons.items():
                if isinstance(icon_info, str):
                    print(f"  {tool_name}: {icon_info}")
                else:
                    print(
                        f"  {tool_name}: Background={icon_info.get('background', 'N/A')}, Content={icon_info.get('content', 'N/A')}"
                    )
        else:
            print("No tool icons available")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def get_app_meta_async():
    """Get application meta information asynchronously"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetAppMetaRequest.builder().build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.app.ameta(req, req_option)
        print("Async Application Meta Information:")

        if response.tool_icons:
            print(f"Tool Icons Count: {len(response.tool_icons)}")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    get_app_meta()
    asyncio.run(get_app_meta_async())
