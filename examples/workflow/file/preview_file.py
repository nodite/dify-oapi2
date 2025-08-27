#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.workflow.v1.model.file.preview_file_request import PreviewFileRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def preview_file_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        file_id = os.getenv("FILE_ID")
        if not file_id:
            raise ValueError("FILE_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = PreviewFileRequest.builder().file_id(file_id).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.file.preview_file(req, req_option)

        if response.success:
            print(f"File preview: {response.content_type}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def preview_file_async() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        file_id = os.getenv("FILE_ID")
        if not file_id:
            raise ValueError("FILE_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = PreviewFileRequest.builder().file_id(file_id).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.workflow.v1.file.apreview_file(req, req_option)

        if response.success:
            print(f"File preview: {response.content_type}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def preview_file_as_attachment() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        file_id = os.getenv("FILE_ID")
        if not file_id:
            raise ValueError("FILE_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = PreviewFileRequest.builder().file_id(file_id).as_attachment(True).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.file.preview_file(req, req_option)

        if response.success:
            print(f"File download: {response.content_type}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Preview File Sync ===")
    preview_file_sync()

    print("\n=== Preview File Async ===")
    asyncio.run(preview_file_async())

    print("\n=== Preview File as Attachment ===")
    preview_file_as_attachment()
