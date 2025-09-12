import asyncio
import os

from dify_oapi.api.chat.v1.model.configure_annotation_reply_request import ConfigureAnnotationReplyRequest
from dify_oapi.api.chat.v1.model.configure_annotation_reply_request_body import ConfigureAnnotationReplyRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def enable_annotation_reply():
    """Enable annotation reply settings"""
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        ConfigureAnnotationReplyRequestBody.builder()
        .embedding_provider_name("openai")
        .embedding_model_name("text-embedding-ada-002")
        .score_threshold(0.8)
        .build()
    )

    req = ConfigureAnnotationReplyRequest.builder().action("enable").request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.configure(req, req_option)
        print("Annotation reply enabled successfully!")
        print(f"Job ID: {response.job_id}")
        print(f"Job Status: {response.job_status}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def disable_annotation_reply():
    """Disable annotation reply settings"""
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = ConfigureAnnotationReplyRequestBody.builder().score_threshold(0.0).build()

    req = ConfigureAnnotationReplyRequest.builder().action("disable").request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.configure(req, req_option)
        print("Annotation reply disabled successfully!")
        print(f"Job ID: {response.job_id}")
        print(f"Job Status: {response.job_status}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def configure_annotation_reply_custom():
    """Configure annotation reply with custom settings"""
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        ConfigureAnnotationReplyRequestBody.builder()
        .embedding_provider_name("huggingface")
        .embedding_model_name("sentence-transformers/all-MiniLM-L6-v2")
        .score_threshold(0.75)
        .build()
    )

    req = ConfigureAnnotationReplyRequest.builder().action("enable").request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.configure(req, req_option)
        print("Custom annotation reply configured!")
        print(f"Job ID: {response.job_id}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def configure_annotation_reply_async():
    """Configure annotation reply asynchronously"""
    api_key = os.getenv("CHAT_KEY")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req_body = (
        ConfigureAnnotationReplyRequestBody.builder()
        .embedding_provider_name("openai")
        .embedding_model_name("text-embedding-ada-002")
        .score_threshold(0.85)
        .build()
    )

    req = ConfigureAnnotationReplyRequest.builder().action("enable").request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.annotation.aconfigure(req, req_option)
        print("Async annotation reply configured!")
        print(f"Job ID: {response.job_id}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    enable_annotation_reply()
    disable_annotation_reply()
    configure_annotation_reply_custom()
    asyncio.run(configure_annotation_reply_async())
