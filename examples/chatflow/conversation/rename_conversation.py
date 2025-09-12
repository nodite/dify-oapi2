#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chatflow.v1.model.rename_conversation_request_body import RenameConversationRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def rename_conversation_sync():
    """Rename conversation synchronously."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body with custom name
    request_body = (
        RenameConversationRequestBody.builder().name("[Example] Renamed Conversation").user("user-123").build()
    )

    # Build request
    request = RenameConversationRequest.builder().conversation_id(conversation_id).request_body(request_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.conversation.rename(request, request_option)

        if response.success:
            print(f"Successfully renamed conversation: {conversation_id}")
            print(f"New name: {response.name}")
            print(f"Status: {response.status}")
            print(f"Updated at: {response.updated_at}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def rename_conversation_async():
    """Rename conversation asynchronously."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body with custom name
    request_body = (
        RenameConversationRequestBody.builder().name("[Example] Async Renamed Conversation").user("user-123").build()
    )

    # Build request
    request = RenameConversationRequest.builder().conversation_id(conversation_id).request_body(request_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.conversation.arename(request, request_option)

        if response.success:
            print(f"Successfully renamed conversation (async): {conversation_id}")
            print(f"New name: {response.name}")
            print(f"Status: {response.status}")
            if response.introduction:
                print(f"Introduction: {response.introduction}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def rename_conversation_auto_generate():
    """Rename conversation with auto-generated name."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body with auto-generate enabled
    request_body = RenameConversationRequestBody.builder().auto_generate(True).user("user-123").build()

    # Build request
    request = RenameConversationRequest.builder().conversation_id(conversation_id).request_body(request_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.conversation.rename(request, request_option)

        if response.success:
            print(f"Successfully auto-generated name for conversation: {conversation_id}")
            print(f"Auto-generated name: {response.name}")
            print(f"Created at: {response.created_at}")
            print(f"Updated at: {response.updated_at}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def rename_conversation_clear_name():
    """Clear conversation name (set to None)."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body with name set to None
    request_body = RenameConversationRequestBody.builder().name(None).user("user-123").build()

    # Build request
    request = RenameConversationRequest.builder().conversation_id(conversation_id).request_body(request_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.conversation.rename(request, request_option)

        if response.success:
            print(f"Successfully cleared name for conversation: {conversation_id}")
            print(f"Name: {response.name}")
            print(f"Status: {response.status}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def rename_example_conversation():
    """Create and rename an example conversation for safety."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # First, create an example conversation
    from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
    from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody

    try:
        # Create a test conversation
        create_request_body = (
            SendChatMessageRequestBody.builder()
            .query(
                "[Example] Test conversation for renaming. Keep response brief. Please answer within 10 words. No thinking process."
            )
            .user("user-123")
            .response_mode("blocking")
            .build()
        )

        create_request = SendChatMessageRequest.builder().request_body(create_request_body).build()

        request_option = RequestOption.builder().api_key(api_key).build()

        # Create conversation
        create_response = client.chatflow.v1.chatflow.send(create_request, request_option)

        if create_response.success:
            conversation_id = create_response.conversation_id
            print(f"Created example conversation: {conversation_id}")

            # Now rename it
            rename_request_body = (
                RenameConversationRequestBody.builder()
                .name("[Example] Renamed Test Conversation")
                .user("user-123")
                .build()
            )

            rename_request = (
                RenameConversationRequest.builder()
                .conversation_id(conversation_id)
                .request_body(rename_request_body)
                .build()
            )

            # Execute rename
            rename_response = client.chatflow.v1.conversation.rename(rename_request, request_option)

            if rename_response.success:
                print(f"Successfully renamed example conversation: {conversation_id}")
                print(f"New name: {rename_response.name}")
            else:
                print(f"Error renaming conversation: {rename_response.msg}")
        else:
            print(f"Error creating conversation: {create_response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Rename Conversation Examples ===")

    print("\n1. Sync Example:")
    rename_conversation_sync()

    print("\n2. Async Example:")
    asyncio.run(rename_conversation_async())

    print("\n3. Auto-generate Name Example:")
    rename_conversation_auto_generate()

    print("\n4. Clear Name Example:")
    rename_conversation_clear_name()

    print("\n5. Safe Example (creates and renames):")
    rename_example_conversation()
