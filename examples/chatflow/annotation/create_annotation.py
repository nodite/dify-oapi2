#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chatflow.v1.model.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_annotation_sync():
    """Create annotation synchronously."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    req_body = (
        CreateAnnotationRequestBody.builder()
        .question("[Example] What is the purpose of this chatflow API?")
        .answer(
            "[Example] This chatflow API provides advanced chat functionality with workflow events, file support, conversation management, and comprehensive application settings."
        )
        .build()
    )

    # Build request
    request = CreateAnnotationRequest.builder().request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.annotation.create(request, request_option)

        if response.success:
            print("Created annotation successfully!")
            print(f"Annotation ID: {response.id}")
            print(f"Question: {response.question}")
            print(f"Answer: {response.answer}")
            print(f"Hit Count: {response.hit_count}")
            print(f"Created at: {response.created_at}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def create_annotation_async():
    """Create annotation asynchronously."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request body
    req_body = (
        CreateAnnotationRequestBody.builder()
        .question("[Example] How do I use the streaming mode in chatflow?")
        .answer(
            "[Example] Set response_mode to 'streaming' in your request to enable real-time streaming responses with Server-Sent Events."
        )
        .build()
    )

    # Build request
    request = CreateAnnotationRequest.builder().request_body(req_body).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.annotation.acreate(request, request_option)

        if response.success:
            print("Created annotation successfully (async)!")
            print(f"Annotation ID: {response.id}")
            print(f"Question: {response.question}")
            print(f"Answer: {response.answer[:100]}...")
            print(f"Hit Count: {response.hit_count}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def create_multiple_annotations():
    """Create multiple annotations example."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    annotations_to_create = [
        {
            "question": "[Example] What file types are supported for upload?",
            "answer": "[Example] Supported file types include documents (TXT, MD, PDF, HTML, XLSX, DOCX, CSV, EML, MSG, PPTX, XML, EPUB), images (JPG, PNG, GIF, WEBP, SVG), audio (MP3, M4A, WAV, WEBM, AMR), and video (MP4, MOV, MPEG, MPGA).",
        },
        {
            "question": "[Example] How do I handle conversation management?",
            "answer": "[Example] Use the conversation APIs to get message history, list conversations, delete conversations, rename conversations, and retrieve conversation variables.",
        },
        {
            "question": "[Example] What are the TTS capabilities?",
            "answer": "[Example] The TTS APIs support speech-to-text conversion from audio files and text-to-audio conversion with various audio formats and streaming support.",
        },
    ]

    created_annotations = []

    try:
        for i, annotation_data in enumerate(annotations_to_create):
            print(f"Creating annotation {i + 1}...")

            # Build request body
            req_body = (
                CreateAnnotationRequestBody.builder()
                .question(annotation_data["question"])
                .answer(annotation_data["answer"])
                .build()
            )

            # Build request
            request = CreateAnnotationRequest.builder().request_body(req_body).build()

            # Execute request
            response = client.chatflow.v1.annotation.create(request, request_option)

            if response.success:
                print(f"  Created: {response.id}")
                created_annotations.append(response.id)
            else:
                print(f"  Error: {response.msg}")

        print(f"Successfully created {len(created_annotations)} annotations")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Create Annotation Examples ===")

    print("\n1. Sync Example:")
    create_annotation_sync()

    print("\n2. Async Example:")
    asyncio.run(create_annotation_async())

    print("\n3. Multiple Annotations Example:")
    create_multiple_annotations()
