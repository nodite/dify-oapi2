import asyncio
import os

from dify_oapi.api.chat.v1.model.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_annotation():
    """Delete an annotation"""
    api_key = os.getenv("CHAT_API_KEY")
    annotation_id = os.getenv("ANNOTATION_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not annotation_id:
        print("Note: ANNOTATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real annotation id to execute.")
        print("Set ANNOTATION_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = DeleteAnnotationRequest.builder().annotation_id(annotation_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.delete(req, req_option)
        print("Annotation deleted successfully!")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def delete_annotation_async():
    """Delete an annotation asynchronously"""
    api_key = os.getenv("CHAT_API_KEY")
    annotation_id = os.getenv("ANNOTATION_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not annotation_id:
        print("Note: ANNOTATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real annotation id to execute.")
        print("Set ANNOTATION_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = DeleteAnnotationRequest.builder().annotation_id(annotation_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.annotation.adelete(req, req_option)
        print("Annotation deleted asynchronously!")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    delete_annotation()
    asyncio.run(delete_annotation_async())
