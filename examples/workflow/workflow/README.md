# Workflow Execution Examples

This directory contains examples for executing and managing workflows (6 APIs). Workflows enable automated AI processing pipelines with support for complex multi-step operations, file processing, and real-time streaming.

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

### Workflow Execution APIs (4 APIs)
- **Run Workflow**: Execute workflows with flexible parameter configuration
- **Stop Workflow**: Interrupt running workflow executions
- **Get Workflow Logs**: Retrieve comprehensive execution logs and events
- **Get Workflow Run Detail**: Access detailed run information and step results

### Execution Capabilities
- **Dual Modes**: Blocking (synchronous) and streaming (real-time) execution
- **Parameter Flexibility**: Support for complex input types (text, numbers, files, objects)
- **File Processing**: Upload and process files within workflow steps
- **Event Streaming**: Real-time workflow events and progress updates
- **Error Handling**: Comprehensive error reporting and recovery mechanisms

### Monitoring & Management
- **Progress Tracking**: Monitor workflow execution in real-time
- **Detailed Logging**: Access step-by-step execution logs
- **Performance Metrics**: Track execution time and resource usage
- **Status Management**: Control workflow lifecycle and state
- **Result Access**: Retrieve workflow outputs and intermediate results

### Advanced Features
- **Multi-step Workflows**: Support for complex processing pipelines
- **Conditional Logic**: Dynamic workflow paths based on conditions
- **Integration Support**: Connect with other Dify APIs and external services
- **Scalability**: Handle high-volume workflow executions efficiently
- **Version Control**: Manage different workflow versions and configurations

## 🔗 Related Examples

- [File Management](../file/) - Upload files for workflows
