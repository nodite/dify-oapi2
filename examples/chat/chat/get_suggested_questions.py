import asyncio
import os

from dify_oapi.api.chat.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_suggested_questions():
    """Get suggested questions for a message"""
    api_key = os.getenv("CHAT_API_KEY")
    message_id = os.getenv("MESSAGE_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not message_id:
        print("Note: MESSAGE_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real message id to execute.")
        print("Set MESSAGE_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetSuggestedQuestionsRequest.builder().message_id(message_id).user("user-123").build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.chat.suggested(req, req_option)
        print("Suggested questions:")
        if hasattr(response, "data") and response.data:
            for i, question in enumerate(response.data, 1):
                print(f"{i}. {question}")
        else:
            print(response.msg)
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def get_suggested_questions_async():
    """Get suggested questions for a message asynchronously"""
    api_key = os.getenv("CHAT_API_KEY")
    message_id = os.getenv("MESSAGE_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not message_id:
        print("Note: MESSAGE_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real message id to execute.")
        print("Set MESSAGE_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetSuggestedQuestionsRequest.builder().message_id(message_id).user("user-123").build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.chat.asuggested(req, req_option)
        print("Async suggested questions:")
        if hasattr(response, "data") and response.data:
            for i, question in enumerate(response.data, 1):
                print(f"{i}. {question}")
        else:
            print("No suggested questions available (async)")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    get_suggested_questions()
    asyncio.run(get_suggested_questions_async())
