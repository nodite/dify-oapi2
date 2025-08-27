# Workflow API Implementation Plan - AI Prompts

This document provides step-by-step prompts for implementing the complete workflow application functionality in the dify-oapi workflow module. Each step includes implementation and testing phases to ensure code quality.

## Overview

The implementation covers 10 workflow-related APIs organized into four main resource groups:
- **Workflow Management**: 4 APIs (run workflow, run specific workflow, get workflow run detail, stop workflow)
- **File Management**: 2 APIs (upload file, preview file)
- **Log Management**: 1 API (get workflow logs)
- **Application Information**: 3 APIs (get info, get parameters, get site)

## Implementation Steps

### Phase 1: Common Models Foundation

#### Step 1: Create Workflow Types and Shared Common Models
**Prompt:**
```
Create the workflow types and shared common models for the workflow API implementation in `dify_oapi/api/workflow/v1/model/workflow/`. 

First, create `workflow_types.py` with all Literal types for type safety:

```python
from typing import Literal

# Response mode types
ResponseMode = Literal["streaming", "blocking"]

# File types
FileType = Literal["document", "image", "audio", "video", "custom"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Workflow status types
WorkflowStatus = Literal["running", "succeeded", "failed", "stopped"]

# Event types
EventType = Literal["workflow_started", "node_started", "text_chunk", "node_finished", "workflow_finished", "tts_message", "tts_message_end", "ping"]

# Node types
NodeType = Literal["start", "end", "llm", "code", "template", "knowledge_retrieval", "question_classifier", "if_else", "variable_assigner", "parameter_extractor"]

# Icon types
IconType = Literal["emoji", "image"]

# App mode types
AppMode = Literal["workflow"]

# Log status types
LogStatus = Literal["succeeded", "failed", "stopped"]

# Created by role types
CreatedByRole = Literal["end_user", "account"]

# Created from types
CreatedFrom = Literal["service-api", "web-app"]
```

Then implement the following model files with proper type hints, builder patterns, and Pydantic validation:

1. `workflow_run_info.py` - WorkflowRunInfo class with fields:
   - workflow_run_id: str | None = None
   - task_id: str | None = None
   - data: WorkflowRunData | None = None

2. `workflow_run_data.py` - WorkflowRunData class with fields:
   - id: str | None = None
   - workflow_id: str | None = None
   - status: WorkflowStatus | None = None
   - outputs: dict[str, Any] | None = None
   - error: str | None = None
   - elapsed_time: float | None = None
   - total_tokens: int | None = None
   - total_steps: int | None = None
   - created_at: int | None = None
   - finished_at: int | None = None

3. `workflow_inputs.py` - WorkflowInputs class with fields:
   - Dynamic inputs based on workflow configuration (dict-like structure)

4. `node_info.py` - NodeInfo class with fields:
   - id: str | None = None
   - node_id: str | None = None
   - node_type: NodeType | None = None
   - title: str | None = None
   - index: int | None = None
   - predecessor_node_id: str | None = None
   - inputs: dict[str, Any] | None = None
   - outputs: dict[str, Any] | None = None
   - status: WorkflowStatus | None = None
   - error: str | None = None
   - elapsed_time: float | None = None
   - execution_metadata: ExecutionMetadata | None = None
   - created_at: int | None = None

5. `execution_metadata.py` - ExecutionMetadata class with fields:
   - total_tokens: int | None = None
   - total_price: float | None = None
   - currency: str | None = None

6. `streaming_event.py` - StreamingEvent class with fields:
   - event: EventType | None = None
   - task_id: str | None = None
   - workflow_run_id: str | None = None
   - data: dict[str, Any] | None = None

MANDATORY REQUIREMENTS:
- ALL classes MUST inherit from `pydantic.BaseModel`
- ALL classes MUST include `from __future__ import annotations` at the top
- ALL classes MUST have builder patterns with proper type hints
- Use `@staticmethod` decorator for builder() methods
- Builder classes MUST follow naming pattern: ClassNameBuilder
- All fields MUST use proper type hints with `| None = None` for optional fields
- Use Literal types from workflow_types.py for type safety
- Follow existing project patterns in dify_oapi for consistency
```

#### Step 2: Test Workflow Common Models
**Prompt:**
```
Create comprehensive unit tests for all common models created in Step 1. 

Create test file `tests/workflow/v1/model/test_workflow_models.py` that covers:

1. Model instantiation and validation
2. Builder pattern functionality for all models
3. Serialization/deserialization using Pydantic
4. Edge cases and validation errors
5. Optional field handling
6. Nested model relationships (WorkflowRunInfo with WorkflowRunData)
7. Literal type validation (WorkflowStatus, EventType, etc.)

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations for parameters and return types
- Use `-> None` for test method return types
- Import `typing.Any` for complex mock objects
- Use pytest framework with proper fixtures
- Test both direct instantiation and builder pattern approaches
- Verify method chaining works correctly in builders
- Test serialization with `model_dump()` method
- Test Literal type validation (invalid values should raise errors)
- Ensure all tests pass with good coverage (>90%)

Example test structure:
```python
# ===== SHARED WORKFLOW MODELS TESTS =====

def test_workflow_run_info_creation() -> None:
    # Test valid workflow run info creation

def test_workflow_run_info_builder_pattern() -> None:
    # Test builder pattern functionality

def test_workflow_status_literal_validation() -> None:
    # Test WorkflowStatus literal type validation

def test_node_info_builder() -> None:
    # Test node info builder pattern
```

Note: This file will be extended in subsequent steps to include all API model tests.
```

### Phase 2: Workflow Management APIs (4 APIs)

#### Step 3: Create Run Workflow API Models
**Prompt:**
```
Create run workflow API models in `dify_oapi/api/workflow/v1/model/workflow/` following MANDATORY code style rules.

Implement the following model files with STRICT adherence to patterns:

**POST Request Models (with RequestBody)**:
1. `run_workflow_request.py` - RunWorkflowRequest + RunWorkflowRequestBuilder (inherits BaseRequest)
2. `run_workflow_request_body.py` - RunWorkflowRequestBody + RunWorkflowRequestBodyBuilder (inherits BaseModel)
   Fields: inputs (WorkflowInputs), response_mode (ResponseMode), user, files, trace_id

**Response Models**:
3. `run_workflow_response.py` - RunWorkflowResponse (inherits WorkflowRunInfo, BaseResponse)

CRITICAL REQUIREMENTS:
- ALL class names MUST match file names exactly (NO module prefixes)
- Request classes MUST inherit from BaseRequest
- RequestBody classes MUST inherit from BaseModel
- Response classes MUST inherit from BaseResponse (MANDATORY - ZERO TOLERANCE)
- Use `request_body()` method pattern for POST requests
- Builder variables MUST use full descriptive names (e.g., `self._run_workflow_request`)
- Set correct HTTP methods and URIs in builder constructors
- NO Builder patterns for Response classes
- Use Literal types from workflow_types.py for type safety

URI Pattern:
- POST /v1/workflows/run → `RunWorkflowRequest`
```

#### Step 4: Test Run Workflow API Models
**Prompt:**
```
Add comprehensive unit tests for run workflow API models to the existing `tests/workflow/v1/model/test_workflow_models.py` file:

Add a new section for Run Workflow API models:

Requirements:
- Add tests to the existing consolidated test file
- Test RunWorkflowRequest builder pattern
- Test RunWorkflowRequestBody validation and builder
- Test RunWorkflowResponse model with multiple inheritance
- Test request body serialization
- Verify HTTP method and URI configuration
- Test Literal type validation (ResponseMode)
- Include edge cases and validation errors
- All test methods must have proper type hints
- Test builder method chaining
- Use clear section comments to organize tests

Example test structure addition:
```python
# ===== RUN WORKFLOW API MODELS TESTS =====

def test_run_workflow_request_builder() -> None:
    # Test RunWorkflowRequest builder pattern

def test_run_workflow_request_body_validation() -> None:
    # Test RunWorkflowRequestBody validation and builder

def test_run_workflow_response_model() -> None:
    # Test RunWorkflowResponse model
```

Run tests: `poetry run pytest tests/workflow/v1/model/test_workflow_models.py -v`
```

#### Step 5: Create Run Specific Workflow API Models
**Prompt:**
```
Create run specific workflow API models in `dify_oapi/api/workflow/v1/model/workflow/`:

1. `run_specific_workflow_request.py` - RunSpecificWorkflowRequest + RunSpecificWorkflowRequestBuilder (inherits BaseRequest)
   Path params: workflow_id
   
2. `run_specific_workflow_request_body.py` - RunSpecificWorkflowRequestBody + RunSpecificWorkflowRequestBodyBuilder (inherits BaseModel)
   Fields: inputs (WorkflowInputs), response_mode (ResponseMode), user, files, trace_id

3. `run_specific_workflow_response.py` - RunSpecificWorkflowResponse (inherits WorkflowRunInfo, BaseResponse)

Requirements:
- Handle workflow_id path parameter using `self._request.paths["workflow_id"] = workflow_id`
- Follow POST request patterns with RequestBody
- Include proper type hints and docstrings
- Include `from __future__ import annotations`
- Use Literal types for type safety

URI Pattern:
- POST /v1/workflows/:workflow_id/run → `RunSpecificWorkflowRequest`
```

#### Step 6: Test Run Specific Workflow API Models
**Prompt:**
```
Add unit tests for run specific workflow API models to `tests/workflow/v1/model/test_workflow_models.py`:

Add a new section for Run Specific Workflow API models:

Requirements:
- Add tests to the existing consolidated test file
- Test path parameter handling (workflow_id)
- Test RunSpecificWorkflowRequestBody validation
- Test RunSpecificWorkflowResponse model
- Include proper type hints for all test methods
- Test builder patterns
- Use clear section comments to organize tests

Example test structure addition:
```python
# ===== RUN SPECIFIC WORKFLOW API MODELS TESTS =====

def test_run_specific_workflow_request_builder() -> None:
    # Test RunSpecificWorkflowRequest builder pattern
```

Run tests: `poetry run pytest tests/workflow/v1/model/test_workflow_models.py -v`
```

#### Step 7: Create Get Workflow Run Detail API Models
**Prompt:**
```
Create get workflow run detail API models in `dify_oapi/api/workflow/v1/model/workflow/`:

1. `get_workflow_run_detail_request.py` - GetWorkflowRunDetailRequest + GetWorkflowRunDetailRequestBuilder (inherits BaseRequest)
   Path params: workflow_run_id

2. `get_workflow_run_detail_response.py` - GetWorkflowRunDetailResponse (inherits BaseResponse)
   Fields: id, workflow_id, status (WorkflowStatus), inputs, outputs, error, total_steps, total_tokens, created_at, finished_at, elapsed_time

Requirements:
- Handle workflow_run_id path parameter
- GET request with no RequestBody
- Include proper type hints and docstrings
- Use Literal types for type safety

URI Pattern:
- GET /v1/workflows/run/:workflow_run_id → `GetWorkflowRunDetailRequest`
```

#### Step 8: Test Get Workflow Run Detail API Models
**Prompt:**
```
Add unit tests for get workflow run detail API models to `tests/workflow/v1/model/test_workflow_models.py`:

Add a new section for Get Workflow Run Detail API models:

Requirements:
- Add tests to the existing consolidated test file
- Test path parameter handling (workflow_run_id)
- Test GET request model
- Test response model with WorkflowStatus literal type
- Include proper type hints for all test methods
- Test builder patterns
- Use clear section comments to organize tests

Example test structure addition:
```python
# ===== GET WORKFLOW RUN DETAIL API MODELS TESTS =====

def test_get_workflow_run_detail_request_builder() -> None:
    # Test GetWorkflowRunDetailRequest builder pattern
```

Run tests: `poetry run pytest tests/workflow/v1/model/test_workflow_models.py -v`
```

#### Step 9: Create Stop Workflow API Models
**Prompt:**
```
Create stop workflow API models in `dify_oapi/api/workflow/v1/model/workflow/`:

1. `stop_workflow_request.py` - StopWorkflowRequest + StopWorkflowRequestBuilder (inherits BaseRequest)
   Path params: task_id
   
2. `stop_workflow_request_body.py` - StopWorkflowRequestBody + StopWorkflowRequestBodyBuilder (inherits BaseModel)
   Fields: user

3. `stop_workflow_response.py` - StopWorkflowResponse (inherits BaseResponse)
   Fields: result

Requirements:
- Handle task_id path parameter using `self._request.paths["task_id"] = task_id`
- Follow POST request patterns with RequestBody
- Include proper type hints and docstrings
- Include `from __future__ import annotations`

URI Pattern:
- POST /v1/workflows/tasks/:task_id/stop → `StopWorkflowRequest`
```

#### Step 10: Test Stop Workflow API Models
**Prompt:**
```
Add unit tests for stop workflow API models to `tests/workflow/v1/model/test_workflow_models.py`:

Add a new section for Stop Workflow API models:

Requirements:
- Add tests to the existing consolidated test file
- Test path parameter handling (task_id)
- Test StopWorkflowRequestBody validation
- Test StopWorkflowResponse model
- Include proper type hints for all test methods
- Test builder patterns
- Use clear section comments to organize tests

Example test structure addition:
```python
# ===== STOP WORKFLOW API MODELS TESTS =====

def test_stop_workflow_request_builder() -> None:
    # Test StopWorkflowRequest builder pattern
```

Run tests: `poetry run pytest tests/workflow/v1/model/test_workflow_models.py -v`
```

### Phase 3: File Management APIs (2 APIs)

#### Step 11: Create File Models
**Prompt:**
```
Create file management models in `dify_oapi/api/workflow/v1/model/file/`:

1. `file_info.py` - FileInfo class with fields:
   - id: str | None = None
   - name: str | None = None
   - size: int | None = None
   - extension: str | None = None
   - mime_type: str | None = None
   - created_by: str | None = None
   - created_at: int | None = None

2. `upload_file_request.py` - UploadFileRequest + UploadFileRequestBuilder (inherits BaseRequest)
   Special handling for multipart/form-data with file field

3. `upload_file_request_body.py` - UploadFileRequestBody + UploadFileRequestBodyBuilder (inherits BaseModel)
   Fields: user

4. `upload_file_response.py` - UploadFileResponse (inherits FileInfo, BaseResponse)

5. `preview_file_request.py` - PreviewFileRequest + PreviewFileRequestBuilder (inherits BaseRequest)
   Path params: file_id
   Query params: as_attachment (optional)

6. `preview_file_response.py` - PreviewFileResponse (inherits BaseResponse)
   Fields: content_type, content_length, content (binary data)

CRITICAL PATTERN for multipart/form-data:
- Request class MUST support both `files` and `body` fields in BaseRequest
- Use nested data structure pattern for complex form data
- Builder methods MUST handle file streams and form data separately

Implementation Pattern:
```python
class UploadFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file: BytesIO | None = None
        
    def file(self, file: BytesIO, file_name: str | None = None) -> UploadFileRequestBuilder:
        self._request.file = file
        file_name = file_name or "upload"
        self._request.files = {"file": (file_name, file)}
        return self
        
    def request_body(self, request_body: UploadFileRequestBody) -> UploadFileRequestBuilder:
        if request_body.user:
            self._request.body = {"user": request_body.user}
        return self
```

URI Patterns:
- POST /v1/files/upload → `UploadFileRequest`
- GET /v1/files/:file_id/preview → `PreviewFileRequest`
```

#### Step 12: Test File Models
**Prompt:**
```
Add unit tests for file models to `tests/workflow/v1/model/test_workflow_models.py`:

Add a new section for File API models:

Requirements:
- Add tests to the existing consolidated test file
- Test multipart/form-data handling
- Test file upload scenarios
- Test FileInfo builder pattern
- Test UploadFileRequest special handling
- Test PreviewFileRequest path and query parameters
- Include proper type hints for all test methods
- Test builder patterns
- Use clear section comments to organize tests

Example test structure addition:
```python
# ===== FILE API MODELS TESTS =====

def test_file_info_builder_pattern() -> None:
    # Test FileInfo builder pattern

def test_upload_file_request_multipart() -> None:
    # Test UploadFileRequest multipart handling

def test_preview_file_request_parameters() -> None:
    # Test PreviewFileRequest path and query parameters
```

Run tests: `poetry run pytest tests/workflow/v1/model/test_workflow_models.py -v`
```

### Phase 4: Log Management APIs (1 API)

#### Step 13: Create Log Models
**Prompt:**
```
Create log management models in `dify_oapi/api/workflow/v1/model/log/`:

1. `log_info.py` - LogInfo class with fields:
   - id: str | None = None
   - workflow_run: WorkflowRunLogInfo | None = None
   - created_from: CreatedFrom | None = None
   - created_by_role: CreatedByRole | None = None
   - created_by_account: str | None = None
   - created_by_end_user: EndUserInfo | None = None
   - created_at: int | None = None

2. `workflow_run_log_info.py` - WorkflowRunLogInfo class with fields:
   - id: str | None = None
   - version: str | None = None
   - status: LogStatus | None = None
   - error: str | None = None
   - elapsed_time: float | None = None
   - total_tokens: int | None = None
   - total_steps: int | None = None
   - created_at: int | None = None
   - finished_at: int | None = None

3. `end_user_info.py` - EndUserInfo class with fields:
   - id: str | None = None
   - type: str | None = None
   - is_anonymous: bool | None = None
   - session_id: str | None = None

4. `get_workflow_logs_request.py` - GetWorkflowLogsRequest + GetWorkflowLogsRequestBuilder (inherits BaseRequest)
   Query params: keyword, status (LogStatus), page, limit, created_by_end_user_session_id, created_by_account

5. `get_workflow_logs_response.py` - GetWorkflowLogsResponse (inherits BaseResponse)
   Fields: page, limit, total, has_more, data (list[LogInfo])

Requirements:
- Handle multiple query parameters
- GET request with no RequestBody
- Use Literal types for type safety (LogStatus, CreatedFrom, CreatedByRole)
- Include `from __future__ import annotations`

URI Pattern:
- GET /v1/workflows/logs → `GetWorkflowLogsRequest`
```

#### Step 14: Test Log Models
**Prompt:**
```
Add unit tests for log models to `tests/workflow/v1/model/test_workflow_models.py`:

Add a new section for Log API models:

Requirements:
- Add tests to the existing consolidated test file
- Test LogInfo builder pattern with nested models
- Test query parameter handling (keyword, status, page, limit, etc.)
- Test LogStatus literal type validation
- Test WorkflowRunLogInfo and EndUserInfo builder patterns
- Include proper type hints for all test methods
- Test builder patterns
- Use clear section comments to organize tests

Example test structure addition:
```python
# ===== LOG API MODELS TESTS =====

def test_log_info_builder_pattern() -> None:
    # Test LogInfo builder pattern

def test_get_workflow_logs_request_query_params() -> None:
    # Test GetWorkflowLogsRequest query parameter handling

def test_log_status_literal_validation() -> None:
    # Test LogStatus literal type validation
```

Run tests: `poetry run pytest tests/workflow/v1/model/test_workflow_models.py -v`
```

### Phase 5: Application Information APIs (3 APIs)

#### Step 15: Create Info Models
**Prompt:**
```
Create application information models in `dify_oapi/api/workflow/v1/model/info/`:

1. `app_info.py` - AppInfo class with fields:
   - name: str | None = None
   - description: str | None = None
   - tags: list[str] | None = None
   - mode: AppMode | None = None
   - author_name: str | None = None

2. `parameters_info.py` - ParametersInfo class with fields:
   - user_input_form: list[UserInputForm] | None = None
   - file_upload: FileUploadConfig | None = None
   - system_parameters: SystemParameters | None = None

3. `site_info.py` - SiteInfo class with fields:
   - title: str | None = None
   - icon_type: IconType | None = None
   - icon: str | None = None
   - icon_background: str | None = None
   - icon_url: str | None = None
   - description: str | None = None
   - copyright: str | None = None
   - privacy_policy: str | None = None
   - custom_disclaimer: str | None = None
   - default_language: str | None = None
   - show_workflow_steps: bool | None = None

4. `user_input_form.py` - UserInputForm class with fields:
   - label: str | None = None
   - variable: str | None = None
   - required: bool | None = None
   - default: str | None = None
   - options: list[str] | None = None

5. `file_upload_config.py` - FileUploadConfig class with fields:
   - document: dict[str, Any] | None = None
   - image: dict[str, Any] | None = None
   - audio: dict[str, Any] | None = None
   - video: dict[str, Any] | None = None
   - custom: dict[str, Any] | None = None

6. `system_parameters.py` - SystemParameters class with fields:
   - file_size_limit: int | None = None
   - image_file_size_limit: int | None = None
   - audio_file_size_limit: int | None = None
   - video_file_size_limit: int | None = None

7. `get_info_request.py` - GetInfoRequest + GetInfoRequestBuilder (inherits BaseRequest)
8. `get_info_response.py` - GetInfoResponse (inherits AppInfo, BaseResponse)

9. `get_parameters_request.py` - GetParametersRequest + GetParametersRequestBuilder (inherits BaseRequest)
10. `get_parameters_response.py` - GetParametersResponse (inherits ParametersInfo, BaseResponse)

11. `get_site_request.py` - GetSiteRequest + GetSiteRequestBuilder (inherits BaseRequest)
12. `get_site_response.py` - GetSiteResponse (inherits SiteInfo, BaseResponse)

Requirements:
- All are GET requests with no RequestBody
- All public classes MUST have Builder patterns
- Use Literal types for type safety (AppMode, IconType)
- Follow established patterns
- Include `from __future__ import annotations`

URI Patterns:
- GET /v1/info → `GetInfoRequest`
- GET /v1/parameters → `GetParametersRequest`
- GET /v1/site → `GetSiteRequest`
```

#### Step 16: Test Info Models
**Prompt:**
```
Add unit tests for info models to `tests/workflow/v1/model/test_workflow_models.py`:

Add a new section for Info API models:

Requirements:
- Add tests to the existing consolidated test file
- Test all public class builder patterns (AppInfo, ParametersInfo, SiteInfo, etc.)
- Test GET request models
- Test multiple inheritance in response models
- Test complex nested structures (ParametersInfo with UserInputForm, FileUploadConfig)
- Test Literal type validation (AppMode, IconType)
- Include proper type hints for all test methods
- Test builder patterns
- Use clear section comments to organize tests

Example test structure addition:
```python
# ===== INFO API MODELS TESTS =====

def test_app_info_builder_pattern() -> None:
    # Test AppInfo builder pattern

def test_parameters_info_complex_structure() -> None:
    # Test ParametersInfo complex nested structure

def test_get_info_request_builder() -> None:
    # Test GetInfoRequest builder pattern

def test_app_mode_literal_validation() -> None:
    # Test AppMode literal type validation
```

Run tests: `poetry run pytest tests/workflow/v1/model/test_workflow_models.py -v`
```

### Phase 6: Resource Implementation

#### Step 17: Implement Workflow Resource
**Prompt:**
```
Implement the Workflow resource class in `dify_oapi/api/workflow/v1/resource/workflow.py`.

Create a Workflow class with the following methods:
1. `run_workflow(request: RunWorkflowRequest, request_option: RequestOption, stream: bool = False) -> RunWorkflowResponse | Iterator[str]`
2. `arun_workflow(request: RunWorkflowRequest, request_option: RequestOption, stream: bool = False) -> RunWorkflowResponse | AsyncIterator[str]`
3. `run_specific_workflow(request: RunSpecificWorkflowRequest, request_option: RequestOption, stream: bool = False) -> RunSpecificWorkflowResponse | Iterator[str]`
4. `arun_specific_workflow(request: RunSpecificWorkflowRequest, request_option: RequestOption, stream: bool = False) -> RunSpecificWorkflowResponse | AsyncIterator[str]`
5. `get_workflow_run_detail(request: GetWorkflowRunDetailRequest, request_option: RequestOption) -> GetWorkflowRunDetailResponse`
6. `aget_workflow_run_detail(request: GetWorkflowRunDetailRequest, request_option: RequestOption) -> GetWorkflowRunDetailResponse`
7. `stop_workflow(request: StopWorkflowRequest, request_option: RequestOption) -> StopWorkflowResponse`
8. `astop_workflow(request: StopWorkflowRequest, request_option: RequestOption) -> StopWorkflowResponse`

Requirements:
- Handle streaming responses for run_workflow and run_specific_workflow
- Use Transport.execute() for sync and ATransport.aexecute() for async
- Use Transport.stream() for streaming responses
- Follow existing resource patterns in the project
- Include proper type hints and docstrings
```

#### Step 18: Test Workflow Resource
**Prompt:**
```
Create comprehensive unit tests for the Workflow resource in `tests/workflow/v1/resource/test_workflow_resource.py`.

Requirements:
- Test all 8 methods (4 sync + 4 async)
- Test streaming functionality for run_workflow and run_specific_workflow
- Mock Transport.execute() and ATransport.aexecute() calls
- Test error handling scenarios
- Include proper type hints for all test methods
- Use pytest framework with proper fixtures

Run tests: `poetry run pytest tests/workflow/v1/resource/test_workflow_resource.py -v`
```

#### Step 19: Implement File Resource
**Prompt:**
```
Implement the File resource class in `dify_oapi/api/workflow/v1/resource/file.py`.

Create a File class with the following methods:
1. `upload_file(request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse`
2. `aupload_file(request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse`
3. `preview_file(request: PreviewFileRequest, request_option: RequestOption) -> PreviewFileResponse`
4. `apreview_file(request: PreviewFileRequest, request_option: RequestOption) -> PreviewFileResponse`

Requirements:
- Handle multipart/form-data uploads
- Handle binary file preview responses
- Use Transport.execute() for sync and ATransport.aexecute() for async
- Follow existing resource patterns
- Include proper type hints and docstrings
```

#### Step 20: Test File Resource
**Prompt:**
```
Create comprehensive unit tests for the File resource in `tests/workflow/v1/resource/test_file_resource.py`.

Requirements:
- Test all 4 methods (2 sync + 2 async)
- Test multipart/form-data handling
- Test binary file preview responses
- Mock file upload and preview scenarios
- Include proper type hints for all test methods
- Use pytest framework with proper fixtures

Run tests: `poetry run pytest tests/workflow/v1/resource/test_file_resource.py -v`
```

#### Step 21: Implement Log Resource
**Prompt:**
```
Implement the Log resource class in `dify_oapi/api/workflow/v1/resource/log.py`.

Create a Log class with the following methods:
1. `get_workflow_logs(request: GetWorkflowLogsRequest, request_option: RequestOption) -> GetWorkflowLogsResponse`
2. `aget_workflow_logs(request: GetWorkflowLogsRequest, request_option: RequestOption) -> GetWorkflowLogsResponse`

Requirements:
- Handle query parameter filtering
- Use Transport.execute() for sync and ATransport.aexecute() for async
- Follow existing resource patterns
- Include proper type hints and docstrings
```

#### Step 22: Test Log Resource
**Prompt:**
```
Create comprehensive unit tests for the Log resource in `tests/workflow/v1/resource/test_log_resource.py`.

Requirements:
- Test both sync and async methods
- Test query parameter handling
- Mock API responses
- Test error handling scenarios
- Include proper type hints for all test methods
- Use pytest framework with proper fixtures

Run tests: `poetry run pytest tests/workflow/v1/resource/test_log_resource.py -v`
```

#### Step 23: Implement Info Resource
**Prompt:**
```
Implement the Info resource class in `dify_oapi/api/workflow/v1/resource/info.py`.

Create an Info class with the following methods:
1. `get_info(request: GetInfoRequest, request_option: RequestOption) -> GetInfoResponse`
2. `aget_info(request: GetInfoRequest, request_option: RequestOption) -> GetInfoResponse`
3. `get_parameters(request: GetParametersRequest, request_option: RequestOption) -> GetParametersResponse`
4. `aget_parameters(request: GetParametersRequest, request_option: RequestOption) -> GetParametersResponse`
5. `get_site(request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse`
6. `aget_site(request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse`

Requirements:
- All are GET requests
- Use Transport.execute() for sync and ATransport.aexecute() for async
- Follow existing resource patterns
- Include proper type hints and docstrings
```

#### Step 24: Test Info Resource
**Prompt:**
```
Create comprehensive unit tests for the Info resource in `tests/workflow/v1/resource/test_info_resource.py`.

Requirements:
- Test all 6 methods (3 sync + 3 async)
- Mock API responses for all info endpoints
- Test error handling scenarios
- Include proper type hints for all test methods
- Use pytest framework with proper fixtures

Run tests: `poetry run pytest tests/workflow/v1/resource/test_info_resource.py -v`
```

### Phase 7: Version Integration

#### Step 25: Update Version Integration
**Prompt:**
```
Update the workflow v1 version integration to include all new resources.

Modify `dify_oapi/api/workflow/v1/version.py` to:
1. Import all new resource classes
2. Add properties for all resources to the V1 class
3. Initialize all resources with the config parameter
4. Ensure backward compatibility with existing workflow resource

Requirements:
- Import: Workflow, File, Log, Info
- Initialize all resources with config parameter
- Maintain existing API structure
- Update any necessary import statements

Example integration:
```python
from .resource.workflow import Workflow
from .resource.file import File
from .resource.log import Log
from .resource.info import Info

class V1:
    def __init__(self, config: Config):
        self.workflow = Workflow(config)
        self.file = File(config)
        self.log = Log(config)
        self.info = Info(config)
```
```

#### Step 26: Test Version Integration
**Prompt:**
```
Create integration tests for the updated V1 version class in `tests/workflow/v1/integration/test_version_integration.py`.

Test:
1. All resources are properly initialized
2. Config is correctly passed to all resources
3. All new resources are accessible
4. Client integration works end-to-end

Requirements:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest framework with proper fixtures
- Test resource initialization and accessibility
- Verify config propagation to all resources
- Ensure complete workflow module works as expected

Run tests: `poetry run pytest tests/workflow/v1/integration/test_version_integration.py -v`
```

### Phase 8: Examples Implementation

#### Step 27: Create Workflow Examples
**Prompt:**
```
Create comprehensive usage examples for workflow functionality in `examples/workflow/workflow/`.

Create examples using MINIMAL code approach:

1. `run_workflow.py` - Run workflow examples (sync + async)
2. `run_specific_workflow.py` - Run specific workflow examples (sync + async)
3. `get_workflow_run_detail.py` - Get workflow run detail examples (sync + async)
4. `stop_workflow.py` - Stop workflow examples (sync + async)

MANDATORY REQUIREMENTS:
- Write ABSOLUTE MINIMAL code needed to demonstrate each API correctly
- ALL resource names MUST use "[Example]" prefix for safety
- Environment variable validation at function start (raise ValueError if missing)
- Both synchronous and asynchronous implementations
- Basic try-catch error handling
- Follow existing example patterns in the project
- Validate API_KEY environment variable

Environment variable validation pattern:
```python
def run_workflow_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        # Initialize client and continue...
```
```

#### Step 28: Test Workflow Examples
**Prompt:**
```
Test the workflow examples created in Step 27:

1. **Set Environment Variables**:
   ```bash
   export API_KEY="your-api-key"
   export DOMAIN="https://api.dify.ai"
   ```

2. **Run Examples**:
   ```bash
   cd examples/workflow/workflow/
   python run_workflow.py
   python run_specific_workflow.py
   python get_workflow_run_detail.py
   python stop_workflow.py
   ```

Requirements:
- All examples run without errors
- Resources are created with "[Example]" prefix
- Both sync and async functions work correctly
- Environment variable validation works
- Error handling functions properly
```

#### Step 29: Create File Examples
**Prompt:**
```
Create file management examples in `examples/workflow/file/`:

1. `upload_file.py` - Upload file examples (sync + async)
2. `preview_file.py` - Preview file examples (sync + async)

Requirements:
- Follow same patterns as workflow examples
- MANDATORY: Environment variable validation at function start
- MANDATORY: "[Example]" prefix for resources
- MANDATORY: Code minimalism principles
- Include both sync and async examples
- Handle file upload and preview scenarios
- Include proper error handling
```

#### Step 30: Test File Examples
**Prompt:**
```
Test the file examples created in Step 29:

1. **Run File Examples**:
   ```bash
   cd examples/workflow/file/
   python upload_file.py
   python preview_file.py
   ```

Requirements:
- All file examples must work correctly
- File operations should handle uploads and previews properly
- Environment variable validation should work
```

#### Step 31: Create Log Examples
**Prompt:**
```
Create log management examples in `examples/workflow/log/`:

1. `get_workflow_logs.py` - Get workflow logs examples (sync + async)

Requirements:
- Follow same patterns as previous examples
- MANDATORY: Environment variable validation at function start
- MANDATORY: Code minimalism principles
- Include both sync and async examples
- Handle log retrieval with filtering
- Include proper error handling
```

#### Step 32: Test Log Examples
**Prompt:**
```
Test the log examples created in Step 31:

1. **Run Log Examples**:
   ```bash
   cd examples/workflow/log/
   python get_workflow_logs.py
   ```

Requirements:
- All log examples must work correctly
- Log retrieval should function properly
- Environment variable validation should work
```

#### Step 33: Create Info Examples
**Prompt:**
```
Create application information examples in `examples/workflow/info/`:

1. `get_info.py` - Get info examples (sync + async)
2. `get_parameters.py` - Get parameters examples (sync + async)
3. `get_site.py` - Get site examples (sync + async)

Requirements:
- Follow same patterns as previous examples
- MANDATORY: Environment variable validation at function start
- MANDATORY: Code minimalism principles
- Include both sync and async examples
- Handle info retrieval operations
- Include proper error handling
```

#### Step 34: Test Info Examples
**Prompt:**
```
Test the info examples created in Step 33:

1. **Run Info Examples**:
   ```bash
   cd examples/workflow/info/
   python get_info.py
   python get_parameters.py
   python get_site.py
   ```

Requirements:
- All info examples must work correctly
- Info retrieval should function properly
- Environment variable validation should work
```

### Phase 9: Integration Testing

#### Step 35: Comprehensive Integration Testing
**Prompt:**
```
Create comprehensive end-to-end integration tests for all workflow resources:

Create `tests/workflow/v1/integration/test_workflow_api_integration.py`:

Test scenarios:
1. **Complete Workflow Lifecycle**:
   - Run workflow with streaming
   - Get workflow run details
   - Stop workflow execution
   - Run specific workflow version

2. **File Management**:
   - Upload files for workflow input
   - Preview uploaded files
   - Verify file handling in workflows

3. **Workflow Monitoring**:
   - Get workflow execution logs
   - Filter logs by status and user
   - Monitor workflow performance

4. **Application Configuration**:
   - Get application info
   - Get workflow parameters
   - Get site configuration

5. **Error Scenarios**:
   - Invalid API keys
   - Missing required fields
   - Network errors
   - Permission errors

Requirements:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use realistic test data and scenarios
- Mock all API calls with proper responses
- Test error scenarios and edge cases
- Ensure all 10 APIs work together correctly
- Test both sync and async operations
```

#### Step 36: Final Quality Assurance
**Prompt:**
```
Perform final quality assurance and create comprehensive validation.

Tasks:
1. Run all tests and ensure 100% pass rate
2. Verify code coverage meets project standards (>90%)
3. Validate all 10 workflow APIs are fully functional
4. Test integration with existing dify-oapi modules
5. Perform code review checklist:
   - Type hints are comprehensive and correct
   - Error handling is consistent across all resources
   - Builder patterns work correctly for all models
   - Async/sync parity is maintained
   - All Response classes inherit from BaseResponse
   - Literal types are used for type safety
   - Documentation is complete and accurate

Create a final validation report confirming all requirements are met and all workflow APIs are production-ready.

Commands to run for validation:
```bash
# Full test suite
poetry run pytest tests/workflow/v1/model/test_workflow_models.py -v
poetry run pytest tests/workflow/v1/resource/ -v
poetry run pytest tests/workflow/v1/integration/ -v

# Code quality checks
poetry run ruff check dify_oapi/api/workflow/v1/model/
poetry run ruff format dify_oapi/api/workflow/v1/model/
poetry run mypy dify_oapi/api/workflow/v1/model/

# Example validation
cd examples/workflow/
find . -name "*.py" -exec python {} \;
```

Requirements:
- Document any breaking changes from existing implementations
- Provide clear integration paths with existing workflow module
- Ensure all code follows project conventions
- Verify all examples work correctly
- Confirm comprehensive test coverage
- Validate all 10 APIs function correctly
```

## Success Criteria

Each step should meet the following criteria:
- ✅ All code follows existing project patterns and conventions
- ✅ Comprehensive type hints and Pydantic validation
- ✅ Both sync and async method variants implemented
- ✅ Builder pattern support for all request models and public classes
- ✅ Proper error handling and HTTP status code mapping
- ✅ Unit tests with good coverage (>90%)
- ✅ Integration tests with mock API responses
- ✅ Documentation and examples provided
- ✅ **CRITICAL**: All Response classes MUST inherit from BaseResponse (ZERO TOLERANCE)
- ✅ **CRITICAL**: All fields with predefined values MUST use Literal types (ZERO TOLERANCE)
- ✅ **Test typing requirements**: All test method parameters and return types must include proper type annotations
- ✅ **Environment variable validation**: All examples must validate required environment variables and raise errors
- ✅ **Code minimalism**: All examples follow minimal code principles while maintaining functionality

## API Coverage Summary

### Workflow Management APIs (4 APIs)
1. POST /v1/workflows/run - Execute workflow
2. POST /v1/workflows/:workflow_id/run - Execute specific version workflow
3. GET /v1/workflows/run/:workflow_run_id - Get workflow execution details
4. POST /v1/workflows/tasks/:task_id/stop - Stop workflow execution

### File Management APIs (2 APIs)
5. POST /v1/files/upload - Upload files for multimodal support
6. GET /v1/files/:file_id/preview - Preview or download uploaded files

### Log Management APIs (1 API)
7. GET /v1/workflows/logs - Get workflow execution logs

### Application Information APIs (3 APIs)
8. GET /v1/info - Get application basic information
9. GET /v1/parameters - Get application parameters
10. GET /v1/site - Get WebApp settings

## Code Style Rules (MANDATORY - NO EXCEPTIONS)

### Response Model Inheritance (CRITICAL - ZERO TOLERANCE)
**MANDATORY RULE**: Every single Response class in the workflow module MUST inherit from `BaseResponse`
- **Rationale**: Ensures all API responses have consistent error handling capabilities
- **Properties Provided**: `success`, `code`, `msg`, `raw` for comprehensive error management
- **Zero Exceptions**: No Response class may inherit directly from `pydantic.BaseModel`
- **Validation**: All examples and tests must check `response.success` before accessing data
- **Implementation**: Use `from dify_oapi.core.model.base_response import BaseResponse`

### Strict Type Safety Rules (MANDATORY - ZERO TOLERANCE)
**MANDATORY RULE**: Every field that has predefined values MUST use Literal types for type safety
- **Rationale**: Ensures compile-time validation and prevents invalid values
- **Implementation**: Use `from typing import Literal` and define type aliases in `workflow_types.py`
- **Zero Exceptions**: No field with predefined values may use generic `str` type
- **Validation**: IDE and type checkers will catch invalid values at development time

### Public Class Builder Pattern Rules (MANDATORY)
**All public classes MUST implement builder patterns for consistency and usability**
- **Target Classes**: All public/common classes that inherit from `pydantic.BaseModel`
- **Examples**: `WorkflowRunInfo`, `FileInfo`, `LogInfo`, `AppInfo`, `ParametersInfo`, etc.
- **Exclusions**: Request, RequestBody, and Response classes (which have their own builder rules)

### Environment Variable Validation (MANDATORY)
**All examples MUST validate required environment variables and raise errors**
- **Validation Rule**: Check for required environment variables at the start of each function
- **Error Handling**: Raise `ValueError` with descriptive message if required variables are missing
- **No Print Fallbacks**: NEVER use `print()` statements for missing environment variables
- **Required Variables**: All examples must validate `API_KEY`, resource-specific examples must validate resource IDs
- **Validation Order**: ALL environment variable validations MUST be placed at the very beginning of each function

### Code Minimalism Strategy (MANDATORY)
**All examples follow minimal code principles while maintaining functionality**
- **Objective**: Write only the ABSOLUTE MINIMAL amount of code needed to demonstrate each API correctly
- **Avoid Verbose Implementations**: Remove any code that doesn't directly contribute to the core demonstration
- **Simplify Output**: Reduce verbose logging and status messages to essential information only
- **Remove Redundant Functions**: Eliminate multiple similar functions that don't add educational value
- **Maintain Core Functionality**: Ensure all essential features and safety checks remain intact

#### Minimalism Principles:
1. **Concise Variable Initialization**: Combine client and request option creation where possible
2. **Simplified Output Messages**: Replace verbose success messages with concise status indicators
3. **Reduced Function Count**: Remove redundant demonstration functions, keep only sync/async pairs
4. **Streamlined Error Handling**: Maintain essential error handling without verbose explanations
5. **Essential Comments Only**: Remove explanatory comments that don't add technical value
6. **Consistent Patterns**: Apply the same minimization approach across all resource examples

#### Safety Features:
- Environment variable validation at function start
- "[Example]" prefix checking for delete operations
- Basic error handling with try-catch blocks
- Resource existence verification before operations
- Consistent API key and resource ID validation

## Latest Improvements and Optimizations

### 1. Enhanced Streaming Support
**Recent Updates**:
- **Real-time Processing**: Improved streaming response handling for workflow execution
- **Event Management**: Better handling of workflow events (workflow_started, node_started, text_chunk, node_finished, workflow_finished)
- **Connection Management**: Better connection lifecycle management for streaming operations
- **Error Recovery**: Enhanced error handling and recovery mechanisms for streaming failures
- **Performance Optimization**: Reduced latency and improved throughput for streaming responses

### 2. Advanced File Processing
**Implementation Enhancements**:
- **Multi-format Support**: Enhanced support for various file formats (documents, images, audio, video, custom)
- **File Validation**: Improved file type and size validation mechanisms
- **Upload Optimization**: Streamlined file upload process with better error handling
- **Preview Capabilities**: Advanced file preview and download functionality
- **Metadata Extraction**: Automatic metadata extraction from uploaded files

### 3. Workflow Execution Intelligence
**Latest Features**:
- **Node Tracking**: Comprehensive node execution tracking and monitoring
- **Execution Analytics**: Advanced analytics for workflow execution performance
- **Error Diagnostics**: Enhanced error diagnostics and troubleshooting capabilities
- **Resource Management**: Intelligent resource allocation and management for workflow execution
- **Automated Insights**: AI-powered insights from workflow execution data

### 4. Logging and Monitoring
**Recent Improvements**:
- **Comprehensive Logging**: Detailed logging of workflow execution steps and events
- **Performance Metrics**: Advanced performance metrics and monitoring capabilities
- **Search and Filter**: Enhanced search and filtering capabilities for workflow logs
- **Real-time Monitoring**: Real-time monitoring of workflow execution status
- **Historical Analysis**: Historical analysis and trend identification for workflow performance

### 5. Application Configuration
**Configuration Enhancements**:
- **Dynamic Settings**: Real-time application configuration updates
- **User Preferences**: Enhanced user preference management
- **Theme Customization**: Advanced theme and UI customization options
- **Feature Toggles**: Flexible feature toggle system for application functionality
- **Multi-language Support**: Enhanced multi-language support for global applications

### 6. Workflow Intelligence
**Smart Workflow Features**:
- **Auto-optimization**: AI-powered workflow optimization suggestions
- **Context Awareness**: Context-aware workflow execution and recommendations
- **Batch Operations**: Efficient batch workflow processing capabilities
- **Quality Scoring**: Automatic quality scoring for workflow outputs
- **Performance Tuning**: Intelligent performance tuning and optimization

### 7. Enhanced Type Safety
**Type System Improvements**:
- **Comprehensive Literal Types**: Complete coverage of all predefined values with Literal types
- **Advanced Type Validation**: Enhanced compile-time type checking and validation
- **Better IDE Support**: Improved auto-completion and error highlighting in IDEs
- **Type-safe Refactoring**: Enhanced support for type-safe code refactoring
- **Documentation Integration**: Better integration of type information with documentation

### 8. Performance Optimizations
**Implementation Enhancements**:
- **Reduced Memory Footprint**: Optimized model instantiation and data handling
- **Faster Request Processing**: Streamlined request building and validation
- **Improved Async Support**: Enhanced asynchronous operation handling
- **Better Resource Management**: Optimized resource allocation and cleanup
- **Caching Mechanisms**: Intelligent caching for frequently accessed data

### 9. Developer Experience Improvements
**Latest Features**:
- **Enhanced Builder Patterns**: More intuitive and powerful builder pattern implementations
- **Improved Error Messages**: More descriptive error messages for debugging
- **Better Documentation**: Enhanced inline documentation and examples
- **Simplified API Usage**: More intuitive method signatures and parameter handling
- **Interactive Examples**: More practical, real-world usage examples

### 10. Testing and Quality Assurance
**Recent Enhancements**:
- **Comprehensive Test Coverage**: Expanded test suite covering all edge cases and scenarios
- **Performance Testing**: Added performance benchmarks and optimization tests
- **Integration Testing**: Enhanced integration tests with real API scenarios
- **Code Quality Metrics**: Improved code quality monitoring and enforcement
- **Automated Validation**: Enhanced automated validation and testing pipelines

## Summary

This comprehensive plan provides step-by-step prompts for implementing all 10 workflow APIs with proper testing, documentation, and examples. Each step builds upon the previous ones and includes specific requirements to ensure code quality and consistency with the existing dify-oapi architecture.

The modular resource-based organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for workflow operations including workflow execution, file management, execution monitoring, logging, and application configuration.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage. The code minimalism approach optimizes all examples for clarity while maintaining full functionality and safety features.

### Key Features
- **Code Minimalism**: All workflow examples follow minimal code principles
- **Improved Readability**: Simplified output messages and reduced verbose logging
- **Maintained Safety**: All safety features and validation remain intact
- **Consistent Patterns**: Uniform minimization approach across all 10 API examples
- **Educational Focus**: Examples focus purely on demonstrating API functionality without unnecessary complexity
- **Performance Optimization**: Enhanced streaming, file processing, and workflow execution capabilities
- **Enhanced Type Safety**: Comprehensive Literal types and improved type annotations
- **Better Error Handling**: Robust error propagation and user-friendly error messages
- **Advanced Features**: Support for intelligent workflow execution, comprehensive logging, and dynamic configuration
- **Comprehensive Architecture**: Streamlined model organization and improved builder patterns
- **Developer Experience**: Enhanced IDE support, better documentation, and simplified API usage
- **Quality Assurance**: Comprehensive testing, performance monitoring, and code quality enforcement
- **Streaming Excellence**: Advanced streaming support with comprehensive event handling
- **File Management**: Complete file upload, preview, and management capabilities
- **Execution Monitoring**: Real-time workflow execution monitoring and logging
- **Configuration Management**: Dynamic application configuration and customization options