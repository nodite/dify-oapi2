#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.get_site_request import GetSiteRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_site_sync():
    """Get application WebApp settings synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request
    request = GetSiteRequest.builder().build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.application.site(request, request_option)

        if response.success:
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
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def get_site_async():
    """Get application WebApp settings asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request
    request = GetSiteRequest.builder().build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.application.asite(request, request_option)

        if response.success:
            print(f"Title (async): {response.title}")
            print(f"Description: {response.description}")
            print(f"Default Language: {response.default_language}")

            # Display theme settings
            print("Theme Settings:")
            print(f"  Color Theme: {response.chat_color_theme}")
            print(f"  Inverted: {response.chat_color_theme_inverted}")

            # Display icon settings
            print("Icon Settings:")
            print(f"  Type: {response.icon_type}")
            print(f"  Icon: {response.icon}")
            print(f"  Background: {response.icon_background}")
            if response.icon_url:
                print(f"  URL: {response.icon_url}")

            # Display feature settings
            print("Feature Settings:")
            print(f"  Show Workflow Steps: {response.show_workflow_steps}")
            print(f"  Use Icon as Answer Icon: {response.use_icon_as_answer_icon}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Get Application Site Settings Examples ===")

    print("\n1. Sync Example:")
    get_site_sync()

    print("\n2. Async Example:")
    asyncio.run(get_site_async())
