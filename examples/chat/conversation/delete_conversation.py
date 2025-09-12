import asyncio
import os

from dify_oapi.api.chat.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chat.v1.model.delete_conversation_request_body import DeleteConversationRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_conversation():
    """Delete a conversation"""
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

    req_body = DeleteConversationRequestBody.builder().user("user-123").build()
    req = DeleteConversationRequest.builder().conversation_id(conversation_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.delete(req, req_option)
        print("Conversation deleted successfully")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def delete_conversation_async():
    """Delete a conversation asynchronously"""
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

    req_body = DeleteConversationRequestBody.builder().user("user-123").build()
    req = DeleteConversationRequest.builder().conversation_id(conversation_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.conversation.adelete(req, req_option)
        print("Conversation deleted asynchronously")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    delete_conversation()
    asyncio.run(delete_conversation_async())
