#!/usr/bin/env python3

import asyncio
import os
from io import BytesIO

from dify_oapi.api.completion.v1.model.file.upload_file_request import UploadFileRequest
from dify_oapi.api.completion.v1.model.file.upload_file_request_body import UploadFileRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def upload_file_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Create sample image file
        sample_image = BytesIO(b"fake_image_data_for_example")

        req_body = UploadFileRequestBody.builder().user("[Example] User").build()

        req = UploadFileRequest.builder().file(sample_image, "[Example] test_image.jpg").request_body(req_body).build()

        response = client.completion.v1.file.upload_file(req, req_option)

        if response.success:
            print(f"File uploaded: {response.name} ({response.size} bytes)")
        else:
            print(f"Upload failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def upload_file_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Create sample image file
        sample_image = BytesIO(b"fake_image_data_for_example")

        req_body = UploadFileRequestBody.builder().user("[Example] User").build()

        req = UploadFileRequest.builder().file(sample_image, "[Example] test_image.jpg").request_body(req_body).build()

        response = await client.completion.v1.file.aupload_file(req, req_option)

        if response.success:
            print(f"File uploaded: {response.name} ({response.size} bytes)")
        else:
            print(f"Upload failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== File Upload Examples ===")

    print("\n1. Sync Upload:")
    upload_file_sync()

    print("\n2. Async Upload:")
    asyncio.run(upload_file_async())


if __name__ == "__main__":
    main()
