import asyncio
import os

from dify_oapi.api.chat.v1.model.message_history_request import GetMessageHistoryRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_message_history():
    """Get conversation message history"""
    api_key = os.getenv("CHAT_KEY")
    conversation_id = os.getenv("CONVERSATION_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetMessageHistoryRequest.builder().conversation_id(conversation_id).user("user-123").limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.history(req, req_option)
        print(f"Retrieved {len(response.data)} messages")
        print(f"Has more: {response.has_more}")

        for message in response.data:
            print(f"- Message ID: {message.id}")
            print(f"  Query: {message.query}")
            print(f"  Answer: {message.answer}")
            print(f"  Created: {message.created_at}")
            print()

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def get_message_history_paginated():
    """Get message history with pagination"""
    api_key = os.getenv("CHAT_KEY")
    conversation_id = os.getenv("CONVERSATION_ID")
    first_id = os.getenv("FIRST_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_builder = GetMessageHistoryRequest.builder().conversation_id(conversation_id).user("user-123").limit(10)
    if first_id:
        req_builder.first_id(first_id)
    req = req_builder.build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.history(req, req_option)
        print(f"Retrieved {len(response.data)} messages (paginated)")

        for message in response.data:
            print(f"- Message ID: {message.id}")
            print(f"  Query: {message.query[:50]}...")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def get_message_history_async():
    """Get message history asynchronously"""
    api_key = os.getenv("CHAT_KEY")
    conversation_id = os.getenv("CONVERSATION_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetMessageHistoryRequest.builder().conversation_id(conversation_id).user("user-123").limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.conversation.ahistory(req, req_option)
        print(f"Async retrieved {len(response.data)} messages")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    get_message_history()
    get_message_history_paginated()
    asyncio.run(get_message_history_async())
