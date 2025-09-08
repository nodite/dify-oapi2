import asyncio
import os

from dify_oapi.api.chat.v1.model.get_conversation_list_request import GetConversationsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_conversations():
    """Get conversations list"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetConversationsRequest.builder().user("user-123").limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.list(req, req_option)
        print(f"Retrieved {len(response.data)} conversations")
        print(f"Has more: {response.has_more}")

        for conversation in response.data:
            print(f"- Conversation ID: {conversation.id}")
            print(f"  Name: {conversation.name}")
            print(f"  Status: {conversation.status}")
            print(f"  Created: {conversation.created_at}")
            print(f"  Updated: {conversation.updated_at}")
            print()

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def get_conversations_sorted():
    """Get conversations with sorting"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetConversationsRequest.builder().user("user-123").limit(10).sort_by("-created_at").build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.list(req, req_option)
        print(f"Retrieved {len(response.data)} conversations (sorted by creation date desc)")

        for conversation in response.data:
            print(f"- {conversation.name} (Created: {conversation.created_at})")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def get_conversations_paginated():
    """Get conversations with pagination"""
    api_key = os.getenv("API_KEY")
    last_id = os.getenv("LAST_ID")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_builder = GetConversationsRequest.builder().user("user-123").limit(5)
    if last_id:
        req_builder.last_id(last_id)
    req = req_builder.build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.list(req, req_option)
        print(f"Retrieved {len(response.data)} conversations (paginated)")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def get_conversations_async():
    """Get conversations asynchronously"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetConversationsRequest.builder().user("user-123").limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.conversation.alist(req, req_option)
        print(f"Async retrieved {len(response.data)} conversations")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    get_conversations()
    get_conversations_sorted()
    get_conversations_paginated()
    asyncio.run(get_conversations_async())
