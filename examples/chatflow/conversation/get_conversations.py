#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.get_conversations_request import GetConversationsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_conversations_sync():
    """Get conversations list synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = GetConversationsRequest.builder().user("user-123").limit(20).sort_by("-updated_at").build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.conversation.list(request, request_option)

        if response.success:
            print(f"Retrieved {len(response.data)} conversations")
            print(f"Has more: {response.has_more}")
            print(f"Limit: {response.limit}")

            for conversation in response.data:
                print(f"Conversation ID: {conversation.id}")
                print(f"Name: {conversation.name}")
                print(f"Status: {conversation.status}")
                print(f"Created at: {conversation.created_at}")
                print(f"Updated at: {conversation.updated_at}")
                if conversation.introduction:
                    print(f"Introduction: {conversation.introduction}")
                print("---")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def get_conversations_async():
    """Get conversations list asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request with different sorting
    request = GetConversationsRequest.builder().user("user-123").limit(10).sort_by("created_at").build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.conversation.alist(request, request_option)

        if response.success:
            print(f"Retrieved {len(response.data)} conversations (async)")
            print(f"Has more: {response.has_more}")

            for conversation in response.data:
                print(f"Conversation: {conversation.name}")
                print(f"Status: {conversation.status}")
                if conversation.inputs:
                    print(f"Inputs: {conversation.inputs}")
                print("---")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def get_conversations_with_pagination():
    """Get conversations with pagination example."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        last_id = None
        page = 1

        while True:
            # Build request with pagination
            request_builder = GetConversationsRequest.builder().user("user-123").limit(5).sort_by("-updated_at")

            if last_id:
                request_builder.last_id(last_id)

            request = request_builder.build()

            # Execute request
            response = client.chatflow.v1.conversation.list(request, request_option)

            if response.success:
                print(f"Page {page}: Retrieved {len(response.data)} conversations")

                if not response.data:
                    print("No more conversations")
                    break

                for conversation in response.data:
                    print(f"  - {conversation.name} ({conversation.status})")

                if not response.has_more:
                    print("Reached end of conversations")
                    break

                # Set last_id for next page
                last_id = response.data[-1].id
                page += 1

            else:
                print(f"Error: {response.msg}")
                break

    except Exception as e:
        print(f"Exception occurred: {e}")


def get_conversations_with_sorting():
    """Get conversations with different sorting options."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    # Test different sorting options
    sort_options = ["-updated_at", "updated_at", "-created_at", "created_at"]

    for sort_by in sort_options:
        print(f"\nSorting by: {sort_by}")

        try:
            # Build request
            request = GetConversationsRequest.builder().user("user-123").limit(3).sort_by(sort_by).build()

            # Execute request
            response = client.chatflow.v1.conversation.list(request, request_option)

            if response.success:
                for conversation in response.data:
                    print(f"  - {conversation.name} (updated: {conversation.updated_at})")
            else:
                print(f"  Error: {response.msg}")

        except Exception as e:
            print(f"  Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Get Conversations Examples ===")

    print("\n1. Sync Example:")
    get_conversations_sync()

    print("\n2. Async Example:")
    asyncio.run(get_conversations_async())

    print("\n3. Pagination Example:")
    get_conversations_with_pagination()

    print("\n4. Sorting Example:")
    get_conversations_with_sorting()
