"""
Dify System API - Get Site Settings Example

Demonstrates how to retrieve WebApp site settings and customization.
"""

import os

from dify_oapi.api.dify.v1.model.get_site_request import GetSiteRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_site_settings_sync():
    """Synchronous site settings retrieval"""

    # Environment validation
    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    # Initialize client
    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    # Build request
    request = GetSiteRequest.builder().build()

    try:
        # Get site settings
        response = client.dify.v1.info.site(request, request_option)

        print("Site settings retrieved successfully:")
        print(f"Site title: {response.title}")
        print(f"Site icon: {response.icon}")
        print(f"Site description: {response.description}")
        print(f"Default language: {response.default_language}")
        print(f"Copyright: {response.copyright}")
        print(f"Privacy policy: {response.privacy_policy}")

        if hasattr(response, "custom_disclaimer"):
            print(f"Custom disclaimer: {response.custom_disclaimer}")

        return response

    except Exception as e:
        print(f"Failed to get site settings: {e}")
        raise


async def get_site_settings_async():
    """Asynchronous site settings retrieval"""

    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    request = GetSiteRequest.builder().build()

    try:
        response = await client.dify.v1.info.asite(request, request_option)

        print("Async site settings retrieved successfully:")
        print(f"Site title: {response.title}")
        print(f"Default language: {response.default_language}")

        return response

    except Exception as e:
        print(f"Async site settings retrieval failed: {e}")
        raise


if __name__ == "__main__":
    print("=== Dify System API - Get Site Settings Example ===")
    get_site_settings_sync()
