# Workflow API Examples

The Workflow API enables automated workflow execution with support for both blocking and streaming modes. This directory contains examples for workflow management and execution.

## 📁 Resources

### [workflow/](./workflow/) - Workflow Management
Core workflow execution and management operations.

**Available Examples:**
- `run_workflow.py` - Execute workflows with parameters
- `stop_workflow.py` - Stop running workflows
- `get_workflow_logs.py` - Retrieve workflow execution logs
- `get_workflow_run_detail.py` - Get detailed workflow run information
- `blocking_workflow.py` - Blocking workflow execution example
- `streaming_workflow.py` - Streaming workflow execution example

### [file/](./file/) - File Management
File upload and management for workflow inputs.

**Available Examples:**
- `upload_file.py` - Upload files for workflow processing

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

print(f"Workflow ID: {response.workflow_run_id}")
print(f"Result: {response.data}")
```

### Streaming Workflow Execution

```python
req_body = (
    RunWorkflowRequestBody.builder()
    .inputs({"input_text": "Process this data"})
    .response_mode("streaming")
    .user("user-123")
    .build()
)

req = RunWorkflowRequest.builder().request_body(req_body).build()
response = client.workflow.v1.workflow.run_workflow(req, req_option, True)

for chunk in response:
    print(f"Event: {chunk}")
```

### Monitor Workflow Execution

```python
from dify_oapi.api.workflow.v1.model.get_workflow_run_detail_request import GetWorkflowRunDetailRequest

req = GetWorkflowRunDetailRequest.builder()
    .workflow_run_id("your-workflow-run-id")
    .build()

response = client.workflow.v1.workflow.get_workflow_run_detail(req, req_option)
print(f"Status: {response.status}")
print(f"Steps: {response.steps}")
```

## 🔧 Features

### Execution Modes
- **Blocking Mode**: Synchronous execution, wait for completion
- **Streaming Mode**: Real-time event streaming during execution

### Workflow Management
- **Parameter Passing**: Flexible input parameter configuration
- **Status Monitoring**: Track workflow execution progress
- **Log Retrieval**: Access detailed execution logs
- **Error Handling**: Comprehensive error management

### Advanced Features
- **File Processing**: Upload and process files within workflows
- **Event Streaming**: Real-time workflow event notifications
- **Step-by-Step Execution**: Monitor individual workflow steps
- **Resource Management**: Efficient resource utilization

## 📖 Workflow Events

When using streaming mode, you'll receive various event types:

- **workflow_started**: Workflow execution begins
- **node_started**: Individual node execution starts
- **node_finished**: Individual node execution completes
- **workflow_finished**: Workflow execution completes
- **error**: Error occurred during execution

## 🔧 Input Configuration

Workflows accept various input types:

```python
inputs = {
    "text_input": "Your text here",
    "number_input": 42,
    "boolean_input": True,
    "file_input": "uploaded-file-id",
    "array_input": ["item1", "item2"],
    "object_input": {"key": "value"}
}
```

## 📖 Environment Variables

```bash
export DOMAIN="https://api.dify.ai"
export WORKFLOW_KEY="your-workflow-api-key"
```

## 🔗 Integration Examples

Workflows can integrate with other Dify services:

- **Knowledge Base**: Query knowledge bases within workflows
- **Chat API**: Use workflow results in chat responses
- **File Processing**: Process uploaded files through workflows

## 📚 Best Practices

1. **Use Appropriate Mode**: Choose blocking for simple workflows, streaming for complex ones
2. **Handle Events Properly**: Process all event types in streaming mode
3. **Monitor Resource Usage**: Track workflow execution resources
4. **Implement Timeouts**: Set appropriate timeouts for long-running workflows
5. **Error Recovery**: Implement retry logic for failed workflows
6. **Log Management**: Regularly clean up old workflow logs