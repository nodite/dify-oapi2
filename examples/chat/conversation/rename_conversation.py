import asyncio
import os

from dify_oapi.api.chat.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chat.v1.model.rename_conversation_request_body import RenameConversationRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def rename_conversation():
    """Rename a conversation"""
    api_key = os.getenv("CHAT_API_KEY")
    conversation_id = os.getenv("CONVERSATION_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not conversation_id:
        raise ValueError("CONVERSATION_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = RenameConversationRequestBody.builder().name("My Important Chat").user("user-123").build()
    req = RenameConversationRequest.builder().conversation_id(conversation_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.rename(req, req_option)
        print("Conversation renamed successfully")
        print(f"New name: {response.name}")
        print(f"Updated at: {response.updated_at}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def rename_conversation_auto_generate():
    """Rename a conversation with auto-generated name"""
    api_key = os.getenv("CHAT_API_KEY")
    conversation_id = os.getenv("CONVERSATION_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not conversation_id:
        raise ValueError("CONVERSATION_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = RenameConversationRequestBody.builder().auto_generate(True).user("user-123").build()
    req = RenameConversationRequest.builder().conversation_id(conversation_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.rename(req, req_option)
        print("Conversation renamed with auto-generated name")
        print(f"Generated name: {response.name}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def rename_conversation_async():
    """Rename a conversation asynchronously"""
    api_key = os.getenv("CHAT_API_KEY")
    conversation_id = os.getenv("CONVERSATION_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not conversation_id:
        raise ValueError("CONVERSATION_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = RenameConversationRequestBody.builder().name("Async Renamed Chat").user("user-123").build()
    req = RenameConversationRequest.builder().conversation_id(conversation_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.conversation.arename(req, req_option)
        print("Conversation renamed asynchronously")
        print(f"New name: {response.name}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    rename_conversation()
    rename_conversation_auto_generate()
    asyncio.run(rename_conversation_async())
