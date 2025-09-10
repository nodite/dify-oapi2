#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chatflow.v1.model.delete_conversation_request_body import DeleteConversationRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_conversation_sync():
    """Delete conversation synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        raise ValueError("CONVERSATION_ID environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    request_body = DeleteConversationRequestBody.builder().user("user-123").build()

    # Build request
    request = DeleteConversationRequest.builder().conversation_id(conversation_id).request_body(request_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.conversation.delete(request, request_option)

        if response.success:
            print(f"Successfully deleted conversation: {conversation_id}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def delete_conversation_async():
    """Delete conversation asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID_2")
    if not conversation_id:
        raise ValueError("CONVERSATION_ID_2 environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    request_body = DeleteConversationRequestBody.builder().user("user-123").build()

    # Build request
    request = DeleteConversationRequest.builder().conversation_id(conversation_id).request_body(request_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.conversation.adelete(request, request_option)

        if response.success:
            print(f"Successfully deleted conversation (async): {conversation_id}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def delete_example_conversation():
    """Delete a conversation with [Example] prefix for safety."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # First, create an example conversation to delete
    from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
    from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody

    try:
        # Create a test conversation
        create_request_body = (
            SendChatMessageRequestBody.builder()
            .query("[Example] Test conversation for deletion")
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

            # Now delete it
            delete_request_body = DeleteConversationRequestBody.builder().user("user-123").build()

            delete_request = (
                DeleteConversationRequest.builder()
                .conversation_id(conversation_id)
                .request_body(delete_request_body)
                .build()
            )

            # Execute delete
            delete_response = client.chatflow.v1.conversation.delete(delete_request, request_option)

            if delete_response.success:
                print(f"Successfully deleted example conversation: {conversation_id}")
            else:
                print(f"Error deleting conversation: {delete_response.msg}")
        else:
            print(f"Error creating conversation: {create_response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def delete_conversation_with_confirmation():
    """Delete conversation with user confirmation."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    conversation_id = os.getenv("CONVERSATION_ID")
    if not conversation_id:
        raise ValueError("CONVERSATION_ID environment variable is required")

    # Safety check - only delete conversations with [Example] prefix
    if not conversation_id.startswith("[Example]"):
        print("Safety check: Only conversations with '[Example]' prefix can be deleted")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    request_body = DeleteConversationRequestBody.builder().user("user-123").build()

    # Build request
    request = DeleteConversationRequest.builder().conversation_id(conversation_id).request_body(request_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Confirm deletion
        print(f"About to delete conversation: {conversation_id}")
        confirmation = input("Are you sure? (yes/no): ")

        if confirmation.lower() == "yes":
            # Execute request
            response = client.chatflow.v1.conversation.delete(request, request_option)

            if response.success:
                print(f"Successfully deleted conversation: {conversation_id}")
            else:
                print(f"Error: {response.msg}")
        else:
            print("Deletion cancelled")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Delete Conversation Examples ===")

    print("\n1. Sync Example:")
    delete_conversation_sync()

    print("\n2. Async Example:")
    asyncio.run(delete_conversation_async())

    print("\n3. Safe Example (creates and deletes):")
    delete_example_conversation()

    print("\n4. Confirmation Example:")
    delete_conversation_with_confirmation()
