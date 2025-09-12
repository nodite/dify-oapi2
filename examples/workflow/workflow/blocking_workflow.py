"""
Blocking Workflow Example

This example demonstrates blocking workflow execution.
"""

import os

from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.run_workflow_request_body import RunWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow_inputs import WorkflowInputs
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def main():
    """Demonstrate blocking workflow execution."""
    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

    inputs = (
        WorkflowInputs.builder()
        .inputs({"input_text": "Hello, world! Please answer within 10 words. No thinking process."})
        .build()
    )

    req_body = RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("user-123").build()

    req = RunWorkflowRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(os.getenv("WORKFLOW_KEY", "<your-api-key>")).build()

    try:
        response = client.workflow.v1.workflow.run(req, req_option, False)
        print(f"Workflow ID: {response.workflow_run_id}")
        print(f"Task ID: {response.task_id}")
        print(f"Data: {response.data}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
