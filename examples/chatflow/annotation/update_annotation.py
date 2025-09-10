#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.chatflow.v1.model.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_annotation_sync():
    """Update annotation synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    annotation_id = os.getenv("ANNOTATION_ID")
    if not annotation_id:
        raise ValueError("ANNOTATION_ID environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request body
    req_body = (
        UpdateAnnotationRequestBody.builder()
        .question("[Example] What is the updated purpose of this chatflow API?")
        .answer(
            "[Example] This updated chatflow API provides comprehensive advanced chat functionality with enhanced workflow events, improved file support, robust conversation management, and extensive application configuration settings."
        )
        .build()
    )

    # Build request
    request = UpdateAnnotationRequest.builder().annotation_id(annotation_id).request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.annotation.update(request, request_option)

        if response.success:
            print("Updated annotation successfully!")
            print(f"Annotation ID: {response.id}")
            print(f"Question: {response.question}")
            print(f"Answer: {response.answer}")
            print(f"Hit Count: {response.hit_count}")
            print(f"Created at: {response.created_at}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def update_annotation_async():
    """Update annotation asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    annotation_id = os.getenv("ANNOTATION_ID")
    if not annotation_id:
        raise ValueError("ANNOTATION_ID environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request body
    req_body = (
        UpdateAnnotationRequestBody.builder()
        .question("[Example] How do I use the enhanced streaming mode in chatflow?")
        .answer(
            "[Example] Set response_mode to 'streaming' in your request to enable real-time streaming responses with comprehensive Server-Sent Events including workflow events, TTS messages, and error handling."
        )
        .build()
    )

    # Build request
    request = UpdateAnnotationRequest.builder().annotation_id(annotation_id).request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.annotation.aupdate(request, request_option)

        if response.success:
            print("Updated annotation successfully (async)!")
            print(f"Annotation ID: {response.id}")
            print(f"Question: {response.question}")
            print(f"Answer: {response.answer[:100]}...")
            print(f"Hit Count: {response.hit_count}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def update_annotation_with_validation():
    """Update annotation with validation example."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    annotation_id = os.getenv("ANNOTATION_ID")
    if not annotation_id:
        raise ValueError("ANNOTATION_ID environment variable is required")

    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # First, get the current annotation to validate it exists
        from dify_oapi.api.chatflow.v1.model.get_annotations_request import GetAnnotationsRequest

        get_request = GetAnnotationsRequest.builder().page(1).limit(100).build()
        get_response = client.chatflow.v1.annotation.list(get_request, request_option)

        if not get_response.success:
            print(f"Error getting annotations: {get_response.msg}")
            return

        # Find the annotation to update
        target_annotation = None
        for annotation in get_response.data:
            if annotation.id == annotation_id:
                target_annotation = annotation
                break

        if not target_annotation:
            print(f"Annotation with ID {annotation_id} not found")
            return

        print("Found annotation to update:")
        print(f"  Current Question: {target_annotation.question}")
        print(f"  Current Answer: {target_annotation.answer[:100]}...")

        # Build updated request body
        req_body = (
            UpdateAnnotationRequestBody.builder()
            .question(f"[Example] Updated: {target_annotation.question}")
            .answer(f"[Example] Enhanced: {target_annotation.answer}")
            .build()
        )

        # Build request
        request = UpdateAnnotationRequest.builder().annotation_id(annotation_id).request_body(req_body).build()

        # Execute update request
        response = client.chatflow.v1.annotation.update(request, request_option)

        if response.success:
            print("Successfully updated annotation!")
            print(f"  New Question: {response.question}")
            print(f"  New Answer: {response.answer[:100]}...")
            print(f"  Hit Count: {response.hit_count}")
        else:
            print(f"Error updating annotation: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Update Annotation Examples ===")

    print("\n1. Sync Example:")
    update_annotation_sync()

    print("\n2. Async Example:")
    asyncio.run(update_annotation_async())

    print("\n3. Update with Validation Example:")
    update_annotation_with_validation()
