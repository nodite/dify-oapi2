#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.get_conversation_messages_request import GetConversationMessagesRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_conversation_messages_sync():
    """Get conversation messages synchronously with pagination."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_API_KEY")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    if not api_key:
        raise ValueError("CHATFLOW_API_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = (
        GetConversationMessagesRequest.builder().conversation_id(conversation_id).user("user-123").limit(20).build()
    )

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.conversation.messages(request, request_option)

        if response.success:
            print(f"Retrieved {len(response.data)} messages")
            print(f"Has more: {response.has_more}")
            print(f"Limit: {response.limit}")

            for message in response.data:
                print(f"Message ID: {message.id}")
                print(f"Query: {message.query}")
                print(f"Answer: {message.answer[:100]}...")
                print("---")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def get_conversation_messages_async():
    """Get conversation messages asynchronously with pagination."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_API_KEY")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    if not api_key:
        raise ValueError("CHATFLOW_API_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request with pagination
    request = (
        GetConversationMessagesRequest.builder().conversation_id(conversation_id).user("user-123").limit(10).build()
    )

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.conversation.amessages(request, request_option)

        if response.success:
            print(f"Retrieved {len(response.data)} messages (async)")
            print(f"Has more: {response.has_more}")

            for message in response.data:
                print(f"Message ID: {message.id}")
                print(f"Created at: {message.created_at}")
                if message.feedback:
                    print(f"Feedback: {message.feedback.rating}")
                print("---")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def get_conversation_messages_with_pagination():
    """Get conversation messages with pagination example."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_API_KEY")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    if not api_key:
        raise ValueError("CHATFLOW_API_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        first_id = None
        page = 1

        while True:
            # Build request with pagination
            request_builder = (
                GetConversationMessagesRequest.builder().conversation_id(conversation_id).user("user-123").limit(5)
            )

            if first_id:
                request_builder.first_id(first_id)

            request = request_builder.build()

            # Execute request
            response = client.chatflow.v1.conversation.messages(request, request_option)

            if response.success:
                print(f"Page {page}: Retrieved {len(response.data)} messages")

                if not response.data:
                    print("No more messages")
                    break

                for message in response.data:
                    print(f"  - {message.id}: {message.query[:50]}...")

                if not response.has_more:
                    print("Reached end of messages")
                    break

                # Set first_id for next page
                first_id = response.data[-1].id
                page += 1

            else:
                print(f"Error: {response.msg}")
                break

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Get Conversation Messages Examples ===")

    print("\n1. Sync Example:")
    get_conversation_messages_sync()

    print("\n2. Async Example:")
    asyncio.run(get_conversation_messages_async())

    print("\n3. Pagination Example:")
    get_conversation_messages_with_pagination()
