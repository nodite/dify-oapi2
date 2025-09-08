import asyncio
import os

from dify_oapi.api.chat.v1.model.submit_feedback_request import SubmitFeedbackRequest
from dify_oapi.api.chat.v1.model.submit_feedback_request_body import SubmitFeedbackRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def submit_positive_feedback():
    """Submit positive feedback for a message"""
    api_key = os.getenv("CHAT_API_KEY")
    message_id = os.getenv("MESSAGE_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not message_id:
        raise ValueError("MESSAGE_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = (
        SubmitFeedbackRequestBody.builder()
        .rating("like")
        .user("user-123")
        .content("Great response! Very helpful.")
        .build()
    )

    req = SubmitFeedbackRequest.builder().message_id(message_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.feedback.submit(req, req_option)
        print(f"Feedback submitted: {response.result}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def submit_negative_feedback():
    """Submit negative feedback for a message"""
    api_key = os.getenv("CHAT_API_KEY")
    message_id = os.getenv("MESSAGE_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not message_id:
        raise ValueError("MESSAGE_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = (
        SubmitFeedbackRequestBody.builder()
        .rating("dislike")
        .user("user-123")
        .content("Response could be improved.")
        .build()
    )

    req = SubmitFeedbackRequest.builder().message_id(message_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.feedback.submit(req, req_option)
        print(f"Feedback submitted: {response.result}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def submit_feedback_async():
    """Submit feedback asynchronously"""
    api_key = os.getenv("CHAT_API_KEY")
    message_id = os.getenv("MESSAGE_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not message_id:
        raise ValueError("MESSAGE_ID environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    req_body = (
        SubmitFeedbackRequestBody.builder()
        .rating("like")
        .user("user-123")
        .content("Async feedback submission test.")
        .build()
    )

    req = SubmitFeedbackRequest.builder().message_id(message_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.feedback.asubmit(req, req_option)
        print(f"Async feedback submitted: {response.result}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    submit_positive_feedback()
    submit_negative_feedback()
    asyncio.run(submit_feedback_async())
