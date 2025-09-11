"""
Dify System-level API - File Upload Example

Demonstrates how to use the unified dify.v1.file API for file upload
"""

import os

from dify_oapi.api.dify.v1.model.upload_file_body import UploadFileBody
from dify_oapi.api.dify.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def upload_file_example():
    """File upload example"""

    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    # Initialize client
    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    # Build file upload request
    if os.path.exists("README.md"):
        file_body = UploadFileBody.builder().user("user-123").build()
        request = UploadFileRequest.builder().file(open("README.md", "rb"), "README.md").request_body(file_body).build()
    else:
        print("README.md not found, skipping upload")
        return

    try:
        # Execute file upload
        response = client.dify.v1.file.upload(request, request_option)

        print("File upload successful:")
        print(f"File ID: {response.id}")
        print(f"File name: {response.name}")
        print(f"File size: {response.size}")
        print(f"File type: {response.type}")

    except Exception as e:
        print(f"File upload failed: {e}")


async def async_upload_file_example():
    """Async file upload example"""

    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
    request_option = RequestOption.builder().api_key(api_key).build()

    if os.path.exists("README.md"):
        file_body = UploadFileBody.builder().user("user-123").build()
        request = UploadFileRequest.builder().file(open("README.md", "rb"), "README.md").request_body(file_body).build()
    else:
        print("README.md not found, skipping upload")
        return

    try:
        # Execute async file upload
        response = await client.dify.v1.file.aupload(request, request_option)

        print("Async file upload successful:")
        print(f"File ID: {response.id}")

    except Exception as e:
        print(f"Async file upload failed: {e}")


if __name__ == "__main__":
    print("=== Dify System-level API - File Upload Example ===")
    upload_file_example()

    # Async example needs to run in async environment
    # import asyncio
    # asyncio.run(async_upload_file_example())
