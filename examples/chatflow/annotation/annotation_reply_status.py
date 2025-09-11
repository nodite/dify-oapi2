#!/usr/bin/env python3

import asyncio
import os
import time

from dify_oapi.api.chatflow.v1.model.annotation_reply_status_request import AnnotationReplyStatusRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_annotation_reply_status_sync():
    """Get annotation reply status synchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    job_id = os.getenv("JOB_ID")
    if not job_id:
        raise ValueError("JOB_ID environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = AnnotationReplyStatusRequest.builder().action("enable").job_id(job_id).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute request
        response = client.chatflow.v1.annotation.reply_status(request, request_option)

        if response.success:
            print("Annotation reply status retrieved successfully!")
            print(f"Job ID: {response.job_id}")
            print(f"Job Status: {response.job_status}")
            if response.error_msg:
                print(f"Error Message: {response.error_msg}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


async def get_annotation_reply_status_async():
    """Get annotation reply status asynchronously."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    job_id = os.getenv("JOB_ID")
    if not job_id:
        raise ValueError("JOB_ID environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request
    request = AnnotationReplyStatusRequest.builder().action("enable").job_id(job_id).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        # Execute async request
        response = await client.chatflow.v1.annotation.areply_status(request, request_option)

        if response.success:
            print("Annotation reply status retrieved successfully (async)!")
            print(f"Job ID: {response.job_id}")
            print(f"Job Status: {response.job_status}")
            if response.error_msg:
                print(f"Error Message: {response.error_msg}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


def poll_annotation_reply_status():
    """Poll annotation reply status until completion."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    job_id = os.getenv("JOB_ID")
    if not job_id:
        raise ValueError("JOB_ID environment variable is required")

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        max_attempts = 30  # Maximum polling attempts
        poll_interval = 2  # Seconds between polls

        print(f"Polling job status for Job ID: {job_id}")
        print(f"Max attempts: {max_attempts}, Poll interval: {poll_interval}s")

        for attempt in range(1, max_attempts + 1):
            print(f"\nAttempt {attempt}/{max_attempts}...")

            # Build request
            request = AnnotationReplyStatusRequest.builder().action("enable").job_id(job_id).build()

            # Execute request
            response = client.chatflow.v1.annotation.reply_status(request, request_option)

            if response.success:
                print(f"  Job Status: {response.job_status}")

                if response.job_status == "completed":
                    print("  ✓ Job completed successfully!")
                    break
                elif response.job_status == "failed":
                    print("  ✗ Job failed!")
                    if response.error_msg:
                        print(f"  Error: {response.error_msg}")
                    break
                elif response.job_status in ["waiting", "running"]:
                    print("  ⏳ Job still in progress...")
                    if attempt < max_attempts:
                        print(f"  Waiting {poll_interval}s before next check...")
                        time.sleep(poll_interval)
                else:
                    print(f"  ❓ Unknown job status: {response.job_status}")
            else:
                print(f"  ✗ Error getting status: {response.msg}")
                break

        else:
            print(f"\n⚠️  Reached maximum polling attempts ({max_attempts})")

    except Exception as e:
        print(f"Exception occurred: {e}")


def check_multiple_job_statuses():
    """Check status of multiple annotation reply jobs."""
    # Validate environment variables
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    # Example job IDs (in real usage, these would come from previous reply_settings calls)
    job_ids = os.getenv("JOB_IDS", "").split(",") if os.getenv("JOB_IDS") else []

    if not job_ids or job_ids == [""]:
        print("No JOB_IDS environment variable provided. Using example job ID from JOB_ID.")
        job_id = os.getenv("JOB_ID")
        if job_id:
            job_ids = [job_id]
        else:
            print("No job IDs available to check")
            return

    # Initialize client
    domain = os.getenv("DOMAIN", "https://api.dify.ai")
    client = Client.builder().domain(domain).build()

    # Build request option
    request_option = RequestOption.builder().api_key(api_key).build()

    try:
        print(f"Checking status of {len(job_ids)} jobs...")

        for i, job_id in enumerate(job_ids):
            print(f"\nJob {i + 1}: {job_id}")

            # Build request
            request = AnnotationReplyStatusRequest.builder().action("enable").job_id(job_id.strip()).build()

            # Execute request
            response = client.chatflow.v1.annotation.reply_status(request, request_option)

            if response.success:
                print(f"  Status: {response.job_status}")
                if response.error_msg:
                    print(f"  Error: {response.error_msg}")
            else:
                print(f"  Error: {response.msg}")

    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":
    print("=== Annotation Reply Status Examples ===")

    print("\n1. Sync Example:")
    get_annotation_reply_status_sync()

    print("\n2. Async Example:")
    asyncio.run(get_annotation_reply_status_async())

    print("\n3. Polling Example:")
    poll_annotation_reply_status()

    print("\n4. Multiple Jobs Example:")
    check_multiple_job_statuses()
