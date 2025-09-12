import asyncio
import os

from dify_oapi.api.chat.v1.model.get_annotation_reply_status_request import GetAnnotationReplyStatusRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_annotation_reply_status():
    """Get annotation reply configuration status"""
    api_key = os.getenv("CHAT_KEY")
    job_id = os.getenv("JOB_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not job_id:
        print("Note: JOB_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real job id to execute.")
        print("Set JOB_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetAnnotationReplyStatusRequest.builder().action("enable").job_id(job_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.status(req, req_option)
        print("Annotation Reply Status:")
        print(f"Job ID: {response.job_id}")
        print(f"Job Status: {response.job_status}")
        if response.error_msg:
            print(f"Error Message: {response.error_msg}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def get_disable_status():
    """Get disable annotation reply status"""
    api_key = os.getenv("CHAT_KEY")
    job_id = os.getenv("JOB_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not job_id:
        print("Note: JOB_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real job id to execute.")
        print("Set JOB_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetAnnotationReplyStatusRequest.builder().action("disable").job_id(job_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = client.chat.v1.annotation.status(req, req_option)
        print("Disable Status:")
        print(f"Job Status: {response.job_status}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


def poll_status_until_complete():
    """Poll status until job is complete"""
    api_key = os.getenv("CHAT_KEY")
    job_id = os.getenv("JOB_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not job_id:
        print("Note: JOB_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real job id to execute.")
        print("Set JOB_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetAnnotationReplyStatusRequest.builder().action("enable").job_id(job_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    import time

    max_attempts = 10
    attempt = 0

    try:
        while attempt < max_attempts:
            response = client.chat.v1.annotation.status(req, req_option)
            print(f"Attempt {attempt + 1}: Status = {response.job_status}")

            if response.job_status in ["completed", "failed"]:
                print(f"Job finished with status: {response.job_status}")
                if response.error_msg:
                    print(f"Error: {response.error_msg}")
                return response

            time.sleep(2)
            attempt += 1

        print("Max attempts reached. Job may still be running.")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


async def get_annotation_reply_status_async():
    """Get annotation reply status asynchronously"""
    api_key = os.getenv("CHAT_KEY")
    job_id = os.getenv("JOB_ID")
    if not api_key:
        raise ValueError("CHAT_KEY environment variable is required")
    if not job_id:
        print("Note: JOB_ID environment variable is required for this example.")
        print("This example demonstrates the API structure but needs a real job id to execute.")
        print("Set JOB_ID environment variable with a valid ID to test this functionality.")
        return

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    req = GetAnnotationReplyStatusRequest.builder().action("enable").job_id(job_id).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    try:
        response = await client.chat.v1.annotation.astatus(req, req_option)
        print("Async Status:")
        print(f"Job Status: {response.job_status}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    get_annotation_reply_status()
    get_disable_status()
    poll_status_until_complete()
    asyncio.run(get_annotation_reply_status_async())
