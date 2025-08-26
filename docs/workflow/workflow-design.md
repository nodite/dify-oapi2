# Workflow API Design Document

## Overview

This document outlines the design for implementing comprehensive workflow application functionality in the dify-oapi workflow module. The implementation will support all 10 workflow-related APIs covering workflow execution, file management, execution monitoring, and application configuration.

## Design Decisions

### 1. Module Organization
**Decision**: Extend existing `workflow/v1/` module structure
- Continue using the established version-based API organization
- Maintain consistency with existing chat, completion, and knowledge_base modules
- Leverage existing infrastructure and patterns

### 2. Resource Structure
**Decision**: Create comprehensive resource classes within workflow module

**Extended Existing Resources**:
- `workflow` - Extend existing resource with new methods (4 APIs total)

**New Resource Classes**:
- `file` - File upload and management (2 APIs)
- `log` - Workflow execution logs (1 API)
- `info` - Application information and configuration (3 APIs)

### 3. Response Model Strategy
**Decision**: Create dedicated Response models for every API
- Maintain type safety and consistency across all endpoints
- Include specific response models even for simple `{\"result\": \"success\"}` responses
- Ensure comprehensive IDE support and validation

### 4. Nested Object Handling
**Decision**: Define all nested objects as independent model class files within their respective functional domains
- Create separate model files regardless of complexity
- Place models within their respective functional domain directories
- Create domain-specific variants for cross-domain models
- Use consistent naming without domain prefixes

**Model Distribution Strategy**:
- Each functional domain contains its own version of shared models
- Models maintain consistent naming across domains
- Domain-specific customizations are handled through separate variants
- No central `common/` directory - models belong to their primary use domain

### 5. Method Naming Convention
**Decision**: Use descriptive method names for clarity
- Core operations: `run_workflow`, `run_specific_workflow`, `get_workflow_run_detail`, `stop_workflow`
- File operations: `upload_file`, `preview_file`
- Log operations: `get_workflow_logs`
- Info operations: `get_info`, `get_parameters`, `get_site`

### 6. Response Model Inheritance Rules (CRITICAL - ZERO TOLERANCE)
**Decision**: ALL Response classes MUST inherit from BaseResponse for error handling

**MANDATORY RULE**: Every single Response class in the workflow module MUST inherit from `BaseResponse`
- **Rationale**: Ensures all API responses have consistent error handling capabilities
- **Properties Provided**: `success`, `code`, `msg`, `raw` for comprehensive error management
- **Zero Exceptions**: No Response class may inherit directly from `pydantic.BaseModel`
- **Validation**: All examples and tests must check `response.success` before accessing data
- **Implementation**: Use `from dify_oapi.core.model.base_response import BaseResponse`

**Correct Response Class Patterns**:
```python
# ✅ CORRECT: Simple response inheriting from BaseResponse
class StopWorkflowResponse(BaseResponse):
    result: str | None = None

# ✅ CORRECT: Response with data using multiple inheritance
class RunWorkflowResponse(WorkflowRunInfo, BaseResponse):
    pass

# ❌ WRONG: Direct BaseModel inheritance
class RunWorkflowResponse(BaseModel):  # NEVER DO THIS
    pass
```

### 7. Request/Response Model Code Style Rules (MANDATORY)
**Decision**: Strict adherence to established patterns for consistency across all workflow APIs

#### Request Model Architecture
**Request Classes**:
- MUST inherit from `BaseRequest` (never from `BaseModel`)
- MUST include `request_body` attribute of type `RequestBody | None` for POST/PATCH/PUT requests
- MUST use `request_body()` method in builder to accept entire RequestBody object
- Builder variables MUST use full descriptive names (e.g., `self._run_workflow_request`)
- MUST set `http_method` and `uri` in builder constructor
- Path parameters MUST use `self._request.paths[\"param_name\"] = value` pattern
- Query parameters MUST use `self._request.add_query(\"key\", value)` pattern

**RequestBody Separation (For POST/PATCH/PUT requests)**:
- RequestBody MUST be in separate file from Request
- RequestBody MUST inherit from `pydantic.BaseModel`
- RequestBody MUST include its own Builder pattern
- File naming convention: `run_workflow_request.py` and `run_workflow_request_body.py`
- Both Request and RequestBody MUST have Builder classes

#### HTTP Method Patterns
**GET Requests** (get_workflow_run_detail, preview_file, get_workflow_logs, get_info, get_parameters, get_site):
- No RequestBody file needed
- Use query parameters: `self._request.add_query(\"key\", value)`
- Use path parameters: `self._request.paths[\"param_name\"] = value`

**POST Requests** (run_workflow, run_specific_workflow, stop_workflow, upload_file):
- Require separate RequestBody file
- Use `request_body()` method in Request builder
- RequestBody builder methods set fields directly

#### Multipart/Form-Data Handling (CRITICAL PATTERN)
**Decision**: Special handling for APIs that require multipart/form-data (file uploads)

**Pattern Requirements**:
- APIs requiring file uploads MUST use multipart/form-data content type
- Request classes MUST support both `files` and `body` fields in BaseRequest
- RequestBody classes MUST use nested data structure pattern for complex form data
- Builder methods MUST handle file streams and form data separately

**Implementation Pattern**:
```python
# For APIs with file uploads (e.g., upload_file)
class UploadFileRequestBody(BaseModel):
    user: str | None = None
    
    def user(self, user: str) -> UploadFileRequestBodyBuilder:
        self._request_body.user = user
        return self

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

#### Class Naming Convention (MANDATORY - ZERO TOLERANCE)
**Universal Naming Pattern**:
- File names determine class names exactly (e.g., `run_workflow_request.py` → `RunWorkflowRequest`)
- Each class has corresponding Builder (e.g., `RunWorkflowRequest` + `RunWorkflowRequestBuilder`)
- Pattern applies to all model types: Request, RequestBody, Response

**STRICT Naming Rules (NO EXCEPTIONS)**:
- Remove ALL module/domain prefixes from class names
- Class names MUST match file names exactly (case-sensitive)
- Apply uniformly across ALL resources: workflow, file, log, info
- Use operation-based names: `RunWorkflowRequest`, `GetInfoResponse`, `UploadFileRequestBody`
- NEVER use domain-specific names: `WorkflowRunWorkflowRequest`, `WorkflowGetInfoResponse`
- NO legacy naming patterns allowed
- Consistent across all HTTP methods and operation types

#### URI and HTTP Method Configuration
**Workflow APIs**:
- `POST /v1/workflows/run` → `RunWorkflowRequest`
- `POST /v1/workflows/:workflow_id/run` → `RunSpecificWorkflowRequest`
- `GET /v1/workflows/run/:workflow_run_id` → `GetWorkflowRunDetailRequest`
- `POST /v1/workflows/tasks/:task_id/stop` → `StopWorkflowRequest`

**File APIs**:
- `POST /v1/files/upload` → `UploadFileRequest`
- `GET /v1/files/:file_id/preview` → `PreviewFileRequest`

**Log APIs**:
- `GET /v1/workflows/logs` → `GetWorkflowLogsRequest`

**Info APIs**:
- `GET /v1/info` → `GetInfoRequest`
- `GET /v1/parameters` → `GetParametersRequest`
- `GET /v1/site` → `GetSiteRequest`

#### Public Class Inheritance Rules (CRITICAL)
**Public/Common Classes**:
- Public classes (WorkflowRunInfo, FileInfo, LogInfo, etc.) MUST inherit from `pydantic.BaseModel` ONLY
- Public classes MUST NOT inherit from `BaseResponse`
- Public classes MUST have Builder patterns for consistency and ease of use
- Public classes are reusable components that can be used across different contexts

**Response Classes (MANDATORY - ZERO TOLERANCE)**:
- ALL Response classes MUST inherit from `BaseResponse` for error handling capabilities
- Response classes MAY use multiple inheritance when they need to include public class data
- Pattern: `class RunWorkflowResponse(WorkflowRunInfo, BaseResponse):`
- This allows response classes to have both data fields and error handling capabilities
- Response classes MUST NOT have Builder patterns (unlike Request classes)
- **CRITICAL**: NEVER inherit from `pydantic.BaseModel` directly - ALWAYS use `BaseResponse`

### 8. Strict Type Safety Rules (MANDATORY - ZERO TOLERANCE)
**Decision**: ALL API fields MUST use strict typing with Literal types instead of generic strings

**MANDATORY RULE**: Every field that has predefined values MUST use Literal types for type safety
- **Rationale**: Ensures compile-time validation and prevents invalid values
- **Implementation**: Use `from typing import Literal` and define type aliases
- **Zero Exceptions**: No field with predefined values may use generic `str` type
- **Validation**: IDE and type checkers will catch invalid values at development time

**Strict Type Implementation Pattern**:
```python
# workflow_types.py - Define all Literal types
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

**Model Usage Pattern**:
```python
# Use Literal types in models
from .workflow_types import ResponseMode, FileType

class RunWorkflowRequestBody(BaseModel):
    response_mode: ResponseMode | None = None
    # NOT: response_mode: str | None = None
```

**Structured Input Objects (MANDATORY)**:
- Replace generic `dict[str, Any]` with structured classes
- Create dedicated input classes with builder patterns
- Provide type safety for complex nested objects

**Example - Structured Inputs**:
```python
# workflow_inputs.py
class WorkflowInputs(BaseModel):
    # Dynamic inputs based on workflow configuration
    # Can contain any key-value pairs defined by the workflow
    
    @staticmethod
    def builder() -> WorkflowInputsBuilder:
        return WorkflowInputsBuilder()

# Usage in RequestBody
class RunWorkflowRequestBody(BaseModel):
    inputs: WorkflowInputs | None = None
    # NOT: inputs: dict[str, Any] | None = None
```

**Strict Type Coverage**:
- **Response Modes**: `"streaming"` | `"blocking"`
- **File Types**: `"document"` | `"image"` | `"audio"` | `"video"` | `"custom"`
- **Transfer Methods**: `"remote_url"` | `"local_file"`
- **Workflow Status**: `"running"` | `"succeeded"` | `"failed"` | `"stopped"`
- **Event Types**: `"workflow_started"` | `"node_started"` | `"text_chunk"` | `"node_finished"` | `"workflow_finished"` | `"tts_message"` | `"tts_message_end"` | `"ping"`
- **Icon Types**: `"emoji"` | `"image"`
- **App Modes**: `"workflow"`
- **Log Status**: `"succeeded"` | `"failed"` | `"stopped"`

**Benefits of Strict Typing**:
- **Compile-time Validation**: Catch invalid values during development
- **IDE Support**: Auto-completion and error highlighting
- **Documentation**: Self-documenting code with clear valid values
- **Refactoring Safety**: Type-safe refactoring across the codebase
- **API Consistency**: Ensures consistent usage of predefined values

### 9. Public Class Builder Pattern Rules (MANDATORY)
**Decision**: All public classes MUST implement builder patterns for consistency and usability

#### Builder Pattern Implementation Requirements
**Scope**: All public/common classes that inherit from `pydantic.BaseModel`
- **Target Classes**: `WorkflowRunInfo`, `FileInfo`, `LogInfo`, `AppInfo`, `ParametersInfo`, `SiteInfo`, `UserInputForm`, `FileUploadConfig`, `SystemParameters`, `NodeInfo`, `ExecutionMetadata`, and all other public model classes
- **Exclusions**: Request, RequestBody, and Response classes (which have their own builder rules)

#### Implementation Pattern
**Standard Builder Structure**:
```python
class PublicClass(BaseModel):
    field1: str | None = None
    field2: int | None = None
    # ... other fields
    
    @staticmethod
    def builder() -> PublicClassBuilder:
        return PublicClassBuilder()

class PublicClassBuilder:
    def __init__(self):
        self._public_class = PublicClass()
    
    def build(self) -> PublicClass:
        return self._public_class
    
    def field1(self, field1: str) -> PublicClassBuilder:
        self._public_class.field1 = field1
        return self
    
    def field2(self, field2: int) -> PublicClassBuilder:
        self._public_class.field2 = field2
        return self
```

### 10. Model File Organization
**Decision**: Organize models by resource grouping with shared common models

```
model/
├── workflow/        # Core workflow functionality
│   ├── run_workflow_request.py
│   ├── run_workflow_request_body.py
│   ├── run_workflow_response.py
│   ├── run_specific_workflow_request.py
│   ├── run_specific_workflow_request_body.py
│   ├── run_specific_workflow_response.py
│   ├── get_workflow_run_detail_request.py
│   ├── get_workflow_run_detail_response.py
│   ├── stop_workflow_request.py
│   ├── stop_workflow_request_body.py
│   ├── stop_workflow_response.py
│   ├── workflow_run_info.py
│   ├── workflow_inputs.py
│   ├── node_info.py
│   ├── execution_metadata.py
│   └── streaming_event.py
├── file/            # File management
│   ├── upload_file_request.py
│   ├── upload_file_request_body.py
│   ├── upload_file_response.py
│   ├── preview_file_request.py
│   ├── preview_file_response.py
│   └── file_info.py
├── log/             # Workflow logs
│   ├── get_workflow_logs_request.py
│   ├── get_workflow_logs_response.py
│   ├── log_info.py
│   └── end_user_info.py
└── info/            # Application information
    ├── get_info_request.py
    ├── get_info_response.py
    ├── get_parameters_request.py
    ├── get_parameters_response.py
    ├── get_site_request.py
    ├── get_site_response.py
    ├── app_info.py
    ├── parameters_info.py
    ├── site_info.py
    ├── user_input_form.py
    ├── file_upload_config.py
    └── system_parameters.py
```

## API Implementation Plan

### Workflow Management APIs (4 APIs)

#### Core Workflow Operations
1. **POST /workflows/run** → `workflow.run_workflow()` - Execute workflow
2. **POST /workflows/:workflow_id/run** → `workflow.run_specific_workflow()` - Execute specific version workflow
3. **GET /workflows/run/:workflow_run_id** → `workflow.get_workflow_run_detail()` - Get workflow execution details
4. **POST /workflows/tasks/:task_id/stop** → `workflow.stop_workflow()` - Stop workflow execution

### File Management APIs (2 APIs)

#### File Upload Operations
5. **POST /files/upload** → `file.upload_file()` - Upload files for multimodal support
6. **GET /files/:file_id/preview** → `file.preview_file()` - Preview or download uploaded files

### Log Management APIs (1 API)

#### Log Operations
7. **GET /workflows/logs** → `log.get_workflow_logs()` - Get workflow execution logs

### Application Information APIs (3 APIs)

#### Info Operations
8. **GET /info** → `info.get_info()` - Get application basic information
9. **GET /parameters** → `info.get_parameters()` - Get application parameters
10. **GET /site** → `info.get_site()` - Get WebApp settings

## Technical Implementation Details

### Resource Class Structure
```python
# Example: workflow resource
class Workflow:
    def __init__(self, config: Config):
        self.config = config

    def run_workflow(self, request: RunWorkflowRequest, request_option: RequestOption, stream: bool = False) -> RunWorkflowResponse | Iterator[str]:
        if stream:
            return Transport.stream(self.config, request, option=request_option)
        return Transport.execute(self.config, request, unmarshal_as=RunWorkflowResponse, option=request_option)

    async def arun_workflow(self, request: RunWorkflowRequest, request_option: RequestOption, stream: bool = False) -> RunWorkflowResponse | AsyncIterator[str]:
        if stream:
            return ATransport.astream(self.config, request, option=request_option)
        return await ATransport.aexecute(self.config, request, unmarshal_as=RunWorkflowResponse, option=request_option)
```

### Complete Code Style Examples

#### POST Request Pattern (with RequestBody)
```python
# run_workflow_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest
from .run_workflow_request_body import RunWorkflowRequestBody

class RunWorkflowRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: RunWorkflowRequestBody | None = None

    @staticmethod
    def builder() -> RunWorkflowRequestBuilder:
        return RunWorkflowRequestBuilder()

class RunWorkflowRequestBuilder:
    def __init__(self):
        run_workflow_request = RunWorkflowRequest()
        run_workflow_request.http_method = HttpMethod.POST
        run_workflow_request.uri = "/v1/workflows/run"
        self._run_workflow_request = run_workflow_request

    def build(self) -> RunWorkflowRequest:
        return self._run_workflow_request

    def request_body(self, request_body: RunWorkflowRequestBody) -> RunWorkflowRequestBuilder:
        self._run_workflow_request.request_body = request_body
        self._run_workflow_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
```

```python
# run_workflow_request_body.py
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from .workflow_inputs import WorkflowInputs
from .file_info import FileInfo
from ..workflow_types import ResponseMode

class RunWorkflowRequestBody(BaseModel):
    inputs: WorkflowInputs | None = None
    response_mode: ResponseMode | None = None
    user: str | None = None
    files: Optional[List[FileInfo]] = None
    trace_id: str | None = None

    @staticmethod
    def builder() -> RunWorkflowRequestBodyBuilder:
        return RunWorkflowRequestBodyBuilder()

class RunWorkflowRequestBodyBuilder:
    def __init__(self):
        self._run_workflow_request_body = RunWorkflowRequestBody()

    def build(self) -> RunWorkflowRequestBody:
        return self._run_workflow_request_body

    def inputs(self, inputs: WorkflowInputs) -> RunWorkflowRequestBodyBuilder:
        self._run_workflow_request_body.inputs = inputs
        return self

    def response_mode(self, response_mode: ResponseMode) -> RunWorkflowRequestBodyBuilder:
        self._run_workflow_request_body.response_mode = response_mode
        return self

    def user(self, user: str) -> RunWorkflowRequestBodyBuilder:
        self._run_workflow_request_body.user = user
        return self

    def files(self, files: List[FileInfo]) -> RunWorkflowRequestBodyBuilder:
        self._run_workflow_request_body.files = files
        return self

    def trace_id(self, trace_id: str) -> RunWorkflowRequestBodyBuilder:
        self._run_workflow_request_body.trace_id = trace_id
        return self
```

#### GET Request Pattern (with path parameters)
```python
# get_workflow_run_detail_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class GetWorkflowRunDetailRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.workflow_run_id: str | None = None

    @staticmethod
    def builder() -> GetWorkflowRunDetailRequestBuilder:
        return GetWorkflowRunDetailRequestBuilder()

class GetWorkflowRunDetailRequestBuilder:
    def __init__(self):
        get_workflow_run_detail_request = GetWorkflowRunDetailRequest()
        get_workflow_run_detail_request.http_method = HttpMethod.GET
        get_workflow_run_detail_request.uri = "/v1/workflows/run/:workflow_run_id"
        self._get_workflow_run_detail_request = get_workflow_run_detail_request

    def build(self) -> GetWorkflowRunDetailRequest:
        return self._get_workflow_run_detail_request

    def workflow_run_id(self, workflow_run_id: str) -> GetWorkflowRunDetailRequestBuilder:
        self._get_workflow_run_detail_request.workflow_run_id = workflow_run_id
        self._get_workflow_run_detail_request.paths["workflow_run_id"] = workflow_run_id
        return self
```

#### GET Request Pattern (with query parameters)
```python
# get_workflow_logs_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class GetWorkflowLogsRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetWorkflowLogsRequestBuilder:
        return GetWorkflowLogsRequestBuilder()

class GetWorkflowLogsRequestBuilder:
    def __init__(self):
        get_workflow_logs_request = GetWorkflowLogsRequest()
        get_workflow_logs_request.http_method = HttpMethod.GET
        get_workflow_logs_request.uri = "/v1/workflows/logs"
        self._get_workflow_logs_request = get_workflow_logs_request

    def build(self) -> GetWorkflowLogsRequest:
        return self._get_workflow_logs_request

    def keyword(self, keyword: str) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("keyword", keyword)
        return self

    def status(self, status: str) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("status", status)
        return self

    def page(self, page: int) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("page", str(page))
        return self

    def limit(self, limit: int) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("limit", str(limit))
        return self

    def created_by_end_user_session_id(self, session_id: str) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("created_by_end_user_session_id", session_id)
        return self

    def created_by_account(self, account: str) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("created_by_account", account)
        return self
```

### Version Integration
Update `v1/version.py` to include new resources:
```python
class V1:
    def __init__(self, config: Config):
        self.workflow = Workflow(config)
        self.file = File(config)           # New
        self.log = Log(config)             # New
        self.info = Info(config)           # New
```

## Quality Assurance

### Type Safety
- Comprehensive type hints for all models and methods
- Pydantic validation for request/response models
- Builder pattern support for all request models
- **Test typing requirements**: All test methods must include proper type annotations for parameters and return types

### Error Handling
- Consistent error response handling across all APIs
- Proper HTTP status code mapping
- Detailed error message propagation

### Testing Strategy
- Unit tests for all resource methods
- Integration tests with mock API responses
- Validation tests for all model classes
- **Comprehensive typing hints**: All test method parameters and return types must include proper type annotations
- **Test File Organization**: All model tests MUST follow flat structure in `tests/workflow/v1/model/` directory
- **Naming Consistency**: Use `test_{resource}_models.py` pattern for all model test files
- **No Nested Directories**: Avoid creating resource-specific test subdirectories

### Test File Organization Rules (MANDATORY)
**Decision**: Test files MUST be organized using mixed approach - by resource type, then by functionality
- **Resource Separation**: Each resource gets its own test file (e.g., `test_workflow_models.py`, `test_file_models.py`)
- **API Operation Grouping**: Within each resource file, organize tests by API operation with dedicated test classes
- **Method Organization**: Within each test class, organize methods by model type (Request, RequestBody, Response)
- **Public Class Separation**: Create separate files for public/common model tests (e.g., `test_workflow_public_models.py`)
- **Flat Structure**: All model test files are placed directly in `tests/workflow/v1/model/` directory
- **Naming Convention**: Use `test_{resource}_models.py` and `test_{resource}_public_models.py` patterns

### Test Class Organization Pattern
**Within each resource test file, organize by API operations:**
```python
# test_workflow_models.py
class TestRunWorkflowModels:
    # Request tests
    def test_request_builder(self): ...
    def test_request_validation(self): ...
    # RequestBody tests  
    def test_request_body_builder(self): ...
    def test_request_body_validation(self): ...
    # Response tests
    def test_response_inheritance(self): ...
    def test_response_data_access(self): ...

class TestRunSpecificWorkflowModels:
    # Request tests
    def test_request_builder(self): ...
    def test_request_validation(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetWorkflowRunDetailModels:
    # Request tests (GET - no RequestBody)
    def test_request_builder(self): ...
    def test_request_path_parameters(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestStopWorkflowModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

**Public/Common classes get separate files:**
```python
# test_workflow_public_models.py
class TestWorkflowRunInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestNodeInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestExecutionMetadata:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...
```

### Test Directory Structure
```
tests/
└── workflow/
    └── v1/
        ├── model/
        │   ├── test_workflow_models.py          # RunWorkflow, RunSpecificWorkflow, GetWorkflowRunDetail, StopWorkflow API tests
        │   ├── test_workflow_public_models.py   # WorkflowRunInfo, NodeInfo, ExecutionMetadata, etc.
        │   ├── test_file_models.py              # UploadFile, PreviewFile API tests
        │   ├── test_file_public_models.py       # FileInfo, etc.
        │   ├── test_log_models.py               # GetWorkflowLogs API tests
        │   ├── test_log_public_models.py        # LogInfo, EndUserInfo, etc.
        │   ├── test_info_models.py              # GetInfo, GetParameters, GetSite API tests
        │   └── test_info_public_models.py       # AppInfo, ParametersInfo, SiteInfo, etc.
        ├── resource/
        │   ├── test_workflow_resource.py
        │   ├── test_file_resource.py
        │   ├── test_log_resource.py
        │   └── test_info_resource.py
        ├── integration/
        │   ├── test_workflow_api_integration.py
        │   ├── test_file_api_integration.py
        │   ├── test_log_api_integration.py
        │   ├── test_info_api_integration.py
        │   ├── test_comprehensive_integration.py
        │   ├── test_examples_validation.py
        │   └── test_version_integration.py
        └── __init__.py
```

## Examples Strategy

### Examples Organization
**Decision**: Resource-based directory structure with API-specific files
- Each resource gets its own directory under `examples/workflow/`
- Each API gets its own file within the resource directory
- Each file contains both sync and async examples
- Basic try-catch error handling for educational purposes

### Resource Naming Convention (MANDATORY)
**Decision**: All example resources MUST use "[Example]" prefix for safety
- **Creation Rule**: All resources created in examples MUST have "[Example]" prefix in their names
- **Deletion Rule**: Delete operations MUST only target resources with "[Example]" prefix
- **Safety Measure**: This prevents accidental deletion of production or important resources
- **Applies to**: Workflow inputs, file names, and any other named resources
- **Examples**:
  - Workflow inputs: `{"query": "[Example] Translate this text"}`, `{"content": "[Example] Summarize this article"}`
  - File names: "[Example] test_document.pdf", "[Example] sample_image.jpg"
- **Cleanup Functions**: Each delete example should include a cleanup function that removes all "[Example]" prefixed resources

### Code Minimalism Strategy
**Decision**: All examples follow minimal code principles while maintaining functionality
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

### Examples Directory Structure
```
examples/workflow/
├── workflow/
│   ├── run_workflow.py              # Run workflow examples (sync + async)
│   ├── run_specific_workflow.py     # Run specific workflow examples (sync + async)
│   ├── get_workflow_run_detail.py   # Get workflow run detail examples (sync + async)
│   └── stop_workflow.py             # Stop workflow examples (sync + async)
├── file/
│   ├── upload_file.py               # Upload file examples (sync + async)
│   └── preview_file.py              # Preview file examples (sync + async)
├── log/
│   └── get_workflow_logs.py         # Get workflow logs examples (sync + async)
├── info/
│   ├── get_info.py                  # Get info examples (sync + async)
│   ├── get_parameters.py            # Get parameters examples (sync + async)
│   └── get_site.py                  # Get site examples (sync + async)
└── README.md                        # Examples overview and usage guide
```

### Environment Variable Validation (MANDATORY)
**Decision**: All examples MUST validate required environment variables and raise errors
- **Validation Rule**: Check for required environment variables at the start of each function
- **Error Handling**: Raise `ValueError` with descriptive message if required variables are missing
- **No Print Fallbacks**: NEVER use `print()` statements for missing environment variables
- **Required Variables**: All examples must validate `API_KEY`, resource-specific examples must validate resource IDs
- **Validation Order**: ALL environment variable validations MUST be placed at the very beginning of each function, immediately after the try block
- **Examples**:
  ```python
  def example_function() -> None:
      try:
          # Check required environment variables (MUST be first)
          api_key = os.getenv("API_KEY")
          if not api_key:
              raise ValueError("API_KEY environment variable is required")

          # Initialize client and other logic after validation
          client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
          # ... rest of function
  ```
- **Consistency**: Apply this pattern to ALL functions in ALL examples
- **Main Function**: Remove environment variable checks from main() functions
- **Zero Tolerance**: This rule applies to ALL workflow examples without exception

### Examples Content Strategy
- **Simple API Calls**: Each example focuses on a single API operation with minimal code
- **Educational Purpose**: Essential functionality demonstration without verbose explanations
- **Dual Versions**: Both synchronous and asynchronous implementations (mandatory)
- **Environment Validation**: All functions validate required environment variables and raise errors
- **Basic Error Handling**: Simple try-catch blocks for common exceptions
- **Real-world Data**: Use realistic but simple test data with "[Example]" prefix
- **Safety First**: All resource creation uses "[Example]" prefix, all deletion checks for this prefix
- **Cleanup Functions**: Delete examples include functions to clean up all example resources
- **Integration Reference**: Examples can serve as integration test references
- **Documentation Support**: Examples complement API documentation with minimal overhead
- **Main README Update**: Always update `examples/README.md` to include new examples with proper categorization and descriptions
- **Code Minimalism**: Follow the principle of writing only essential code that directly demonstrates the API functionality

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

## Summary

This design provides a comprehensive solution for workflow application management in dify-oapi, covering all 10 workflow-related APIs with a clean, maintainable architecture. The implementation prioritizes type safety, consistency, and developer experience while ensuring full compatibility with the latest Dify API specifications.

The modular resource-based organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for workflow operations including workflow execution, file management, execution monitoring, logging, and application configuration.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage. The code minimalism approach optimizes all examples for clarity while maintaining full functionality and safety features.

### Key Features
- **Code Minimalism**: All workflow examples follow minimal code principles
- **Improved Readability**: Simplified output messages and reduced verbose logging
- **Maintained Safety**: All safety features and validation remain intact
- **Consistent Patterns**: Uniform minimization approach across all 10 API examples
- **Educational Focus**: Examples focus purely on demonstrating API functionality without unnecessary complexity
- **Performance Optimization**: Enhanced streaming, file processing, and workflow execution capabilities
- **Enhanced Type Safety**: Improved type annotations and validation mechanisms
- **Better Error Handling**: Robust error propagation and user-friendly error messages
- **Advanced Features**: Support for intelligent workflow execution, comprehensive logging, and dynamic configuration
- **Comprehensive Coverage**: Full implementation of all workflow application APIs with consistent architecture
- **Streaming Excellence**: Advanced streaming support with comprehensive event handling
- **File Management**: Complete file upload, preview, and management capabilities
- **Execution Monitoring**: Real-time workflow execution monitoring and logging
- **Configuration Management**: Dynamic application configuration and customization options