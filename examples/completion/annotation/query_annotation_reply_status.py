#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.annotation.query_annotation_reply_status_request import (
    QueryAnnotationReplyStatusRequest,
)
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def query_annotation_reply_status_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Use example job ID (in real usage, this would come from annotation_reply_settings response)
        job_id = "example-job-id-123"

        req = QueryAnnotationReplyStatusRequest.builder().action("enable").job_id(job_id).build()
        response = client.completion.v1.annotation.query_annotation_reply_status(req, req_option)

        if response.success:
            print(f"Job ID: {response.job_id}")
            print(f"Job Status: {response.job_status}")
            print(f"Error Message: {response.error_msg}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def query_annotation_reply_status_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Use example job ID (in real usage, this would come from annotation_reply_settings response)
        job_id = "example-job-id-456"

        req = QueryAnnotationReplyStatusRequest.builder().action("enable").job_id(job_id).build()
        response = await client.completion.v1.annotation.aquery_annotation_reply_status(req, req_option)

        if response.success:
            print(f"Job ID (async): {response.job_id}")
            print(f"Job Status (async): {response.job_status}")
            print(f"Error Message (async): {response.error_msg}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Query Annotation Reply Status Examples ===")

    print("\n1. Sync query annotation reply status:")
    query_annotation_reply_status_sync()

    print("\n2. Async query annotation reply status:")
    asyncio.run(query_annotation_reply_status_async())


if __name__ == "__main__":
    main()
