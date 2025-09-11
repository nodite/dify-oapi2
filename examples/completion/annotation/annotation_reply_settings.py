#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_request import (
    AnnotationReplySettingsRequest,
)
from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_request_body import (
    AnnotationReplySettingsRequestBody,
)
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def annotation_reply_settings_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_API_KEY")
        if not api_key:
            raise ValueError("COMPLETION_API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req_body = (
            AnnotationReplySettingsRequestBody.builder()
            .embedding_provider_name("openai")
            .embedding_model_name("text-embedding-ada-002")
            .score_threshold(0.8)
            .build()
        )

        req = AnnotationReplySettingsRequest.builder().action("enable").request_body(req_body).build()
        response = client.completion.v1.annotation.annotation_reply_settings(req, req_option)

        if response.success:
            print(f"Job ID: {response.job_id}")
            print(f"Job Status: {response.job_status}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def annotation_reply_settings_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_API_KEY")
        if not api_key:
            raise ValueError("COMPLETION_API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        req_body = (
            AnnotationReplySettingsRequestBody.builder()
            .embedding_provider_name("openai")
            .embedding_model_name("text-embedding-ada-002")
            .score_threshold(0.8)
            .build()
        )

        req = AnnotationReplySettingsRequest.builder().action("enable").request_body(req_body).build()
        response = await client.completion.v1.annotation.aannotation_reply_settings(req, req_option)

        if response.success:
            print(f"Job ID (async): {response.job_id}")
            print(f"Job Status (async): {response.job_status}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Annotation Reply Settings Examples ===")

    print("\n1. Sync annotation reply settings:")
    annotation_reply_settings_sync()

    print("\n2. Async annotation reply settings:")
    asyncio.run(annotation_reply_settings_async())


if __name__ == "__main__":
    main()
