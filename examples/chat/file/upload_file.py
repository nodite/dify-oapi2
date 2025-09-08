import asyncio
import os
from io import BytesIO

from dify_oapi.api.chat.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def upload_file():
    """Upload a file for chat"""
    api_key = os.getenv("CHAT_API_KEY")
    file_path = os.getenv("FILE_PATH")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not file_path:
        raise ValueError("FILE_PATH environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    try:
        with open(file_path, "rb") as f:
            file_data = BytesIO(f.read())

        req = UploadFileRequest.builder().file(file_data, os.path.basename(file_path)).user("user-123").build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.chat.v1.file.upload(req, req_option)
        print("File uploaded successfully!")
        print(f"File ID: {response.id}")
        print(f"File name: {response.name}")
        print(f"File size: {response.size} bytes")
        print(f"MIME type: {response.mime_type}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def upload_file_async():
    """Upload a file for chat asynchronously"""
    api_key = os.getenv("CHAT_API_KEY")
    file_path = os.getenv("FILE_PATH")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not file_path:
        raise ValueError("FILE_PATH environment variable is required")

    client = Client.builder().domain("https://api.dify.ai").build()

    try:
        with open(file_path, "rb") as f:
            file_data = BytesIO(f.read())

        req = UploadFileRequest.builder().file(file_data, os.path.basename(file_path)).user("user-123").build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.chat.v1.file.aupload(req, req_option)
        print("File uploaded asynchronously!")
        print(f"File ID: {response.id}")
        print(f"File name: {response.name}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    if os.getenv("FILE_PATH"):
        upload_file()
        asyncio.run(upload_file_async())
    else:
        print("FILE_PATH environment variable not set. Skipping file upload example.")
