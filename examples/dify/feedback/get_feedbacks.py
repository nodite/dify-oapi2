"""
Dify System API - Get Feedbacks Example

Demonstrates how to retrieve feedback list with pagination and filtering.
"""

import os

from dify_oapi.api.dify.v1.model.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_feedbacks_sync():
    """Synchronous feedback list retrieval"""

    # Environment validation
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    page = int(os.getenv("PAGE", "1"))
    limit = int(os.getenv("LIMIT", "10"))
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    # Initialize client
    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    # Build request
    request = GetFeedbacksRequest.builder().page(page).limit(limit).build()

    try:
        # Get feedback list
        response = client.dify.v1.feedback.list(request, request_option)

        print("Feedback list retrieved successfully:")
        print(f"Total feedbacks: {response.total}")
        print(f"Current page: {response.page}")
        print(f"Items per page: {response.limit}")
        print(f"Has more pages: {response.has_more}")

        print("\nFeedback details:")
        for i, feedback in enumerate(response.data, 1):
            print(f"{i}. Feedback ID: {feedback.id}")
            print(f"   Rating: {feedback.rating}")
            print(f"   Content: {feedback.content}")
            print(f"   User: {feedback.user}")
            print(f"   Message ID: {feedback.message_id}")
            print(f"   Created at: {feedback.created_at}")
            print()

        return response

    except Exception as e:
        print(f"Failed to get feedback list: {e}")
        raise


def get_feedbacks_with_pagination():
    """Get feedbacks with custom pagination"""

    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    # Get first page
    request = GetFeedbacksRequest.builder().page(1).limit(5).build()

    try:
        response = client.dify.v1.feedback.list(request, request_option)

        print("First page of feedbacks:")
        print(f"Total: {response.total}, Page: {response.page}, Limit: {response.limit}")

        # Get second page if available
        if response.has_more:
            request = GetFeedbacksRequest.builder().page(2).limit(5).build()

            response2 = client.dify.v1.feedback.list(request, request_option)
            print("\nSecond page of feedbacks:")
            print(f"Total: {response2.total}, Page: {response2.page}, Limit: {response2.limit}")

        return response

    except Exception as e:
        print(f"Failed to get paginated feedbacks: {e}")
        raise


async def get_feedbacks_async():
    """Asynchronous feedback list retrieval"""

    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    page = int(os.getenv("PAGE", "1"))
    limit = int(os.getenv("LIMIT", "10"))
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    request = GetFeedbacksRequest.builder().page(page).limit(limit).build()

    try:
        response = await client.dify.v1.feedback.alist(request, request_option)

        print("Async feedback list retrieved successfully:")
        print(f"Total feedbacks: {response.total}")
        print(f"Retrieved {len(response.data)} feedbacks")

        return response

    except Exception as e:
        print(f"Async feedback retrieval failed: {e}")
        raise


if __name__ == "__main__":
    print("=== Dify System API - Get Feedbacks Example ===")

    print("\n1. Get feedback list:")
    get_feedbacks_sync()

    print("\n2. Get feedbacks with pagination:")
    get_feedbacks_with_pagination()
