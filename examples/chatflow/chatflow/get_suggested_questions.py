#!/usr/bin/env python3
"""
Get Suggested Questions Example

This example demonstrates how to get suggested questions for a message using the Chatflow API
with both sync and async operations.
"""

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def validate_environment():
    """Validate required environment variables."""
    api_key = os.getenv("CHATFLOW_API_KEY")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    if not api_key:
        raise ValueError("CHATFLOW_API_KEY environment variable is required")
    return api_key, domain


def get_suggested_questions():
    """Get suggested questions for a message (sync)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Example message ID from a previous chat message
    message_id = "msg-12345"  # Replace with actual message ID

    # Build request
    req = GetSuggestedQuestionsRequest.builder().message_id(message_id).user("user-123").build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.chatflow.suggested(req, req_option)

    if response.success:
        print("✅ Suggested questions retrieved successfully!")
        print(f"Result: {response.result}")
        if response.data:
            print(f"Number of suggestions: {len(response.data)}")
            for i, question in enumerate(response.data, 1):
                print(f"  {i}. {question}")
        else:
            print("No suggested questions available.")
    else:
        print(f"❌ Error: {response.msg}")


async def get_suggested_questions_async():
    """Get suggested questions for a message (async)."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Example message ID from a previous chat message
    message_id = "msg-67890"  # Replace with actual message ID

    # Build request
    req = GetSuggestedQuestionsRequest.builder().message_id(message_id).user("user-123").build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute async request
    response = await client.chatflow.v1.chatflow.asuggested(req, req_option)

    if response.success:
        print("✅ Async suggested questions retrieved successfully!")
        print(f"Result: {response.result}")
        if response.data:
            print(f"Number of suggestions: {len(response.data)}")
            for i, question in enumerate(response.data, 1):
                print(f"  {i}. {question}")
        else:
            print("No suggested questions available.")
    else:
        print(f"❌ Error: {response.msg}")


def get_suggested_questions_for_multiple_messages():
    """Get suggested questions for multiple messages."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Example message IDs from previous chat messages
    message_ids = ["msg-111", "msg-222", "msg-333"]

    for message_id in message_ids:
        print(f"💡 Getting suggestions for message: {message_id}")

        # Build request
        req = GetSuggestedQuestionsRequest.builder().message_id(message_id).user("user-123").build()

        req_option = RequestOption.builder().api_key(api_key).build()

        # Execute request
        response = client.chatflow.v1.chatflow.suggested(req, req_option)

        if response.success:
            print(f"  ✅ Suggestions retrieved for {message_id}")
            if response.data:
                for i, question in enumerate(response.data, 1):
                    print(f"    {i}. {question}")
            else:
                print("    No suggestions available.")
        else:
            print(f"  ❌ Failed to get suggestions for {message_id}: {response.msg}")
        print()


def demonstrate_conversation_flow():
    """Demonstrate a complete conversation flow with suggested questions."""
    api_key, domain = validate_environment()

    print("🔄 This example shows how suggested questions work in a conversation flow.")
    print("In a real scenario, you would:")
    print("1. Send a chat message")
    print("2. Get the message_id from the response")
    print("3. Use that message_id to get suggested questions")
    print("4. Present suggestions to the user for follow-up questions")
    print()

    # Example of what the message_id extraction would look like:
    print("Example chat response:")
    print('{"id": "msg-abc123", "conversation_id": "conv-xyz789", "answer": "AI can help with...", ...}')
    print("Extract message_id: msg-abc123")
    print()

    # Simulate getting suggestions with the extracted message_id
    message_id = "msg-abc123"

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    req = GetSuggestedQuestionsRequest.builder().message_id(message_id).user("user-123").build()

    req_option = RequestOption.builder().api_key(api_key).build()

    # Execute request
    response = client.chatflow.v1.chatflow.suggested(req, req_option)

    if response.success:
        print("✅ Suggested questions for conversation flow:")
        if response.data:
            print("Here are some follow-up questions you might ask:")
            for i, question in enumerate(response.data, 1):
                print(f"  {i}. {question}")
            print("\nUser can select one of these questions to continue the conversation.")
        else:
            print("No suggested questions available for this message.")
    else:
        print(f"❌ Error: {response.msg}")


def get_suggestions_with_different_users():
    """Get suggested questions with different user contexts."""
    api_key, domain = validate_environment()

    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Same message ID but different users
    message_id = "msg-shared-123"
    users = ["user-alice", "user-bob", "user-charlie"]

    for user in users:
        print(f"👤 Getting suggestions for user: {user}")

        # Build request
        req = GetSuggestedQuestionsRequest.builder().message_id(message_id).user(user).build()

        req_option = RequestOption.builder().api_key(api_key).build()

        # Execute request
        response = client.chatflow.v1.chatflow.suggested(req, req_option)

        if response.success:
            print(f"  ✅ Suggestions for {user}:")
            if response.data:
                for i, question in enumerate(response.data, 1):
                    print(f"    {i}. {question}")
            else:
                print("    No suggestions available.")
        else:
            print(f"  ❌ Failed to get suggestions for {user}: {response.msg}")
        print()


def main():
    """Run all get suggested questions examples."""
    print("=== Get Suggested Questions Examples ===\n")

    try:
        print("1. Get Suggested Questions (Sync)")
        get_suggested_questions()
        print()

        print("2. Get Suggested Questions (Async)")
        asyncio.run(get_suggested_questions_async())
        print()

        print("3. Get Suggestions for Multiple Messages")
        get_suggested_questions_for_multiple_messages()
        print()

        print("4. Conversation Flow Demonstration")
        demonstrate_conversation_flow()
        print()

        print("5. Suggestions with Different Users")
        get_suggestions_with_different_users()
        print()

    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()
