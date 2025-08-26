#!/usr/bin/env python3

import asyncio
import os
from io import BytesIO

from dify_oapi.api.workflow.v1.model.file.upload_file_request import UploadFileRequest
from dify_oapi.api.workflow.v1.model.file.upload_file_request_body import UploadFileRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def upload_file_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        # Create sample file content
        file_content = b"[Example] This is a test document for upload."
        file_stream = BytesIO(file_content)

        req_body = UploadFileRequestBody.builder().user("[Example] user-123").build()

        req = (
            UploadFileRequest.builder().file(file_stream, "[Example] test_document.txt").request_body(req_body).build()
        )
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.file.upload_file(req, req_option)

        if response.success:
            print(f"File uploaded: {response.id}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def upload_file_async() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        # Create sample file content
        file_content = b"[Example] This is a test document for async upload."
        file_stream = BytesIO(file_content)

        req_body = UploadFileRequestBody.builder().user("[Example] user-123").build()

        req = (
            UploadFileRequest.builder()
            .file(file_stream, "[Example] test_document_async.txt")
            .request_body(req_body)
            .build()
        )
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.workflow.v1.file.aupload_file(req, req_option)

        if response.success:
            print(f"File uploaded: {response.id}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Upload File Sync ===")
    upload_file_sync()

    print("\n=== Upload File Async ===")
    asyncio.run(upload_file_async())
