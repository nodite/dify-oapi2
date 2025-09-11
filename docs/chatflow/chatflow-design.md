# Chatflow API Design Document

## Overview

This document outlines the comprehensive chatflow application functionality in the dify-oapi chatflow module. The implementation supports all 17 chatflow-related APIs covering advanced chat functionality, file management, conversation management, feedback systems, TTS operations, application configuration, and annotation management based on the latest Dify OpenAPI specification.

## Migration Guide from Legacy Code

### 🔄 API Changes Summary

#### **Resource Consolidation**
```python
# OLD: Multiple resources (if existed)
# client.chatflow.v1.chat.send_message()
# client.chatflow.v1.file.upload_file()
# client.chatflow.v1.conversation.get_conversations()
# client.chatflow.v1.feedback.message_feedback()

# NEW: Multi-resource structure
client.chatflow.v1.chatflow.send()         # ✅ Simplified method names
client.chatflow.v1.chatflow.stop()         # ✅ Clear operations
client.chatflow.v1.chatflow.suggested()    # ✅ Concise naming
client.chatflow.v1.file.upload()           # ✅ Direct file operations
client.chatflow.v1.feedback.message()      # ✅ Feedback operations
client.chatflow.v1.feedback.list()         # ✅ Get feedbacks
client.chatflow.v1.conversation.messages() # ✅ Message history
client.chatflow.v1.conversation.list()     # ✅ Conversation list
client.chatflow.v1.conversation.delete()   # ✅ Delete conversation
client.chatflow.v1.conversation.rename()   # ✅ Rename conversation
client.chatflow.v1.conversation.variables() # ✅ Get variables
client.chatflow.v1.tts.speech_to_text()    # ✅ Audio to text
client.chatflow.v1.tts.text_to_audio()     # ✅ Text to audio
client.chatflow.v1.application.info()      # ✅ App info
client.chatflow.v1.application.parameters() # ✅ App parameters
client.chatflow.v1.application.meta()      # ✅ App meta
client.chatflow.v1.application.site()      # ✅ App site settings
client.chatflow.v1.annotation.list()       # ✅ Annotation list
client.chatflow.v1.annotation.create()     # ✅ Create annotation
client.chatflow.v1.annotation.update()     # ✅ Update annotation
client.chatflow.v1.annotation.delete()     # ✅ Delete annotation
client.chatflow.v1.annotation.reply_settings() # ✅ Reply settings
client.chatflow.v1.annotation.reply_status()   # ✅ Reply status
```

#### **Method Name Changes**
| Old Method | New Method | Status |
|------------|------------|--------|
| `send_chat_message()` | `send()` | ✅ Simplified |
| `stop_chat_message()` | `stop()` | ✅ Clear |
| `get_suggested_questions()` | `suggested()` | ✅ Concise |
| `upload_file()` | `upload()` | ✅ Direct |
| `message_feedback()` | `message()` | ✅ Clear |
| `get_app_feedbacks()` | `list()` | ✅ Simple |
| `get_conversation_messages()` | `messages()` | ✅ Direct |
| `get_conversations()` | `list()` | ✅ Simple |
| `delete_conversation()` | `delete()` | ✅ Clear |
| `rename_conversation()` | `rename()` | ✅ Direct |
| `get_conversation_variables()` | `variables()` | ✅ Simple |
| `audio_to_text()` | `speech_to_text()` | ✅ Clear |
| `text_to_audio()` | `text_to_audio()` | ✅ Unchanged |
| `get_info()` | `info()` | ✅ Simple |
| `get_parameters()` | `parameters()` | ✅ Direct |
| `get_meta()` | `meta()` | ✅ Simple |
| `get_site()` | `site()` | ✅ Direct |
| `get_annotations()` | `list()` | ✅ Simple |
| `create_annotation()` | `create()` | ✅ Direct |
| `update_annotation()` | `update()` | ✅ Simple |
| `delete_annotation()` | `delete()` | ✅ Direct |
| `annotation_reply_settings()` | `reply_settings()` | ✅ Clear |
| `annotation_reply_status()` | `reply_status()` | ✅ Simple |

#### **Model Import Changes**
```python
# OLD: Nested imports (if existed)
# from dify_oapi.api.chatflow.v1.model.chatflow.send_request import SendRequest
# from dify_oapi.api.chatflow.v1.model.file.upload_request import UploadRequest

# NEW: Flat imports
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.upload_file_request import UploadFileRequest
```

#### **Response Handling Changes**
```python
# OLD: Direct model access (if existed)
# response = client.chatflow.v1.chatflow.send_chat_message(request, option)
# print(response.message_id)  # Might fail on error

# NEW: BaseResponse with error handling
response = client.chatflow.v1.chatflow.send(request, option)
if response.success:
    print(f"Success: {response.message_id}")
else:
    print(f"Error: {response.msg}")
```

#### **Streaming Changes**
```python
# OLD: Basic streaming (if existed)
# for chunk in client.chatflow.v1.chatflow.send_chat_message(request, option, stream=True):
#     print(chunk)

# NEW: Type-safe streaming with overloads
response = client.chatflow.v1.chatflow.send(request, option, stream=True)
for chunk in response:
    print(chunk, end="", flush=True)
```

### 🛠️ Migration Steps

1. **Update Imports**: Change to flat model imports
2. **Update Method Calls**: Use simplified method names across 7 resources
3. **Add Error Handling**: Check `response.success` before accessing data
4. **Update Type Hints**: Use new response types with BaseResponse
5. **Test Thoroughly**: Validate all chatflow operations work correctly

### ⚠️ Breaking Changes
- Method names simplified (remove redundant prefixes)
- All responses now inherit from BaseResponse
- Model imports use flat structure
- Streaming methods use type-safe overloads
- Multi-resource organization (7 resources instead of single resource)

### ✅ Backward Compatibility
- All core functionality preserved
- Request/response data structures unchanged
- API endpoints remain the same
- Authentication and configuration unchanged

## Current Implementation Status

### 📋 Implementation Required
- **All 17 Chatflow APIs**: Need implementation with sync/async support
- **Streaming Support**: Real-time chat with comprehensive event handling
- **File Upload**: Multipart form-data support for various file types
- **Type Safety**: Strict Literal types for all enum values
- **Builder Patterns**: Consistent builder patterns across all models
- **Error Handling**: BaseResponse inheritance for all response classes
- **Testing**: Comprehensive unit tests for all models and resources
- **Examples**: Complete examples for all 17 APIs with sync/async variants
- **Documentation**: Full API documentation with request/response schemas

### 📁 Target Structure
```
dify_oapi/api/chatflow/v1/
├── model/                    # Flat structure (85+ model files)
│   ├── send_chat_message_request.py
│   ├── send_chat_message_request_body.py
│   ├── send_chat_message_response.py
│   ├── chatflow_types.py     # Strict Literal types
│   └── ... (all other models)
├── resource/
│   ├── chatflow.py          # Chatflow operations (3 APIs)
│   ├── file.py              # File operations (1 API)
│   ├── feedback.py          # Feedback operations (2 APIs)
│   ├── conversation.py      # Conversation operations (5 APIs)
│   ├── tts.py               # TTS operations (2 APIs)
│   ├── application.py       # Application operations (4 APIs)
│   └── annotation.py        # Annotation operations (6 APIs)
└── version.py               # V1 class with all 7 resources
```

### 🧪 Testing Coverage Required
```
tests/chatflow/v1/
├── model/
│   ├── test_chatflow_models.py      # Chatflow API model tests
│   ├── test_file_models.py          # File API model tests
│   ├── test_feedback_models.py      # Feedback API model tests
│   ├── test_conversation_models.py  # Conversation API model tests
│   ├── test_tts_models.py           # TTS API model tests
│   ├── test_application_models.py   # Application API model tests
│   ├── test_annotation_models.py    # Annotation API model tests
│   └── test_chatflow_public_models.py # Public model tests
├── resource/
│   ├── test_chatflow_resource.py    # Chatflow resource tests
│   ├── test_file_resource.py        # File resource tests
│   ├── test_feedback_resource.py    # Feedback resource tests
│   ├── test_conversation_resource.py # Conversation resource tests
│   ├── test_tts_resource.py         # TTS resource tests
│   ├── test_application_resource.py # Application resource tests
│   └── test_annotation_resource.py  # Annotation resource tests
└── integration/                     # Integration tests
```

### 📚 Examples Coverage Required
```
examples/chatflow/
├── chatflow/
│   ├── send_chat_message.py         # Sync + Async + Streaming
│   ├── stop_chat_message.py         # Sync + Async
│   └── get_suggested_questions.py   # Sync + Async
├── file/
│   └── upload_file.py               # Sync + Async
├── feedback/
│   ├── message_feedback.py          # Sync + Async
│   └── get_app_feedbacks.py         # Sync + Async
├── conversation/
│   ├── get_conversation_messages.py # Sync + Async
│   ├── get_conversations.py         # Sync + Async
│   ├── delete_conversation.py       # Sync + Async
│   ├── rename_conversation.py       # Sync + Async
│   └── get_conversation_variables.py # Sync + Async
├── tts/
│   ├── audio_to_text.py             # Sync + Async
│   └── text_to_audio.py             # Sync + Async
├── application/
│   ├── get_info.py                  # Sync + Async
│   ├── get_parameters.py            # Sync + Async
│   ├── get_meta.py                  # Sync + Async
│   └── get_site.py                  # Sync + Async
├── annotation/
│   ├── get_annotations.py           # Sync + Async
│   ├── create_annotation.py         # Sync + Async
│   ├── update_annotation.py         # Sync + Async
│   ├── delete_annotation.py         # Sync + Async
│   ├── annotation_reply_settings.py # Sync + Async
│   └── annotation_reply_status.py   # Sync + Async
└── README.md                        # Usage guide
```

## Design Decisions

### 1. Module Organization
**Decision**: Create new `chatflow/v1/` module structure
- Follow established version-based API organization
- Maintain consistency with existing chat, completion, knowledge, and workflow modules
- Leverage existing infrastructure and patterns

### 2. Resource Structure
**Decision**: Implement chatflow APIs across multiple specialized resources

**Multi-Resource Implementation**:
- `chatflow` - Core chatflow operations (3 APIs)
  - Chat operations: `send()`, `stop()`, `suggested()`
- `file` - File management operations (1 API)
  - File operations: `upload()`
- `feedback` - Feedback operations (2 APIs)
  - Feedback operations: `message()`, `list()`
- `conversation` - Conversation management operations (5 APIs)
  - Conversation operations: `messages()`, `list()`, `delete()`, `rename()`, `variables()`
- `tts` - Text-to-Speech operations (2 APIs)
  - TTS operations: `speech_to_text()`, `text_to_audio()`
- `application` - Application configuration operations (4 APIs)
  - App operations: `info()`, `parameters()`, `meta()`, `site()`
- `annotation` - Annotation management operations (6 APIs)
  - Annotation operations: `list()`, `create()`, `update()`, `delete()`, `reply_settings()`, `reply_status()`

### 3. Response Model Strategy
**Decision**: Dedicated Response models for every API
- Type safety and consistency across all endpoints
- Specific response models for all responses including simple success responses
- Comprehensive IDE support and validation
- All response classes inherit from BaseResponse for error handling

### 4. Nested Object Handling
**Decision**: Independent model class files in flat structure
- Separate model files for all objects regardless of complexity
- Flat model directory structure (no subdirectories)
- Domain-specific class naming to avoid conflicts
- Consistent naming without redundant prefixes

### 5. Method Naming Convention
**Decision**: Simple, concise method names for clarity
- Chatflow operations: `send`, `stop`, `suggested`
- File operations: `upload`
- Feedback operations: `message`, `list`
- Conversation operations: `messages`, `list`, `delete`, `rename`, `variables`
- TTS operations: `speech_to_text`, `text_to_audio`
- Application operations: `info`, `parameters`, `meta`, `site`
- Annotation operations: `list`, `create`, `update`, `delete`, `reply_settings`, `reply_status`

**Naming Rules**:
- Shortest meaningful names possible
- No redundant prefixes (e.g., `send` not `send_chat_message`)
- Underscores only when necessary for clarity
- Async methods use `a` prefix (e.g., `asend`, `astop`, `aupload`)

**Ambiguity Resolution Rules**:
- When multiple operations in the same resource could cause naming ambiguity, use descriptive names
- Get operations use descriptive names when needed for clarity
- Maintain method names concise but unambiguous within the resource context

### 6. Class Naming Conflict Resolution
**Decision**: Domain-specific prefixes for conflicting class names

**Required Naming Patterns for Chatflow Module**:
- **Chat classes**: `Chat*` (e.g., `ChatMessage`, `ChatFile`)
- **File classes**: `File*` (e.g., `FileInfo`, `FileUpload`)
- **Feedback classes**: `Feedback*` (e.g., `FeedbackInfo`, `FeedbackRating`)
- **Conversation classes**: `Conversation*` (e.g., `ConversationInfo`, `ConversationVariable`)
- **TTS classes**: `TTS*` or `Audio*` (e.g., `AudioInfo`, `TTSConfig`)
- **Application classes**: `App*` (e.g., `AppInfo`, `AppParameters`)
- **Annotation classes**: `Annotation*` (e.g., `AnnotationInfo`, `AnnotationReply`)

### 7. Response Model Inheritance Rules (CRITICAL - ZERO TOLERANCE)
**Decision**: ALL Response classes MUST inherit from BaseResponse for error handling

**MANDATORY RULE**: Every single Response class in the chatflow module MUST inherit from `BaseResponse`
- **Rationale**: Ensures all API responses have consistent error handling capabilities
- **Properties Provided**: `success`, `code`, `msg`, `raw` for comprehensive error management
- **Zero Exceptions**: No Response class may inherit directly from `pydantic.BaseModel`

**Correct Response Class Patterns**:
```python
# ✅ CORRECT: Simple response inheriting from BaseResponse
class StopChatMessageResponse(BaseResponse):
    result: str | None = None

# ✅ CORRECT: Response with data using multiple inheritance
class SendChatMessageResponse(ChatMessage, BaseResponse):
    pass

# ❌ WRONG: Direct BaseModel inheritance
class SendChatMessageResponse(BaseModel):  # NEVER DO THIS
    pass
```

### 8. Request/Response Model Code Style Rules (MANDATORY)
**Decision**: Strict adherence to established patterns for consistency across all chatflow APIs

#### Request Model Architecture
**Request Classes**:
- MUST inherit from `BaseRequest` (never from `BaseModel`)
- MUST include `request_body` attribute of type `RequestBody | None` for POST/PATCH/PUT requests
- MUST use `request_body()` method in builder to accept entire RequestBody object
- Builder variables MUST use full descriptive names (e.g., `self._send_chat_message_request`)
- MUST set `http_method` and `uri` in builder constructor
- Path parameters MUST use `self._request.paths["param_name"] = value` pattern
- Query parameters MUST use `self._request.add_query("key", value)` pattern

#### HTTP Method Patterns
**GET Requests** (get_suggested_questions, get_app_feedbacks, get_conversations, etc.):
- No RequestBody file needed
- Use query parameters: `self._request.add_query("key", value)`
- Use path parameters: `self._request.paths["param_name"] = value`

**POST Requests** (send_chat_message, stop_chat_message, upload_file, etc.):
- Require separate RequestBody file
- Use `request_body()` method in Request builder
- RequestBody builder methods set fields directly

**DELETE Requests** (delete_conversation, delete_annotation):
- May require RequestBody file for additional data
- Use path parameters for resource identification

#### Multipart/Form-Data Handling (CRITICAL PATTERN)
**Decision**: Special handling for APIs that require multipart/form-data (file uploads)

**Pattern Requirements**:
- APIs requiring file uploads MUST use multipart/form-data content type
- Request classes MUST support both `files` and `body` fields in BaseRequest
- RequestBody classes MUST use nested data structure pattern for complex form data

#### Class Naming Convention (MANDATORY - ZERO TOLERANCE)
**Universal Naming Pattern**:
- File names determine class names exactly (e.g., `send_chat_message_request.py` → `SendChatMessageRequest`)
- Each class has corresponding Builder (e.g., `SendChatMessageRequest` + `SendChatMessageRequestBuilder`)
- Pattern applies to all model types: Request, RequestBody, Response

**STRICT Naming Rules (NO EXCEPTIONS)**:
- Remove ALL module/domain prefixes from class names
- Class names MUST match file names exactly (case-sensitive)
- Apply uniformly across ALL resources
- Use operation-based names: `SendChatMessageRequest`, `GetInfoResponse`, `UploadFileRequestBody`
- NEVER use domain-specific names: `ChatflowSendChatMessageRequest`
- NO legacy naming patterns allowed
- Consistent across all HTTP methods and operation types

### 9. Strict Type Safety Rules (MANDATORY - ZERO TOLERANCE)
**Decision**: ALL API fields MUST use strict typing with Literal types instead of generic strings

**MANDATORY RULE**: Every field that has predefined values MUST use Literal types for type safety

**Strict Type Implementation Pattern**:
```python
# chatflow_types.py - Define all Literal types
from typing import Literal

# Response mode types
ResponseMode = Literal["streaming", "blocking"]

# File types
FileType = Literal["document", "image", "audio", "video", "custom"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Stream event types
StreamEvent = Literal["message", "message_file", "message_end", "tts_message", "tts_message_end", "message_replace", "workflow_started", "node_started", "node_finished", "workflow_finished", "error", "ping"]

# Conversation status types
ConversationStatus = Literal["normal", "archived"]

# Variable value types
VariableValueType = Literal["string", "number", "select"]

# Form input types
FormInputType = Literal["text-input", "paragraph", "select"]

# Job status types
JobStatus = Literal["waiting", "running", "completed", "failed"]

# Audio formats
AudioFormat = Literal["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]

# Language codes
LanguageCode = Literal["en", "zh", "ja", "ko", "es", "fr", "de", "it", "pt", "ru"]

# Chat color theme types
ChatColorTheme = Literal["blue", "green", "purple", "orange", "red"]

# Default language types
DefaultLanguage = Literal["en-US", "zh-Hans", "zh-Hant", "ja-JP", "ko-KR", "es-ES", "fr-FR", "de-DE", "it-IT", "pt-BR", "ru-RU"]

# Message file belongs to types
MessageFileBelongsTo = Literal["user", "assistant"]

# Feedback rating types
FeedbackRating = Literal["like", "dislike"]

# Sort by types
SortBy = Literal["created_at", "-created_at", "updated_at", "-updated_at"]

# Icon types
IconType = Literal["emoji", "image"]

# AutoPlay types
AutoPlay = Literal["enabled", "disabled"]

# Action types
AnnotationAction = Literal["enable", "disable"]

# Node status types
NodeStatus = Literal["running", "succeeded", "failed", "stopped"]

# Workflow status types
WorkflowStatus = Literal["running", "succeeded", "failed", "stopped"]
```

### 10. Public Class Builder Pattern Rules (MANDATORY)
**Decision**: All public classes MUST implement builder patterns for consistency and usability

#### Builder Pattern Implementation Requirements
**Scope**: All public/common classes that inherit from `pydantic.BaseModel`
- **Target Classes**: `ChatMessage`, `FileInfo`, `ConversationInfo`, `FeedbackInfo`, `AppInfo`, `AnnotationInfo`, and all other public model classes
- **Exclusions**: Request, RequestBody, and Response classes (which have their own builder rules)

### 11. File Organization Strategy
**Decision**: Different organization strategies for models vs resources

#### Model Organization: Flat Structure
**Models use flat structure without grouping**:
```
model/
├── send_chat_message_request.py
├── send_chat_message_request_body.py
├── send_chat_message_response.py
├── upload_file_request.py
├── chatflow_types.py
└── [all other model files in flat structure]
```

#### Resource Organization: Functional Grouping
**Resources are grouped by functionality**:
```
resource/
├── chatflow.py      # Chatflow operations
├── file.py          # File operations
├── feedback.py      # Feedback operations
├── conversation.py  # Conversation operations
├── tts.py           # TTS operations
├── application.py   # Application operations
└── annotation.py    # Annotation operations
```

#### __init__.py File Policy (MANDATORY)
**Decision**: ALL `__init__.py` files MUST remain empty for clean module structure

**STRICT RULE**: Every `__init__.py` file in the project MUST be empty
- **Rationale**: Maintains clean module structure and avoids import complexity
- **Scope**: Applies to ALL modules including api/, model/, resource/, tests/, examples/
- **Zero Exceptions**: No `__init__.py` file may contain any imports or exports
- **Import Pattern**: Use direct imports from specific modules instead of package-level exports

**Correct Import Patterns**:
```python
# ✅ CORRECT: Direct imports from specific modules
from dify_oapi.api.chatflow.service import ChatflowService
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest

# ❌ WRONG: Package-level imports (requires __init__.py exports)
from dify_oapi.api.chatflow import ChatflowService  # NEVER DO THIS
from dify_oapi.api.chatflow.v1.model import SendChatMessageRequest  # NEVER DO THIS
```

**Rationale**:
- **Models**: Flat structure for easy imports and reduced nesting
- **Resources**: Grouped by domain for logical separation of concerns
- **Clean Modules**: Empty `__init__.py` files prevent import pollution and circular dependencies

## API Implementation Plan

### Chatflow Operations (3 APIs)

#### Chatflow Resource Implementation
1. **POST /chat-messages** → `chatflow.send()` - Send chat message with streaming support
2. **POST /chat-messages/{task_id}/stop** → `chatflow.stop()` - Stop chat message generation
3. **GET /messages/{message_id}/suggested** → `chatflow.suggested()` - Get suggested questions

### File Operations (1 API)

#### File Resource Implementation
1. **POST /files/upload** → `file.upload()` - Upload file for multimodal support

### Feedback Operations (2 APIs)

#### Feedback Resource Implementation
1. **POST /messages/{message_id}/feedbacks** → `feedback.message()` - Provide message feedback
2. **GET /app/feedbacks** → `feedback.list()` - Get application feedbacks

### Conversation Operations (5 APIs)

#### Conversation Resource Implementation
1. **GET /messages** → `conversation.messages()` - Get conversation history messages
2. **GET /conversations** → `conversation.list()` - Get conversations list
3. **DELETE /conversations/{conversation_id}** → `conversation.delete()` - Delete conversation
4. **POST /conversations/{conversation_id}/name** → `conversation.rename()` - Rename conversation
5. **GET /conversations/{conversation_id}/variables** → `conversation.variables()` - Get conversation variables

### TTS Operations (2 APIs)

#### TTS Resource Implementation
1. **POST /audio-to-text** → `tts.speech_to_text()` - Convert audio to text
2. **POST /text-to-audio** → `tts.text_to_audio()` - Convert text to audio

### Application Operations (4 APIs)

#### Application Resource Implementation
1. **GET /info** → `application.info()` - Get application basic information
2. **GET /parameters** → `application.parameters()` - Get application parameters
3. **GET /meta** → `application.meta()` - Get application meta information
4. **GET /site** → `application.site()` - Get application WebApp settings

### Annotation Operations (6 APIs)

#### Annotation Resource Implementation
1. **GET /apps/annotations** → `annotation.list()` - Get annotation list
2. **POST /apps/annotations** → `annotation.create()` - Create annotation
3. **PUT /apps/annotations/{annotation_id}** → `annotation.update()` - Update annotation
4. **DELETE /apps/annotations/{annotation_id}** → `annotation.delete()` - Delete annotation
5. **POST /apps/annotation-reply/{action}** → `annotation.reply_settings()` - Initial annotation reply settings
6. **GET /apps/annotation-reply/{action}/status/{job_id}** → `annotation.reply_status()` - Query annotation reply status

## Technical Implementation Details

### Resource Class Structure
```python
# Example: chatflow resource
class Chatflow:
    def __init__(self, config: Config):
        self.config = config

    @overload
    def send(self, request: SendChatMessageRequest, request_option: RequestOption, stream: Literal[True]) -> Generator[bytes, None, None]: ...
    
    @overload
    def send(self, request: SendChatMessageRequest, request_option: RequestOption, stream: Literal[False] = False) -> SendChatMessageResponse: ...

    def send(self, request: SendChatMessageRequest, request_option: RequestOption, stream: bool = False) -> SendChatMessageResponse | Generator[bytes, None, None]:
        if stream:
            return Transport.execute(self.config, request, stream=True, option=request_option)
        return Transport.execute(self.config, request, unmarshal_as=SendChatMessageResponse, option=request_option)

    async def asend(self, request: SendChatMessageRequest, request_option: RequestOption, stream: bool = False) -> SendChatMessageResponse | AsyncGenerator[bytes, None]:
        if stream:
            return await ATransport.aexecute(self.config, request, stream=True, option=request_option)
        return await ATransport.aexecute(self.config, request, unmarshal_as=SendChatMessageResponse, option=request_option)

# Example: conversation resource
class Conversation:
    def __init__(self, config: Config):
        self.config = config

    def messages(self, request: GetConversationMessagesRequest, request_option: RequestOption) -> GetConversationMessagesResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetConversationMessagesResponse, option=request_option)

    async def amessages(self, request: GetConversationMessagesRequest, request_option: RequestOption) -> GetConversationMessagesResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetConversationMessagesResponse, option=request_option)
```

### Version Integration
**Target Structure**:
```python
class V1:
    def __init__(self, config: Config):
        self.chatflow = Chatflow(config)
        self.file = File(config)
        self.feedback = Feedback(config)
        self.conversation = Conversation(config)
        self.tts = TTS(config)
        self.application = Application(config)
        self.annotation = Annotation(config)
```

**Migration Steps**:
1. **Module Creation**: Create new chatflow module structure with 7 resource classes
2. **API Implementation**: Implement all 17 APIs across the appropriate resource classes
3. **Model Development**: Create all 85+ model files with proper inheritance and builder patterns
4. **Version Integration**: Update V1 class to expose all 7 chatflow resources
5. **Client Integration**: Update main Client class to include ChatflowService
6. **Pattern Consistency**: Ensure all method signatures follow established patterns
7. **Test Implementation**: Implement comprehensive test suite with all test classes
8. **Example Creation**: Create all 17 example files with sync/async variants
9. **Validation**: Validate all APIs work correctly with proper error handling
10. **Documentation**: Update documentation and README files
11. **Quality Assurance**: Run all quality checks and ensure 100% test coverage
12. **Integration Testing**: Perform end-to-end integration testing
13. **Performance Testing**: Validate performance meets requirements
14. **Final Review**: Complete final code review and documentation review

**Integration Steps**:
1. Create `dify_oapi/api/chatflow/service.py`
2. Update `dify_oapi/api/chatflow/__init__.py` to export ChatflowService
3. Update `dify_oapi/api/__init__.py` to include chatflow module
4. Update `dify_oapi/client.py` to include chatflow service
5. Update all relevant import statements
6. Test client integration with all 7 chatflow resources

## Quality Assurance

### Type Safety
- Comprehensive type hints for all models and methods
- Pydantic validation for request/response models
- Builder pattern support for all request models
- Literal types for all predefined values

### Error Handling
- Consistent error response handling across all APIs
- Proper HTTP status code mapping
- Detailed error message propagation

### Testing Strategy
- Unit tests for all resource methods
- Integration tests with mock API responses
- Validation tests for all model classes
- Comprehensive typing hints for all test methods

### Examples Strategy

#### Examples Organization
**Decision**: Resource-based directory structure with API-specific files
- Each resource gets its own directory under `examples/chatflow/`
- Each API gets its own file within the resource directory
- Each file contains both sync and async examples

#### Resource Naming Convention (MANDATORY)
**Decision**: All example resources MUST use "[Example]" prefix for safety
- **Creation Rule**: All resources created in examples MUST have "[Example]" prefix in their names
- **Deletion Rule**: Delete operations MUST only target resources with "[Example]" prefix
- **Safety Measure**: This prevents accidental deletion of production or important resources

#### Code Minimalism Strategy
**Decision**: All examples follow minimal code principles while maintaining functionality
- **Objective**: Write only the ABSOLUTE MINIMAL amount of code needed to demonstrate each API correctly
- **Avoid Verbose Implementations**: Remove any code that doesn't directly contribute to the core demonstration
- **Maintain Core Functionality**: Ensure all essential features and safety checks remain intact

#### Environment Variable Validation (MANDATORY)
**Decision**: All examples MUST validate required environment variables and raise errors
- **Validation Rule**: Check for required environment variables at the start of each function
- **Error Handling**: Raise `ValueError` with descriptive message if required variables are missing
- **Required Variables**: All examples must validate `API_KEY`, resource-specific examples must validate resource IDs

### Complete Code Style Examples

#### POST Request Pattern (with RequestBody)
```python
# send_chat_message_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest
from .send_chat_message_request_body import SendChatMessageRequestBody

class SendChatMessageRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: SendChatMessageRequestBody | None = None

    @staticmethod
    def builder() -> SendChatMessageRequestBuilder:
        return SendChatMessageRequestBuilder()

class SendChatMessageRequestBuilder:
    def __init__(self):
        send_chat_message_request = SendChatMessageRequest()
        send_chat_message_request.http_method = HttpMethod.POST
        send_chat_message_request.uri = "/v1/chat-messages"
        self._send_chat_message_request = send_chat_message_request

    def build(self) -> SendChatMessageRequest:
        return self._send_chat_message_request

    def request_body(self, request_body: SendChatMessageRequestBody) -> SendChatMessageRequestBuilder:
        self._send_chat_message_request.request_body = request_body
        self._send_chat_message_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
```

```python
# send_chat_message_request_body.py
from pydantic import BaseModel
from .chat_file import ChatFile
from .chatflow_types import ResponseMode

class SendChatMessageRequestBody(BaseModel):
    query: str | None = None
    inputs: dict[str, str] | None = None
    response_mode: ResponseMode | None = None
    user: str | None = None
    conversation_id: str | None = None
    files: list[ChatFile] | None = None
    auto_generate_name: bool | None = None

    @staticmethod
    def builder() -> SendChatMessageRequestBodyBuilder:
        return SendChatMessageRequestBodyBuilder()

class SendChatMessageRequestBodyBuilder:
    def __init__(self):
        self._send_chat_message_request_body = SendChatMessageRequestBody()

    def build(self) -> SendChatMessageRequestBody:
        return self._send_chat_message_request_body

    def query(self, query: str) -> SendChatMessageRequestBodyBuilder:
        self._send_chat_message_request_body.query = query
        return self

    def inputs(self, inputs: dict[str, str]) -> SendChatMessageRequestBodyBuilder:
        self._send_chat_message_request_body.inputs = inputs
        return self

    def response_mode(self, response_mode: ResponseMode) -> SendChatMessageRequestBodyBuilder:
        self._send_chat_message_request_body.response_mode = response_mode
        return self

    def user(self, user: str) -> SendChatMessageRequestBodyBuilder:
        self._send_chat_message_request_body.user = user
        return self

    def conversation_id(self, conversation_id: str) -> SendChatMessageRequestBodyBuilder:
        self._send_chat_message_request_body.conversation_id = conversation_id
        return self

    def files(self, files: list[ChatFile]) -> SendChatMessageRequestBodyBuilder:
        self._send_chat_message_request_body.files = files
        return self

    def auto_generate_name(self, auto_generate_name: bool) -> SendChatMessageRequestBodyBuilder:
        self._send_chat_message_request_body.auto_generate_name = auto_generate_name
        return self
```

#### GET Request Pattern (with path parameters)
```python
# get_suggested_questions_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class GetSuggestedQuestionsRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.message_id: str | None = None

    @staticmethod
    def builder() -> GetSuggestedQuestionsRequestBuilder:
        return GetSuggestedQuestionsRequestBuilder()

class GetSuggestedQuestionsRequestBuilder:
    def __init__(self):
        get_suggested_questions_request = GetSuggestedQuestionsRequest()
        get_suggested_questions_request.http_method = HttpMethod.GET
        get_suggested_questions_request.uri = "/v1/messages/:message_id/suggested"
        self._get_suggested_questions_request = get_suggested_questions_request

    def build(self) -> GetSuggestedQuestionsRequest:
        return self._get_suggested_questions_request

    def message_id(self, message_id: str) -> GetSuggestedQuestionsRequestBuilder:
        self._get_suggested_questions_request.message_id = message_id
        self._get_suggested_questions_request.paths["message_id"] = message_id
        return self

    def user(self, user: str) -> GetSuggestedQuestionsRequestBuilder:
        self._get_suggested_questions_request.add_query("user", user)
        return self
```

#### Multipart Form-Data Pattern (file upload)
```python
# upload_file_request.py
from io import BytesIO
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class UploadFileRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.file: BytesIO | None = None
        self.user: str | None = None

    @staticmethod
    def builder() -> UploadFileRequestBuilder:
        return UploadFileRequestBuilder()

class UploadFileRequestBuilder:
    def __init__(self):
        upload_file_request = UploadFileRequest()
        upload_file_request.http_method = HttpMethod.POST
        upload_file_request.uri = "/v1/files/upload"
        self._upload_file_request = upload_file_request

    def build(self) -> UploadFileRequest:
        return self._upload_file_request

    def file(self, file: BytesIO, file_name: str | None = None) -> UploadFileRequestBuilder:
        self._upload_file_request.file = file
        file_name = file_name or "upload"
        self._upload_file_request.files = {"file": (file_name, file)}
        return self

    def user(self, user: str) -> UploadFileRequestBuilder:
        self._upload_file_request.user = user
        self._upload_file_request.body = {"user": user}
        return self
```

### Test File Organization Rules (MANDATORY)
**Decision**: Test files MUST be organized by resource functionality
- **API Operation Grouping**: Organize tests by API operation with dedicated test classes
- **Method Organization**: Within each test class, organize methods by model type (Request, RequestBody, Response)
- **Public Class Separation**: Create separate files for public/common model tests
- **Flat Structure**: All model test files are placed directly in `tests/chatflow/v1/model/` directory
- **Naming Convention**: Use resource-based naming patterns for test files
- **Complete Coverage**: All 17 APIs must have corresponding test classes

### Test Class Organization Pattern
**Within chatflow test files, organize by API operations:**
```python
# test_chatflow_models.py
class TestSendChatMessageModels:
    # Request tests
    def test_request_builder(self): ...
    def test_request_validation(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    def test_request_body_validation(self): ...
    # Response tests
    def test_response_inheritance(self): ...
    def test_response_data_access(self): ...

class TestStopChatMessageModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetSuggestedQuestionsModels:
    # Request tests (GET - no RequestBody)
    def test_request_builder(self): ...
    def test_request_query_parameters(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

```python
# test_file_models.py
class TestUploadFileModels:
    # Request tests
    def test_request_builder(self): ...
    def test_file_upload_handling(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

```python
# test_feedback_models.py
class TestMessageFeedbackModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetAppFeedbacksModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

```python
# test_conversation_models.py
class TestGetConversationMessagesModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetConversationsModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestDeleteConversationModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestRenameConversationModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetConversationVariablesModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

```python
# test_tts_models.py
class TestAudioToTextModels:
    # Request tests
    def test_request_builder(self): ...
    def test_file_upload_handling(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestTextToAudioModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

```python
# test_application_models.py
class TestGetInfoModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetParametersModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetMetaModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetSiteModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

```python
# test_annotation_models.py
class TestGetAnnotationsModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestCreateAnnotationModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestUpdateAnnotationModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestDeleteAnnotationModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestAnnotationReplySettingsModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestAnnotationReplyStatusModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

**Public/Common classes get separate files:**
```python
# test_chatflow_public_models.py
class TestChatMessage:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestChatFile:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestFileInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestConversationInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestFeedbackInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestAppInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestAnnotationInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...
```

### Test Directory Structure
```
tests/chatflow/v1/
├── model/
│   ├── test_chatflow_models.py          # Chatflow API tests (3 test classes)
│   ├── test_file_models.py              # File API tests (1 test class)
│   ├── test_feedback_models.py          # Feedback API tests (2 test classes)
│   ├── test_conversation_models.py      # Conversation API tests (5 test classes)
│   ├── test_tts_models.py               # TTS API tests (2 test classes)
│   ├── test_application_models.py       # Application API tests (4 test classes)
│   ├── test_annotation_models.py        # Annotation API tests (6 test classes)
│   └── test_chatflow_public_models.py   # All public models
├── resource/
│   ├── test_chatflow_resource.py        # Chatflow resource tests
│   ├── test_file_resource.py            # File resource tests
│   ├── test_feedback_resource.py        # Feedback resource tests
│   ├── test_conversation_resource.py    # Conversation resource tests
│   ├── test_tts_resource.py             # TTS resource tests
│   ├── test_application_resource.py     # Application resource tests
│   └── test_annotation_resource.py      # Annotation resource tests
├── integration/
│   ├── test_chatflow_api_integration.py # All 17 chatflow API integration tests
│   ├── test_comprehensive_integration.py
│   ├── test_examples_validation.py
│   └── test_version_integration.py
└── __init__.py
```

## Summary

This design provides a comprehensive solution for chatflow management in dify-oapi, covering all 17 chatflow-related APIs with a clean, maintainable architecture. The implementation prioritizes type safety, consistency, and developer experience while ensuring full compatibility with the latest Dify API specifications.

The multi-resource organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for chatflow operations including advanced chat functionality, file management, conversation management, feedback systems, TTS operations, application configuration, and annotation management.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage. The code minimalism approach optimizes all examples for clarity while maintaining full functionality and safety features.

### Key Features
- **Comprehensive Coverage**: Full implementation of all 17 chatflow APIs with consistent architecture
- **Multi-resource Organization**: Logical separation of concerns across 7 specialized resources
- **Advanced Type Safety**: Strict typing with Literal types for all predefined values
- **Enhanced Chat Processing**: Complete chat message handling with streaming support
- **File Management**: Comprehensive file upload and processing capabilities
- **Conversation Management**: Full conversation lifecycle management
- **Feedback System**: Complete feedback collection and analysis
- **TTS Integration**: Text-to-speech and speech-to-text capabilities
- **Application Configuration**: Comprehensive application settings management
- **Annotation System**: Complete annotation management and reply settings
- **Code Minimalism**: All chatflow examples follow minimal code principles
- **Safety Features**: Comprehensive validation and error handling mechanisms
- **Educational Focus**: Examples focus purely on demonstrating API functionality
- **Consistent Patterns**: Uniform architecture and naming conventions across all resources

### Documentation Consistency Requirements
- **Examples Documentation**: Must be updated to reflect all 17 APIs accurately (3+1+2+5+2+4+6)
- **File Completeness**: All APIs must have corresponding example files
- **Naming Standardization**: Consistent file naming across all example categories
- **README Accuracy**: Examples README must match API documentation specifications
- **Test Structure Consistency**: Test structure must align with final 7-resource API specifications
- **Test Coverage Completeness**: All 17 APIs must have corresponding test files
- **Resource Test Alignment**: Resource tests must match final 7-resource organization
- **Integration Test Coverage**: All APIs must be covered in integration tests

**Total APIs**: 17 endpoints across 7 resources:
- **Chatflow**: 3 APIs (send, stop, suggested)
- **File**: 1 API (upload)
- **Feedback**: 2 APIs (message, list)
- **Conversation**: 5 APIs (messages, list, delete, rename, variables)
- **TTS**: 2 APIs (speech_to_text, text_to_audio)
- **Application**: 4 APIs (info, parameters, meta, site)
- **Annotation**: 6 APIs (list, create, update, delete, reply_settings, reply_status)

### URI and HTTP Method Configuration
**All Chatflow APIs**:
- `POST /v1/chat-messages` → `SendChatMessageRequest`
- `POST /v1/chat-messages/:task_id/stop` → `StopChatMessageRequest`
- `GET /v1/messages/:message_id/suggested` → `GetSuggestedQuestionsRequest`
- `POST /v1/files/upload` → `UploadFileRequest`
- `POST /v1/messages/:message_id/feedbacks` → `MessageFeedbackRequest`
- `GET /v1/app/feedbacks` → `GetAppFeedbacksRequest`
- `GET /v1/messages` → `GetConversationMessagesRequest`
- `GET /v1/conversations` → `GetConversationsRequest`
- `DELETE /v1/conversations/:conversation_id` → `DeleteConversationRequest`
- `POST /v1/conversations/:conversation_id/name` → `RenameConversationRequest`
- `GET /v1/conversations/:conversation_id/variables` → `GetConversationVariablesRequest`
- `POST /v1/audio-to-text` → `AudioToTextRequest`
- `POST /v1/text-to-audio` → `TextToAudioRequest`
- `GET /v1/info` → `GetInfoRequest`
- `GET /v1/parameters` → `GetParametersRequest`
- `GET /v1/meta` → `GetMetaRequest`
- `GET /v1/site` → `GetSiteRequest`
- `GET /v1/apps/annotations` → `GetAnnotationsRequest`
- `POST /v1/apps/annotations` → `CreateAnnotationRequest`
- `PUT /v1/apps/annotations/:annotation_id` → `UpdateAnnotationRequest`
- `DELETE /v1/apps/annotations/:annotation_id` → `DeleteAnnotationRequest`
- `POST /v1/apps/annotation-reply/:action` → `AnnotationReplySettingsRequest`
- `GET /v1/apps/annotation-reply/:action/status/:job_id` → `AnnotationReplyStatusRequest`

### Client Integration Requirements
**Client Class Update**: The main Client class must be updated to include chatflow module

**Current Client Structure**:
```python
class Client:
    def __init__(self, config: Config):
        self.chat = ChatService(config)
        self.completion = CompletionService(config)
        self.knowledge = KnowledgeService(config)
        self.workflow = WorkflowService(config)
        self.dify = DifyService(config)
```

**Target Client Structure**:
```python
class Client:
    def __init__(self, config: Config):
        self.chat = ChatService(config)
        self.completion = CompletionService(config)
        self.knowledge = KnowledgeService(config)
        self.workflow = WorkflowService(config)
        self.chatflow = ChatflowService(config)  # ✅ New chatflow service
        self.dify = DifyService(config)
```

**Service Class Implementation**:
```python
# dify_oapi/api/chatflow/service.py
from dify_oapi.core.model.config import Config
from .v1.version import V1

class ChatflowService:
    def __init__(self, config: Config):
        self.v1 = V1(config)
```

**Implementation Priority**:
1. **Phase 1**: Core chatflow operations (3 APIs) - Essential chat functionality
2. **Phase 2**: File and feedback operations (3 APIs) - Supporting features
3. **Phase 3**: Conversation management (5 APIs) - Advanced chat features
4. **Phase 4**: TTS and application configuration (6 APIs) - Extended functionality

**Quality Assurance Checklist**:
- ✅ All 17 APIs documented with complete request/response schemas
- ✅ Multi-resource architecture with 7 specialized resources
- ✅ Comprehensive type safety with Literal types
- ✅ Complete testing strategy with unit, integration, and example tests
- ✅ Migration guide for smooth transition
- ✅ Examples strategy with minimal code approach
- ✅ Error handling with BaseResponse inheritance
- ✅ Builder patterns for all models
- ✅ Streaming support with type-safe overloads
- ✅ File upload support with multipart/form-data
- ✅ Client integration with ChatflowService
- ✅ Complete URI and HTTP method configuration

### Final Implementation Checklist

#### Core Implementation (MANDATORY)
- [ ] **Module Structure**: Create complete `dify_oapi/api/chatflow/v1/` structure
- [ ] **Model Files**: Implement all 85+ model files with flat structure
- [ ] **Resource Classes**: Implement all 7 resource classes with sync/async methods
- [ ] **Type Safety**: Implement strict Literal types in `chatflow_types.py`
- [ ] **Builder Patterns**: Implement builders for all Request, RequestBody, and public classes
- [ ] **BaseResponse Inheritance**: Ensure ALL Response classes inherit from BaseResponse
- [ ] **Version Integration**: Update V1 class to expose all 7 resources
- [ ] **Client Integration**: Update main Client class to include ChatflowService

#### Quality Assurance (MANDATORY)
- [ ] **Unit Tests**: Implement all model and resource tests (8 test files)
- [ ] **Integration Tests**: Implement comprehensive API integration tests
- [ ] **Example Files**: Create all 17 example files with sync/async variants
- [ ] **Documentation**: Update all README files and documentation
- [ ] **Type Checking**: Ensure MyPy passes with no errors
- [ ] **Code Quality**: Ensure Ruff linting passes with no issues
- [ ] **Test Coverage**: Achieve 100% test coverage for all implemented code

#### Validation Requirements (MANDATORY)
- [ ] **API Completeness**: All 17 APIs implemented and tested
- [ ] **Resource Organization**: All 7 resources properly organized and functional
- [ ] **Error Handling**: All error scenarios properly handled and tested
- [ ] **Streaming Support**: Streaming functionality implemented and tested
- [ ] **File Upload**: Multipart form-data handling implemented and tested
- [ ] **Environment Variables**: All examples validate required environment variables
- [ ] **Safety Features**: All examples use "[Example]" prefix for safety
- [ ] **Performance**: All APIs perform within acceptable latency limits

All APIs follow RESTful conventions with proper HTTP methods, consistent request/response formats, and comprehensive error handling.