#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.annotation_reply_settings_request import AnnotationReplySettingsRequest
from dify_oapi.api.chatflow.v1.model.annotation_reply_settings_request_body import AnnotationReplySettingsRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def enable_annotation_reply_sync():
    """Enable annotation reply settings synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    req_body = (
        AnnotationReplySettingsRequestBody.builder()
        .embedding_provider_name("openai")
        .embedding_model_name("text-embedding-ada-002")
        .score_threshold(0.8)
        .build()
    )

    # Build request
    request = AnnotationReplySettingsRequest.builder().action("enable").request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.annotation.reply_settings(request, request_option)

        if response.success:
            print("Enabled annotation reply settings successfully!")
            print(f"Job ID: {response.job_id}")
            print(f"Job Status: {response.job_status}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def enable_annotation_reply_async():
    """Enable annotation reply settings asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    req_body = (
        AnnotationReplySettingsRequestBody.builder()
        .embedding_provider_name("openai")
        .embedding_model_name("text-embedding-3-small")
        .score_threshold(0.75)
        .build()
    )

    # Build request
    request = AnnotationReplySettingsRequest.builder().action("enable").request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.annotation.areply_settings(request, request_option)

        if response.success:
            print("Enabled annotation reply settings successfully (async)!")
            print(f"Job ID: {response.job_id}")
            print(f"Job Status: {response.job_status}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def disable_annotation_reply_sync():
    """Disable annotation reply settings synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body (minimal for disable)
    req_body = AnnotationReplySettingsRequestBody.builder().score_threshold(0.0).build()

    # Build request
    request = AnnotationReplySettingsRequest.builder().action("disable").request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.annotation.reply_settings(request, request_option)

        if response.success:
            print("Disabled annotation reply settings successfully!")
            print(f"Job ID: {response.job_id}")
            print(f"Job Status: {response.job_status}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def configure_annotation_reply_with_different_models():
    """Configure annotation reply with different embedding models."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    # Different embedding configurations to try
    configurations = [
        {"name": "OpenAI Ada-002", "provider": "openai", "model": "text-embedding-ada-002", "threshold": 0.8},
        {"name": "OpenAI 3-Small", "provider": "openai", "model": "text-embedding-3-small", "threshold": 0.75},
        {"name": "High Precision", "provider": "openai", "model": "text-embedding-3-large", "threshold": 0.9},
    ]

    try:
        for i, config in enumerate(configurations):
            print(f"\nConfiguring {config['name']}...")

            # Build request body
            req_body = (
                AnnotationReplySettingsRequestBody.builder()
                .embedding_provider_name(config["provider"])
                .embedding_model_name(config["model"])
                .score_threshold(config["threshold"])
                .build()
            )

            # Build request
            request = AnnotationReplySettingsRequest.builder().action("enable").request_body(req_body).build()

            # Execute request
            response = client.chatflow.v1.annotation.reply_settings(request, request_option)

            if response.success:
                print("  ✓ Configured successfully")
                print(f"    Job ID: {response.job_id}")
                print(f"    Job Status: {response.job_status}")

                # For demo purposes, only configure the first one
                if i == 0:
                    print(f"  Using {config['name']} configuration for this example")
                    break
            else:
                print(f"  ✗ Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Annotation Reply Settings Examples ===")

    print("\n1. Enable Sync Example:")
    enable_annotation_reply_sync()

    print("\n2. Enable Async Example:")
    asyncio.run(enable_annotation_reply_async())

    print("\n3. Disable Example:")
    disable_annotation_reply_sync()

    print("\n4. Different Models Configuration:")
    configure_annotation_reply_with_different_models()
