#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.annotation.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.list_annotations_request import ListAnnotationsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_annotation_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_KEY")
        if not api_key:
            raise ValueError("COMPLETION_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # First, get existing annotations to find one with [Example] prefix
        list_req = ListAnnotationsRequest.builder().page("1").limit("10").build()
        list_response = client.completion.v1.annotation.list_annotations(list_req, req_option)

        if not list_response.success or not list_response.data:
            print("No annotations found to delete")
            return

        # Find annotation with [Example] prefix
        example_annotation = None
        for annotation in list_response.data:
            if annotation.question and "[Example]" in annotation.question:
                example_annotation = annotation
                break

        if not example_annotation:
            print("No [Example] annotation found to delete")
            return

        req = DeleteAnnotationRequest.builder().annotation_id(example_annotation.id).build()
        response = client.completion.v1.annotation.delete_annotation(req, req_option)

        if response.success:
            print(f"Annotation deleted successfully: {example_annotation.id}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def delete_annotation_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_KEY")
        if not api_key:
            raise ValueError("COMPLETION_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # First, get existing annotations to find one with [Example] prefix
        list_req = ListAnnotationsRequest.builder().page("1").limit("10").build()
        list_response = await client.completion.v1.annotation.alist_annotations(list_req, req_option)

        if not list_response.success or not list_response.data:
            print("No annotations found to delete")
            return

        # Find annotation with [Example] prefix
        example_annotation = None
        for annotation in list_response.data:
            if annotation.question and "[Example]" in annotation.question:
                example_annotation = annotation
                break

        if not example_annotation:
            print("No [Example] annotation found to delete")
            return

        req = DeleteAnnotationRequest.builder().annotation_id(example_annotation.id).build()
        response = await client.completion.v1.annotation.adelete_annotation(req, req_option)

        if response.success:
            print(f"Annotation deleted successfully (async): {example_annotation.id}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def cleanup_example_annotations() -> None:
    """Clean up all annotations with [Example] prefix"""
    try:
        # Check required environment variables
        api_key = os.getenv("COMPLETION_KEY")
        if not api_key:
            raise ValueError("COMPLETION_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # Get all annotations
        list_req = ListAnnotationsRequest.builder().page("1").limit("100").build()
        list_response = client.completion.v1.annotation.list_annotations(list_req, req_option)

        if not list_response.success or not list_response.data:
            print("No annotations found")
            return

        # Delete all annotations with [Example] prefix
        deleted_count = 0
        for annotation in list_response.data:
            if annotation.question and "[Example]" in annotation.question:
                req = DeleteAnnotationRequest.builder().annotation_id(annotation.id).build()
                response = client.completion.v1.annotation.delete_annotation(req, req_option)
                if response.success:
                    deleted_count += 1

        print(f"Cleaned up {deleted_count} [Example] annotations")

    except Exception as e:
        print(f"Error during cleanup: {e}")


def main() -> None:
    print("=== Delete Annotation Examples ===")

    print("\n1. Sync delete annotation:")
    delete_annotation_sync()

    print("\n2. Async delete annotation:")
    asyncio.run(delete_annotation_async())

    print("\n3. Cleanup all [Example] annotations:")
    cleanup_example_annotations()


if __name__ == "__main__":
    main()
