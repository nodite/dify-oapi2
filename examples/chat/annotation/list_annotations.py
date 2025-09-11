import asyncio
import os

from dify_oapi.api.chat.v1.model.list_annotations_request import ListAnnotationsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def list_annotations():
    """List annotations"""
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = ListAnnotationsRequest.builder().page(1).limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.list(req, req_option)
        print(f"Retrieved {len(response.data)} annotations")
        print(f"Total: {response.total}")
        print(f"Has more: {response.has_more}")

        for annotation in response.data:
            print(f"- Annotation ID: {annotation.id}")
            print(f"  Question: {annotation.question}")
            print(f"  Answer: {annotation.answer}")
            print(f"  Hit Count: {annotation.hit_count}")
            print(f"  Created: {annotation.created_at}")
            print()

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def list_annotations_paginated():
    """List annotations with pagination"""
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = ListAnnotationsRequest.builder().page(2).limit(10).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.list(req, req_option)
        print(f"Retrieved {len(response.data)} annotations (page 2, limit 10)")

        for annotation in response.data:
            print(f"- {annotation.question[:50]}...")

        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def list_annotations_async():
    """List annotations asynchronously"""
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = ListAnnotationsRequest.builder().page(1).limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.annotation.alist(req, req_option)
        print(f"Async retrieved {len(response.data)} annotations")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    list_annotations()
    list_annotations_paginated()
    asyncio.run(list_annotations_async())
