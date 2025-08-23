#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.completion.v1.model.annotation.list_annotations_request import ListAnnotationsRequest
from dify_oapi.api.completion.v1.model.annotation.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_annotation_sync() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # First, get existing annotations to find one with [Example] prefix
        list_req = ListAnnotationsRequest.builder().page("1").limit("10").build()
        list_response = client.completion.v1.annotation.list_annotations(list_req, req_option)

        if not list_response.success or not list_response.data:
            print("No annotations found to update")
            return

        # Find annotation with [Example] prefix
        example_annotation = None
        for annotation in list_response.data:
            if annotation.question and "[Example]" in annotation.question:
                example_annotation = annotation
                break

        if not example_annotation:
            print("No [Example] annotation found to update")
            return

        req_body = (
            UpdateAnnotationRequestBody.builder()
            .question("[Example] What is the updated completion API?")
            .answer("[Example] The updated completion API provides enhanced text generation capabilities.")
            .build()
        )

        req = UpdateAnnotationRequest.builder().annotation_id(example_annotation.id).request_body(req_body).build()
        response = client.completion.v1.annotation.update_annotation(req, req_option)

        if response.success:
            print(f"Annotation updated: {response.id}")
            print(f"New question: {response.question}")
            print(f"New answer: {response.answer}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def update_annotation_async() -> None:
    try:
        # Check required environment variables
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        # First, get existing annotations to find one with [Example] prefix
        list_req = ListAnnotationsRequest.builder().page("1").limit("10").build()
        list_response = await client.completion.v1.annotation.alist_annotations(list_req, req_option)

        if not list_response.success or not list_response.data:
            print("No annotations found to update")
            return

        # Find annotation with [Example] prefix
        example_annotation = None
        for annotation in list_response.data:
            if annotation.question and "[Example]" in annotation.question:
                example_annotation = annotation
                break

        if not example_annotation:
            print("No [Example] annotation found to update")
            return

        req_body = (
            UpdateAnnotationRequestBody.builder()
            .question("[Example] How to use async updated completion API?")
            .answer("[Example] The async updated completion API supports concurrent text generation operations.")
            .build()
        )

        req = UpdateAnnotationRequest.builder().annotation_id(example_annotation.id).request_body(req_body).build()
        response = await client.completion.v1.annotation.aupdate_annotation(req, req_option)

        if response.success:
            print(f"Annotation updated (async): {response.id}")
            print(f"New question (async): {response.question}")
            print(f"New answer (async): {response.answer}")
        else:
            print(f"Failed: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Update Annotation Examples ===")

    print("\n1. Sync update annotation:")
    update_annotation_sync()

    print("\n2. Async update annotation:")
    asyncio.run(update_annotation_async())


if __name__ == "__main__":
    main()
