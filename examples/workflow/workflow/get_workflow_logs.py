#!/usr/bin/env python3

import asyncio
import os

from dify_oapi.api.workflow.v1.model.get_workflow_logs_request import GetWorkflowLogsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def get_workflow_logs_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("WORKFLOW_KEY")
        if not api_key:
            raise ValueError("WORKFLOW_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = GetWorkflowLogsRequest.builder().page(1).limit(10).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.workflow.logs(req, req_option)

        if response.success:
            print(f"Logs retrieved: {response.total} total, {len(response.data or [])} on page")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


async def get_workflow_logs_async() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("WORKFLOW_KEY")
        if not api_key:
            raise ValueError("WORKFLOW_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = GetWorkflowLogsRequest.builder().page(1).limit(10).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = await client.workflow.v1.workflow.alogs(req, req_option)

        if response.success:
            print(f"Logs retrieved: {response.total} total, {len(response.data or [])} on page")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


def get_workflow_logs_filtered() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("WORKFLOW_KEY")
        if not api_key:
            raise ValueError("WORKFLOW_KEY environment variable is required")

        client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

        req = GetWorkflowLogsRequest.builder().keyword("[Example]").status("succeeded").page(1).limit(5).build()
        req_option = RequestOption.builder().api_key(api_key).build()

        response = client.workflow.v1.workflow.logs(req, req_option)

        if response.success:
            print(f"Filtered logs: {response.total} total, {len(response.data or [])} on page")
        else:
            print(f"Error: {response.msg}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Get Workflow Logs Sync ===")
    get_workflow_logs_sync()

    print("\n=== Get Workflow Logs Async ===")
    asyncio.run(get_workflow_logs_async())

    print("\n=== Get Workflow Logs Filtered ===")
    get_workflow_logs_filtered()
