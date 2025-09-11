#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.workflow.v1.model.get_workflow_run_detail_request import GetWorkflowRunDetailRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_workflow_run_detail_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("WORKFLOW_API_KEY")
        if not api_key:
            raise ValueError("WORKFLOW_API_KEY environment variable is required")

        workflow_run_id = os.getenv("WORKFLOW_RUN_ID")
        if not workflow_run_id:
            raise ValueError("WORKFLOW_RUN_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = GetWorkflowRunDetailRequest.builder().workflow_run_id(workflow_run_id).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.workflow.detail(req, req_option)

        if response.success:
            print(f"Workflow detail: {response.status} - {response.elapsed_time}s")
            print(f"Inputs: {response.inputs}")
            print(f"Outputs: {response.outputs}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def get_workflow_run_detail_async() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("WORKFLOW_API_KEY")
        if not api_key:
            raise ValueError("WORKFLOW_API_KEY environment variable is required")

        workflow_run_id = os.getenv("WORKFLOW_RUN_ID")
        if not workflow_run_id:
            raise ValueError("WORKFLOW_RUN_ID environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = GetWorkflowRunDetailRequest.builder().workflow_run_id(workflow_run_id).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.workflow.v1.workflow.adetail(req, req_option)

        if response.success:
            print(f"Workflow detail: {response.status} - {response.elapsed_time}s")
            print(f"Inputs: {response.inputs}")
            print(f"Outputs: {response.outputs}")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Get Workflow Run Detail Sync ===")
    get_workflow_run_detail_sync()

    print("\n=== Get Workflow Run Detail Async ===")
    asyncio.run(get_workflow_run_detail_async())
