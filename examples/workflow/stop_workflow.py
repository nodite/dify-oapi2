#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.workflow.v1.model.stop_workflow_request import StopWorkflowRequest
from dify_oapi.api.workflow.v1.model.stop_workflow_request_body import StopWorkflowRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def stop_workflow_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        task_id = os.getenv("TASK_ID")
        if not task_id:
            raise ValueError("TASK_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req_body = StopWorkflowRequestBody.builder().user("[Example] user-123").build()
        req = StopWorkflowRequest.builder().task_id(task_id).request_body(req_body).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.workflow.stop(req, req_option)

        if response.success:
            print(f"Workflow stopped: {response.result}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def stop_workflow_async() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        task_id = os.getenv("TASK_ID")
        if not task_id:
            raise ValueError("TASK_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req_body = StopWorkflowRequestBody.builder().user("[Example] user-123").build()
        req = StopWorkflowRequest.builder().task_id(task_id).request_body(req_body).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.workflow.v1.workflow.astop(req, req_option)

        if response.success:
            print(f"Workflow stopped: {response.result}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Stop Workflow Sync ===")
    stop_workflow_sync()

    print("\n=== Stop Workflow Async ===")
    asyncio.run(stop_workflow_async())
