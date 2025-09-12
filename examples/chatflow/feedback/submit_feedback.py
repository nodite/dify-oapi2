"""
Dify System API - Submit Feedback Example

Demonstrates how to submit user feedback (like/dislike) for messages.
"""

import os

from dify_oapi.api.dify.v1.model.submit_feedback_request import SubmitFeedbackRequest
from dify_oapi.api.dify.v1.model.submit_feedback_request_body import SubmitFeedbackRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def submit_positive_feedback():
    """Submit positive feedback (like)"""

    # Environment validation
    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    message_id = os.getenv("MESSAGE_ID")
    if not message_id:
        print("Note: MESSAGE_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real message id to execute.")
        print("Set MESSAGE_ID environment variable with a valid ID to test this functionality.")
        return

    user_id = os.getenv("USER_ID", "user-123")
    feedback_content = os.getenv("FEEDBACK_CONTENT", "This answer is very helpful!")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    # Initialize client
    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    # Build request
    request_body = SubmitFeedbackRequestBody.builder().rating("like").user(user_id).content(feedback_content).build()

    request = SubmitFeedbackRequest.builder().message_id(message_id).request_body(request_body).build()

    try:
        # Submit feedback
        response = client.dify.v1.feedback.submit(request, request_option)

        print("Positive feedback submitted successfully:")
        print(f"Feedback ID: {response.result}")
        return response

    except Exception as e:
        print(f"Failed to submit positive feedback: {e}")
        raise


def submit_negative_feedback():
    """Submit negative feedback (dislike)"""

    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    message_id = os.getenv("MESSAGE_ID")
    if not message_id:
        print("Note: MESSAGE_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real message id to execute.")
        print("Set MESSAGE_ID environment variable with a valid ID to test this functionality.")
        return

    user_id = os.getenv("USER_ID", "user-123")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    request_body = (
        SubmitFeedbackRequestBody.builder()
        .rating("dislike")
        .user(user_id)
        .content("The answer needs improvement.")
        .build()
    )

    request = SubmitFeedbackRequest.builder().message_id(message_id).request_body(request_body).build()

    try:
        response = client.dify.v1.feedback.submit(request, request_option)
        print(f"Negative feedback submitted successfully: {response.result}")
        return response

    except Exception as e:
        print(f"Failed to submit negative feedback: {e}")
        raise


async def submit_feedback_async():
    """Asynchronous feedback submission"""

    api_key = os.getenv("DIFY_KEY")
    if not api_key:
        raise ValueError("DIFY_KEY environment variable is required")

    message_id = os.getenv("MESSAGE_ID")
    if not message_id:
        print("Note: MESSAGE_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real message id to execute.")
        print("Set MESSAGE_ID environment variable with a valid ID to test this functionality.")
        return

    rating = os.getenv("RATING", "like")
    user_id = os.getenv("USER_ID", "user-123")
    domain = os.getenv("DOMAIN", "https://api.dify.ai")

    client = Client.builder().domain(domain).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    request_body = (
        SubmitFeedbackRequestBody.builder().rating(rating).user(user_id).content("Async feedback submission").build()
    )

    request = SubmitFeedbackRequest.builder().message_id(message_id).request_body(request_body).build()

    try:
        response = await client.dify.v1.feedback.asubmit(request, request_option)
        print(f"Async feedback submitted successfully: {response.result}")
        return response

    except Exception as e:
        print(f"Async feedback submission failed: {e}")
        raise


if __name__ == "__main__":
    print("=== Dify System API - Submit Feedback Example ===")

    print("\n1. Submit positive feedback:")
    submit_positive_feedback()

    print("\n2. Submit negative feedback:")
    submit_negative_feedback()
