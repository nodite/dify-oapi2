# Workflow API Implementation Plan

Based on workflow-api and workflow-design documents, this plan breaks down the Workflow API implementation into specific steps, with each implementation step followed by a testing step to ensure code quality.

## Overview

Workflow API contains **8 APIs** distributed across **3 resource categories**:
- **Workflow Execution** (4 APIs): Run, detail, stop, logs
- **File Management** (1 API): File upload
- **Application Configuration** (3 APIs): Info, parameters, site

## Implementation Steps

### Step 1: Implement Workflow Types Definition

**Implementation Prompt:**
```
Implement all type definitions for Workflow API, ensuring strict type safety.

Requirements:
1. Create `dify_oapi/api/workflow/v1/model/workflow_types.py`
2. Define all Literal types based on API specifications:
   - ResponseMode = Literal["streaming", "blocking"]  # Response modes
   - FileType = Literal["document", "image", "audio", "video", "custom"]  # File types
   - TransferMethod = Literal["remote_url", "local_file"]  # File transfer methods
   - WorkflowStatus = Literal["running", "succeeded", "failed", "stopped"]  # Workflow status
   - NodeStatus = Literal["running", "succeeded", "failed", "stopped"]  # Node execution status
   - EventType = Literal["workflow_started", "node_started", "text_chunk", "node_finished", "workflow_finished", "tts_message", "tts_message_end", "ping"]  # SSE event types
   - IconType = Literal["emoji", "image"]  # Icon types for WebApp
   - AppMode = Literal["workflow"]  # Application mode
   - LogStatus = Literal["succeeded", "failed", "stopped", "running"]  # Log status filter (includes "running")
   - CreatedByRole = Literal["end_user", "account"]  # Creator role types
   - CreatedFrom = Literal["service-api", "web-app"]  # Creation source
   - UserInputFormType = Literal["text-input", "paragraph", "select"]  # Form control types
   - NodeType = Literal["start", "end", "llm", "code", "template", "knowledge_retrieval", "question_classifier", "if_else", "variable_assigner", "parameter_extractor"]  # Node types

3. Import Literal from typing_extensions for Python 3.10+ compatibility
4. Add clear docstrings explaining each type's purpose
5. Ensure all types match the API specification exactly
6. Include validation constants for UUID format validation
```

**Testing Prompt:**
```
Create comprehensive tests for Workflow Types.

Requirements:
1. Create `tests/workflow/v1/model/test_workflow_types.py`
2. Test all valid values for each Literal type
3. Verify type constraints work correctly with mypy
4. Test that invalid values are properly rejected by type checkers
5. Ensure all type definitions can be correctly imported and used
6. Use pytest framework for all tests
7. Achieve 100% test coverage
```

### Step 2: Implement Common Model Classes

**Implementation Prompt:**
```
Implement all common model classes for Workflow API that can be reused across multiple APIs.

Requirements:
1. Create common model files in `dify_oapi/api/workflow/v1/model/`:
   - `workflow_inputs.py` - Dynamic workflow input parameters
   - `input_file_object_workflow.py` - File input object for multimodal support
   - `workflow_run_info.py` - Workflow execution information
   - `workflow_run_data.py` - Workflow execution data details
   - `node_info.py` - Node execution information
   - `execution_metadata.py` - Execution metadata with tokens and pricing
   - `workflow_file_info.py` - File information for uploads
   - `workflow_log_info.py` - Workflow log entry information
   - `workflow_run_log_info.py` - Workflow run log details
   - `end_user_info.py` - End user information
   - `app_info.py` - Application basic information
   - `parameters_info.py` - Application parameters configuration
   - `site_info.py` - WebApp site configuration
   - `user_input_form.py` - User input form configuration
   - `file_upload_config.py` - File upload settings
   - `system_parameters.py` - System configuration parameters

2. All models must:
   - Inherit from `pydantic.BaseModel`
   - Implement Builder pattern with @classmethod builder()
   - Use strict Literal types from workflow_types
   - Include proper field validation and constraints
   - Support optional fields with None defaults where specified
   - Use proper field aliases for API compatibility

3. **CRITICAL**: Streaming event models required:
   - `workflow_completion_response.py` - Blocking mode response structure
   - `chunk_workflow_event.py` - Base streaming event structure
   - Individual event data models for all 8 event types:
     * `workflow_started_data.py` - workflow_started event data
     * `node_started_data.py` - node_started event data
     * `text_chunk_data.py` - text_chunk event data
     * `node_finished_data.py` - node_finished event data
     * `workflow_finished_data.py` - workflow_finished event data
     * `tts_message_data.py` - tts_message event data
     * `tts_message_end_data.py` - tts_message_end event data
     * `ping_data.py` - ping event data (empty)

4. Key model specifications:
   - InputFileObjectWorkflow: type, transfer_method, url?, upload_file_id? (with validation rules)
   - WorkflowRunInfo: id, workflow_id, status, outputs, error, elapsed_time, total_tokens, total_steps, created_at, finished_at
   - NodeInfo: id, node_id, node_type, title, index, predecessor_node_id, inputs, outputs, status, error, elapsed_time, execution_metadata, created_at
   - ExecutionMetadata: total_tokens, total_price, currency
   - WorkflowFileInfo: id, name, size, extension, mime_type, created_by, created_at
   - UserInputForm: Support text-input, paragraph, select types with options
   - WorkflowCompletionResponse: workflow_run_id, task_id, data (for blocking mode)
   - ChunkWorkflowEvent: event, task_id, workflow_run_id, data (for streaming mode)

5. **MANDATORY**: InputFileObjectWorkflow validation rules:
   - When transfer_method is "remote_url": url is required, upload_file_id must be None
   - When transfer_method is "local_file": upload_file_id is required, url must be None
   - Must include proper field validation using Pydantic validators

6. Streaming event data structures (8 types):
   - workflow_started: id, workflow_id, sequence_number, created_at
   - node_started: id, node_id, node_type, title, index, predecessor_node_id, inputs, created_at
   - text_chunk: text, from_variable_selector
   - node_finished: complete node info with outputs, status, error, elapsed_time, execution_metadata
   - workflow_finished: complete workflow info with outputs, status, error, elapsed_time, total_tokens, total_steps
   - tts_message/tts_message_end: message_id, audio, created_at
   - ping: empty data
```

**Testing Prompt:**
```
Create comprehensive tests for all common model classes.

Requirements:
1. Create `tests/workflow/v1/model/test_workflow_public_models.py`
2. Create test classes for each common model:
   - TestWorkflowInputs
   - TestInputFileObjectWorkflow (including validation rules)
   - TestWorkflowRunInfo
   - TestWorkflowRunData
   - TestNodeInfo
   - TestExecutionMetadata
   - TestWorkflowFileInfo
   - TestWorkflowLogInfo
   - TestWorkflowRunLogInfo
   - TestEndUserInfo
   - TestAppInfo
   - TestParametersInfo
   - TestSiteInfo
   - TestUserInputForm
   - TestFileUploadConfig
   - TestSystemParameters
   - TestWorkflowCompletionResponse
   - TestChunkWorkflowEvent
   - TestWorkflowEventData

3. Test each model's:
   - Builder pattern functionality
   - Field validation and type constraints
   - Required vs optional field handling
   - Default value behavior
   - Pydantic serialization/deserialization
   - Integration with Literal types

4. **CRITICAL**: Special validation tests:
   - InputFileObjectWorkflow validation rules (remote_url vs local_file)
   - Streaming event data structure validation for all 8 event types
   - UUID format validation for ID fields
   - Enum value validation for status fields
   - Cross-field validation (transfer_method vs url/upload_file_id)

5. Use pytest fixtures for common test data
6. Achieve 100% test coverage
```

### Step 3: Implement Workflow Execution API Models (4 APIs)

**Implementation Prompt:**
```
Implement all request and response models for Workflow Execution APIs.

Requirements:
1. Create Workflow Execution API request models:
   - `run_workflow_request.py` + `run_workflow_request_body.py`
     * POST /v1/workflows/run
     * Support streaming and blocking modes
     * Support file array variables with InputFileObjectWorkflow
     * Fields: inputs (required Dict[str, Any]), response_mode (required), user (required)
   - `get_workflow_run_detail_request.py`
     * GET /v1/workflows/run/{workflow_run_id}
     * Path parameter: workflow_run_id (UUID format)
   - `stop_workflow_request.py` + `stop_workflow_request_body.py`
     * POST /v1/workflows/tasks/{task_id}/stop
     * Path parameter: task_id (UUID format)
     * Fields: user (required)
   - `get_workflow_logs_request.py`
     * GET /v1/workflows/logs
     * Query parameters: keyword, status, page, limit, created_by_end_user_session_id, created_by_account

2. Create corresponding response models (ALL inherit from BaseResponse):
   - `run_workflow_response.py` - Contains workflow_run_id, task_id, data fields for blocking mode
   - `get_workflow_run_detail_response.py` - Contains complete workflow run details
   - `stop_workflow_response.py` - Contains result field ("success")
   - `get_workflow_logs_response.py` - Contains page, limit, total, has_more, data fields

3. **CRITICAL**: Streaming response handling:
   - run_workflow_response must support both blocking and streaming modes
   - Blocking mode: Returns WorkflowCompletionResponse with workflow_run_id, task_id, data
   - Streaming mode: Returns ChunkWorkflowEvent stream with different event types
   - Must handle 8 different streaming event types with specific data structures

4. **CRITICAL**: All Request classes must:
   - Inherit from BaseRequest (MANDATORY)
   - Include proper HTTP method and URI configuration in builder
   - Handle path parameters using self._request.paths["param_name"] = value
   - Handle query parameters using self._request.add_query("key", value)
   - Handle request bodies using self._request.body = request_body.model_dump()

5. **CRITICAL**: All RequestBody classes must:
   - Inherit from pydantic.BaseModel (NOT BaseResponse)
   - Use Literal types for all predefined values
   - Implement builder patterns with proper field methods
   - Include comprehensive field validation

6. **CRITICAL**: All Response classes must:
   - Inherit from BaseResponse (ZERO TOLERANCE)
   - Use multiple inheritance when including data: class XResponse(DataInfo, BaseResponse)
   - Never inherit directly from pydantic.BaseModel
   - Support both blocking and streaming modes for run_workflow_response
```

**Testing Prompt:**
```
Create comprehensive tests for Workflow Execution API models.

Requirements:
1. Create `tests/workflow/v1/model/test_workflow_execution_models.py`
2. Implement 4 test classes:
   - TestRunWorkflowModels
   - TestGetWorkflowRunDetailModels
   - TestStopWorkflowModels
   - TestGetWorkflowLogsModels

3. Test content includes:
   - Request and RequestBody Builder patterns
   - Response class BaseResponse inheritance (CRITICAL)
   - Field validation and type constraints
   - HTTP method and URI configuration
   - Path parameter handling (workflow_run_id, task_id)
   - Query parameter handling (keyword, status, page, limit, created_by_end_user_session_id, created_by_account)
   - File array variable support with InputFileObjectWorkflow
   - Streaming and blocking mode support
   - UUID format validation for path parameters
   - Multiple inheritance patterns (DataInfo + BaseResponse)

4. **MANDATORY**: Verify all Response classes inherit from BaseResponse
5. Test streaming response handling for run_workflow
6. Verify all model integrations work properly
7. Ensure test coverage reaches 100%
```

### Step 4: Implement File Upload API Models (1 API)

**Implementation Prompt:**
```
Implement request and response models for File Upload API.

Requirements:
1. Create file upload API models:
   - `upload_file_request.py` + `upload_file_request_body.py`
     * POST /v1/files/upload
     * Use multipart/form-data
     * Fields: file (binary), user
     * Support any file formats for workflow use

2. Create response models:
   - `upload_file_response.py` - Inherits from WorkflowFileInfo and BaseResponse
   - Contains file information: id, name, size, extension, mime_type, created_by, created_at

3. **CRITICAL**: Special handling requirements:
   - Request class must support file upload (files field)
   - Properly handle multipart/form-data content type
   - File size and type validation
   - Use BytesIO to handle file data
   - RequestBody must handle form data fields (user)
   - Request must set files = {"file": (filename, file_data)} pattern

4. **MANDATORY**: File upload pattern:
   ```python
   class UploadFileRequest(BaseRequest):
       def file(self, file: BytesIO, filename: str) -> UploadFileRequestBuilder:
           self._request.files = {"file": (filename, file)}
           return self
   ```

5. Ensure integration with WorkflowFileInfo common model
```

**Testing Prompt:**
```
Create comprehensive tests for File Upload API models.

Requirements:
1. Create `tests/workflow/v1/model/test_file_upload_models.py`
2. Implement TestUploadFileModels test class
3. Test content includes:
   - Request and RequestBody Builder patterns
   - Response class BaseResponse inheritance (CRITICAL)
   - File upload functionality with BytesIO
   - Multipart form-data handling
   - Field validation and type constraints
   - HTTP method and URI configuration
   - Files field handling ({"file": (filename, file_data)} pattern)

4. **MANDATORY**: File upload specific tests:
   - Test BytesIO file handling
   - Test multipart/form-data content type
   - Test files field configuration
   - Test filename handling
   - Test form data integration

5. Use mock file data for testing
6. Verify file upload integration works correctly
7. Achieve 100% test coverage
```

### Step 5: Implement Application Configuration API Models (3 APIs)

**Implementation Prompt:**
```
Implement request and response models for Application Configuration APIs.

Requirements:
1. Create application configuration API models:
   - `get_info_request.py`
     * GET /v1/info
     * No parameters required
   - `get_parameters_request.py`
     * GET /v1/parameters
     * No parameters required
   - `get_site_request.py`
     * GET /v1/site
     * No parameters required

2. Create corresponding response models:
   - `get_info_response.py` - Inherits from AppInfo and BaseResponse
   - `get_parameters_response.py` - Inherits from ParametersInfo and BaseResponse
   - `get_site_response.py` - Inherits from SiteInfo and BaseResponse

3. Ensure all models:
   - Request classes inherit from BaseRequest
   - Response classes inherit from BaseResponse
   - Implement complete Builder pattern
   - Use strict Literal types
   - Handle simple GET requests without parameters
```

**Testing Prompt:**
```
Create comprehensive tests for Application Configuration API models.

Requirements:
1. Create `tests/workflow/v1/model/test_app_config_models.py`
2. Implement 3 test classes:
   - TestGetInfoModels
   - TestGetParametersModels
   - TestGetSiteModels

3. Test content includes:
   - Request Builder patterns
   - Response class BaseResponse inheritance
   - Field validation and type constraints
   - HTTP method and URI configuration
   - Simple GET request handling

4. Verify all model integrations work properly
5. Ensure test coverage reaches 100%
```

### Step 6: Implement Workflow Resource Class

**Implementation Prompt:**
```
Implement Workflow resource class containing all workflow-related API methods.

Requirements:
1. Create `dify_oapi/api/workflow/v1/resource/workflow.py`
2. Implement Workflow class with the following methods:
   - `run()` - Execute workflow (support streaming and blocking modes)
   - `detail()` - Get workflow run detail
   - `stop()` - Stop workflow task generation
   - `upload()` - Upload file for workflow
   - `logs()` - Get workflow logs
   - `info()` - Get application basic information
   - `parameters()` - Get application parameters
   - `site()` - Get application WebApp settings

3. Method characteristics:
   - Support synchronous and asynchronous operations (arun, adetail, astop, aupload, alogs, ainfo, aparameters, asite)
   - Use @overload decorator to support streaming/blocking mode type hints for run() method
   - Proper error handling
   - Complete type annotations

4. Streaming response handling:
   - Streaming mode returns Generator[bytes, None, None]
   - Blocking mode returns specific Response object
   - Properly handle SSE event streams

5. Ensure proper integration with existing Transport layer
```

**Testing Prompt:**
```
Create comprehensive tests for Workflow resource class.

Requirements:
1. Create `tests/workflow/v1/resource/test_workflow_resource.py`
2. Implement TestWorkflowResource class
3. Test all methods:
   - test_run_blocking - Test blocking mode workflow execution
   - test_run_streaming - Test streaming mode workflow execution
   - test_detail - Test get workflow run detail
   - test_stop - Test stop workflow task
   - test_upload - Test file upload
   - test_logs - Test get workflow logs
   - test_info - Test get application info
   - test_parameters - Test get application parameters
   - test_site - Test get application site settings
   - test_async_methods - Test all async methods

4. Use Mock objects to simulate Transport layer
5. Verify method signatures and return types
6. Test error handling scenarios
7. Ensure streaming and blocking modes work correctly
```

### Step 7: Implement Version Integration

**Implementation Prompt:**
```
Implement V1 version class to integrate the Workflow resource.

Requirements:
1. Create `dify_oapi/api/workflow/v1/version.py`
2. Implement V1 class with workflow resource:
   - Initialize Workflow resource with config
   - Expose workflow resource as public property
   - Maintain consistency with other API modules

3. Update `dify_oapi/api/workflow/v1/__init__.py`:
   - Export V1 class
   - Maintain clean module interface

4. Integration requirements:
   - Follow existing patterns from chat, completion, knowledge modules
   - Ensure proper config passing
   - Maintain type safety
```

**Testing Prompt:**
```
Create comprehensive tests for Version integration.

Requirements:
1. Create `tests/workflow/v1/test_version_integration.py`
2. Test V1 class:
   - test_v1_initialization - Test V1 class initialization
   - test_workflow_resource_access - Test workflow resource access
   - test_config_passing - Test config passing to resource
   - test_method_availability - Test all workflow methods are available

3. Verify integration with main client
4. Test that all 8 workflow methods are accessible through client.workflow.v1.workflow
5. Ensure proper error handling and type safety
```

### Step 8: Create Comprehensive Examples

**Implementation Prompt:**
```
Create comprehensive examples for all 8 Workflow APIs.

Requirements:
1. Create example files in `examples/workflow/`:
   - `run_workflow.py` - Execute workflow (sync + async + streaming)
   - `get_workflow_run_detail.py` - Get workflow run detail (sync + async)
   - `stop_workflow.py` - Stop workflow task (sync + async)
   - `upload_file.py` - Upload file (sync + async)
   - `get_workflow_logs.py` - Get workflow logs (sync + async)
   - `get_info.py` - Get application info (sync + async)
   - `get_parameters.py` - Get application parameters (sync + async)
   - `get_site.py` - Get application site settings (sync + async)

2. Example requirements:
   - Each file contains both sync and async examples
   - Use "[Example]" prefix for all created resources
   - Environment variable validation at function start
   - Proper error handling with try-catch blocks
   - Minimal code approach - only essential functionality
   - Real-world but simple test data

3. Special considerations:
   - run_workflow.py must include streaming example with event handling
   - upload_file.py must demonstrate file upload with BytesIO and multipart/form-data
   - get_workflow_logs.py must show filtering and pagination
   - All examples must validate required environment variables (raise ValueError if missing)
   - Include examples with InputFileObjectWorkflow for file array variables
   - Demonstrate both remote_url and local_file transfer methods

4. Safety features:
   - Check for "[Example]" prefix in resource names
   - Environment variable validation
   - Basic error handling
   - Resource cleanup functions where applicable
```

**Testing Prompt:**
```
Create comprehensive tests for all Workflow examples.

Requirements:
1. Create `tests/workflow/v1/integration/test_examples_validation.py`
2. Test all example functions:
   - Validate example code syntax and imports
   - Test environment variable validation
   - Verify "[Example]" prefix usage
   - Test error handling scenarios
   - Validate async/sync function pairs

3. Mock external dependencies:
   - Mock API calls to prevent actual requests
   - Mock file operations
   - Mock environment variables

4. Verify examples demonstrate:
   - Proper client initialization
   - Correct request building
   - Response handling and error checking
   - Streaming functionality with event handling (for run_workflow)
   - File upload functionality with multipart/form-data (for upload_file)
   - InputFileObjectWorkflow usage with validation rules
   - Environment variable validation with ValueError
   - Both sync and async patterns

5. Ensure all examples are production-ready and educational
```

### Step 9: Update Service Integration

**Implementation Prompt:**
```
Update workflow service integration to expose V1 API.

Requirements:
1. Update `dify_oapi/api/workflow/service.py`:
   - Import V1 class from version module
   - Initialize V1 with config in WorkflowService class
   - Expose v1 property for API access

2. Ensure consistency with existing service patterns:
   - Follow same structure as chat, completion, knowledge services
   - Maintain proper config passing
   - Ensure type safety

3. Integration verification:
   - Verify client.workflow.v1.workflow access pattern works
   - Ensure all 8 workflow methods are accessible
   - Test with different config options
```

**Testing Prompt:**
```
Create comprehensive tests for Service integration.

Requirements:
1. Create `tests/workflow/v1/integration/test_service_integration.py`
2. Test WorkflowService class:
   - test_service_initialization - Test service initialization
   - test_v1_access - Test v1 property access
   - test_workflow_resource_access - Test workflow resource access
   - test_all_methods_available - Test all 8 methods are available

3. Integration testing:
   - Test full client integration path
   - Verify client.workflow.v1.workflow.{method} works
   - Test with different client configurations
   - Ensure proper error propagation

4. Mock external dependencies appropriately
5. Achieve comprehensive integration test coverage
```

### Step 10: Final Integration and Documentation

**Implementation Prompt:**
```
Complete final integration and create comprehensive documentation.

Requirements:
1. Update main client integration:
   - Ensure workflow service is properly integrated in main Client class
   - Verify all access patterns work correctly
   - Test complete integration chain

2. Create comprehensive README:
   - Update `examples/workflow/README.md` with all 8 examples
   - Include usage patterns and best practices
   - Add troubleshooting section
   - Document environment variable requirements

3. Documentation updates:
   - Ensure all docstrings are complete and accurate
   - Update type hints throughout the codebase
   - Add inline comments for complex logic

4. Final validation:
   - Run all tests and ensure 100% pass rate
   - Verify examples work with real API (if possible)
   - Check code quality with linting tools
   - Ensure consistent code style throughout
```

**Testing Prompt:**
```
Create final comprehensive integration tests.

Requirements:
1. Create `tests/workflow/v1/integration/test_final_validation.py`
2. Comprehensive integration tests:
   - test_complete_client_integration - Test full client integration
   - test_all_apis_accessible - Test all 8 APIs are accessible
   - test_streaming_integration - Test streaming functionality
   - test_file_upload_integration - Test file upload functionality
   - test_error_handling_integration - Test error handling across all APIs
   - test_async_integration - Test async functionality across all APIs

3. End-to-end workflow tests:
   - Test complete workflow execution cycle
   - Test file upload and workflow execution with files
   - Test workflow monitoring and logging
   - Test application configuration retrieval

4. Performance and reliability tests:
   - Test concurrent API calls
   - Test large file uploads
   - Test long-running workflows
   - Test error recovery scenarios

5. Final validation checklist:
   - All 8 APIs implemented and tested
   - All examples working and validated
   - Complete documentation coverage
   - 100% test coverage achieved
   - Code quality standards met
```

## Quality Assurance Checklist

### Code Quality Standards
- [ ] All models use strict Literal types from workflow_types.py
- [ ] All Response classes inherit from BaseResponse
- [ ] All Request classes inherit from BaseRequest
- [ ] Builder patterns implemented for all models
- [ ] Proper error handling throughout
- [ ] Complete type annotations
- [ ] Consistent naming conventions
- [ ] UUID format validation for path parameters
- [ ] InputFileObjectWorkflow validation rules implemented

### API Coverage
- [ ] POST /workflows/run - Execute workflow (streaming + blocking)
- [ ] GET /workflows/run/{workflow_run_id} - Get workflow run detail
- [ ] POST /workflows/tasks/{task_id}/stop - Stop workflow task
- [ ] POST /files/upload - Upload file (multipart/form-data)
- [ ] GET /workflows/logs - Get workflow logs (with pagination)
- [ ] GET /info - Get application info
- [ ] GET /parameters - Get application parameters
- [ ] GET /site - Get application site settings

### Streaming Support Requirements
- [ ] Streaming event handling (8 event types)
- [ ] Event-specific data structures
- [ ] Generator[bytes, None, None] return type for streaming
- [ ] @overload decorators for streaming/blocking modes
- [ ] SSE (Server-Sent Events) format support

### Testing Requirements
- [ ] Unit tests for all models (100% coverage)
- [ ] Resource method tests (sync and async)
- [ ] Integration tests for all APIs
- [ ] Example validation tests
- [ ] Error handling tests
- [ ] Streaming functionality tests
- [ ] File upload tests with BytesIO
- [ ] Validation rule tests (InputFileObjectWorkflow)
- [ ] UUID format validation tests

### Documentation Standards
- [ ] Complete API documentation
- [ ] Working examples for all 8 APIs
- [ ] README with usage patterns
- [ ] Inline code documentation
- [ ] Type hints throughout
- [ ] Streaming examples with event handling
- [ ] File upload examples with multipart/form-data

### Safety and Best Practices
- [ ] "[Example]" prefix for all example resources
- [ ] Environment variable validation (API_KEY required)
- [ ] Proper error handling in examples
- [ ] Resource cleanup functions
- [ ] Minimal code approach in examples
- [ ] ValueError for missing environment variables (no print statements)

## Complete Model File List

### Required Model Files (44 total):

**Types and Common Models (27 files):**
- `workflow_types.py` - All Literal type definitions
- `workflow_inputs.py` - Dynamic workflow input parameters
- `input_file_object_workflow.py` - File input with validation rules
- `workflow_run_info.py` - Workflow execution information
- `workflow_run_data.py` - Workflow execution data details
- `node_info.py` - Node execution information
- `execution_metadata.py` - Execution metadata with tokens/pricing
- `workflow_file_info.py` - File information for uploads
- `workflow_log_info.py` - Workflow log entry information
- `workflow_run_log_info.py` - Workflow run log details
- `end_user_info.py` - End user information
- `app_info.py` - Application basic information
- `parameters_info.py` - Application parameters configuration
- `site_info.py` - WebApp site configuration
- `user_input_form.py` - User input form configuration
- `file_upload_config.py` - File upload settings
- `system_parameters.py` - System configuration parameters
- `workflow_completion_response.py` - Blocking mode response structure
- `chunk_workflow_event.py` - Streaming event base structure
- `workflow_started_data.py` - workflow_started event data
- `node_started_data.py` - node_started event data
- `text_chunk_data.py` - text_chunk event data
- `node_finished_data.py` - node_finished event data
- `workflow_finished_data.py` - workflow_finished event data
- `tts_message_data.py` - tts_message event data
- `tts_message_end_data.py` - tts_message_end event data
- `ping_data.py` - ping event data (empty)

**API Request/Response Models (17 files):**
- `run_workflow_request.py` + `run_workflow_request_body.py` + `run_workflow_response.py`
- `get_workflow_run_detail_request.py` + `get_workflow_run_detail_response.py`
- `stop_workflow_request.py` + `stop_workflow_request_body.py` + `stop_workflow_response.py`
- `get_workflow_logs_request.py` + `get_workflow_logs_response.py`
- `upload_file_request.py` + `upload_file_request_body.py` + `upload_file_response.py`
- `get_info_request.py` + `get_info_response.py`
- `get_parameters_request.py` + `get_parameters_response.py`
- `get_site_request.py` + `get_site_response.py`

## Implementation Timeline

**Estimated Timeline: 8-10 development cycles**

1. **Steps 1-2**: Types and Common Models (2 cycles)
2. **Steps 3-5**: API Models Implementation (3 cycles)
3. **Step 6**: Resource Implementation (1 cycle)
4. **Step 7**: Version Integration (1 cycle)
5. **Steps 8-9**: Examples and Service Integration (2 cycles)
6. **Step 10**: Final Integration and Documentation (1 cycle)

Each cycle includes both implementation and testing phases to ensure code quality and reliability.

## Success Criteria

- ✅ All 8 Workflow APIs fully implemented
- ✅ Complete type safety with strict Literal types
- ✅ Comprehensive test coverage (100%)
- ✅ Working examples for all APIs
- ✅ Streaming support for workflow execution
- ✅ File upload functionality
- ✅ Proper error handling throughout
- ✅ Clean, maintainable code architecture
- ✅ Complete documentation coverage
- ✅ Production-ready implementation

This implementation plan provides a systematic approach to building a complete, production-ready Workflow API module for the dify-oapi project, ensuring high code quality, comprehensive testing, and excellent developer experience.