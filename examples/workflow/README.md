# Workflow API Examples

This directory contains comprehensive examples for all Workflow API functionality in the dify-oapi2 SDK.

## Overview

The Workflow API provides 8 main endpoints for workflow execution, file management, logging, and application configuration. All examples demonstrate both synchronous and asynchronous usage patterns.

## Examples

### Workflow Execution

#### 1. Run Workflow (`run_workflow.py`)
Execute workflows with support for both blocking and streaming modes.

**Features:**
- Sync and async execution
- Blocking mode for immediate results
- Streaming mode for real-time responses
- Custom workflow inputs

**Environment Variables:**
- `API_KEY` (required): Your Dify API key
- `DOMAIN` (optional): API domain, defaults to `https://api.dify.ai`

#### 2. Get Workflow Run Detail (`get_workflow_run_detail.py`)
Retrieve detailed information about workflow execution.

**Features:**
- Sync and async retrieval
- Execution status and timing information
- Input/output data access

**Environment Variables:**
- `API_KEY` (required): Your Dify API key
- `WORKFLOW_RUN_ID` (required): ID of the workflow run to retrieve
- `DOMAIN` (optional): API domain

#### 3. Stop Workflow (`stop_workflow.py`)
Stop running workflow executions.

**Features:**
- Sync and async stopping
- Task-based workflow termination

**Environment Variables:**
- `API_KEY` (required): Your Dify API key
- `TASK_ID` (required): ID of the task to stop
- `DOMAIN` (optional): API domain

### File Management

#### 4. Upload File (`upload_file.py`)
Upload files for use in workflows with multimodal support.

**Features:**
- Sync and async file upload
- Multipart/form-data handling
- File metadata retrieval

**Environment Variables:**
- `API_KEY` (required): Your Dify API key
- `DOMAIN` (optional): API domain

### Logging and Monitoring

#### 5. Get Workflow Logs (`get_workflow_logs.py`)
Retrieve workflow execution logs with filtering capabilities.

**Features:**
- Sync and async log retrieval
- Pagination support
- Filtering by keyword and status
- Basic and filtered log queries

**Environment Variables:**
- `API_KEY` (required): Your Dify API key
- `DOMAIN` (optional): API domain

### Application Information

#### 6. Get Application Info (`get_info.py`)
Retrieve basic application information.

**Features:**
- Sync and async info retrieval
- Application name and description

**Environment Variables:**
- `API_KEY` (required): Your Dify API key
- `DOMAIN` (optional): API domain

#### 7. Get Application Parameters (`get_parameters.py`)
Retrieve application parameter configuration.

**Features:**
- Sync and async parameter retrieval
- User input form configuration
- File upload settings
- System parameters

**Environment Variables:**
- `API_KEY` (required): Your Dify API key
- `DOMAIN` (optional): API domain

#### 8. Get WebApp Settings (`get_site.py`)
Retrieve WebApp configuration and settings.

**Features:**
- Sync and async settings retrieval
- UI configuration and theming
- Icon and branding settings

**Environment Variables:**
- `API_KEY` (required): Your Dify API key
- `DOMAIN` (optional): API domain

## Usage Patterns

### Basic Usage
```python
import os
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

# Initialize client
client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
req_option = RequestOption.builder().api_key(os.getenv("API_KEY")).build()

# All workflow APIs are accessed through: client.workflow.v1.workflow
response = client.workflow.v1.workflow.method_name(request, req_option)
```

### Streaming Usage
```python
# For streaming workflow execution
response = client.workflow.v1.workflow.run_workflow(req, req_option, True)
for chunk in response:
    print(chunk, end="", flush=True)
```

### Async Usage
```python
import asyncio

async def async_example():
    response = await client.workflow.v1.workflow.amethod_name(request, req_option)
    return response

# Run async function
asyncio.run(async_example())
```

## Safety Features

All examples include:
- **Environment Variable Validation**: Required variables are checked at function start
- **"[Example]" Prefix**: All created resources use "[Example]" prefix for safety
- **Error Handling**: Comprehensive try-catch blocks for robust error management
- **Resource Safety**: Examples only create/modify resources with "[Example]" prefix

## Running Examples

1. Set required environment variables:
   ```bash
   export API_KEY="your-dify-api-key"
   export DOMAIN="https://api.dify.ai"  # optional
   ```

2. For examples requiring resource IDs, set additional variables:
   ```bash
   export WORKFLOW_RUN_ID="your-workflow-run-id"
   export TASK_ID="your-task-id"
   ```

3. Run individual examples:
   ```bash
   python examples/workflow/run_workflow.py
   python examples/workflow/upload_file.py
   # ... etc
   ```

## Code Minimalism

All examples follow minimal code principles:
- **Essential Code Only**: Only code directly needed for API demonstration
- **Concise Output**: Simplified success/error messages
- **Streamlined Functions**: Reduced redundancy while maintaining functionality
- **Clear Patterns**: Consistent structure across all examples

## Integration with Tests

These examples serve as:
- **Educational References**: Clear demonstration of API usage patterns
- **Integration Test Validation**: Examples validate real API integration
- **Documentation Support**: Complement API documentation with working code

## Error Handling

All examples include:
- **Environment validation** at function start with descriptive error messages
- **API response validation** checking `response.success` before accessing data
- **Exception handling** with try-catch blocks for robust error management
- **Meaningful error messages** for debugging and troubleshooting

## Next Steps

After running these examples:
1. Explore the [main project documentation](../../README.md)
2. Review the [Workflow API design document](../../docs/workflow/workflow-design.md)
3. Check the [comprehensive test suite](../../tests/workflow/) for advanced usage patterns
4. Integrate workflow functionality into your applications using these patterns