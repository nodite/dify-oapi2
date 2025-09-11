#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.chatflow.v1.model.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_annotation_sync():
    """Delete annotation synchronously."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_API_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_API_KEY environment variable is required")

    annotation_id = os.getenv("ANNOTATION_ID")
    if not annotation_id:
        print("Note: ANNOTATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real annotation id to execute.")
        print("Set ANNOTATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = DeleteAnnotationRequest.builder().annotation_id(annotation_id).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.annotation.delete(request, request_option)

        if response.success:
            print("Deleted annotation successfully!")
            print(f"Annotation ID: {annotation_id}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def delete_annotation_async():
    """Delete annotation asynchronously."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_API_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_API_KEY environment variable is required")

    annotation_id = os.getenv("ANNOTATION_ID")
    if not annotation_id:
        print("Note: ANNOTATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real annotation id to execute.")
        print("Set ANNOTATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = DeleteAnnotationRequest.builder().annotation_id(annotation_id).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.annotation.adelete(request, request_option)

        if response.success:
            print("Deleted annotation successfully (async)!")
            print(f"Annotation ID: {annotation_id}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def delete_example_annotations():
    """Delete all annotations with [Example] prefix for safety."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_API_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_API_KEY environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # First, get all annotations
        from dify_oapi.api.chatflow.v1.model.get_annotations_request import GetAnnotationsRequest

        get_request = GetAnnotationsRequest.builder().page(1).limit(100).build()
        get_response = client.chatflow.v1.annotation.list(get_request, request_option)

        if not get_response.success:
            print(f"Error getting annotations: {get_response.msg}")
            return

        # Find annotations with [Example] prefix
        example_annotations = []
        for annotation in get_response.data:
            if annotation.question and annotation.question.startswith("[Example]"):
                example_annotations.append(annotation)

        if not example_annotations:
            print("No [Example] annotations found to delete")
            return

        print(f"Found {len(example_annotations)} [Example] annotations to delete")

        # Delete each example annotation
        deleted_count = 0
        for annotation in example_annotations:
            print(f"Deleting annotation: {annotation.id}")
            print(f"  Question: {annotation.question[:50]}...")

            # Build delete request
            request = DeleteAnnotationRequest.builder().annotation_id(annotation.id).build()

            # Execute delete request
            response = client.chatflow.v1.annotation.delete(request, request_option)

            if response.success:
                print("  ✓ Deleted successfully")
                deleted_count += 1
            else:
                print(f"  ✗ Error: {response.msg}")

        print(f"Successfully deleted {deleted_count} out of {len(example_annotations)} [Example] annotations")

    except Exception as e:
        print(f"Exception occurred: {e}")


def delete_annotation_with_confirmation():
    """Delete annotation with confirmation example."""
    # Validate environment variables
    api_key = os.getenv("CHATFLOW_API_KEY")
    if not api_key:
        raise ValueError("CHATFLOW_API_KEY environment variable is required")

    annotation_id = os.getenv("ANNOTATION_ID")
    if not annotation_id:
        print("Note: ANNOTATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real annotation id to execute.")
        print("Set ANNOTATION_ID environment variable with a valid ID to test this functionality.")
        return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # First, get the annotation to confirm it exists
        from dify_oapi.api.chatflow.v1.model.get_annotations_request import GetAnnotationsRequest

        get_request = GetAnnotationsRequest.builder().page(1).limit(100).build()
        get_response = client.chatflow.v1.annotation.list(get_request, request_option)

        if not get_response.success:
            print(f"Error getting annotations: {get_response.msg}")
            return

        # Find the annotation to delete
        target_annotation = None
        for annotation in get_response.data:
            if annotation.id == annotation_id:
                target_annotation = annotation
                break

        if not target_annotation:
            print(f"Annotation with ID {annotation_id} not found")
            return

        print("Found annotation to delete:")
        print(f"  ID: {target_annotation.id}")
        print(f"  Question: {target_annotation.question}")
        print(f"  Answer: {target_annotation.answer[:100]}...")
        print(f"  Hit Count: {target_annotation.hit_count}")

        # Only delete if it's an example annotation for safety
        if not target_annotation.question.startswith("[Example]"):
            print("⚠️  This annotation does not have [Example] prefix. Skipping deletion for safety.")
            return

        # Build delete request
        request = DeleteAnnotationRequest.builder().annotation_id(annotation_id).build()

        # Execute delete request
        response = client.chatflow.v1.annotation.delete(request, request_option)

        if response.success:
            print(f"✓ Successfully deleted annotation {annotation_id}")
        else:
            print(f"✗ Error deleting annotation: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Delete Annotation Examples ===")

    print("\n1. Sync Example:")
    delete_annotation_sync()

    print("\n2. Async Example:")
    asyncio.run(delete_annotation_async())

    print("\n3. Delete Example Annotations (Safe):")
    delete_example_annotations()

    print("\n4. Delete with Confirmation Example:")
    delete_annotation_with_confirmation()
