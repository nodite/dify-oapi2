#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_request import RunSpecificWorkflowRequest
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_request_body import RunSpecificWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow.workflow_inputs import WorkflowInputs
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def run_specific_workflow_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        workflow_id = os.getenv("WORKFLOW_ID")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")
        if not workflow_id:
            raise ValueError("WORKFLOW_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        inputs = WorkflowInputs.builder().build()
        req_body = (
            RunSpecificWorkflowRequestBody.builder()
            .inputs(inputs)
            .response_mode("blocking")
            .user("[Example] user-123")
            .build()
        )

        req = RunSpecificWorkflowRequest.builder().workflow_id(workflow_id).request_body(req_body).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.workflow.run_specific_workflow(req, req_option, False)

        if response.success:
            print(f"Specific workflow executed: {response.workflow_run_id}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def run_specific_workflow_async() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        workflow_id = os.getenv("WORKFLOW_ID")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")
        if not workflow_id:
            raise ValueError("WORKFLOW_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        inputs = WorkflowInputs.builder().build()
        req_body = (
            RunSpecificWorkflowRequestBody.builder()
            .inputs(inputs)
            .response_mode("blocking")
            .user("[Example] user-123")
            .build()
        )

        req = RunSpecificWorkflowRequest.builder().workflow_id(workflow_id).request_body(req_body).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.workflow.v1.workflow.arun_specific_workflow(req, req_option, False)

        if response.success:
            print(f"Specific workflow executed: {response.workflow_run_id}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Run Specific Workflow Sync ===")
    run_specific_workflow_sync()

    print("\n=== Run Specific Workflow Async ===")
    asyncio.run(run_specific_workflow_async())
