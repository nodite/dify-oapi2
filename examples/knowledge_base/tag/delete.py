#!/usr/bin/env python3
"""
Tag Delete Example

This example demonstrates how to delete knowledge type tags using the Dify API.
"""

import asyncio
import os

from dify_oapi.api.knowledge_base.v1.model.tag.delete_request import DeleteRequest
from dify_oapi.api.knowledge_base.v1.model.tag.delete_request_body import (
    DeleteRequestBody,
)
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_tag_sync() -> None:
    """Delete tag synchronously (only [Example] prefixed tags)."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        tag_id = os.getenv("TAG_ID")
        if not tag_id:
            raise ValueError("TAG_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        from dify_oapi.api.knowledge_base.v1.model.tag.list_request import ListRequest

        list_request = ListRequest.builder().build()
        list_response = client.knowledge_base.v1.tag.list(list_request, request_option)

        target_tag = None
        if list_response.data:
            target_tag = next(
                (tag for tag in list_response.data if tag.id == tag_id), None
            )

        if not target_tag:
            print(f"Tag {tag_id} not found")
            return

        if not target_tag.name or not target_tag.name.startswith("[Example]"):
            print(f"Skipping '{target_tag.name}' - not an example tag")
            return

        request_body = DeleteRequestBody.builder().tag_id(tag_id).build()
        request = DeleteRequest.builder().request_body(request_body).build()
        client.knowledge_base.v1.tag.delete(request, request_option)
        print(f"Deleted: {target_tag.name}")

    except Exception as e:
        print(f"Error deleting tag: {e}")


async def delete_tag_async() -> None:
    """Delete tag asynchronously (only [Example] prefixed tags)."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        tag_id = os.getenv("TAG_ID")
        if not tag_id:
            raise ValueError("TAG_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        from dify_oapi.api.knowledge_base.v1.model.tag.list_request import ListRequest

        list_request = ListRequest.builder().build()
        list_response = await client.knowledge_base.v1.tag.alist(list_request, request_option)

        target_tag = None
        if list_response.data:
            target_tag = next(
                (tag for tag in list_response.data if tag.id == tag_id), None
            )

        if not target_tag:
            print(f"Tag {tag_id} not found")
            return

        if not target_tag.name or not target_tag.name.startswith("[Example]"):
            print(f"Skipping '{target_tag.name}' - not an example tag")
            return

        request_body = DeleteRequestBody.builder().tag_id(tag_id).build()
        request = DeleteRequest.builder().request_body(request_body).build()
        await client.knowledge_base.v1.tag.adelete(request, request_option)
        print(f"Deleted (async): {target_tag.name}")

    except Exception as e:
        print(f"Error deleting tag (async): {e}")


def delete_example_tags() -> None:
    """Delete all tags with [Example] prefix."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        request_option = RequestOption.builder().api_key(api_key).build()

        from dify_oapi.api.knowledge_base.v1.model.tag.list_request import ListRequest

        list_request = ListRequest.builder().build()
        list_response = client.knowledge_base.v1.tag.list(list_request, request_option)

        example_tags = [
            t for t in list_response.data if t.name and t.name.startswith("[Example]")
        ]

        if not example_tags:
            print("No example tags found")
            return

        print(f"Deleting {len(example_tags)} example tags...")
        
        for tag in example_tags:
            try:
                request_body = DeleteRequestBody.builder().tag_id(tag.id).build()
                request = DeleteRequest.builder().request_body(request_body).build()
                client.knowledge_base.v1.tag.delete(request, request_option)
                print(f"✓ {tag.name}")
            except Exception as e:
                print(f"✗ {tag.name}: {e}")

    except Exception as e:
        print(f"Error in cleanup: {e}")


def main() -> None:
    """Main function to run examples."""
    print("=== Tag Delete Examples ===\n")
    
    print("1. Deleting specific tag synchronously...")
    delete_tag_sync()
    
    print("\n2. Deleting specific tag asynchronously...")
    asyncio.run(delete_tag_async())
    
    print("\n3. Cleaning up all example tags...")
    delete_example_tags()


if __name__ == "__main__":
    main()
