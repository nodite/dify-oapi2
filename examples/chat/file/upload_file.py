"""
Chat File Upload Example

This example demonstrates how to upload files in the Chat API.
"""

import os

from dify_oapi.api.chat.v1.model.chat_file import ChatFile
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def upload_image_example():
    """Upload an image file and ask about it."""
    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    # Create file object with remote URL
    req_file = (
        ChatFile.builder()
        .type("image")
        .transfer_method("remote_url")
        .url("https://cloud.dify.ai/logo/logo-site.png")
        .build()
    )

    req_body = (
        ChatRequestBody.builder()
        .inputs({})
        .query("What do you see in this image? Please be concise. Please answer within 10 words. No thinking process.")
        .response_mode("blocking")
        .user("user-123")
        .files([req_file])
        .build()
    )

    req = ChatRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(os.getenv("CHAT_KEY", "<your-api-key>")).build()

    try:
        response = client.chat.v1.chat.chat(req, req_option, False)
        print(f"Response: {response.answer}")
    except Exception as e:
        print(f"Error: {e}")


def upload_document_example():
    """Upload a document file."""
    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    # Create file object for document
    req_file = (
        ChatFile.builder()
        .type("document")
        .transfer_method("local_file")
        .upload_file_id("your-uploaded-file-id")  # Get this from file upload API
        .build()
    )

    req_body = (
        ChatRequestBody.builder()
        .inputs({})
        .query("Please provide a brief summary of this document. Please answer within 10 words. No thinking process.")
        .response_mode("blocking")
        .user("user-123")
        .files([req_file])
        .build()
    )

    req = ChatRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(os.getenv("CHAT_KEY", "<your-api-key>")).build()

    try:
        response = client.chat.v1.chat.chat(req, req_option, False)
        print(f"Response: {response.answer}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Run file upload examples."""
    print("=== Image Upload Example ===")
    upload_image_example()

    print("\n=== Document Upload Example ===")
    upload_document_example()


if __name__ == "__main__":
    main()
