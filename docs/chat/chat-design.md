# Chat API Design Document

## Overview

This document outlines the design for implementing comprehensive chat functionality in the dify-oapi chat module. The implementation will support all 22 chat-related APIs covering chat messages, file management, feedback management, conversation management, audio processing, application information, and annotation management.

## Design Decisions

### 1. Module Organization
**Decision**: Extend existing `chat/v1/` module structure
- Continue using the established version-based API organization
- Maintain consistency with existing completion, knowledge, and workflow modules
- Leverage existing infrastructure and patterns

### 2. Resource Structure
**Decision**: Implement chat APIs across multiple specialized resources

**Multi-Resource Implementation**:
- `chat` - Chat message APIs (3 APIs)
  - Message operations: `chat`, `stop`, `suggested`
- `file` - File management APIs (1 API)
  - File operations: `upload`
- `feedback` - Feedback management APIs (2 APIs)
  - Feedback operations: `submit`, `list`
- `conversation` - Conversation management APIs (5 APIs)
  - Conversation operations: `list`, `delete`, `rename`, `variables`, `history`
- `audio` - Audio processing APIs (2 APIs)
  - Audio operations: `to_text`, `to_audio`
- `app` - Application information APIs (4 APIs)
  - App operations: `info`, `parameters`, `meta`, `site`
- `annotation` - Annotation management APIs (6 APIs)
  - Annotation operations: `list`, `create`, `update`, `delete`, `configure`, `status`

**Legacy Code Migration (MANDATORY)**:
- **Current Structure Assessment**: Evaluate existing chat module implementation structure
- **Migration Required**: Consolidate existing functionality into the new multi-resource structure
- **Backward Compatibility**: Maintain existing API signatures during migration
- **Model Consolidation**: Move all models from subdirectories to flat structure
- **Resource Organization**: Ensure proper separation of concerns across the 7 resource classes
- **Version Update**: Update V1 class to expose all 7 chat resources

### 3. Response Model Strategy
**Decision**: Create dedicated Response models for every API
- Maintain type safety and consistency across all endpoints
- Include specific response models even for simple `{\"result\": \"success\"}` responses
- Ensure comprehensive IDE support and validation

### 4. Method Naming Convention
**Decision**: Use simple, concise method names for clarity
- Chat operations: `chat`, `stop`, `suggested`
- File operations: `upload`
- Feedback operations: `submit`, `list`
- Conversation operations: `list`, `delete`, `rename`, `variables`, `history`
- Audio operations: `to_text`, `to_audio`
- App operations: `info`, `parameters`, `meta`, `site`
- Annotation operations: `list`, `create`, `update`, `delete`, `configure`, `status`

**Naming Rules**:
- Use the shortest meaningful name possible
- Avoid redundant prefixes (e.g., `chat` instead of `send_chat` in Chat resource)
- Use underscores only when necessary for clarity
- Async methods use `a` prefix (e.g., `achat`, `alist`, `aupload`)

### 5. Class Naming Conflict Resolution (MANDATORY)
**Decision**: When class names conflict across different functional domains, add domain-specific prefixes

**Required Naming Patterns for Chat Module**:
- **Chat classes**: `Chat*` (e.g., `ChatMessage`, `ChatResponse`)
- **File classes**: `File*` (e.g., `FileInfo`, `FileUpload`)
- **Feedback classes**: `Feedback*` (e.g., `FeedbackInfo`, `FeedbackSubmission`)
- **Conversation classes**: `Conversation*` (e.g., `ConversationInfo`, `ConversationVariable`)
- **Audio classes**: `Audio*` (e.g., `AudioTranscription`, `AudioSynthesis`)
- **App classes**: `App*` (e.g., `AppInfo`, `AppParameters`)
- **Annotation classes**: `Annotation*` (e.g., `AnnotationInfo`, `AnnotationReply`)
- **Message classes**: `Message*` (e.g., `MessageInfo`, `MessageHistory`)

### 6. Response Model Inheritance Rules (CRITICAL - ZERO TOLERANCE)
**Decision**: ALL Response classes MUST inherit from BaseResponse for error handling

**MANDATORY RULE**: Every single Response class in the chat module MUST inherit from `BaseResponse`
- **Rationale**: Ensures all API responses have consistent error handling capabilities
- **Properties Provided**: `success`, `code`, `msg`, `raw` for comprehensive error management
- **Zero Exceptions**: No Response class may inherit directly from `pydantic.BaseModel`

### 7. Strict Type Safety Rules (MANDATORY - ZERO TOLERANCE)
**Decision**: ALL API fields MUST use strict typing with Literal types instead of generic strings

**Strict Type Implementation Pattern**:
```python
# chat_types.py - Define all Literal types
from typing import Literal

# Response mode types
ResponseMode = Literal["streaming", "blocking"]

# File types
FileType = Literal["image"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Rating types
Rating = Literal["like", "dislike"]

# Sort types
SortBy = Literal["created_at", "-created_at", "updated_at", "-updated_at"]

# Icon types
IconType = Literal["emoji", "image"]

# Auto play types
AutoPlay = Literal["enabled", "disabled"]

# Annotation action types
AnnotationAction = Literal["enable", "disable"]

# Job status types
JobStatus = Literal["waiting", "running", "completed", "failed"]

# Message belongs to types
MessageBelongsTo = Literal["user", "assistant"]

# Conversation status types
ConversationStatus = Literal["normal", "archived"]

# Variable value types
VariableValueType = Literal["string", "number", "select"]

# Form input types
FormInputType = Literal["text-input", "paragraph", "select"]

# Streaming event types
StreamingEventType = Literal[
    "message", "agent_message", "tts_message", "tts_message_end", 
    "agent_thought", "message_file", "message_end", "message_replace", 
    "error", "ping"
]

# Audio file formats
AudioFormat = Literal["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]

# Image file formats
ImageFormat = Literal["png", "jpg", "jpeg", "webp", "gif"]

# HTTP status codes
HttpStatusCode = Literal[200, 204, 400, 401, 403, 404, 413, 415, 429, 500, 503]
```

### 8. Request/Response Model Code Style Rules (MANDATORY)
**Decision**: Strict adherence to established patterns for consistency across all chat APIs

#### Request Model Architecture
**Request Classes**:
- MUST inherit from `BaseRequest` (never from `BaseModel`)
- MUST include `request_body` attribute of type `RequestBody | None` for POST/PATCH/PUT requests
- MUST use `request_body()` method in builder to accept entire RequestBody object
- Builder variables MUST use full descriptive names (e.g., `self._chat_request`)
- MUST set `http_method` and `uri` in builder constructor
- Path parameters MUST use `self._request.paths["param_name"] = value` pattern
- Query parameters MUST use `self._request.add_query("key", value)` pattern

#### HTTP Method Patterns
**GET Requests** (get_conversations, get_app_info, etc.):
- No RequestBody file needed
- Use query parameters: `self._request.add_query("key", value)`
- Use path parameters: `self._request.paths["param_name"] = value`

**POST Requests** (chat, submit_feedback, create_annotation, etc.):
- Require separate RequestBody file
- Use `request_body()` method in Request builder
- RequestBody builder methods set fields directly

**PUT/PATCH Requests** (update_annotation):
- Require separate RequestBody file
- Use `request_body()` method in Request builder

**DELETE Requests** (delete_conversation, delete_annotation):
- May require RequestBody file for user identification
- Use path parameters for resource identification

#### Multipart/Form-Data Handling (CRITICAL PATTERN)
**Decision**: Special handling for APIs that require multipart/form-data (file uploads)

**Pattern Requirements**:
- APIs requiring file uploads MUST use multipart/form-data content type
- Request classes MUST support both `files` and `body` fields in BaseRequest
- RequestBody classes MUST use nested data structure pattern for complex form data

**Implementation Pattern**:
```python
# For APIs with file uploads (e.g., upload_file, audio_to_text)
class UploadFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file: BytesIO | None = None

    def file(self, file: BytesIO, file_name: str | None = None) -> UploadFileRequestBuilder:
        self._request.file = file
        file_name = file_name or "upload"
        self._request.files = {"file": (file_name, file)}
        return self

    def user(self, user: str) -> UploadFileRequestBuilder:
        self._request.body = {"user": user}
        return self
```

#### Class Naming Convention (MANDATORY - ZERO TOLERANCE)
**Universal Naming Pattern**:
- File names determine class names exactly (e.g., `chat_request.py` → `ChatRequest`)
- Each class has corresponding Builder (e.g., `ChatRequest` + `ChatRequestBuilder`)
- Pattern applies to all model types: Request, RequestBody, Response

**STRICT Naming Rules (NO EXCEPTIONS)**:
- Remove ALL module/domain prefixes from class names
- Class names MUST match file names exactly (case-sensitive)
- Apply uniformly across ALL resources: chat, file, feedback, conversation, audio, app, annotation
- Use operation-based names: `ChatRequest`, `UploadFileResponse`, `SubmitFeedbackRequestBody`
- NEVER use domain-specific names: `ChatChatRequest`, `FileUploadFileResponse`
- NO legacy naming patterns allowed
- Consistent across all HTTP methods and operation types

#### URI and HTTP Method Configuration
**All Chat APIs**:
- `POST /v1/chat-messages` → `ChatRequest`
- `POST /v1/chat-messages/:task_id/stop` → `StopChatRequest`
- `GET /v1/messages/:message_id/suggested` → `GetSuggestedQuestionsRequest`
- `POST /v1/files/upload` → `UploadFileRequest`
- `POST /v1/messages/:message_id/feedbacks` → `SubmitFeedbackRequest`
- `GET /v1/app/feedbacks` → `GetFeedbacksRequest`
- `GET /v1/messages` → `GetMessageHistoryRequest`
- `GET /v1/conversations` → `GetConversationsRequest`
- `DELETE /v1/conversations/:conversation_id` → `DeleteConversationRequest`
- `POST /v1/conversations/:conversation_id/name` → `RenameConversationRequest`
- `GET /v1/conversations/:conversation_id/variables` → `GetConversationVariablesRequest`
- `POST /v1/audio-to-text` → `AudioToTextRequest`
- `POST /v1/text-to-audio` → `TextToAudioRequest`
- `GET /v1/info` → `GetAppInfoRequest`
- `GET /v1/parameters` → `GetAppParametersRequest`
- `GET /v1/meta` → `GetAppMetaRequest`
- `GET /v1/site` → `GetSiteSettingsRequest`
- `GET /v1/apps/annotations` → `ListAnnotationsRequest`
- `POST /v1/apps/annotations` → `CreateAnnotationRequest`
- `PUT /v1/apps/annotations/:annotation_id` → `UpdateAnnotationRequest`
- `DELETE /v1/apps/annotations/:annotation_id` → `DeleteAnnotationRequest`
- `POST /v1/apps/annotation-reply/:action` → `ConfigureAnnotationReplyRequest`
- `GET /v1/apps/annotation-reply/:action/status/:job_id` → `GetAnnotationReplyStatusRequest`

#### Public Class Inheritance Rules (CRITICAL)
**Public/Common Classes**:
- Public classes (MessageInfo, ConversationInfo, FileInfo, etc.) MUST inherit from `pydantic.BaseModel` ONLY
- Public classes MUST NOT inherit from `BaseResponse`
- Public classes MUST have Builder patterns for consistency and ease of use
- Public classes are reusable components that can be used across different contexts

**Response Classes (MANDATORY - ZERO TOLERANCE)**:
- ALL Response classes MUST inherit from `BaseResponse` for error handling capabilities
- Response classes MAY use multiple inheritance when they need to include public class data
- Pattern: `class ChatResponse(MessageInfo, BaseResponse):`
- This allows response classes to have both data fields and error handling capabilities
- Response classes MUST NOT have Builder patterns (unlike Request classes)
- **CRITICAL**: NEVER inherit from `pydantic.BaseModel` directly - ALWAYS use `BaseResponse`

### 9. File Organization Strategy
**Decision**: Different organization strategies for models vs resources

#### Model Organization: Flat Structure
**Models use flat structure without grouping**:
```
model/
├── chat_request.py
├── chat_request_body.py
├── chat_response.py
├── stop_chat_request.py
├── upload_file_request.py
├── chat_types.py
└── [all other model files in flat structure]
```

#### Resource Organization: Functional Grouping
**Resources are grouped by functionality**:
```
resource/
├── chat.py         # Chat message operations
├── file.py         # File management operations
├── feedback.py     # Feedback operations
├── conversation.py # Conversation management operations
├── audio.py        # Audio processing operations
├── app.py          # Application information operations
└── annotation.py   # Annotation management operations
```

### 10. Public Class Builder Pattern Rules (MANDATORY)
**Decision**: All public classes MUST implement builder patterns for consistency and usability

#### Builder Pattern Implementation Requirements
**Scope**: All public/common classes that inherit from `pydantic.BaseModel`
- **Target Classes**: `MessageInfo`, `ConversationInfo`, `FileInfo`, `FeedbackInfo`, `AppInfo`, `AnnotationInfo`, `UsageInfo`, `RetrieverResource`, `AgentThought`, `MessageFile`, `ConversationVariable`, `AppParameters`, `SiteSettings`, `ToolIcon`, and all other public model classes
- **Exclusions**: Request, RequestBody, and Response classes (which have their own builder rules)

## API Implementation Plan

### Chat Message APIs (3 APIs)

#### Chat Resource Implementation
1. **POST /chat-messages** → `chat.chat()` - Send chat message
2. **POST /chat-messages/{task_id}/stop** → `chat.stop()` - Stop chat generation
3. **GET /messages/{message_id}/suggested** → `chat.suggested()` - Get suggested questions

### File Management APIs (1 API)

#### File Resource Implementation
1. **POST /files/upload** → `file.upload()` - Upload file

### Feedback Management APIs (2 APIs)

#### Feedback Resource Implementation
1. **POST /messages/{message_id}/feedbacks** → `feedback.submit()` - Submit feedback
2. **GET /app/feedbacks** → `feedback.list()` - Get feedbacks

### Conversation Management APIs (5 APIs)

#### Conversation Resource Implementation
1. **GET /messages** → `conversation.history()` - Get message history
2. **GET /conversations** → `conversation.list()` - Get conversations
3. **DELETE /conversations/{conversation_id}** → `conversation.delete()` - Delete conversation
4. **POST /conversations/{conversation_id}/name** → `conversation.rename()` - Rename conversation
5. **GET /conversations/{conversation_id}/variables** → `conversation.variables()` - Get variables

### Audio Processing APIs (2 APIs)

#### Audio Resource Implementation
1. **POST /audio-to-text** → `audio.to_text()` - Speech to text
2. **POST /text-to-audio** → `audio.to_audio()` - Text to speech

### Application Information APIs (4 APIs)

#### App Resource Implementation
1. **GET /info** → `app.info()` - Get app info
2. **GET /parameters** → `app.parameters()` - Get app parameters
3. **GET /meta** → `app.meta()` - Get app meta
4. **GET /site** → `app.site()` - Get site settings

### Annotation Management APIs (6 APIs)

#### Annotation Resource Implementation
1. **GET /apps/annotations** → `annotation.list()` - List annotations
2. **POST /apps/annotations** → `annotation.create()` - Create annotation
3. **PUT /apps/annotations/{annotation_id}** → `annotation.update()` - Update annotation
4. **DELETE /apps/annotations/{annotation_id}** → `annotation.delete()` - Delete annotation
5. **POST /apps/annotation-reply/{action}** → `annotation.configure()` - Configure reply settings
6. **GET /apps/annotation-reply/{action}/status/{job_id}** → `annotation.status()` - Get status

## Target Model Structure

**Migration Steps**:
1. Move all model files from subdirectories to root model/ directory (if applicable)
2. Update all import statements to reflect new flat structure
3. Remove empty subdirectories if they exist
4. Update __init__.py files to export from new locations
5. Ensure all cross-references between models are updated to new flat structure

```
model/
├── chat_request.py
├── chat_request_body.py
├── chat_response.py
├── stop_chat_request.py
├── stop_chat_request_body.py
├── stop_chat_response.py
├── get_suggested_questions_request.py
├── get_suggested_questions_response.py
├── upload_file_request.py
├── upload_file_response.py
├── submit_feedback_request.py
├── submit_feedback_request_body.py
├── submit_feedback_response.py
├── get_feedbacks_request.py
├── get_feedbacks_response.py
├── get_message_history_request.py
├── get_message_history_response.py
├── get_conversations_request.py
├── get_conversations_response.py
├── delete_conversation_request.py
├── delete_conversation_request_body.py
├── delete_conversation_response.py
├── rename_conversation_request.py
├── rename_conversation_request_body.py
├── rename_conversation_response.py
├── get_conversation_variables_request.py
├── get_conversation_variables_response.py
├── audio_to_text_request.py
├── audio_to_text_response.py
├── text_to_audio_request.py
├── text_to_audio_response.py
├── get_app_info_request.py
├── get_app_info_response.py
├── get_app_parameters_request.py
├── get_app_parameters_response.py
├── get_app_meta_request.py
├── get_app_meta_response.py
├── get_site_settings_request.py
├── get_site_settings_response.py
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
├── configure_annotation_reply_request.py
├── configure_annotation_reply_request_body.py
├── configure_annotation_reply_response.py
├── get_annotation_reply_status_request.py
├── get_annotation_reply_status_response.py
├── message_info.py
├── conversation_info.py
├── file_info.py
├── feedback_info.py
├── app_info.py
├── annotation_info.py
├── chat_file.py
├── usage_info.py
├── retriever_resource.py
├── agent_thought.py
├── conversation_variable.py
├── app_parameters.py
├── site_settings.py
├── tool_icon.py
├── message_file.py
├── pagination_info.py
└── chat_types.py
```

## Technical Implementation Details

### Resource Class Structure
```python
# Example: chat resource
class Chat:
    def __init__(self, config: Config):
        self.config = config

    @overload
    def chat(self, request: ChatRequest, option: RequestOption | None, stream: Literal[True]) -> Generator[bytes, None, None]: ...

    @overload
    def chat(self, request: ChatRequest, option: RequestOption | None, stream: Literal[False]) -> ChatResponse: ...

    def chat(self, request: ChatRequest, option: RequestOption | None = None, stream: bool = False):
        if stream:
            return Transport.execute(self.config, request, option=option, stream=True)
        else:
            return Transport.execute(self.config, request, unmarshal_as=ChatResponse, option=option)

    async def achat(self, request: ChatRequest, option: RequestOption | None = None, stream: bool = False):
        if stream:
            return await ATransport.aexecute(self.config, request, option=option, stream=True)
        else:
            return await ATransport.aexecute(self.config, request, unmarshal_as=ChatResponse, option=option)
```

### Version Integration
**Target Structure**:
```python
class V1:
    def __init__(self, config: Config):
        self.chat = Chat(config)
        self.file = File(config)
        self.feedback = Feedback(config)
        self.conversation = Conversation(config)
        self.audio = Audio(config)
        self.app = App(config)
        self.annotation = Annotation(config)
```

**Migration Steps**:
1. Assess current chat module structure and existing implementations
2. Create new resource classes (Chat, File, Feedback, Conversation, Audio, App, Annotation)
3. Migrate existing methods to appropriate resource classes
4. Update V1 class to expose all 7 chat resources
5. Ensure all existing method signatures are preserved during migration
6. Update import statements and references throughout the codebase

## Examples Strategy

### Examples Organization
**Decision**: Resource-based directory structure with API-specific files
- Each resource gets its own directory under `examples/chat/`
- Each API gets its own file within the resource directory
- Each file contains both sync and async examples

### Examples Directory Structure
```
examples/chat/
├── chat/
│   ├── send_chat_message.py          # Chat message examples
│   ├── stop_chat_generation.py       # Stop generation examples
│   └── get_suggested_questions.py    # Suggested questions examples
├── file/
│   └── upload_file.py                # File upload examples
├── feedback/
│   ├── submit_feedback.py            # Submit feedback examples
│   └── get_feedbacks.py              # Get feedbacks examples
├── conversation/
│   ├── get_message_history.py        # Message history examples
│   ├── get_conversations.py          # Conversations list examples
│   ├── delete_conversation.py        # Delete conversation examples
│   ├── rename_conversation.py        # Rename conversation examples
│   └── get_conversation_variables.py # Conversation variables examples
├── audio/
│   ├── audio_to_text.py              # Speech to text examples
│   └── text_to_audio.py              # Text to speech examples
├── app/
│   ├── get_app_info.py               # App info examples
│   ├── get_app_parameters.py         # App parameters examples
│   ├── get_app_meta.py               # App meta examples
│   └── get_site_settings.py          # Site settings examples
├── annotation/
│   ├── list_annotations.py           # List annotations examples
│   ├── create_annotation.py          # Create annotation examples
│   ├── update_annotation.py          # Update annotation examples
│   ├── delete_annotation.py          # Delete annotation examples
│   ├── configure_annotation_reply.py # Configure reply examples
│   └── get_annotation_reply_status.py # Get status examples
└── README.md                         # Examples overview and usage guide
```

## Chat Message Examples

### Send Chat Message (send_chat_message.py)

```python
import os
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

def send_blocking_chat():
    """Send a blocking chat message"""
    # Validate environment variables
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    
    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()
    
    # Build request
    req_body = (
        ChatRequestBody.builder()
        .inputs({})
        .query("Hello, how are you?")
        .response_mode("blocking")
        .user("user-123")
        .build()
    )
    
    req = ChatRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()
    
    try:
        # Execute request
        response = client.chat.v1.chat.chat(req, req_option, False)
        print(f"Response: {response.answer}")
        print(f"Message ID: {response.message_id}")
        print(f"Conversation ID: {response.conversation_id}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise

def send_streaming_chat():
    """Send a streaming chat message"""
    # Validate environment variables
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    
    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()
    
    # Build request
    req_body = (
        ChatRequestBody.builder()
        .inputs({})
        .query("Tell me a short story")
        .response_mode("streaming")
        .user("user-123")
        .build()
    )
    
    req = ChatRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()
    
    try:
        # Execute streaming request
        response = client.chat.v1.chat.chat(req, req_option, True)
        
        print("Streaming response:")
        for chunk in response:
            print(chunk.decode('utf-8'), end="", flush=True)
        print()  # New line after streaming
        
    except Exception as e:
        print(f"Error: {e}")
        raise

async def send_async_chat():
    """Send an async chat message"""
    # Validate environment variables
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    
    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()
    
    # Build request
    req_body = (
        ChatRequestBody.builder()
        .inputs({})
        .query("What's the weather like?")
        .response_mode("blocking")
        .user("user-123")
        .build()
    )
    
    req = ChatRequest.builder().request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()
    
    try:
        # Execute async request
        response = await client.chat.v1.chat.achat(req, req_option, False)
        print(f"Async Response: {response.answer}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    # Run blocking example
    send_blocking_chat()
    
    # Run streaming example
    send_streaming_chat()
    
    # Run async example
    import asyncio
    asyncio.run(send_async_chat())
```

### Stop Chat Generation (stop_chat_generation.py)

```python
import os
from dify_oapi.api.chat.v1.model.stop_chat_request import StopChatRequest
from dify_oapi.api.chat.v1.model.stop_chat_request_body import StopChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

def stop_chat_generation():
    """Stop a chat generation task"""
    # Validate environment variables
    api_key = os.getenv("CHAT_API_KEY")
    task_id = os.getenv("TASK_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not task_id:
        raise ValueError("TASK_ID environment variable is required")
    
    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()
    
    # Build request
    req_body = StopChatRequestBody.builder().user("user-123").build()
    req = StopChatRequest.builder().task_id(task_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()
    
    try:
        # Execute request
        response = client.chat.v1.chat.stop(req, req_option)
        print(f"Stop result: {response.result}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise

async def stop_chat_generation_async():
    """Stop a chat generation task asynchronously"""
    # Validate environment variables
    api_key = os.getenv("CHAT_API_KEY")
    task_id = os.getenv("TASK_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not task_id:
        raise ValueError("TASK_ID environment variable is required")
    
    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()
    
    # Build request
    req_body = StopChatRequestBody.builder().user("user-123").build()
    req = StopChatRequest.builder().task_id(task_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()
    
    try:
        # Execute async request
        response = await client.chat.v1.chat.astop(req, req_option)
        print(f"Async stop result: {response.result}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    # Run sync example
    stop_chat_generation()
    
    # Run async example
    import asyncio
    asyncio.run(stop_chat_generation_async())
```

## File Management Examples

### Upload File (upload_file.py)

```python
import os
from io import BytesIO
from dify_oapi.api.chat.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

def upload_file():
    """Upload a file for chat"""
    # Validate environment variables
    api_key = os.getenv("CHAT_API_KEY")
    file_path = os.getenv("FILE_PATH")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not file_path:
        raise ValueError("FILE_PATH environment variable is required")
    
    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()
    
    try:
        # Read file
        with open(file_path, 'rb') as f:
            file_data = BytesIO(f.read())
        
        # Build request
        req = UploadFileRequest.builder().file(file_data, os.path.basename(file_path)).user("user-123").build()
        req_option = RequestOption.builder().api_key(api_key).build()
        
        # Execute request
        response = client.chat.v1.file.upload(req, req_option)
        print(f"File uploaded successfully!")
        print(f"File ID: {response.id}")
        print(f"File name: {response.name}")
        print(f"File size: {response.size} bytes")
        print(f"MIME type: {response.mime_type}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise

async def upload_file_async():
    """Upload a file for chat asynchronously"""
    # Validate environment variables
    api_key = os.getenv("CHAT_API_KEY")
    file_path = os.getenv("FILE_PATH")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not file_path:
        raise ValueError("FILE_PATH environment variable is required")
    
    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()
    
    try:
        # Read file
        with open(file_path, 'rb') as f:
            file_data = BytesIO(f.read())
        
        # Build request
        req = UploadFileRequest.builder().file(file_data, os.path.basename(file_path)).user("user-123").build()
        req_option = RequestOption.builder().api_key(api_key).build()
        
        # Execute async request
        response = await client.chat.v1.file.aupload(req, req_option)
        print(f"File uploaded asynchronously!")
        print(f"File ID: {response.id}")
        print(f"File name: {response.name}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    # Run file upload example
    if os.getenv("FILE_PATH"):
        upload_file()
    else:
        # Run image upload example with test data
        pass
    
    # Run async example
    if os.getenv("FILE_PATH"):
        import asyncio
        asyncio.run(upload_file_async())
```

## Feedback Management Examples

### Submit Feedback (submit_feedback.py)

```python
import os
from dify_oapi.api.chat.v1.model.submit_feedback_request import SubmitFeedbackRequest
from dify_oapi.api.chat.v1.model.submit_feedback_request_body import SubmitFeedbackRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

def submit_positive_feedback():
    """Submit positive feedback for a message"""
    # Validate environment variables
    api_key = os.getenv("CHAT_API_KEY")
    message_id = os.getenv("MESSAGE_ID")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    if not message_id:
        raise ValueError("MESSAGE_ID environment variable is required")
    
    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()
    
    # Build request
    req_body = (
        SubmitFeedbackRequestBody.builder()
        .rating("like")
        .user("user-123")
        .content("Great response! Very helpful.")
        .build()
    )
    
    req = SubmitFeedbackRequest.builder().message_id(message_id).request_body(req_body).build()
    req_option = RequestOption.builder().api_key(api_key).build()
    
    try:
        # Execute request
        response = client.chat.v1.feedback.submit(req, req_option)
        print(f"Feedback submitted: {response.result}")
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    # Run positive feedback example
    submit_positive_feedback()
```

### Get Feedbacks (get_feedbacks.py)

```python
import os
from dify_oapi.api.chat.v1.model.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

def get_feedbacks():
    """Get application feedbacks"""
    # Validate environment variables
    api_key = os.getenv("CHAT_API_KEY")
    if not api_key:
        raise ValueError("CHAT_API_KEY environment variable is required")
    
    # Initialize client
    client = Client.builder().domain("https://api.dify.ai").build()
    
    # Build request
    req = GetFeedbacksRequest.builder().page(1).limit(20).build()
    req_option = RequestOption.builder().api_key(api_key).build()
    
    try:
        # Execute request
        response = client.chat.v1.feedback.list(req, req_option)
        print(f"Retrieved {len(response.data)} feedbacks")
        
        for feedback in response.data:
            print(f"- ID: {feedback.id}")
            print(f"  Rating: {feedback.rating}")
            print(f"  Content: {feedback.content}")
            print(f"  Created: {feedback.created_at}")
            print()
        
        return response
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    # Run basic example
    get_feedbacks()
```

## Environment Variables

### Required Environment Variables

```bash
# Chat API Examples
export CHAT_API_KEY="your-chat-api-key"
export MESSAGE_ID="your-message-id"
export CONVERSATION_ID="your-conversation-id"
export TASK_ID="your-task-id"
export FILE_PATH="/path/to/your/file.jpg"
export AUDIO_PATH="/path/to/your/audio.mp3"
export ANNOTATION_ID="your-annotation-id"
export JOB_ID="your-job-id"
```

### Environment Validation

All examples include environment variable validation:

```python
def validate_environment():
    """Validate required environment variables"""
    required_vars = ["CHAT_API_KEY"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Usage in examples
validate_environment()
```

## Safety Features

### Resource Naming Convention
All examples use safe, non-production resource names:
- User IDs: `user-123`, `test-user`
- Test files: `test_image.png`, `example_audio.mp3`
- Example content: `[Example] Test Chat`

### Error Handling
All examples include comprehensive error handling:

```python
try:
    # API call
    response = client.chat.v1.chat.chat(req, req_option, False)
    return response
except Exception as e:
    print(f"Error: {e}")
    raise
```

### Cleanup Functions
Examples include cleanup functions where applicable:

```python
def cleanup_test_resources():
    """Clean up test resources created during examples"""
    # Implementation for cleaning up test data
    pass
```

## Usage Instructions

### Running Examples

1. **Set Environment Variables**:
   ```bash
   export CHAT_API_KEY="your-api-key"
   export MESSAGE_ID="your-message-id"
   ```

2. **Run Individual Examples**:
   ```bash
   python examples/chat/chat/send_chat_message.py
   python examples/chat/file/upload_file.py
   ```

3. **Run All Examples**:
   ```bash
   python -m examples.chat.run_all_examples
   ```

### Example Categories

1. **Basic Examples**: Simple API calls with minimal configuration
2. **Advanced Examples**: Complex workflows with multiple API calls
3. **Async Examples**: Asynchronous implementations for all APIs
4. **Error Handling Examples**: Comprehensive error handling patterns
5. **Integration Examples**: End-to-end workflows combining multiple APIs

### Best Practices

1. **Environment Validation**: Always validate required environment variables
2. **Error Handling**: Include comprehensive error handling in all examples
3. **Resource Safety**: Use safe, non-production resource names
4. **Code Minimalism**: Write only essential code for demonstration
5. **Documentation**: Include clear comments explaining each step
6. **Async Support**: Provide both sync and async versions where applicable

## Testing Strategy

### Test Organization Strategy

#### Test Structure Overview
```
tests/chat/v1/
├── model/
│   ├── test_chat_models.py           # Chat API tests (3 test classes)
│   ├── test_file_models.py           # File API tests (1 test class)
│   ├── test_feedback_models.py       # Feedback API tests (2 test classes)
│   ├── test_conversation_models.py   # Conversation API tests (5 test classes)
│   ├── test_audio_models.py          # Audio API tests (2 test classes)
│   ├── test_app_models.py            # App API tests (4 test classes)
│   ├── test_annotation_models.py     # Annotation API tests (6 test classes)
│   └── test_chat_public_models.py    # All public models
├── resource/
│   ├── test_chat_resource.py         # Chat resource tests
│   ├── test_file_resource.py         # File resource tests
│   ├── test_feedback_resource.py     # Feedback resource tests
│   ├── test_conversation_resource.py # Conversation resource tests
│   ├── test_audio_resource.py        # Audio resource tests
│   ├── test_app_resource.py          # App resource tests
│   └── test_annotation_resource.py   # Annotation resource tests
├── integration/
│   ├── test_chat_api_integration.py  # All 22 chat API integration tests
│   ├── test_comprehensive_integration.py
│   ├── test_examples_validation.py
│   └── test_version_integration.py
└── __init__.py
```

### Model Test Cases

#### Chat Models Tests (test_chat_models.py)

**TestSendChatMessageModels**:
```python
class TestSendChatMessageModels:
    def test_chat_request_builder(self):
        """Test ChatRequest builder pattern"""
        request_body = ChatRequestBody.builder().query("Hello").user("user-123").build()
        request = ChatRequest.builder().request_body(request_body).build()
        
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/chat-messages"
        assert request.request_body.query == "Hello"
        assert request.request_body.user == "user-123"

    def test_chat_request_body_validation(self):
        """Test ChatRequestBody field validation"""
        # Test response_mode validation
        with pytest.raises(ValueError):
            ChatRequestBody.builder().response_mode("invalid").build()
        
        # Test valid response_mode
        body = ChatRequestBody.builder().response_mode("streaming").build()
        assert body.response_mode == "streaming"

    def test_chat_response_inheritance(self):
        """Test ChatResponse inherits from BaseResponse"""
        response = ChatResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, 'success')
        assert hasattr(response, 'code')
        assert hasattr(response, 'msg')
```

**TestStopChatGenerationModels**:
```python
class TestStopChatGenerationModels:
    def test_stop_chat_request_builder(self):
        """Test StopChatRequest builder pattern"""
        request_body = StopChatRequestBody.builder().user("user-123").build()
        request = StopChatRequest.builder().task_id("task-123").request_body(request_body).build()
        
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/chat-messages/:task_id/stop"
        assert request.paths["task_id"] == "task-123"

    def test_stop_chat_response_inheritance(self):
        """Test StopChatResponse inherits from BaseResponse"""
        response = StopChatResponse()
        assert isinstance(response, BaseResponse)
```

**TestGetSuggestedQuestionsModels**:
```python
class TestGetSuggestedQuestionsModels:
    def test_suggested_questions_request_builder(self):
        """Test GetSuggestedQuestionsRequest builder pattern"""
        request = GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("user-123").build()
        
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/messages/:message_id/suggested"
        assert request.paths["message_id"] == "msg-123"

    def test_suggested_questions_response_inheritance(self):
        """Test GetSuggestedQuestionsResponse inherits from BaseResponse"""
        response = GetSuggestedQuestionsResponse()
        assert isinstance(response, BaseResponse)
```

#### File Models Tests (test_file_models.py)

**TestUploadFileModels**:
```python
class TestUploadFileModels:
    def test_upload_file_request_builder(self):
        """Test UploadFileRequest builder pattern"""
        file_data = BytesIO(b"test file content")
        request = UploadFileRequest.builder().file(file_data, "test.jpg").user("user-123").build()
        
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/files/upload"
        assert request.file is not None
        assert "file" in request.files

    def test_upload_file_response_inheritance(self):
        """Test UploadFileResponse inherits from BaseResponse"""
        response = UploadFileResponse()
        assert isinstance(response, BaseResponse)

    def test_file_info_builder(self):
        """Test FileInfo builder pattern"""
        file_info = FileInfo.builder().id("file-123").name("test.jpg").size(1024).build()
        
        assert file_info.id == "file-123"
        assert file_info.name == "test.jpg"
        assert file_info.size == 1024
```

#### Public Models Tests (test_chat_public_models.py)

**TestMessageInfo**:
```python
class TestMessageInfo:
    def test_message_info_builder(self):
        """Test MessageInfo builder pattern"""
        message = MessageInfo.builder().id("msg-123").query("Hello").answer("Hi there").build()
        
        assert message.id == "msg-123"
        assert message.query == "Hello"
        assert message.answer == "Hi there"

    def test_message_info_validation(self):
        """Test MessageInfo field validation"""
        message = MessageInfo.builder().id("msg-123").build()
        assert isinstance(message, BaseModel)
```

**TestConversationInfo**:
```python
class TestConversationInfo:
    def test_conversation_info_builder(self):
        """Test ConversationInfo builder pattern"""
        conversation = ConversationInfo.builder().id("conv-123").name("Test Chat").build()
        
        assert conversation.id == "conv-123"
        assert conversation.name == "Test Chat"

    def test_conversation_info_validation(self):
        """Test ConversationInfo field validation"""
        conversation = ConversationInfo.builder().id("conv-123").build()
        assert isinstance(conversation, BaseModel)
```

### Resource Test Cases

#### Chat Resource Tests (test_chat_resource.py)

```python
class TestChatResource:
    @pytest.fixture
    def chat_resource(self):
        config = Config()
        return Chat(config)

    def test_chat_blocking(self, chat_resource, mock_transport):
        """Test blocking chat method"""
        request = ChatRequest.builder().build()
        option = RequestOption.builder().build()
        
        mock_transport.execute.return_value = ChatResponse()
        result = chat_resource.chat(request, option, stream=False)
        
        assert isinstance(result, ChatResponse)
        mock_transport.execute.assert_called_once()

    def test_chat_streaming(self, chat_resource, mock_transport):
        """Test streaming chat method"""
        request = ChatRequest.builder().build()
        option = RequestOption.builder().build()
        
        mock_transport.execute.return_value = iter([b"chunk1", b"chunk2"])
        result = chat_resource.chat(request, option, stream=True)
        
        assert hasattr(result, '__iter__')
        mock_transport.execute.assert_called_once_with(
            chat_resource.config, request, option=option, stream=True
        )

    def test_stop_chat(self, chat_resource, mock_transport):
        """Test stop chat method"""
        request = StopChatRequest.builder().build()
        option = RequestOption.builder().build()
        
        mock_transport.execute.return_value = StopChatResponse()
        result = chat_resource.stop(request, option)
        
        assert isinstance(result, StopChatResponse)
        mock_transport.execute.assert_called_once()

    def test_suggested_questions(self, chat_resource, mock_transport):
        """Test suggested questions method"""
        request = GetSuggestedQuestionsRequest.builder().build()
        option = RequestOption.builder().build()
        
        mock_transport.execute.return_value = GetSuggestedQuestionsResponse()
        result = chat_resource.suggested(request, option)
        
        assert isinstance(result, GetSuggestedQuestionsResponse)
        mock_transport.execute.assert_called_once()
```

#### File Resource Tests (test_file_resource.py)

```python
class TestFileResource:
    @pytest.fixture
    def file_resource(self):
        config = Config()
        return File(config)

    def test_upload_file(self, file_resource, mock_transport):
        """Test file upload method"""
        request = UploadFileRequest.builder().build()
        option = RequestOption.builder().build()
        
        mock_transport.execute.return_value = UploadFileResponse()
        result = file_resource.upload(request, option)
        
        assert isinstance(result, UploadFileResponse)
        mock_transport.execute.assert_called_once()

    async def test_async_upload_file(self, file_resource, mock_atransport):
        """Test async file upload method"""
        request = UploadFileRequest.builder().build()
        option = RequestOption.builder().build()
        
        mock_atransport.aexecute.return_value = UploadFileResponse()
        result = await file_resource.aupload(request, option)
        
        assert isinstance(result, UploadFileResponse)
        mock_atransport.aexecute.assert_called_once()
```

### Integration Test Cases

#### Chat API Integration Tests (test_chat_api_integration.py)

```python
class TestChatAPIIntegration:
    @pytest.fixture
    def client(self):
        return Client.builder().domain("https://api.dify.ai").build()

    def test_complete_chat_flow(self, client):
        """Test complete chat conversation flow"""
        # 1. Send initial chat message
        chat_body = ChatRequestBody.builder().query("Hello").user("test-user").response_mode("blocking").build()
        chat_request = ChatRequest.builder().request_body(chat_body).build()
        option = RequestOption.builder().api_key("test-key").build()
        
        # Mock the response
        with patch.object(Transport, 'execute') as mock_execute:
            mock_execute.return_value = ChatResponse(message_id="msg-123", conversation_id="conv-123")
            
            response = client.chat.v1.chat.chat(chat_request, option, False)
            assert response.message_id == "msg-123"
            assert response.conversation_id == "conv-123"

    def test_file_upload_and_chat(self, client):
        """Test file upload followed by chat with file"""
        # 1. Upload file
        file_data = BytesIO(b"test image content")
        upload_request = UploadFileRequest.builder().file(file_data, "test.jpg").user("test-user").build()
        option = RequestOption.builder().api_key("test-key").build()
        
        with patch.object(Transport, 'execute') as mock_execute:
            mock_execute.return_value = UploadFileResponse(id="file-123")
            
            upload_response = client.chat.v1.file.upload(upload_request, option)
            assert upload_response.id == "file-123"
            
            # 2. Use uploaded file in chat
            chat_file = ChatFile.builder().type("image").transfer_method("local_file").upload_file_id("file-123").build()
            chat_body = ChatRequestBody.builder().query("What's in this image?").user("test-user").files([chat_file]).build()
            chat_request = ChatRequest.builder().request_body(chat_body).build()
            
            mock_execute.return_value = ChatResponse(answer="I can see an image...")
            chat_response = client.chat.v1.chat.chat(chat_request, option, False)
            assert "image" in chat_response.answer
```

### Test Execution Strategy

#### Test Categories
1. **Unit Tests**: Model and resource tests
2. **Integration Tests**: End-to-end API flow tests
3. **Performance Tests**: Load and stress testing
4. **Compatibility Tests**: Backward compatibility validation

#### Test Coverage Requirements
- **Model Tests**: 100% coverage for all model classes
- **Resource Tests**: 100% coverage for all resource methods
- **Integration Tests**: All 22 APIs covered
- **Error Handling**: All error scenarios tested

#### Test Data Management
- **Mock Data**: Use realistic but safe test data
- **Environment Variables**: Validate required environment variables
- **Cleanup**: Proper test data cleanup after each test
- **Isolation**: Each test runs independently

#### Continuous Integration
- **Automated Testing**: All tests run on every commit
- **Coverage Reports**: Generate and track coverage reports
- **Performance Benchmarks**: Track performance metrics
- **Compatibility Checks**: Validate backward compatibility

## Migration Analysis

### Current Implementation Analysis

#### Existing Structure Assessment

**Current Resources (4 resources)**:
1. **Chat Resource** (`chat.py`)
   - `chat()` - Send chat message (✓ Implemented)
   - `stop()` - Stop chat generation (✓ Implemented)
   - Missing: `suggested()` method

2. **Conversation Resource** (`conversation.py`)
   - `list()` - Get conversations (✓ Implemented)
   - `delete()` - Delete conversation (✓ Implemented)
   - `rename()` - Rename conversation (✓ Implemented)
   - Missing: `variables()`, `history()` methods

3. **Message Resource** (`message.py`)
   - `suggested()` - Get suggested questions (✓ Implemented)
   - `history()` - Get message history (✓ Implemented)
   - **Migration Required**: Move methods to appropriate resources

4. **Audio Resource** (`audio.py`)
   - `to_text()` - Audio to text (✓ Implemented)
   - Missing: `to_audio()` method

#### Missing Resources (4 resources)
1. **File Resource** - Not implemented
2. **Feedback Resource** - Not implemented
3. **App Resource** - Not implemented
4. **Annotation Resource** - Not implemented

#### Current Model Structure
**Existing Models (22 models)**:
- `audio_to_text_request.py`, `audio_to_text_request_body.py`, `audio_to_text_response.py`
- `chat_request.py`, `chat_request_body.py`, `chat_request_file.py`, `chat_response.py`
- `delete_conversation_request.py`, `delete_conversation_request_body.py`, `delete_conversation_response.py`
- `get_conversation_list_request.py`, `get_conversation_list_response.py`
- `message_history_request.py`, `message_history_response.py`
- `message_suggested_request.py`, `message_suggested_response.py`
- `rename_conversation_request.py`, `rename_conversation_request_body.py`, `rename_conversation_response.py`
- `stop_chat_request.py`, `stop_chat_request_body.py`, `stop_chat_response.py`

**Missing Models (40+ models)**:
- File upload models (3 models)
- Feedback models (6 models)
- Conversation variables models (3 models)
- Text-to-audio models (3 models)
- App information models (12 models)
- Annotation models (18 models)
- Public/common models (10+ models)
- Type definitions (chat_types.py)

### Migration Strategy

#### Phase 1: Model Migration and Creation

**Step 1.1: Rename Existing Models (Following Flat Structure)**:
```bash
# Current naming → Target naming
get_conversation_list_request.py → get_conversations_request.py
get_conversation_list_response.py → get_conversations_response.py
message_history_request.py → get_message_history_request.py
message_history_response.py → get_message_history_response.py
message_suggested_request.py → get_suggested_questions_request.py
message_suggested_response.py → get_suggested_questions_response.py
```

**Step 1.2: Create Missing Models**:
- **File Management Models (3 models)**: `upload_file_request.py`, `upload_file_response.py`, `file_info.py`
- **Feedback Management Models (6 models)**: `submit_feedback_request.py`, `submit_feedback_request_body.py`, `submit_feedback_response.py`, `get_feedbacks_request.py`, `get_feedbacks_response.py`, `feedback_info.py`
- **Conversation Variables Models (3 models)**: `get_conversation_variables_request.py`, `get_conversation_variables_response.py`, `conversation_variable.py`
- **Text-to-Audio Models (3 models)**: `text_to_audio_request.py`, `text_to_audio_response.py`, `audio_synthesis.py`
- **App Information Models (12 models)**: `get_app_info_request.py`, `get_app_info_response.py`, `get_app_parameters_request.py`, `get_app_parameters_response.py`, `get_app_meta_request.py`, `get_app_meta_response.py`, `get_site_settings_request.py`, `get_site_settings_response.py`, `app_info.py`, `app_parameters.py`, `site_settings.py`, `tool_icon.py`
- **Annotation Models (18 models)**: Complete annotation management model set
- **Common/Public Models (10+ models)**: `message_info.py`, `conversation_info.py`, `usage_info.py`, `retriever_resource.py`, `agent_thought.py`, `message_file.py`, `pagination_info.py`, `chat_types.py`

**Step 1.3: Update Existing Models**:
- Add strict typing with Literal types
- Ensure BaseResponse inheritance for all Response classes

#### Phase 2: Resource Migration and Creation

**Step 2.1: Update Existing Resources**:
- **Chat Resource**: Add `suggested()` method (moved from Message resource)
- **Conversation Resource**: Add `history()` and `variables()` methods
- **Audio Resource**: Add `to_audio()` method

**Step 2.2: Create New Resources**:
- **File Resource**: `upload()` method
- **Feedback Resource**: `submit()`, `list()` methods
- **App Resource**: `info()`, `parameters()`, `meta()`, `site()` methods
- **Annotation Resource**: `list()`, `create()`, `update()`, `delete()`, `configure()`, `status()` methods

**Step 2.3: Remove Message Resource**:
- Move `suggested()` method to Chat resource
- Move `history()` method to Conversation resource
- Mark Message resource as deprecated
- Remove Message resource in next major version

#### Phase 3: Version Integration Update

**Update V1 Class**:
```python
# Before: version.py
class V1:
    def __init__(self, config: Config):
        self.chat: Chat = Chat(config)
        self.conversation: Conversation = Conversation(config)
        self.message: Message = Message(config)  # DEPRECATED
        self.audio: Audio = Audio(config)

# After: version.py
class V1:
    def __init__(self, config: Config):
        self.chat: Chat = Chat(config)
        self.file: File = File(config)
        self.feedback: Feedback = Feedback(config)
        self.conversation: Conversation = Conversation(config)
        self.audio: Audio = Audio(config)
        self.app: App = App(config)
        self.annotation: Annotation = Annotation(config)
        
        # DEPRECATED: Keep for backward compatibility
        self.message: Message = Message(config)
```

### Backward Compatibility Strategy

#### Maintained Interfaces
1. **Existing Method Signatures**: All current method signatures preserved
2. **Resource Access**: Existing resource access patterns maintained
3. **Builder Patterns**: Current builder patterns maintained
4. **Response Types**: Existing response types maintained

#### Deprecation Path
1. **Message Resource**: Mark as deprecated, maintain for 1 major version
2. **Old Model Names**: Support old import paths with deprecation warnings
3. **Migration Guide**: Provide clear migration instructions

#### Breaking Changes (Next Major Version)
1. **Model Import Paths**: Due to flat structure reorganization
2. **Message Resource Removal**: Complete removal of Message resource
3. **Enhanced Type Safety**: Strict Literal type requirements

### Migration Timeline

#### Phase 1: Preparation (Week 1)
- [ ] Create missing model files
- [ ] Update existing models with strict typing
- [ ] Ensure BaseResponse inheritance

#### Phase 2: Resource Updates (Week 2)
- [ ] Update existing resources
- [ ] Create new resources
- [ ] Update V1 class integration

#### Phase 3: Testing (Week 3)
- [ ] Create comprehensive test suite
- [ ] Update existing tests
- [ ] Validate migration with integration tests

#### Phase 4: Examples and Documentation (Week 4)
- [ ] Create missing examples
- [ ] Update existing examples
- [ ] Update documentation
- [ ] Create migration guide

#### Phase 5: Validation (Week 5)
- [ ] End-to-end testing
- [ ] Performance validation
- [ ] Backward compatibility verification
- [ ] Documentation review

### Risk Assessment

#### High Risk
- **Model Import Changes**: May break existing user code
- **Resource Method Migration**: Changes in method locations

#### Medium Risk
- **Type Safety Updates**: May require user code updates
- **New Resource Dependencies**: Additional imports required

#### Low Risk
- **New API Additions**: Purely additive changes
- **Enhanced Features**: Backward compatible improvements

#### Mitigation Strategies
1. **Comprehensive Testing**: Full test coverage for all changes
2. **Deprecation Warnings**: Clear warnings for deprecated features
3. **Migration Documentation**: Detailed migration instructions
4. **Gradual Rollout**: Phased implementation approach
5. **Rollback Plan**: Ability to revert changes if issues arise

### Success Criteria

#### Technical Criteria
- [ ] All 22 APIs implemented and tested
- [ ] 100% backward compatibility maintained
- [ ] All existing tests pass
- [ ] New comprehensive test suite passes
- [ ] Performance benchmarks maintained

#### Documentation Criteria
- [ ] Complete API documentation
- [ ] Migration guide available
- [ ] Examples for all APIs
- [ ] Updated README files

#### Quality Criteria
- [ ] Code review completed
- [ ] Type safety validation passed
- [ ] Integration tests successful
- [ ] User acceptance testing completed

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
- BaseResponse inheritance for all Response classes

### Testing Strategy
- Unit tests for all resource methods
- Integration tests with mock API responses
- Validation tests for all model classes
- Comprehensive typing hints for all test methods
- Complete coverage for all 22 APIs

### Documentation Accuracy
- All 22 APIs documented and implemented
- Examples match API specifications exactly
- Migration guide covers all existing code
- Test structure aligns with implementation

## Summary

This design provides a comprehensive solution for chat management in dify-oapi, covering all 22 chat-related APIs with a clean, maintainable architecture. The implementation prioritizes type safety, consistency, and developer experience while ensuring full compatibility with the latest Dify API specifications.

The multi-resource organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for chat operations including message processing, file management, feedback collection, conversation management, audio processing, application configuration, and annotation management.

**Total Implementation Scope**:
- **22 APIs** across 7 resource categories
- **60+ model files** with flat structure organization
- **7 resource classes** with proper separation of concerns
- **Complete migration strategy** from existing 4-resource structure
- **Comprehensive test suite** with 23+ test classes
- **22 example files** with sync/async implementations
- **Full backward compatibility** with existing interfaces
- **Enhanced type safety** with strict Literal types
- **Consistent architecture** following knowledge-design patterns

### Key Features
- **Comprehensive Coverage**: Full implementation of all 22 chat APIs with consistent architecture
- **Multi-resource Organization**: Logical separation of concerns across chat, file, feedback, conversation, audio, app, and annotation resources
- **Advanced Type Safety**: Strict typing with Literal types for all predefined values
- **Streaming Support**: Complete streaming and blocking response modes with proper overloads
- **File Processing**: Complete file upload and management capabilities with multipart/form-data support
- **Audio Processing**: Speech-to-text and text-to-speech capabilities with binary file handling
- **Conversation Management**: Full conversation lifecycle management with variables support
- **Feedback System**: Comprehensive feedback collection and analysis with rating system
- **Application Configuration**: Complete application information and settings management
- **Annotation System**: Full annotation management and reply configuration with async job status
- **Code Minimalism**: All chat examples follow minimal code principles
- **Safety Features**: Comprehensive validation and error handling mechanisms
- **Educational Focus**: Examples focus purely on demonstrating API functionality
- **Consistent Patterns**: Uniform architecture and naming conventions across all resources
- **Migration Support**: Complete backward compatibility with existing implementations
- **Builder Patterns**: Consistent builder patterns for all Request, RequestBody, and public model classes
- **Error Handling**: All Response classes inherit from BaseResponse for consistent error management
- **Flat Model Structure**: Simplified import paths with flat model organization
- **Comprehensive Testing**: Complete test coverage for all APIs with model, resource, and integration tests
- **Documentation Consistency**: Accurate documentation matching all implemented APIs and features