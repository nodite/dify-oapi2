#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.annotation.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_annotation_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req_body = (
            CreateAnnotationRequestBody.builder()
            .question("[Example] What is the completion API?")
            .answer("[Example] The completion API is used for text generation tasks.")
            .build()
        )

        req = CreateAnnotationRequest.builder().request_body(req_body).build()
        response = client.completion.v1.annotation.create_annotation(req, req_option)

        if response.success:
            print(f"Annotation created: {response.id}")
            print(f"Question: {response.question}")
            print(f"Answer: {response.answer}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def create_annotation_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req_body = (
            CreateAnnotationRequestBody.builder()
            .question("[Example] How to use async completion API?")
            .answer("[Example] Use the async methods with await keyword for non-blocking operations.")
            .build()
        )

        req = CreateAnnotationRequest.builder().request_body(req_body).build()
        response = await client.completion.v1.annotation.acreate_annotation(req, req_option)

        if response.success:
            print(f"Annotation created (async): {response.id}")
            print(f"Question (async): {response.question}")
            print(f"Answer (async): {response.answer}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Create Annotation Examples ===")

    print("\n1. Sync create annotation:")
    create_annotation_sync()

    print("\n2. Async create annotation:")
    asyncio.run(create_annotation_async())


if __name__ == "__main__":
    main()
