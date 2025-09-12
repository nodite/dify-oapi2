import asyncio
import os

from dify_oapi.api.chat.v1.model.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.chat.v1.model.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def update_annotation():
    """Update an existing annotation"""
    api_key = os.getenv("CHAT_KEY")
    annotation_id = os.getenv("ANNOTATION_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not annotation_id:
        print("Note: ANNOTATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real annotation id to execute.")
        print("Set ANNOTATION_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        UpdateAnnotationRequestBody.builder()
        .question("What is artificial intelligence and machine learning?")
        .answer(
            "Artificial Intelligence (AI) is a broad field of computer science focused on creating intelligent machines. Machine Learning (ML) is a subset of AI that enables systems to learn and improve from experience without explicit programming."
        )
        .build()
    )

    req = UpdateAnnotationRequest.builder().annotation_id(annotation_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.update(req, req_option)
        print("Annotation updated successfully!")
        print(f"Annotation ID: {response.id}")
        print(f"Updated Question: {response.question}")
        print(f"Updated Answer: {response.answer}")
        print(f"Hit Count: {response.hit_count}")
        print(f"Created: {response.created_at}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def update_annotation_answer_only():
    """Update only the answer of an annotation"""
    api_key = os.getenv("CHAT_KEY")
    annotation_id = os.getenv("ANNOTATION_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not annotation_id:
        print("Note: ANNOTATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real annotation id to execute.")
        print("Set ANNOTATION_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        UpdateAnnotationRequestBody.builder()
        .question("What is artificial intelligence?")
        .answer(
            "AI is the simulation of human intelligence in machines that are programmed to think and learn like humans. It includes machine learning, natural language processing, computer vision, and robotics."
        )
        .build()
    )

    req = UpdateAnnotationRequest.builder().annotation_id(annotation_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.update(req, req_option)
        print("Annotation answer updated!")
        print(f"New Answer: {response.answer}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def update_annotation_async():
    """Update annotation asynchronously"""
    api_key = os.getenv("CHAT_KEY")
    annotation_id = os.getenv("ANNOTATION_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not annotation_id:
        print("Note: ANNOTATION_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real annotation id to execute.")
        print("Set ANNOTATION_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        UpdateAnnotationRequestBody.builder()
        .question("What are the applications of AI?")
        .answer(
            "AI applications include healthcare diagnostics, autonomous vehicles, recommendation systems, natural language processing, computer vision, robotics, and financial analysis."
        )
        .build()
    )

    req = UpdateAnnotationRequest.builder().annotation_id(annotation_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.annotation.aupdate(req, req_option)
        print("Async annotation updated!")
        print(f"Annotation ID: {response.id}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    update_annotation()
    update_annotation_answer_only()
    asyncio.run(update_annotation_async())
