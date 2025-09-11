# Chatflow API Implementation Plan

## Overview

This document provides a comprehensive step-by-step implementation plan for the Chatflow API module in dify-oapi2. The plan is based on the chatflow-api.md and chatflow-design.md specifications, covering all 17 chatflow-related APIs across 6 resource categories.

**Total APIs**: 17 endpoints across 6 resources:
- **Chatflow**: 3 APIs (send, stop, suggested)
- **File**: 1 API (upload)
- **Feedback**: 2 APIs (message, list)
- **Conversation**: 5 APIs (messages, list, delete, rename, variables)
- **TTS**: 2 APIs (speech_to_text, text_to_audio)
- **Application**: 4 APIs (info, parameters, meta, site)
- **Annotation**: 6 APIs (list, create, update, delete, reply_settings, reply_status)

## Implementation Steps

### Step 1: Create Module Structure

**Implementation Prompt:**
```
Create the basic module structure for the Chatflow API in dify-oapi2.

Requirements:
1. Create directory structure:
   - `dify_oapi/api/chatflow/`
   - `dify_oapi/api/chatflow/v1/`
   - `dify_oapi/api/chatflow/v1/model/`
   - `dify_oapi/api/chatflow/v1/resource/`

2. Create initial files:
   - `dify_oapi/api/chatflow/__init__.py`
   - `dify_oapi/api/chatflow/v1/__init__.py`
   - `dify_oapi/api/chatflow/v1/model/__init__.py`
   - `dify_oapi/api/chatflow/v1/resource/__init__.py`

3. Follow the established pattern from other API modules (chat, completion, knowledge)
4. Ensure proper module exports and imports
```

**Testing Prompt:**
```
Create tests to validate the module structure.

Requirements:
1. Create `tests/chatflow/` directory structure
2. Create `tests/chatflow/__init__.py`
3. Create `tests/chatflow/v1/__init__.py`
4. Test module imports work correctly
5. Verify directory structure matches specification
```

### Step 2: Implement Chatflow Types

**Implementation Prompt:**
```
Implement strict type definitions for all Chatflow API enums and constants.

Requirements:
1. Create `dify_oapi/api/chatflow/v1/model/chatflow_types.py`
2. Define all Literal types based on the API specification:
   - ResponseMode = Literal["streaming", "blocking"]
   - FileType = Literal["document", "image", "audio", "video", "custom"]
   - TransferMethod = Literal["remote_url", "local_file"]
   - StreamEvent = Literal["message", "message_file", "message_end", "tts_message", "tts_message_end", "message_replace", "workflow_started", "node_started", "node_finished", "workflow_finished", "error", "ping"]
   - MessageFileBelongsTo = Literal["user", "assistant"]
   - FeedbackRating = Literal["like", "dislike"]
   - SortBy = Literal["created_at", "-created_at", "updated_at", "-updated_at"]
   - ConversationStatus = Literal["normal", "archived"]
   - VariableValueType = Literal["string", "number", "select"]
   - FormInputType = Literal["text-input", "paragraph", "select"]
   - JobStatus = Literal["waiting", "running", "completed", "failed"]
   - AudioFormat = Literal["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]
   - LanguageCode = Literal["en", "zh", "ja", "ko", "es", "fr", "de", "it", "pt", "ru"]
   - ChatColorTheme = Literal["blue", "green", "purple", "orange", "red"]
   - DefaultLanguage = Literal["en-US", "zh-Hans", "zh-Hant", "ja-JP", "ko-KR", "es-ES", "fr-FR", "de-DE", "it-IT", "pt-BR", "ru-RU"]
   - IconType = Literal["emoji", "image"]
   - AutoPlay = Literal["enabled", "disabled"]
   - AnnotationAction = Literal["enable", "disable"]
   - NodeStatus = Literal["running", "succeeded", "failed", "stopped"]
   - WorkflowStatus = Literal["running", "succeeded", "failed", "stopped"]

3. Use strict typing with no generic strings
4. Include comprehensive docstrings for each type
5. Follow the established pattern from other modules
```

**Testing Prompt:**
```
Create comprehensive tests for all Chatflow types.

Requirements:
1. Create `tests/chatflow/v1/model/test_chatflow_types.py`
2. Test all Literal type definitions
3. Verify type constraints work correctly
4. Test invalid values are rejected
5. Ensure all enum values match API specification
```

### Step 3: Implement Core Public Models

**Implementation Prompt:**
```
Implement core public model classes that will be shared across multiple APIs.

Requirements:
1. Create public model files with builder patterns:
   - `chat_message.py` - Core chat message model
   - `chat_file.py` - File attachment model
   - `file_info.py` - File information model
   - `conversation_info.py` - Conversation information model
   - `feedback_info.py` - Feedback information model
   - `app_info.py` - Application information model
   - `annotation_info.py` - Annotation information model
   - `usage_info.py` - Token usage information model
   - `retriever_resource.py` - Knowledge retrieval resource model

2. All models must:
   - Inherit from pydantic.BaseModel
   - Include comprehensive builder patterns
   - Use strict typing with Literal types from chatflow_types.py
   - Include proper field validation
   - Follow established naming conventions

3. Key model specifications:
   - ChatMessage: id, conversation_id, inputs, query, answer, message_files, feedback, retriever_resources, created_at
   - ChatFile: type (FileType), transfer_method (TransferMethod), url, upload_file_id
   - FileInfo: id, name, size, extension, mime_type, created_by, created_at
   - ConversationInfo: id, name, inputs, status, introduction, created_at, updated_at
   - FeedbackInfo: id, app_id, conversation_id, message_id, rating, content, from_source, from_end_user_id, from_account_id, created_at, updated_at
   - AppInfo: name, description, tags
   - AnnotationInfo: id, question, answer, hit_count, created_at
```

**Testing Prompt:**
```
Create comprehensive tests for all public model classes.

Requirements:
1. Create `tests/chatflow/v1/model/test_chatflow_public_models.py`
2. Test all public model classes:
   - Builder pattern functionality
   - Field validation
   - Type constraints
   - Required vs optional fields
   - Default values
3. Verify models work with real API data structures
4. Test serialization and deserialization
```

### Step 4: Implement Chatflow API Models (3 APIs)

**Implementation Prompt:**
```
Implement all request and response models for the Chatflow resource (3 APIs).

Requirements:
1. Create request models:
   - `send_chat_message_request.py` + `send_chat_message_request_body.py`
     * POST /v1/chat-messages
     * Fields: query (required), inputs, response_mode, user (required), conversation_id, files, auto_generate_name
     * Support streaming and blocking modes
   - `stop_chat_message_request.py` + `stop_chat_message_request_body.py`
     * POST /v1/chat-messages/{task_id}/stop
     * Path param: task_id (required)
     * Fields: user (required)
   - `get_suggested_questions_request.py`
     * GET /v1/messages/{message_id}/suggested
     * Path param: message_id (required)
     * Query param: user (required)

2. Create response models (ALL must inherit from BaseResponse):
   - `send_chat_message_response.py` - Inherits from ChatMessage and BaseResponse
   - `stop_chat_message_response.py` - Simple success response
   - `get_suggested_questions_response.py` - Contains suggested questions array

3. Handle complex nested objects:
   - File attachments with proper multipart support
   - Streaming event handling
   - Workflow events and metadata
   - Usage information and retriever resources

4. All models must:
   - Use builder patterns
   - Include proper validation
   - Use strict typing with Literal types
   - Follow established naming conventions
   - Handle both sync and async scenarios
```

**Testing Prompt:**
```
Create comprehensive tests for all Chatflow API models.

Requirements:
1. Create `tests/chatflow/v1/model/test_chatflow_models.py`
2. Test classes for each API:
   - TestSendChatMessageModels
   - TestStopChatMessageModels
   - TestGetSuggestedQuestionsModels
3. Test all request, request body, and response models
4. Verify BaseResponse inheritance for all response classes
5. Test streaming vs blocking mode handling
6. Test file attachment handling
7. Test path parameter and query parameter handling
```

### Step 5: Implement Chatflow Resource Class

**Implementation Prompt:**
```
Implement the Chatflow resource class with all 3 chatflow operations.

Requirements:
1. Create `dify_oapi/api/chatflow/v1/resource/chatflow.py`
2. Implement methods with proper overloads for streaming:
   - `send()` - Send chat message (sync + async, streaming + blocking)
   - `stop()` - Stop chat message generation (sync + async)
   - `suggested()` - Get suggested questions (sync + async)

3. Method signatures:
   ```python
   @overload
   def send(self, request: SendChatMessageRequest, request_option: RequestOption, stream: Literal[True]) -> Generator[bytes, None, None]: ...
   
   @overload
   def send(self, request: SendChatMessageRequest, request_option: RequestOption, stream: Literal[False] = False) -> SendChatMessageResponse: ...

   def send(self, request: SendChatMessageRequest, request_option: RequestOption, stream: bool = False) -> SendChatMessageResponse | Generator[bytes, None, None]:
       # Implementation with Transport.execute
   
   async def asend(self, request: SendChatMessageRequest, request_option: RequestOption, stream: bool = False) -> SendChatMessageResponse | AsyncGenerator[bytes, None]:
       # Async implementation with ATransport.aexecute
   ```

4. Include proper error handling and response unmarshaling
5. Follow established patterns from other resource classes
```

**Testing Prompt:**
```
Create comprehensive tests for the Chatflow resource class.

Requirements:
1. Create `tests/chatflow/v1/resource/test_chatflow_resource.py`
2. Test all chatflow resource methods:
   - send() method with streaming and blocking modes
   - stop() method
   - suggested() method
3. Test both sync and async variants
4. Mock Transport.execute and ATransport.aexecute calls
5. Test error handling scenarios
6. Verify proper request/response handling
```

### Step 6: Implement File API Models (1 API)

**Implementation Prompt:**
```
Implement request and response models for the File resource (1 API).

Requirements:
1. Create request model:
   - `upload_file_request.py`
     * POST /v1/files/upload
     * Multipart form-data support
     * Fields: file (binary, required), user (string, required)
     * Handle BytesIO file objects

2. Create response model (must inherit from BaseResponse):
   - `upload_file_response.py` - Inherits from FileInfo and BaseResponse

3. Handle multipart/form-data properly:
   - Use files attribute in BaseRequest
   - Support file name and content type detection
   - Handle binary file data correctly

4. Follow established patterns for file upload handling
```

**Testing Prompt:**
```
Create comprehensive tests for File API models.

Requirements:
1. Create `tests/chatflow/v1/model/test_file_models.py`
2. Test class: TestUploadFileModels
3. Test file upload request handling
4. Test multipart form-data structure
5. Test response model inheritance from BaseResponse
6. Test file handling with BytesIO objects
```

### Step 7: Implement File Resource Class

**Implementation Prompt:**
```
Implement the File resource class with file upload functionality.

Requirements:
1. Create `dify_oapi/api/chatflow/v1/resource/file.py`
2. Implement methods:
   - `upload()` - Upload file (sync + async)

3. Handle multipart form-data properly
4. Include proper error handling for file operations
5. Support various file types and size limits
```

**Testing Prompt:**
```
Create comprehensive tests for the File resource class.

Requirements:
1. Create `tests/chatflow/v1/resource/test_file_resource.py`
2. Test file upload functionality
3. Test both sync and async variants
4. Test error scenarios (file too large, unsupported type)
5. Mock file upload operations
```

### Step 8: Implement Feedback API Models (2 APIs)

**Implementation Prompt:**
```
Implement request and response models for the Feedback resource (2 APIs).

Requirements:
1. Create request models:
   - `message_feedback_request.py` + `message_feedback_request_body.py`
     * POST /v1/messages/{message_id}/feedbacks
     * Path param: message_id (required)
     * Fields: rating (FeedbackRating | None), user (required), content (optional)
   - `get_app_feedbacks_request.py`
     * GET /v1/app/feedbacks
     * Query params: page (optional), limit (optional)

2. Create response models (ALL must inherit from BaseResponse):
   - `message_feedback_response.py` - Simple success response
   - `get_app_feedbacks_response.py` - Contains feedback list with pagination

3. Handle feedback rating types properly using Literal types
4. Include pagination support for feedback list
```

**Testing Prompt:**
```
Create comprehensive tests for Feedback API models.

Requirements:
1. Create `tests/chatflow/v1/model/test_feedback_models.py`
2. Test classes:
   - TestMessageFeedbackModels
   - TestGetAppFeedbacksModels
3. Test feedback rating validation
4. Test pagination parameters
5. Test BaseResponse inheritance
```

### Step 9: Implement Feedback Resource Class

**Implementation Prompt:**
```
Implement the Feedback resource class with feedback operations.

Requirements:
1. Create `dify_oapi/api/chatflow/v1/resource/feedback.py`
2. Implement methods:
   - `message()` - Provide message feedback (sync + async)
   - `list()` - Get application feedbacks (sync + async)

3. Handle path parameters and query parameters properly
4. Include proper error handling
```

**Testing Prompt:**
```
Create comprehensive tests for the Feedback resource class.

Requirements:
1. Create `tests/chatflow/v1/resource/test_feedback_resource.py`
2. Test all feedback resource methods
3. Test both sync and async variants
4. Test error scenarios
5. Mock API calls properly
```

### Step 10: Implement Conversation API Models (5 APIs)

**Implementation Prompt:**
```
Implement request and response models for the Conversation resource (5 APIs).

Requirements:
1. Create request models:
   - `get_conversation_messages_request.py`
     * GET /v1/messages
     * Query params: conversation_id (required), user (required), first_id (optional), limit (optional)
   - `get_conversations_request.py`
     * GET /v1/conversations
     * Query params: user (required), last_id (optional), limit (optional), sort_by (optional)
   - `delete_conversation_request.py` + `delete_conversation_request_body.py`
     * DELETE /v1/conversations/{conversation_id}
     * Path param: conversation_id (required)
     * Fields: user (required)
   - `rename_conversation_request.py` + `rename_conversation_request_body.py`
     * POST /v1/conversations/{conversation_id}/name
     * Path param: conversation_id (required)
     * Fields: name (optional), auto_generate (optional), user (required)
   - `get_conversation_variables_request.py`
     * GET /v1/conversations/{conversation_id}/variables
     * Path param: conversation_id (required)
     * Query params: user (required), last_id (optional), limit (optional), variable_name (optional)

2. Create response models (ALL must inherit from BaseResponse):
   - `get_conversation_messages_response.py` - Message list with pagination
   - `get_conversations_response.py` - Conversation list with pagination
   - `delete_conversation_response.py` - No content response
   - `rename_conversation_response.py` - Updated conversation info
   - `get_conversation_variables_response.py` - Variable list with pagination

3. Handle pagination properly for all list endpoints
4. Use SortBy Literal type for sorting options
5. Include conversation variables with proper typing
```

**Testing Prompt:**
```
Create comprehensive tests for Conversation API models.

Requirements:
1. Create `tests/chatflow/v1/model/test_conversation_models.py`
2. Test classes for each API:
   - TestGetConversationMessagesModels
   - TestGetConversationsModels
   - TestDeleteConversationModels
   - TestRenameConversationModels
   - TestGetConversationVariablesModels
3. Test pagination handling
4. Test sorting options
5. Test BaseResponse inheritance
6. Test path and query parameter handling
```

### Step 11: Implement Conversation Resource Class

**Implementation Prompt:**
```
Implement the Conversation resource class with all conversation operations.

Requirements:
1. Create `dify_oapi/api/chatflow/v1/resource/conversation.py`
2. Implement methods:
   - `messages()` - Get conversation messages (sync + async)
   - `list()` - Get conversations list (sync + async)
   - `delete()` - Delete conversation (sync + async)
   - `rename()` - Rename conversation (sync + async)
   - `variables()` - Get conversation variables (sync + async)

3. Handle pagination properly for list methods
4. Include proper error handling
5. Support sorting and filtering options
```

**Testing Prompt:**
```
Create comprehensive tests for the Conversation resource class.

Requirements:
1. Create `tests/chatflow/v1/resource/test_conversation_resource.py`
2. Test all conversation resource methods
3. Test both sync and async variants
4. Test pagination functionality
5. Test error scenarios
6. Mock API calls properly
```

### Step 12: Implement TTS API Models (2 APIs)

**Implementation Prompt:**
```
Implement request and response models for the TTS resource (2 APIs).

Requirements:
1. Create request models:
   - `audio_to_text_request.py`
     * POST /v1/audio-to-text
     * Multipart form-data: file (binary, required), user (string, required)
     * Support audio formats: mp3, mp4, mpeg, mpga, m4a, wav, webm
   - `text_to_audio_request.py` + `text_to_audio_request_body.py`
     * POST /v1/text-to-audio
     * Fields: message_id (optional), text (optional), user (required), streaming (optional)

2. Create response models (ALL must inherit from BaseResponse):
   - `audio_to_text_response.py` - Contains transcribed text
   - `text_to_audio_response.py` - Binary audio data response

3. Handle audio file uploads with proper multipart support
4. Support both message_id and text input for TTS
5. Handle binary audio response data
```

**Testing Prompt:**
```
Create comprehensive tests for TTS API models.

Requirements:
1. Create `tests/chatflow/v1/model/test_tts_models.py`
2. Test classes:
   - TestAudioToTextModels
   - TestTextToAudioModels
3. Test audio file upload handling
4. Test audio format validation
5. Test binary response handling
6. Test BaseResponse inheritance
```

### Step 13: Implement TTS Resource Class

**Implementation Prompt:**
```
Implement the TTS resource class with audio processing operations.

Requirements:
1. Create `dify_oapi/api/chatflow/v1/resource/tts.py`
2. Implement methods:
   - `speech_to_text()` - Convert audio to text (sync + async)
   - `text_to_audio()` - Convert text to audio (sync + async)

3. Handle audio file uploads properly
4. Support streaming audio responses
5. Include proper error handling for audio operations
```

**Testing Prompt:**
```
Create comprehensive tests for the TTS resource class.

Requirements:
1. Create `tests/chatflow/v1/resource/test_tts_resource.py`
2. Test all TTS resource methods
3. Test both sync and async variants
4. Test audio file handling
5. Test error scenarios
6. Mock audio processing operations
```

### Step 14: Implement Application API Models (4 APIs)

**Implementation Prompt:**
```
Implement request and response models for the Application resource (4 APIs).

Requirements:
1. Create request models (all GET requests, no request bodies):
   - `get_info_request.py` - GET /v1/info
   - `get_parameters_request.py` - GET /v1/parameters
   - `get_meta_request.py` - GET /v1/meta
   - `get_site_request.py` - GET /v1/site

2. Create response models (ALL must inherit from BaseResponse):
   - `get_info_response.py` - Basic app information
   - `get_parameters_response.py` - Complex app parameters with nested objects
   - `get_meta_response.py` - Tool icons and meta information
   - `get_site_response.py` - WebApp settings

3. Handle complex nested objects in parameters response:
   - User input forms with different types (text-input, paragraph, select)
   - File upload configurations
   - TTS settings
   - System parameters

4. Use proper Literal types for all enum values:
   - ChatColorTheme, DefaultLanguage, IconType, AutoPlay, etc.
```

**Testing Prompt:**
```
Create comprehensive tests for Application API models.

Requirements:
1. Create `tests/chatflow/v1/model/test_application_models.py`
2. Test classes for each API:
   - TestGetInfoModels
   - TestGetParametersModels
   - TestGetMetaModels
   - TestGetSiteModels
3. Test complex nested object handling
4. Test enum value validation
5. Test BaseResponse inheritance
```

### Step 15: Implement Application Resource Class

**Implementation Prompt:**
```
Implement the Application resource class with configuration operations.

Requirements:
1. Create `dify_oapi/api/chatflow/v1/resource/application.py`
2. Implement methods:
   - `info()` - Get application basic information (sync + async)
   - `parameters()` - Get application parameters (sync + async)
   - `meta()` - Get application meta information (sync + async)
   - `site()` - Get application WebApp settings (sync + async)

3. All methods are simple GET requests
4. Include proper error handling
5. Handle complex response structures
```

**Testing Prompt:**
```
Create comprehensive tests for the Application resource class.

Requirements:
1. Create `tests/chatflow/v1/resource/test_application_resource.py`
2. Test all application resource methods
3. Test both sync and async variants
4. Test complex response handling
5. Test error scenarios
6. Mock API calls properly
```

### Step 16: Implement Annotation API Models (6 APIs)

**Implementation Prompt:**
```
Implement request and response models for the Annotation resource (6 APIs).

Requirements:
1. Create request models:
   - `get_annotations_request.py`
     * GET /v1/apps/annotations
     * Query params: page (optional), limit (optional)
   - `create_annotation_request.py` + `create_annotation_request_body.py`
     * POST /v1/apps/annotations
     * Fields: question (required), answer (required)
   - `update_annotation_request.py` + `update_annotation_request_body.py`
     * PUT /v1/apps/annotations/{annotation_id}
     * Path param: annotation_id (required)
     * Fields: question (required), answer (required)
   - `delete_annotation_request.py`
     * DELETE /v1/apps/annotations/{annotation_id}
     * Path param: annotation_id (required)
   - `annotation_reply_settings_request.py` + `annotation_reply_settings_request_body.py`
     * POST /v1/apps/annotation-reply/{action}
     * Path param: action (AnnotationAction: "enable" | "disable")
     * Fields: embedding_provider_name (optional), embedding_model_name (optional), score_threshold (required)
   - `annotation_reply_status_request.py`
     * GET /v1/apps/annotation-reply/{action}/status/{job_id}
     * Path params: action (AnnotationAction), job_id (required)

2. Create response models (ALL must inherit from BaseResponse):
   - `get_annotations_response.py` - Annotation list with pagination
   - `create_annotation_response.py` - Created annotation info
   - `update_annotation_response.py` - Updated annotation info
   - `delete_annotation_response.py` - No content response
   - `annotation_reply_settings_response.py` - Job information
   - `annotation_reply_status_response.py` - Job status information

3. Use AnnotationAction Literal type for action parameters
4. Handle job status tracking properly
5. Include pagination for annotation list
```

**Testing Prompt:**
```
Create comprehensive tests for Annotation API models.

Requirements:
1. Create `tests/chatflow/v1/model/test_annotation_models.py`
2. Test classes for each API:
   - TestGetAnnotationsModels
   - TestCreateAnnotationModels
   - TestUpdateAnnotationModels
   - TestDeleteAnnotationModels
   - TestAnnotationReplySettingsModels
   - TestAnnotationReplyStatusModels
3. Test annotation action validation
4. Test job status handling
5. Test BaseResponse inheritance
6. Test pagination handling
```

### Step 17: Implement Annotation Resource Class

**Implementation Prompt:**
```
Implement the Annotation resource class with annotation management operations.

Requirements:
1. Create `dify_oapi/api/chatflow/v1/resource/annotation.py`
2. Implement methods:
   - `list()` - Get annotation list (sync + async)
   - `create()` - Create annotation (sync + async)
   - `update()` - Update annotation (sync + async)
   - `delete()` - Delete annotation (sync + async)
   - `reply_settings()` - Configure annotation reply settings (sync + async)
   - `reply_status()` - Get annotation reply status (sync + async)

3. Handle path parameters properly for action and job_id
4. Include proper error handling
5. Support pagination for list method
```

**Testing Prompt:**
```
Create comprehensive tests for the Annotation resource class.

Requirements:
1. Create `tests/chatflow/v1/resource/test_annotation_resource.py`
2. Test all annotation resource methods
3. Test both sync and async variants
4. Test path parameter handling
5. Test error scenarios
6. Mock API calls properly
```

### Step 18: Implement Version Integration

**Implementation Prompt:**
```
Implement the Chatflow V1 version class that integrates all 6 resources.

Requirements:
1. Create `dify_oapi/api/chatflow/v1/version.py`
2. Implement V1 class with all 6 resources:
   - self.chatflow = Chatflow(config)
   - self.file = File(config)
   - self.feedback = Feedback(config)
   - self.conversation = Conversation(config)
   - self.tts = TTS(config)
   - self.application = Application(config)
   - self.annotation = Annotation(config)

3. Follow existing patterns from chat/completion modules
4. Include proper initialization and configuration
5. Ensure all resources are properly exposed
```

**Testing Prompt:**
```
Create comprehensive tests for the Chatflow V1 version integration.

Requirements:
1. Create `tests/chatflow/v1/test_version_integration.py`
2. Test V1 class initialization
3. Verify all 6 resources are properly accessible
4. Test configuration passing to resources
5. Validate resource method accessibility
```

### Step 19: Implement Service Integration

**Implementation Prompt:**
```
Implement the Chatflow service class that provides access to API versions.

Requirements:
1. Create `dify_oapi/api/chatflow/service.py`
2. Implement ChatflowService class with v1 property
3. Follow existing patterns from other API services
4. Include proper initialization and version management
```

**Testing Prompt:**
```
Create tests for the Chatflow service class.

Requirements:
1. Create `tests/chatflow/test_service_integration.py`
2. Test service initialization
3. Verify v1 version accessibility
4. Test configuration propagation
```

### Step 20: Implement Client Integration

**Implementation Prompt:**
```
Integrate the Chatflow API service into the main dify-oapi client.

Requirements:
1. Update `dify_oapi/client.py` to include chatflow service
2. Add self.chatflow = ChatflowService(self.config) to Client class
3. Ensure proper initialization order
4. Follow existing patterns for other API services
5. Update any necessary imports and exports
```

**Testing Prompt:**
```
Create comprehensive tests for Chatflow API client integration.

Requirements:
1. Create `tests/chatflow/test_client_integration.py`
2. Test client initialization with chatflow service
3. Verify chatflow API accessibility through client
4. Test end-to-end API access patterns
5. Validate configuration propagation through all layers
```

### Step 21: Create Chatflow Examples

**Implementation Prompt:**
```
Create comprehensive examples for all Chatflow APIs (3 APIs).

Requirements:
1. Create examples in `examples/chatflow/chatflow/`:
   - send_chat_message.py: Sync, async, streaming, and blocking examples
   - stop_chat_message.py: Sync and async examples
   - get_suggested_questions.py: Sync and async examples

2. All examples must:
   - Use "[Example]" prefix for safety
   - Validate environment variables (API_KEY)
   - Include minimal code with essential functionality
   - Demonstrate both sync and async usage
   - Include proper error handling
   - Use realistic test data
   - Show streaming vs blocking modes for send_chat_message

3. Example structure for send_chat_message.py:
   - Basic blocking chat example
   - Streaming chat example
   - File attachment example
   - Async variants of all above
```

**Testing Prompt:**
```
Create tests to validate all Chatflow examples.

Requirements:
1. Create `tests/chatflow/v1/integration/test_chatflow_examples.py`
2. Test all chatflow examples for:
   - Syntax validation
   - Import correctness
   - Environment variable handling
   - Safety prefix usage
   - Error handling coverage
3. Mock external API calls
4. Verify example completeness and accuracy
5. Ensure all 3 chatflow APIs are covered
```

### Step 22: Create File Examples

**Implementation Prompt:**
```
Create comprehensive examples for File API (1 API).

Requirements:
1. Create examples in `examples/chatflow/file/`:
   - upload_file.py: Sync and async file upload examples

2. Include examples for different file types:
   - Document upload (PDF, TXT, etc.)
   - Image upload (JPG, PNG, etc.)
   - Audio upload (MP3, WAV, etc.)

3. Follow same safety and quality standards as other examples
4. Show proper file handling with BytesIO
```

**Testing Prompt:**
```
Create tests to validate File examples.

Requirements:
1. Create `tests/chatflow/v1/integration/test_file_examples.py`
2. Test file upload examples
3. Test different file type handling
4. Mock file operations
5. Verify error handling
```

### Step 23: Create Feedback Examples

**Implementation Prompt:**
```
Create comprehensive examples for Feedback APIs (2 APIs).

Requirements:
1. Create examples in `examples/chatflow/feedback/`:
   - message_feedback.py: Sync and async feedback examples
   - get_app_feedbacks.py: Sync and async feedback listing examples

2. Show different feedback types (like, dislike, with comments)
3. Include pagination examples for feedback listing
4. Follow established safety and quality standards
```

**Testing Prompt:**
```
Create tests to validate Feedback examples.

Requirements:
1. Create `tests/chatflow/v1/integration/test_feedback_examples.py`
2. Test all feedback examples
3. Test pagination handling
4. Mock API calls
5. Verify error handling
```

### Step 24: Create Conversation Examples

**Implementation Prompt:**
```
Create comprehensive examples for Conversation APIs (5 APIs).

Requirements:
1. Create examples in `examples/chatflow/conversation/`:
   - get_conversation_messages.py: Message history examples
   - get_conversations.py: Conversation listing examples
   - delete_conversation.py: Conversation deletion examples
   - rename_conversation.py: Conversation renaming examples
   - get_conversation_variables.py: Variable retrieval examples

2. Include pagination examples for list operations
3. Show sorting options for conversation listing
4. Include auto-generate name examples
5. Follow established safety and quality standards
```

**Testing Prompt:**
```
Create tests to validate Conversation examples.

Requirements:
1. Create `tests/chatflow/v1/integration/test_conversation_examples.py`
2. Test all conversation examples
3. Test pagination and sorting
4. Mock API calls
5. Verify error handling
```

### Step 25: Create TTS Examples

**Implementation Prompt:**
```
Create comprehensive examples for TTS APIs (2 APIs).

Requirements:
1. Create examples in `examples/chatflow/tts/`:
   - audio_to_text.py: Speech-to-text examples
   - text_to_audio.py: Text-to-speech examples

2. Include examples for different audio formats
3. Show both message_id and text input for TTS
4. Handle binary audio data properly
5. Follow established safety and quality standards
```

**Testing Prompt:**
```
Create tests to validate TTS examples.

Requirements:
1. Create `tests/chatflow/v1/integration/test_tts_examples.py`
2. Test all TTS examples
3. Test audio file handling
4. Mock audio processing
5. Verify error handling
```

### Step 26: Create Application Examples

**Implementation Prompt:**
```
Create comprehensive examples for Application APIs (4 APIs).

Requirements:
1. Create examples in `examples/chatflow/application/`:
   - get_info.py: Basic app information examples
   - get_parameters.py: App parameters examples
   - get_meta.py: App meta information examples
   - get_site.py: WebApp settings examples

2. Show how to handle complex nested response structures
3. Include examples for different configuration types
4. Follow established safety and quality standards
```

**Testing Prompt:**
```
Create tests to validate Application examples.

Requirements:
1. Create `tests/chatflow/v1/integration/test_application_examples.py`
2. Test all application examples
3. Test complex response handling
4. Mock API calls
5. Verify error handling
```

### Step 27: Create Annotation Examples

**Implementation Prompt:**
```
Create comprehensive examples for Annotation APIs (6 APIs).

Requirements:
1. Create examples in `examples/chatflow/annotation/`:
   - get_annotations.py: Annotation listing examples
   - create_annotation.py: Annotation creation examples
   - update_annotation.py: Annotation update examples
   - delete_annotation.py: Annotation deletion examples
   - annotation_reply_settings.py: Reply settings examples
   - annotation_reply_status.py: Reply status examples

2. Include pagination examples for annotation listing
3. Show both enable and disable actions for reply settings
4. Include job status polling examples
5. Follow established safety and quality standards
```

**Testing Prompt:**
```
Create tests to validate Annotation examples.

Requirements:
1. Create `tests/chatflow/v1/integration/test_annotation_examples.py`
2. Test all annotation examples
3. Test job status handling
4. Mock API calls
5. Verify error handling
```

### Step 28: Create Examples README

**Implementation Prompt:**
```
Create comprehensive README documentation for all Chatflow examples.

Requirements:
1. Create `examples/chatflow/README.md`
2. Document all 17 APIs with usage examples
3. Include setup instructions and environment variables
4. Organize by resource categories (6 resources)
5. Include both sync and async usage patterns
6. Document streaming vs blocking modes
7. Include file upload examples
8. Document error handling patterns
```

**Testing Prompt:**
```
Create tests to validate Examples README accuracy.

Requirements:
1. Create `tests/chatflow/v1/integration/test_examples_readme.py`
2. Verify all APIs are documented
3. Check example code syntax
4. Validate environment variable documentation
5. Ensure completeness and accuracy
```

### Step 29: Integration Testing

**Implementation Prompt:**
```
Create comprehensive integration tests for all Chatflow APIs.

Requirements:
1. Create `tests/chatflow/v1/integration/test_chatflow_api_integration.py`
2. Test end-to-end API workflows:
   - Complete chat conversation flow
   - File upload and usage in chat
   - Feedback collection and retrieval
   - Conversation management lifecycle
   - TTS operations
   - Application configuration access
   - Annotation management workflow

3. Test error scenarios and edge cases
4. Mock all external API calls
5. Verify proper request/response handling
6. Test both sync and async operations
```

**Testing Prompt:**
```
Create validation tests for integration test coverage.

Requirements:
1. Create `tests/chatflow/v1/integration/test_integration_coverage.py`
2. Verify all 17 APIs are covered in integration tests
3. Check error scenario coverage
4. Validate mock usage
5. Ensure comprehensive test coverage
```

### Step 30: Final Validation and Documentation

**Implementation Prompt:**
```
Perform final validation and update all documentation.

Requirements:
1. Update main project README to include Chatflow API
2. Update API documentation with Chatflow endpoints
3. Verify all imports and exports work correctly
4. Run comprehensive test suite
5. Validate code quality (ruff, mypy)
6. Ensure 100% test coverage
7. Update version numbers if needed
8. Create migration guide for users

Final checklist:
- [ ] All 17 APIs implemented and tested
- [ ] All 6 resources properly integrated
- [ ] Client integration working
- [ ] Examples complete and tested
- [ ] Documentation updated
- [ ] Code quality checks pass
- [ ] Test coverage at 100%
```

**Testing Prompt:**
```
Create final validation tests.

Requirements:
1. Create `tests/chatflow/test_final_validation.py`
2. Test complete client integration
3. Verify all APIs accessible through client
4. Test example code execution
5. Validate documentation accuracy
6. Ensure no regressions in existing functionality
```

## Implementation Validation Checklist

### Model Validation
- [ ] All Request classes inherit from BaseRequest
- [ ] All Response classes inherit from BaseResponse
- [ ] All models implement Builder pattern
- [ ] Use strict Literal type definitions
- [ ] Correct field validation and type constraints
- [ ] Proper HTTP method and URI configuration
- [ ] Path parameters use colon notation in URI templates
- [ ] Query parameters handled correctly
- [ ] Request body serialization works properly
- [ ] File uploads handled correctly (where applicable)

### Resource Validation
- [ ] All resource classes correctly implement sync and async methods
- [ ] Correct error handling and type annotations
- [ ] Proper integration with Transport layer
- [ ] Support streaming and blocking modes (applicable APIs)
- [ ] Correct handling of file uploads and binary responses
- [ ] Pagination functionality works correctly
- [ ] Path parameter handling implemented properly
- [ ] Query parameter filtering works as expected

### Integration Validation
- [ ] V1 version correctly integrates all 6 resources
- [ ] All 17 APIs can be called correctly
- [ ] Configuration and dependency injection work correctly
- [ ] Consistent with existing architecture
- [ ] ChatflowService properly integrated into main Client
- [ ] All imports and exports work correctly
- [ ] No regressions in existing functionality

### Testing Validation
- [ ] All model tests pass
- [ ] All resource tests pass
- [ ] Integration tests cover all APIs
- [ ] Test coverage reaches expected standards
- [ ] Error handling scenarios adequately tested
- [ ] Streaming functionality tested
- [ ] File upload functionality tested
- [ ] Binary response handling tested
- [ ] Pagination functionality tested
- [ ] Mock usage validated

### Example Validation
- [ ] All 17 APIs have corresponding examples
- [ ] Example code syntax correct and runnable
- [ ] Include both sync and async usage methods
- [ ] Complete error handling examples
- [ ] Environment variable validation implemented
- [ ] Safety prefixes ("[Example]") used correctly
- [ ] README documentation accurate and complete
- [ ] Examples cover all major usage scenarios

### Quality Assurance Checklist

### Implementation Requirements
- [ ] **Module Structure**: Complete chatflow module with proper organization
- [ ] **Type Safety**: All Literal types implemented and used consistently
- [ ] **Model Classes**: All 85+ model files with builder patterns
- [ ] **Resource Classes**: All 6 resource classes with sync/async methods
- [ ] **BaseResponse Inheritance**: ALL response classes inherit from BaseResponse
- [ ] **Version Integration**: V1 class exposes all 6 resources
- [ ] **Client Integration**: ChatflowService integrated into main Client
- [ ] **Error Handling**: Comprehensive error handling throughout

### Testing Requirements
- [ ] **Unit Tests**: All model and resource tests implemented
- [ ] **Integration Tests**: End-to-end API testing
- [ ] **Example Tests**: All example files validated
- [ ] **Coverage**: 100% test coverage achieved
- [ ] **Quality Checks**: Ruff and MyPy pass without errors

### Documentation Requirements
- [ ] **API Documentation**: All 17 APIs documented
- [ ] **Examples**: All APIs have working examples
- [ ] **README Files**: Complete documentation for users
- [ ] **Migration Guide**: Clear upgrade path for users

### Validation Requirements
- [ ] **Functionality**: All APIs work correctly
- [ ] **Performance**: Acceptable response times
- [ ] **Reliability**: Proper error handling and recovery
- [ ] **Usability**: Clear and intuitive API interface

## Summary

This implementation plan breaks down the Chatflow API development into 30 specific steps, each containing detailed implementation requirements and corresponding test validation. This approach ensures:

1. **Code Quality**: Each step has corresponding tests to ensure code quality
2. **Type Safety**: Use strict Literal type definitions for complete type safety
3. **Architecture Consistency**: Follow existing design patterns and architecture specifications
4. **Functional Completeness**: Cover all 17 Chatflow API complete functionality
5. **Usability**: Provide clear usage examples and documentation

Each step's prompts can be directly given to AI for execution, ensuring implementation consistency and quality.

The plan follows established patterns from existing modules while introducing the multi-resource architecture needed for the diverse chatflow functionality. The emphasis on type safety, comprehensive testing, and clear documentation ensures a robust and maintainable implementation.

**Key Features Delivered:**
- Complete coverage of all 17 Chatflow APIs
- Multi-resource architecture with 6 specialized resources
- Streaming support for real-time chat
- File upload capabilities for multimodal interactions
- Comprehensive conversation management
- Feedback collection and analysis
- TTS integration for audio processing
- Application configuration access
- Annotation management system
- Type-safe implementation with strict Literal types
- Comprehensive testing strategy
- Complete example coverage
- Clear documentation and migration guides

The implementation will provide developers with a powerful, type-safe, and well-documented interface for building advanced chatflow applications using the Dify platform.

## API Endpoint Specifications

### Complete URI and HTTP Method Configuration

**All Chatflow API endpoints must be configured with exact URI patterns and HTTP methods:**

#### Chatflow APIs (3 endpoints)
- `POST /v1/chat-messages` → `SendChatMessageRequest`
- `POST /v1/chat-messages/{task_id}/stop` → `StopChatMessageRequest`
- `GET /v1/messages/{message_id}/suggested` → `GetSuggestedQuestionsRequest`

#### File APIs (1 endpoint)
- `POST /v1/files/upload` → `UploadFileRequest`

#### Feedback APIs (2 endpoints)
- `POST /v1/messages/{message_id}/feedbacks` → `MessageFeedbackRequest`
- `GET /v1/app/feedbacks` → `GetAppFeedbacksRequest`

#### Conversation APIs (5 endpoints)
- `GET /v1/messages` → `GetConversationMessagesRequest`
- `GET /v1/conversations` → `GetConversationsRequest`
- `DELETE /v1/conversations/{conversation_id}` → `DeleteConversationRequest`
- `POST /v1/conversations/{conversation_id}/name` → `RenameConversationRequest`
- `GET /v1/conversations/{conversation_id}/variables` → `GetConversationVariablesRequest`

#### TTS APIs (2 endpoints)
- `POST /v1/audio-to-text` → `AudioToTextRequest`
- `POST /v1/text-to-audio` → `TextToAudioRequest`

#### Application APIs (4 endpoints)
- `GET /v1/info` → `GetInfoRequest`
- `GET /v1/parameters` → `GetParametersRequest`
- `GET /v1/meta` → `GetMetaRequest`
- `GET /v1/site` → `GetSiteRequest`

#### Annotation APIs (6 endpoints)
- `GET /v1/apps/annotations` → `GetAnnotationsRequest`
- `POST /v1/apps/annotations` → `CreateAnnotationRequest`
- `PUT /v1/apps/annotations/{annotation_id}` → `UpdateAnnotationRequest`
- `DELETE /v1/apps/annotations/{annotation_id}` → `DeleteAnnotationRequest`
- `POST /v1/apps/annotation-reply/{action}` → `AnnotationReplySettingsRequest`
- `GET /v1/apps/annotation-reply/{action}/status/{job_id}` → `AnnotationReplyStatusRequest`

### Path Parameter Patterns

**Critical**: All path parameters must use colon notation in URI templates:
- `{task_id}` → `:task_id`
- `{message_id}` → `:message_id`
- `{conversation_id}` → `:conversation_id`
- `{annotation_id}` → `:annotation_id`
- `{action}` → `:action`
- `{job_id}` → `:job_id`

### Request Builder Configuration Requirements

**Every Request class builder must configure:**
1. **HTTP Method**: Set in constructor using `HttpMethod` enum
2. **URI Template**: Set in constructor with proper path parameter notation
3. **Path Parameters**: Use `self._request.paths["param_name"] = value` pattern
4. **Query Parameters**: Use `self._request.add_query("key", value)` pattern
5. **Request Body**: Use `self._request.body = request_body.model_dump()` for POST/PUT/PATCH
6. **Files**: Use `self._request.files = {"file": (filename, file_data)}` for multipart uploads

### Content Type Specifications

**Request Content Types:**
- **JSON APIs**: `application/json`
- **File Upload APIs**: `multipart/form-data`
- **Audio APIs**: `multipart/form-data` (for audio-to-text)

**Response Content Types:**
- **JSON APIs**: `application/json`
- **Streaming APIs**: `text/event-stream`
- **Audio APIs**: `audio/wav` or `audio/mp3` (for text-to-audio)

### Implementation Validation Checklist

**For each API endpoint, verify:**
- [ ] Correct HTTP method configured
- [ ] Exact URI pattern with proper path parameter notation
- [ ] All path parameters properly handled
- [ ] All query parameters properly handled
- [ ] Request body properly serialized
- [ ] File uploads properly handled (where applicable)
- [ ] Response unmarshaling configured correctly
- [ ] Error handling for all HTTP status codes
- [ ] Streaming support configured (where applicable)
- [ ] All `__init__.py` files remain empty (MANDATORY)

### Module Structure Rules (MANDATORY)

**__init__.py File Policy**:
- **STRICT RULE**: ALL `__init__.py` files MUST remain empty
- **Scope**: Applies to ALL directories including api/, model/, resource/, tests/, examples/
- **Zero Exceptions**: No `__init__.py` file may contain any code, imports, or exports
- **Import Pattern**: Always use direct imports from specific modules

**Correct Import Examples**:
```python
# ✅ CORRECT: Direct module imports
from dify_oapi.api.chatflow.service import ChatflowService
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow

# ❌ WRONG: Package-level imports
from dify_oapi.api.chatflow import ChatflowService  # NEVER
from dify_oapi.api.chatflow.v1.model import SendChatMessageRequest  # NEVER
```