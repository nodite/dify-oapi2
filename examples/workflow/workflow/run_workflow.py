#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.run_workflow_request_body import RunWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow_inputs import WorkflowInputs
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def run_workflow_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("WORKFLOW_KEY")
        if not api_key:
            raise ValueError("WORKFLOW_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        inputs = WorkflowInputs.builder().build()
        req_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("[Example] user-123").build()
        )

        req = RunWorkflowRequest.builder().request_body(req_body).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.workflow.run(req, req_option, False)

        if response.success:
            print(f"Workflow executed: {response.workflow_run_id}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def run_workflow_async() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("WORKFLOW_KEY")
        if not api_key:
            raise ValueError("WORKFLOW_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        inputs = WorkflowInputs.builder().build()
        req_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("[Example] user-123").build()
        )

        req = RunWorkflowRequest.builder().request_body(req_body).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.workflow.v1.workflow.arun(req, req_option, False)

        if response.success:
            print(f"Workflow executed: {response.workflow_run_id}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def run_workflow_streaming() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("WORKFLOW_KEY")
        if not api_key:
            raise ValueError("WORKFLOW_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        inputs = WorkflowInputs.builder().build()
        req_body = (
            RunWorkflowRequestBody.builder()
            .inputs(inputs)
            .response_mode("streaming")
            .user("[Example] user-123")
            .build()
        )

        req = RunWorkflowRequest.builder().request_body(req_body).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.workflow.run(req, req_option, True)

        for chunk in response:
            print(chunk, end="", flush=True)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Run Workflow Sync ===")
    run_workflow_sync()

    print("\n=== Run Workflow Async ===")
    asyncio.run(run_workflow_async())

    print("\n=== Run Workflow Streaming ===")
    run_workflow_streaming()
