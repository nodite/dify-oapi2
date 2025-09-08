import asyncio
import os

from dify_oapi.api.chat.v1.model.get_site_settings_request import GetSiteSettingsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_site_settings():
    """Get WebApp site settings"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetSiteSettingsRequest.builder().build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.app.site(req, req_option)
        print("Site Settings:")
        print(f"Title: {response.title}")
        print(f"Chat Color Theme: {response.chat_color_theme}")
        print(f"Chat Color Theme Inverted: {response.chat_color_theme_inverted}")
        print(f"Icon Type: {response.icon_type}")
        print(f"Icon: {response.icon}")
        print(f"Icon Background: {response.icon_background}")
        print(f"Icon URL: {response.icon_url}")
        print(f"Description: {response.description}")
        print(f"Copyright: {response.copyright}")
        print(f"Privacy Policy: {response.privacy_policy}")
        print(f"Custom Disclaimer: {response.custom_disclaimer}")
        print(f"Default Language: {response.default_language}")
        print(f"Show Workflow Steps: {response.show_workflow_steps}")
        print(f"Use Icon as Answer Icon: {response.use_icon_as_answer_icon}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def get_site_settings_async():
    """Get WebApp site settings asynchronously"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetSiteSettingsRequest.builder().build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.app.asite(req, req_option)
        print("Async Site Settings:")
        print(f"Title: {response.title}")
        print(f"Default Language: {response.default_language}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    get_site_settings()
    asyncio.run(get_site_settings_async())
