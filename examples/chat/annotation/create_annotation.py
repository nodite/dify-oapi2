import asyncio
import os

from dify_oapi.api.chat.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chat.v1.model.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def create_annotation():
    """Create a new annotation"""
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        CreateAnnotationRequestBody.builder()
        .question("What is artificial intelligence?")
        .answer(
            "Artificial Intelligence (AI) is a branch of computer science that aims to create intelligent machines that can perform tasks that typically require human intelligence."
        )
        .build()
    )

    req = CreateAnnotationRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.create(req, req_option)
        print("Annotation created successfully!")
        print(f"Annotation ID: {response.id}")
        print(f"Question: {response.question}")
        print(f"Answer: {response.answer}")
        print(f"Hit Count: {response.hit_count}")
        print(f"Created: {response.created_at}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def create_technical_annotation():
    """Create a technical annotation"""
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        CreateAnnotationRequestBody.builder()
        .question("How does machine learning work?")
        .answer(
            "Machine learning is a subset of AI that enables computers to learn and improve from experience without being explicitly programmed. It uses algorithms to analyze data, identify patterns, and make predictions or decisions."
        )
        .build()
    )

    req = CreateAnnotationRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.create(req, req_option)
        print("Technical annotation created!")
        print(f"Annotation ID: {response.id}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def create_annotation_async():
    """Create annotation asynchronously"""
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        CreateAnnotationRequestBody.builder()
        .question("What is deep learning?")
        .answer(
            "Deep learning is a subset of machine learning that uses neural networks with multiple layers to model and understand complex patterns in data."
        )
        .build()
    )

    req = CreateAnnotationRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.annotation.acreate(req, req_option)
        print("Async annotation created!")
        print(f"Annotation ID: {response.id}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    create_annotation()
    create_technical_annotation()
    asyncio.run(create_annotation_async())
