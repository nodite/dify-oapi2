import asyncio
import os

from dify_oapi.api.chat.v1.model.get_conversation_variables_request import GetConversationVariablesRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_conversation_variables():
    """Get conversation variables"""
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

    req = GetConversationVariablesRequest.builder().conversation_id(conversation_id).user("user-123").limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.variables(req, req_option)
        print(f"Retrieved {len(response.data)} variables")
        print(f"Has more: {response.has_more}")

        for variable in response.data:
            print(f"- Variable ID: {variable.id}")
            print(f"  Name: {variable.name}")
            print(f"  Value Type: {variable.value_type}")
            print(f"  Value: {variable.value}")
            print(f"  Description: {variable.description}")
            print()

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def get_conversation_variables_filtered():
    """Get conversation variables with name filter"""
    api_key = os.getenv("CHAT_KEY")
    conversation_id = os.getenv("CONVERSATION_ID")
    variable_name = os.getenv("VARIABLE_NAME")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_builder = GetConversationVariablesRequest.builder().conversation_id(conversation_id).user("user-123").limit(10)
    if variable_name:
        req_builder.variable_name(variable_name)
    req = req_builder.build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.variables(req, req_option)
        print(f"Retrieved {len(response.data)} variables (filtered)")

        for variable in response.data:
            print(f"- {variable.name}: {variable.value}")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def get_conversation_variables_paginated():
    """Get conversation variables with pagination"""
    api_key = os.getenv("CHAT_KEY")
    conversation_id = os.getenv("CONVERSATION_ID")
    last_id = os.getenv("LAST_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not conversation_id:
        print("Note: CONVERSATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real conversation id to execute.")
        print("Set CONVERSATION_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_builder = GetConversationVariablesRequest.builder().conversation_id(conversation_id).user("user-123").limit(5)
    if last_id:
        req_builder.last_id(last_id)
    req = req_builder.build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.conversation.variables(req, req_option)
        print(f"Retrieved {len(response.data)} variables (paginated)")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def get_conversation_variables_async():
    """Get conversation variables asynchronously"""
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

    req = GetConversationVariablesRequest.builder().conversation_id(conversation_id).user("user-123").limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.conversation.avariables(req, req_option)
        print(f"Async retrieved {len(response.data)} variables")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    get_conversation_variables()
    get_conversation_variables_filtered()
    get_conversation_variables_paginated()
    asyncio.run(get_conversation_variables_async())
