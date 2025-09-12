# Workflow Execution Examples

This directory contains examples for executing and managing workflows.

## 📋 Available Examples

### Basic Operations
- **`run_workflow.py`** - Execute workflows with parameters
- **`stop_workflow.py`** - Stop running workflows
- **`get_workflow_logs.py`** - Retrieve execution logs
- **`get_workflow_run_detail.py`** - Get detailed run information

### Execution Modes
- **`blocking_workflow.py`** - Synchronous workflow execution
- **`streaming_workflow.py`** - Real-time streaming execution

## 🚀 Quick Start

### Basic Workflow Execution

```python
from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.run_workflow_request_body import RunWorkflowRequestBody

req_body = (
    RunWorkflowRequestBody.builder()
    .inputs({"input_text": "Hello, world!"})
    .response_mode("blocking")
    .user("user-123")
    .build()
)

req = RunWorkflowRequest.builder().request_body(req_body).build()
response = client.workflow.v1.workflow.run_workflow(req, req_option, False)
```

## 🔧 Features

- **Parameter Passing**: Flexible input configuration
- **Execution Modes**: Blocking and streaming support
- **Status Monitoring**: Track execution progress
- **Log Management**: Access detailed execution logs

## 🔗 Related Examples

- [File Management](../file/) - Upload files for workflows