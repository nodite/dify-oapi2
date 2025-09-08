import asyncio
import os

from dify_oapi.api.chat.v1.model.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_feedbacks():
    """Get application feedbacks"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetFeedbacksRequest.builder().page(1).limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.feedback.list(req, req_option)
        print(f"Retrieved {len(response.data)} feedbacks")

        for feedback in response.data:
            print(f"- ID: {feedback.id}")
            print(f"  Rating: {feedback.rating}")
            print(f"  Content: {feedback.content}")
            print(f"  Created: {feedback.created_at}")
            print()

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def get_feedbacks_paginated():
    """Get feedbacks with pagination"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetFeedbacksRequest.builder().page(2).limit(10).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.feedback.list(req, req_option)
        print(f"Retrieved {len(response.data)} feedbacks (page 2, limit 10)")

        for feedback in response.data:
            print(f"- ID: {feedback.id}")
            print(f"  Rating: {feedback.rating}")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def get_feedbacks_async():
    """Get feedbacks asynchronously"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetFeedbacksRequest.builder().page(1).limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.feedback.alist(req, req_option)
        print(f"Async retrieved {len(response.data)} feedbacks")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    get_feedbacks()
    get_feedbacks_paginated()
    asyncio.run(get_feedbacks_async())
