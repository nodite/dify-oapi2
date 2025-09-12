"""
Streaming Workflow Example

This example demonstrates streaming workflow execution.
"""

import os

from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.run_workflow_request_body import RunWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow_inputs import WorkflowInputs
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def main():
    """Demonstrate streaming workflow execution."""
    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    inputs = (
        WorkflowInputs.builder()
        .inputs({"input_text": "Process this data step by step. Please answer within 10 words. No thinking process."})
        .build()
    )

    req_body = RunWorkflowRequestBody.builder().inputs(inputs).response_mode("streaming").user("user-123").build()

    req = RunWorkflowRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(os.getenv("WORKFLOW_KEY", "<your-api-key>")).build()

    try:
        response = client.workflow.v1.workflow.run(req, req_option, True)
        print("Streaming workflow execution:")
        for chunk in response:
            print(f"Chunk: {chunk}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
