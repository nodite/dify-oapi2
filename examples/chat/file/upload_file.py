import asyncio
import os
from io import BytesIO

from dify_oapi.api.chat.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.chat.v1.model.upload_file_request_body import UploadFileRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def upload_file():
    """Upload a file for chat"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    try:
        # Create sample image content (simple PNG header)
        # This is a minimal 1x1 pixel PNG image
        png_content = (
            b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
            b"\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\tpHYs\x00\x00\x0b\x13"
            b"\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\nIDATx\x9cc```"
            b"\x00\x00\x00\x02\x00\x01H\xaf\xa4q\x00\x00\x00\x00IEND\xaeB`\x82"
        )
        file_data = BytesIO(png_content)

        req_body = UploadFileRequestBody.builder().user("[Example] user-123").build()
        req = UploadFileRequest.builder().file(file_data, "[Example] test_image.png").request_body(req_body).build()
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
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    try:
        # Create sample image content (simple PNG header)
        # This is a minimal 1x1 pixel PNG image
        png_content = (
            b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
            b"\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\tpHYs\x00\x00\x0b\x13"
            b"\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\nIDATx\x9cc```"
            b"\x00\x00\x00\x02\x00\x01H\xaf\xa4q\x00\x00\x00\x00IEND\xaeB`\x82"
        )
        file_data = BytesIO(png_content)

        req_body = UploadFileRequestBody.builder().user("[Example] user-123").build()
        req = (
            UploadFileRequest.builder().file(file_data, "[Example] test_image_async.png").request_body(req_body).build()
        )
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
    print("=== Upload File Sync ===")
    upload_file()

    print("\n=== Upload File Async ===")
    asyncio.run(upload_file_async())
