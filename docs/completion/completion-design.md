# Completion API Design Document

## Overview

This document outlines the design for implementing comprehensive text generation application functionality in the dify-oapi completion module. The implementation will support all 15 completion-related APIs covering message generation, file management, feedback systems, audio processing, and application configuration.

## Design Decisions

### 1. Module Organization
**Decision**: Extend existing `completion/v1/` module structure
- Continue using the established version-based API organization
- Maintain consistency with existing chat, knowledge_base, and workflow modules
- Leverage existing infrastructure and patterns

### 2. Resource Structure
**Decision**: Create comprehensive resource classes within completion module

**Extended Existing Resources**:
- `completion` - Extend existing resource with new methods (15 APIs total)

**New Resource Classes**:
- `file` - File upload and management (1 API)
- `feedback` - Message feedback and application feedback management (2 APIs)
- `audio` - Text-to-speech functionality (1 API)
- `info` - Application information and configuration (4 APIs)
- `annotation` - Annotation management and reply settings (7 APIs)

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
- Core operations: `send_message`, `upload_file`, `stop_response`
- Feedback operations: `message_feedback`, `get_feedbacks`
- Audio operations: `text_to_audio`
- Info operations: `get_info`, `get_parameters`, `get_site`
- Annotation operations: `list_annotations`, `create_annotation`, `update_annotation`, `delete_annotation`, `annotation_reply_settings`, `query_annotation_reply_status`

### 6. Response Model Inheritance Rules (CRITICAL - ZERO TOLERANCE)
**Decision**: ALL Response classes MUST inherit from BaseResponse for error handling

**MANDATORY RULE**: Every single Response class in the completion module MUST inherit from `BaseResponse`
- **Rationale**: Ensures all API responses have consistent error handling capabilities
- **Properties Provided**: `success`, `code`, `msg`, `raw` for comprehensive error management
- **Zero Exceptions**: No Response class may inherit directly from `pydantic.BaseModel`
- **Validation**: All examples and tests must check `response.success` before accessing data
- **Implementation**: Use `from dify_oapi.core.model.base_response import BaseResponse`

**Correct Response Class Patterns**:
```python
# ✅ CORRECT: Simple response inheriting from BaseResponse
class StopResponseResponse(BaseResponse):
    result: str | None = None

# ✅ CORRECT: Response with data using multiple inheritance
class SendMessageResponse(CompletionMessageInfo, BaseResponse):
    pass

# ❌ WRONG: Direct BaseModel inheritance
class SendMessageResponse(BaseModel):  # NEVER DO THIS
    pass
```

### 7. Request/Response Model Code Style Rules (MANDATORY)
**Decision**: Strict adherence to established patterns for consistency across all completion APIs

#### Request Model Architecture
**Request Classes**:
- MUST inherit from `BaseRequest` (never from `BaseModel`)
- MUST include `request_body` attribute of type `RequestBody | None` for POST/PATCH/PUT requests
- MUST use `request_body()` method in builder to accept entire RequestBody object
- Builder variables MUST use full descriptive names (e.g., `self._send_message_request`)
- MUST set `http_method` and `uri` in builder constructor
- Path parameters MUST use `self._request.paths[\"param_name\"] = value` pattern
- Query parameters MUST use `self._request.add_query(\"key\", value)` pattern

**RequestBody Separation (For POST/PATCH/PUT requests)**:
- RequestBody MUST be in separate file from Request
- RequestBody MUST inherit from `pydantic.BaseModel`
- RequestBody MUST include its own Builder pattern
- File naming convention: `send_message_request.py` and `send_message_request_body.py`
- Both Request and RequestBody MUST have Builder classes

#### HTTP Method Patterns
**GET Requests** (get_info, get_parameters, get_site, get_feedbacks, list_annotations):
- No RequestBody file needed
- Use query parameters: `self._request.add_query(\"key\", value)`
- Use path parameters: `self._request.paths[\"param_name\"] = value`

**POST Requests** (send_message, upload_file, stop_response, message_feedback, text_to_audio, create_annotation, annotation_reply_settings):
- Require separate RequestBody file
- Use `request_body()` method in Request builder
- RequestBody builder methods set fields directly

**PUT Requests** (update_annotation):
- Require separate RequestBody file
- Support path parameters for resource ID
- Use `request_body()` method in Request builder

**DELETE Requests** (delete_annotation):
- No RequestBody file needed
- Use path parameters for resource ID

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
- File names determine class names exactly (e.g., `send_message_request.py` → `SendMessageRequest`)
- Each class has corresponding Builder (e.g., `SendMessageRequest` + `SendMessageRequestBuilder`)
- Pattern applies to all model types: Request, RequestBody, Response

**STRICT Naming Rules (NO EXCEPTIONS)**:
- Remove ALL module/domain prefixes from class names
- Class names MUST match file names exactly (case-sensitive)
- Apply uniformly across ALL resources: completion, file, feedback, audio, info, annotation
- Use operation-based names: `SendMessageRequest`, `GetInfoResponse`, `UploadFileRequestBody`
- NEVER use domain-specific names: `CompletionSendMessageRequest`, `CompletionGetInfoResponse`
- NO legacy naming patterns allowed
- Consistent across all HTTP methods and operation types

#### URI and HTTP Method Configuration
**Completion APIs**:
- `POST /v1/completion-messages` → `SendMessageRequest`
- `POST /v1/completion-messages/:task_id/stop` → `StopResponseRequest`

**File APIs**:
- `POST /v1/files/upload` → `UploadFileRequest`

**Feedback APIs**:
- `POST /v1/messages/:message_id/feedbacks` → `MessageFeedbackRequest`
- `GET /v1/app/feedbacks` → `GetFeedbacksRequest`

**Audio APIs**:
- `POST /v1/text-to-audio` → `TextToAudioRequest`

**Info APIs**:
- `GET /v1/info` → `GetInfoRequest`
- `GET /v1/parameters` → `GetParametersRequest`
- `GET /v1/site` → `GetSiteRequest`

**Annotation APIs**:
- `GET /v1/apps/annotations` → `ListAnnotationsRequest`
- `POST /v1/apps/annotations` → `CreateAnnotationRequest`
- `PUT /v1/apps/annotations/:annotation_id` → `UpdateAnnotationRequest`
- `DELETE /v1/apps/annotations/:annotation_id` → `DeleteAnnotationRequest`
- `POST /v1/apps/annotation-reply/:action` → `AnnotationReplySettingsRequest`
- `GET /v1/apps/annotation-reply/:action/status/:job_id` → `QueryAnnotationReplyStatusRequest`

#### Public Class Inheritance Rules (CRITICAL)
**Public/Common Classes**:
- Public classes (CompletionMessageInfo, FileInfo, FeedbackInfo, etc.) MUST inherit from `pydantic.BaseModel` ONLY
- Public classes MUST NOT inherit from `BaseResponse`
- Public classes MUST have Builder patterns for consistency and ease of use
- Public classes are reusable components that can be used across different contexts

**Response Classes (MANDATORY - ZERO TOLERANCE)**:
- ALL Response classes MUST inherit from `BaseResponse` for error handling capabilities
- Response classes MAY use multiple inheritance when they need to include public class data
- Pattern: `class SendMessageResponse(CompletionMessageInfo, BaseResponse):`
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
# completion_types.py - Define all Literal types
from typing import Literal

# Response mode types
ResponseMode = Literal["streaming", "blocking"]

# File types
FileType = Literal["image"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Feedback rating types
FeedbackRating = Literal["like", "dislike", "null"]

# Annotation action types
AnnotationAction = Literal["enable", "disable"]

# Icon types
IconType = Literal["emoji", "image"]

# App mode types
AppMode = Literal["completion"]

# Job status types
JobStatus = Literal["waiting", "running", "completed", "failed"]
```

**Model Usage Pattern**:
```python
# Use Literal types in models
from .completion_types import ResponseMode, FileType

class SendMessageRequestBody(BaseModel):
    response_mode: ResponseMode | None = None
    # NOT: response_mode: str | None = None
```

**Structured Input Objects (MANDATORY)**:
- Replace generic `dict[str, Any]` with structured classes
- Create dedicated input classes with builder patterns
- Provide type safety for complex nested objects

**Example - Structured Inputs**:
```python
# completion_inputs.py
class CompletionInputs(BaseModel):
    query: str | None = None  # Required for completion apps
    
    @staticmethod
    def builder() -> CompletionInputsBuilder:
        return CompletionInputsBuilder()

# Usage in RequestBody
class SendMessageRequestBody(BaseModel):
    inputs: CompletionInputs | None = None
    # NOT: inputs: dict[str, Any] | None = None
```

**Strict Type Coverage**:
- **Response Modes**: `"streaming"` | `"blocking"`
- **File Types**: `"image"`
- **Transfer Methods**: `"remote_url"` | `"local_file"`
- **Feedback Ratings**: `"like"` | `"dislike"` | `"null"`
- **Annotation Actions**: `"enable"` | `"disable"`
- **Icon Types**: `"emoji"` | `"image"`
- **App Modes**: `"completion"`
- **Job Status**: `"waiting"` | `"running"` | `"completed"` | `"failed"`

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
- **Target Classes**: `CompletionMessageInfo`, `FileInfo`, `FeedbackInfo`, `AnnotationInfo`, `AppInfo`, `ParametersInfo`, `SiteInfo`, `UserInputForm`, `FileUploadConfig`, `SystemParameters`, and all other public model classes
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
├── completion/       # Core completion functionality
│   ├── send_message_request.py
│   ├── send_message_request_body.py
│   ├── send_message_response.py
│   ├── stop_response_request.py
│   ├── stop_response_request_body.py
│   ├── stop_response_response.py
│   ├── completion_message_info.py
│   ├── usage.py
│   ├── retriever_resource.py
│   └── metadata.py
├── file/            # File management
│   ├── upload_file_request.py
│   ├── upload_file_request_body.py
│   ├── upload_file_response.py
│   └── file_info.py
├── feedback/        # Feedback management
│   ├── message_feedback_request.py
│   ├── message_feedback_request_body.py
│   ├── message_feedback_response.py
│   ├── get_feedbacks_request.py
│   ├── get_feedbacks_response.py
│   └── feedback_info.py
├── audio/           # Audio processing
│   ├── text_to_audio_request.py
│   ├── text_to_audio_request_body.py
│   ├── text_to_audio_response.py
│   └── audio_info.py
├── info/            # Application information
│   ├── get_info_request.py
│   ├── get_info_response.py
│   ├── get_parameters_request.py
│   ├── get_parameters_response.py
│   ├── get_site_request.py
│   ├── get_site_response.py
│   ├── app_info.py
│   ├── parameters_info.py
│   ├── site_info.py
│   ├── user_input_form.py
│   ├── file_upload_config.py
│   └── system_parameters.py
└── annotation/      # Annotation management
    ├── list_annotations_request.py
    ├── list_annotations_response.py
    ├── create_annotation_request.py
    ├── create_annotation_request_body.py
    ├── create_annotation_response.py
    ├── update_annotation_request.py
    ├── update_annotation_request_body.py
    ├── update_annotation_response.py
    ├── delete_annotation_request.py
    ├── delete_annotation_response.py
    ├── annotation_reply_settings_request.py
    ├── annotation_reply_settings_request_body.py
    ├── annotation_reply_settings_response.py
    ├── query_annotation_reply_status_request.py
    ├── query_annotation_reply_status_response.py
    ├── annotation_info.py
    └── job_status_info.py
```

## API Implementation Plan

### Completion Management APIs (2 APIs)

#### Core Message Operations
1. **POST /completion-messages** → `completion.send_message()` - Send completion request
2. **POST /completion-messages/{task_id}/stop** → `completion.stop_response()` - Stop streaming response

### File Management APIs (1 API)

#### File Upload Operations
3. **POST /files/upload** → `file.upload_file()` - Upload files for multimodal support

### Feedback Management APIs (2 APIs)

#### Feedback Operations
4. **POST /messages/{message_id}/feedbacks** → `feedback.message_feedback()` - Submit message feedback
5. **GET /app/feedbacks** → `feedback.get_feedbacks()` - Get application feedbacks

### Audio Processing APIs (1 API)

#### Text-to-Speech Operations
6. **POST /text-to-audio** → `audio.text_to_audio()` - Convert text to speech

### Application Information APIs (3 APIs)

#### Info Operations
7. **GET /info** → `info.get_info()` - Get application basic information
8. **GET /parameters** → `info.get_parameters()` - Get application parameters
9. **GET /site** → `info.get_site()` - Get WebApp settings

### Annotation Management APIs (6 APIs)

#### Annotation CRUD Operations
10. **GET /apps/annotations** → `annotation.list_annotations()` - List annotations
11. **POST /apps/annotations** → `annotation.create_annotation()` - Create annotation
12. **PUT /apps/annotations/{annotation_id}** → `annotation.update_annotation()` - Update annotation
13. **DELETE /apps/annotations/{annotation_id}** → `annotation.delete_annotation()` - Delete annotation

#### Annotation Reply Settings
14. **POST /apps/annotation-reply/{action}** → `annotation.annotation_reply_settings()` - Configure annotation reply
15. **GET /apps/annotation-reply/{action}/status/{job_id}** → `annotation.query_annotation_reply_status()` - Query settings status

## Technical Implementation Details

### Resource Class Structure
```python
# Example: completion resource
class Completion:
    def __init__(self, config: Config):
        self.config = config

    def send_message(self, request: SendMessageRequest, request_option: RequestOption, stream: bool = False) -> SendMessageResponse | Iterator[str]:
        if stream:
            return Transport.stream(self.config, request, option=request_option)
        return Transport.execute(self.config, request, unmarshal_as=SendMessageResponse, option=request_option)

    async def asend_message(self, request: SendMessageRequest, request_option: RequestOption, stream: bool = False) -> SendMessageResponse | AsyncIterator[str]:
        if stream:
            return ATransport.astream(self.config, request, option=request_option)
        return await ATransport.aexecute(self.config, request, unmarshal_as=SendMessageResponse, option=request_option)
```

### Complete Code Style Examples

#### POST Request Pattern (with RequestBody)
```python
# send_message_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest
from .send_message_request_body import SendMessageRequestBody

class SendMessageRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: SendMessageRequestBody | None = None

    @staticmethod
    def builder() -> SendMessageRequestBuilder:
        return SendMessageRequestBuilder()

class SendMessageRequestBuilder:
    def __init__(self):
        send_message_request = SendMessageRequest()
        send_message_request.http_method = HttpMethod.POST
        send_message_request.uri = "/v1/completion-messages"
        self._send_message_request = send_message_request

    def build(self) -> SendMessageRequest:
        return self._send_message_request

    def request_body(self, request_body: SendMessageRequestBody) -> SendMessageRequestBuilder:
        self._send_message_request.request_body = request_body
        self._send_message_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
```

```python
# send_message_request_body.py
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from .file_info import FileInfo

class SendMessageRequestBody(BaseModel):
    inputs: Optional[Dict[str, Any]] = None
    query: str | None = None
    response_mode: str | None = None
    user: str | None = None
    files: Optional[List[FileInfo]] = None

    @staticmethod
    def builder() -> SendMessageRequestBodyBuilder:
        return SendMessageRequestBodyBuilder()

class SendMessageRequestBodyBuilder:
    def __init__(self):
        self._send_message_request_body = SendMessageRequestBody()

    def build(self) -> SendMessageRequestBody:
        return self._send_message_request_body

    def inputs(self, inputs: Dict[str, Any]) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.inputs = inputs
        return self

    def query(self, query: str) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.query = query
        return self

    def response_mode(self, response_mode: str) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.response_mode = response_mode
        return self

    def user(self, user: str) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.user = user
        return self

    def files(self, files: List[FileInfo]) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.files = files
        return self
```

#### GET Request Pattern (with query parameters)
```python
# get_feedbacks_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class GetFeedbacksRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetFeedbacksRequestBuilder:
        return GetFeedbacksRequestBuilder()

class GetFeedbacksRequestBuilder:
    def __init__(self):
        get_feedbacks_request = GetFeedbacksRequest()
        get_feedbacks_request.http_method = HttpMethod.GET
        get_feedbacks_request.uri = "/v1/app/feedbacks"
        self._get_feedbacks_request = get_feedbacks_request

    def build(self) -> GetFeedbacksRequest:
        return self._get_feedbacks_request

    def page(self, page: str) -> GetFeedbacksRequestBuilder:
        self._get_feedbacks_request.add_query("page", page)
        return self

    def limit(self, limit: str) -> GetFeedbacksRequestBuilder:
        self._get_feedbacks_request.add_query("limit", limit)
        return self
```

#### DELETE Request Pattern (with path parameters)
```python
# delete_annotation_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class DeleteAnnotationRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.annotation_id: str | None = None

    @staticmethod
    def builder() -> DeleteAnnotationRequestBuilder:
        return DeleteAnnotationRequestBuilder()

class DeleteAnnotationRequestBuilder:
    def __init__(self):
        delete_annotation_request = DeleteAnnotationRequest()
        delete_annotation_request.http_method = HttpMethod.DELETE
        delete_annotation_request.uri = "/v1/apps/annotations/:annotation_id"
        self._delete_annotation_request = delete_annotation_request

    def build(self) -> DeleteAnnotationRequest:
        return self._delete_annotation_request

    def annotation_id(self, annotation_id: str) -> DeleteAnnotationRequestBuilder:
        self._delete_annotation_request.annotation_id = annotation_id
        self._delete_annotation_request.paths["annotation_id"] = annotation_id
        return self
```

### Version Integration
Update `v1/version.py` to include new resources:
```python
class V1:
    def __init__(self, config: Config):
        self.completion = Completion(config)
        self.file = File(config)           # New
        self.feedback = Feedback(config)   # New
        self.audio = Audio(config)         # New
        self.info = Info(config)           # New
        self.annotation = Annotation(config) # New
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
- **Test File Organization**: All model tests MUST follow flat structure in `tests/completion/v1/model/` directory
- **Naming Consistency**: Use `test_{resource}_models.py` pattern for all model test files
- **No Nested Directories**: Avoid creating resource-specific test subdirectories

### Test File Organization Rules (MANDATORY)
**Decision**: Test files MUST be organized using mixed approach - by resource type, then by functionality
- **Resource Separation**: Each resource gets its own test file (e.g., `test_completion_models.py`, `test_file_models.py`)
- **API Operation Grouping**: Within each resource file, organize tests by API operation with dedicated test classes
- **Method Organization**: Within each test class, organize methods by model type (Request, RequestBody, Response)
- **Public Class Separation**: Create separate files for public/common model tests (e.g., `test_completion_public_models.py`)
- **Flat Structure**: All model test files are placed directly in `tests/completion/v1/model/` directory
- **Naming Convention**: Use `test_{resource}_models.py` and `test_{resource}_public_models.py` patterns

### Test Class Organization Pattern
**Within each resource test file, organize by API operations:**
```python
# test_completion_models.py
class TestSendMessageModels:
    # Request tests
    def test_request_builder(self): ...
    def test_request_validation(self): ...
    # RequestBody tests  
    def test_request_body_builder(self): ...
    def test_request_body_validation(self): ...
    # Response tests
    def test_response_inheritance(self): ...
    def test_response_data_access(self): ...

class TestStopResponseModels:
    # Request tests
    def test_request_builder(self): ...
    def test_request_validation(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

**Public/Common classes get separate files:**
```python
# test_completion_public_models.py
class TestCompletionMessageInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestUsage:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...
```

### Test Directory Structure
```
tests/
└── completion/
    └── v1/
        ├── model/
        │   ├── test_completion_models.py        # SendMessage, StopResponse API tests
        │   ├── test_completion_public_models.py # CompletionMessageInfo, Usage, etc.
        │   ├── test_file_models.py              # UploadFile API tests
        │   ├── test_file_public_models.py       # FileInfo, etc.
        │   ├── test_feedback_models.py          # MessageFeedback, GetFeedbacks API tests
        │   ├── test_feedback_public_models.py   # FeedbackInfo, etc.
        │   ├── test_audio_models.py             # TextToAudio API tests
        │   ├── test_audio_public_models.py      # AudioInfo, etc.
        │   ├── test_info_models.py              # GetInfo, GetParameters, GetSite API tests
        │   ├── test_info_public_models.py       # AppInfo, ParametersInfo, SiteInfo, etc.
        │   ├── test_annotation_models.py        # All annotation API tests
        │   └── test_annotation_public_models.py # AnnotationInfo, JobStatusInfo, etc.
        ├── resource/
        │   ├── test_completion_resource.py
        │   ├── test_file_resource.py
        │   ├── test_feedback_resource.py
        │   ├── test_audio_resource.py
        │   ├── test_info_resource.py
        │   └── test_annotation_resource.py
        ├── integration/
        │   ├── test_completion_api_integration.py
        │   ├── test_file_api_integration.py
        │   ├── test_feedback_api_integration.py
        │   ├── test_audio_api_integration.py
        │   ├── test_info_api_integration.py
        │   ├── test_annotation_api_integration.py
        │   ├── test_comprehensive_integration.py
        │   ├── test_examples_validation.py
        │   └── test_version_integration.py
        └── __init__.py
```

## Examples Strategy

### Examples Organization
**Decision**: Resource-based directory structure with API-specific files
- Each resource gets its own directory under `examples/completion/`
- Each API gets its own file within the resource directory
- Each file contains both sync and async examples
- Basic try-catch error handling for educational purposes

### Resource Naming Convention (MANDATORY)
**Decision**: All example resources MUST use "[Example]" prefix for safety
- **Creation Rule**: All resources created in examples MUST have "[Example]" prefix in their names
- **Deletion Rule**: Delete operations MUST only target resources with "[Example]" prefix
- **Safety Measure**: This prevents accidental deletion of production or important resources
- **Applies to**: Messages, annotations, and any other named resources
- **Examples**:
  - Message queries: "[Example] What is AI?", "[Example] Generate summary"
  - Annotation questions: "[Example] How to use API?", "[Example] What is completion?"
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
examples/completion/
├── completion/
│   ├── send_message.py        # Send message examples (sync + async)
│   └── stop_response.py       # Stop response examples (sync + async)
├── file/
│   └── upload_file.py         # Upload file examples (sync + async)
├── feedback/
│   ├── message_feedback.py    # Message feedback examples (sync + async)
│   └── get_feedbacks.py       # Get feedbacks examples (sync + async)
├── audio/
│   └── text_to_audio.py       # Text to audio examples (sync + async)
├── info/
│   ├── get_info.py            # Get info examples (sync + async)
│   ├── get_parameters.py      # Get parameters examples (sync + async)
│   └── get_site.py            # Get site examples (sync + async)
├── annotation/
│   ├── list_annotations.py    # List annotations examples (sync + async)
│   ├── create_annotation.py   # Create annotation examples (sync + async)
│   ├── update_annotation.py   # Update annotation examples (sync + async)
│   ├── delete_annotation.py   # Delete annotation examples (sync + async)
│   ├── annotation_reply_settings.py # Annotation reply settings examples (sync + async)
│   └── query_annotation_reply_status.py # Query status examples (sync + async)
└── README.md                  # Examples overview and usage guide
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
- **Zero Tolerance**: This rule applies to ALL completion examples without exception

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
- **Real-time Processing**: Improved streaming response handling for completion messages
- **Connection Management**: Better connection lifecycle management for streaming operations
- **Error Recovery**: Enhanced error handling and recovery mechanisms for streaming failures
- **Performance Optimization**: Reduced latency and improved throughput for streaming responses

### 2. Advanced File Processing
**Implementation Enhancements**:
- **Multi-format Support**: Enhanced support for various file formats (images, documents, audio)
- **File Validation**: Improved file type and size validation mechanisms
- **Upload Optimization**: Streamlined file upload process with better error handling
- **Metadata Extraction**: Automatic metadata extraction from uploaded files

### 3. Intelligent Feedback Systems
**Latest Features**:
- **Feedback Analytics**: Advanced analytics for message feedback and user interactions
- **Quality Metrics**: Comprehensive quality metrics for completion responses
- **User Behavior Tracking**: Enhanced tracking of user feedback patterns
- **Automated Insights**: AI-powered insights from feedback data

### 4. Audio Processing Enhancements
**Recent Improvements**:
- **Voice Quality**: Improved text-to-speech quality and naturalness
- **Language Support**: Extended language support for audio generation
- **Audio Formats**: Support for multiple audio output formats
- **Streaming Audio**: Real-time audio streaming capabilities

### 5. Application Configuration
**Configuration Enhancements**:
- **Dynamic Settings**: Real-time application configuration updates
- **User Preferences**: Enhanced user preference management
- **Theme Customization**: Advanced theme and UI customization options
- **Feature Toggles**: Flexible feature toggle system for application functionality

### 6. Annotation Intelligence
**Smart Annotation Features**:
- **Auto-suggestions**: AI-powered annotation suggestions
- **Context Awareness**: Context-aware annotation recommendations
- **Batch Operations**: Efficient batch annotation processing
- **Quality Scoring**: Automatic quality scoring for annotations

## Summary

This design provides a comprehensive solution for completion application management in dify-oapi, covering all 15 completion-related APIs with a clean, maintainable architecture. The implementation prioritizes type safety, consistency, and developer experience while ensuring full compatibility with the latest Dify API specifications.

The modular resource-based organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for completion operations including message generation, file management, feedback systems, audio processing, application configuration, and annotation management.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage. The code minimalism approach optimizes all examples for clarity while maintaining full functionality and safety features.

### Key Features
- **Code Minimalism**: All completion examples follow minimal code principles
- **Improved Readability**: Simplified output messages and reduced verbose logging
- **Maintained Safety**: All safety features and validation remain intact
- **Consistent Patterns**: Uniform minimization approach across all 15 API examples
- **Educational Focus**: Examples focus purely on demonstrating API functionality without unnecessary complexity
- **Performance Optimization**: Enhanced streaming, file processing, and audio capabilities
- **Enhanced Type Safety**: Improved type annotations and validation mechanisms
- **Better Error Handling**: Robust error propagation and user-friendly error messages
- **Advanced Features**: Support for intelligent feedback, smart annotations, and dynamic configuration
- **Comprehensive Coverage**: Full implementation of all completion application APIs with consistent architecture