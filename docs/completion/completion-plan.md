# Completion API Implementation Plan

Based on completion-api and completion-design documents, this plan breaks down the Completion API implementation into specific steps, with each implementation step followed by a testing step to ensure code quality.

## Overview

Completion API contains **9 APIs** distributed across **5 resource categories**:
- **Completion** (2 APIs): Message processing
- **File** (1 API): File upload  
- **Feedback** (2 APIs): Feedback management
- **Audio** (1 API): Audio processing
- **Info** (3 APIs): Application information

## Implementation Steps

### Step 1: Implement Completion Types Definition

**Implementation Prompt:**
```
Implement all type definitions for Completion API, ensuring strict type safety.

Requirements:
1. Create `dify_oapi/api/completion/v1/model/completion_types.py`
2. Ensure all necessary `__init__.py` files exist in the directory structure:
   - `dify_oapi/api/completion/v1/model/__init__.py`
   - `dify_oapi/api/completion/v1/model/completion/__init__.py`
   - `dify_oapi/api/completion/v1/model/file/__init__.py`
   - `dify_oapi/api/completion/v1/model/feedback/__init__.py`
   - `dify_oapi/api/completion/v1/model/audio/__init__.py`
   - `dify_oapi/api/completion/v1/model/info/__init__.py`
   - `dify_oapi/api/completion/v1/resource/__init__.py`
3. Define all Literal types based on API specifications:
   - ResponseMode = Literal["streaming", "blocking"]  # Response modes
   - FileType = Literal["image"]  # Supported file types
   - TransferMethod = Literal["remote_url", "local_file"]  # File transfer methods
   - Rating = Literal["like", "dislike"]  # Feedback rating types (nullable for revocation)
   - IconType = Literal["emoji", "image"]  # Icon types for WebApp
   - EventType = Literal["message", "message_end", "tts_message", "tts_message_end", "message_replace", "error", "ping"]  # SSE event types
   - UserInputFormType = Literal["text-input", "paragraph", "select"]  # Form control types
   - AudioFormat = Literal["mp3", "wav"]  # Audio output formats
   - ImageFormat = Literal["png", "jpg", "jpeg", "webp", "gif"]  # Supported image formats

4. Import Literal from typing_extensions for Python 3.10+ compatibility
5. Add clear docstrings explaining each type's purpose
6. Ensure all types match the API specification exactly
```

**Testing Prompt:**
```
Create comprehensive tests for Completion Types.

Requirements:
1. Create `tests/completion/v1/model/test_completion_types.py`
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
Implement all common model classes for Completion API that can be reused across multiple APIs.

Requirements:
1. Create common model files in `dify_oapi/api/completion/v1/model/`:
   - `input_file_object.py` - File input object for multimodal support
   - `completion_inputs.py` - Input parameters model with query field
   - `metadata.py` - Response metadata including usage and retriever_resources
   - `usage.py` - Token usage and pricing statistics
   - `retriever_resource.py` - Citation and attribution information
   - `file_info.py` - Uploaded file information
   - `feedback_info.py` - Feedback item information
   - `user_input_form.py` - User input form configuration models
   - `system_parameters.py` - System configuration parameters
   - `file_upload_config.py` - File upload settings

2. All models must:
   - Inherit from `pydantic.BaseModel`
   - Implement Builder pattern with @classmethod builder()
   - Use strict Literal types from completion_types
   - Include proper field validation and constraints
   - Support optional fields with None defaults where specified
   - Use proper field aliases for API compatibility

3. Key model specifications:
   - InputFileObject: type, transfer_method, url?, upload_file_id?
   - Usage: prompt_tokens, completion_tokens, total_tokens, pricing info
   - RetrieverResource: document_id, segment_id, score, content
   - FileInfo: id, name, size, extension, mime_type, created_by, created_at
   - UserInputForm: Support text-input, paragraph, select types
```

**Testing Prompt:**
```
Create comprehensive tests for all common model classes.

Requirements:
1. Create `tests/completion/v1/model/test_completion_public_models.py`
2. Create test classes for each common model:
   - TestInputFileObject
   - TestCompletionInputs
   - TestMetadata
   - TestUsage
   - TestRetrieverResource
   - TestFileInfo
   - TestFeedbackInfo
   - TestUserInputForm
   - TestSystemParameters
   - TestFileUploadConfig

3. Test each model's:
   - Builder pattern functionality
   - Field validation and type constraints
   - Required vs optional field handling
   - Default value behavior
   - Pydantic serialization/deserialization
   - Integration with Literal types

4. Use pytest fixtures for common test data
5. Achieve 100% test coverage
```

### Step 3: Implement Completion API Models (2 APIs)

**Implementation Prompt:**
```
Implement all request and response models for Completion API (2 APIs).

Requirements:
1. Create Send Message API models in `dify_oapi/api/completion/v1/model/completion/`:
   - `send_message_request.py`:
     * Inherit from BaseRequest
     * HTTP method: POST, URI: "/v1/completion-messages"
     * Include request_body field
   - `send_message_request_body.py`:
     * Fields: inputs (required), response_mode, user, files
     * inputs: Dict[str, Any] with required "query" field
     * response_mode: ResponseMode ("streaming" | "blocking")
     * files: Optional[List[InputFileObject]]
   - `send_message_response.py`:
     * Inherit from BaseResponse
     * Fields: event, message_id, mode, answer, metadata, created_at
     * metadata includes usage and retriever_resources

2. Create Stop Response API models:
   - `stop_response_request.py`:
     * Inherit from BaseRequest
     * HTTP method: POST, URI: "/v1/completion-messages/{task_id}/stop"
     * Path parameter: task_id
   - `stop_response_request_body.py`:
     * Fields: user (required)
   - `stop_response_response.py`:
     * Inherit from BaseResponse
     * Fields: result ("success")

3. All models must:
   - Implement Builder pattern
   - Use proper type annotations with Literal types
   - Include field validation
   - Support both streaming and blocking response modes
```

**Testing Prompt:**
```
Create comprehensive tests for Completion API models.

Requirements:
1. Create `tests/completion/v1/model/test_completion_models.py`
2. Implement test classes:
   - TestSendMessageModels - Test send message request/response models
   - TestStopResponseModels - Test stop response request/response models

3. Test coverage:
   - Builder pattern functionality for all models
   - BaseRequest/BaseResponse inheritance
   - HTTP method and URI configuration
   - Path parameter handling (task_id)
   - Field validation and type constraints
   - Required vs optional field handling
   - Integration with common models (InputFileObject, Metadata)
   - Response mode support (streaming/blocking)

4. Use pytest fixtures for test data
5. Mock external dependencies
6. Achieve 100% test coverage
```

### Step 4: Implement Completion Resource Class

**Implementation Prompt:**
```
Implement Completion resource class containing all message processing related API methods.

Requirements:
1. Create `dify_oapi/api/completion/v1/resource/completion.py`
2. Implement Completion class with methods:
   - `send_message()` - Send completion message
   - `stop_response()` - Stop response generation
   - `asend_message()` - Async send completion message
   - `astop_response()` - Async stop response generation

3. Method signatures:
   - Use @overload decorator for streaming/blocking mode type hints
   - send_message(request, request_option, stream=False) -> Union[SendMessageResponse, Generator]
   - stop_response(request, request_option) -> StopResponseResponse
   - Include proper type annotations for all parameters and return types

4. Implementation details:
   - Use Transport.execute() for sync operations
   - Use ATransport.aexecute() for async operations
   - Handle streaming mode with Generator[bytes, None, None]
   - Handle blocking mode with specific Response objects
   - Proper error handling and exception propagation

5. Follow existing resource class patterns from chat/knowledge APIs
6. Ensure proper integration with Transport layer
```

**Testing Prompt:**
```
Create comprehensive tests for Completion resource class.

Requirements:
1. Create `tests/completion/v1/resource/test_completion_resource.py`
2. Implement TestCompletionResource class with fixtures:
   - completion_resource fixture with mocked config
   - Mock Transport.execute and ATransport.aexecute

3. Test methods:
   - test_send_message_blocking - Test blocking mode with proper response
   - test_send_message_streaming - Test streaming mode with generator
   - test_stop_response - Test stop response functionality
   - test_async_send_message - Test async send message
   - test_async_stop_response - Test async stop response
   - test_method_signatures - Verify method exists and callable
   - test_error_handling - Test exception propagation

4. Use pytest.mock for Transport layer mocking
5. Verify return types match overload specifications
6. Test both sync and async method variants
7. Achieve 100% test coverage
```

### Step 5: Implement File API Models (1 API)

**Implementation Prompt:**
```
Implement request and response models for File API.

Requirements:
1. Create File Upload API models in `dify_oapi/api/completion/v1/model/file/`:
   - `upload_file_request.py`:
     * Inherit from BaseRequest
     * HTTP method: POST, URI: "/v1/files/upload"
     * Content-Type: multipart/form-data
     * Include files field for file upload
     * Include request_body field
   - `upload_file_request_body.py`:
     * Fields: user (required)
     * Support file parameter through parent request
   - `upload_file_response.py`:
     * Inherit from BaseResponse
     * Fields: id, name, size, extension, mime_type, created_by, created_at
     * Use proper UUID and timestamp types

2. File handling specifications:
   - Support image formats: png, jpg, jpeg, webp, gif
   - Handle multipart/form-data content type
   - File size validation (configurable limits)
   - Proper MIME type detection

3. All models must:
   - Implement Builder pattern
   - Use proper type annotations
   - Include field validation
   - Support file upload through BytesIO
   - Handle binary file data properly

4. Integration requirements:
   - Use FileInfo common model for response data
   - Follow existing file upload patterns from other APIs
```

**Testing Prompt:**
```
Create comprehensive tests for File API models.

Requirements:
1. Create `tests/completion/v1/model/test_file_models.py`
2. Implement TestUploadFileModels test class

3. Test coverage:
   - Builder pattern functionality
   - BaseRequest/BaseResponse inheritance
   - HTTP method and URI configuration
   - multipart/form-data content type handling
   - File upload field validation
   - Supported image format validation
   - File size limit handling
   - Response field validation (UUID, timestamps)
   - Integration with FileInfo model

4. Test utilities:
   - Create mock file data using BytesIO
   - Test various image formats (png, jpg, etc.)
   - Mock file size scenarios
   - Use pytest fixtures for common test data

5. Achieve 100% test coverage
```

### Step 6: Implement File Resource Class

**Implementation Prompt:**
```
Implement File resource class to handle file upload functionality.

Requirements:
1. Create `dify_oapi/api/completion/v1/resource/file.py`
2. Implement File class with methods:
   - `upload()` - Upload file
   - `aupload()` - Async upload file

3. Method signatures:
   - upload(request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse
   - aupload(request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse
   - Include proper type annotations

4. Implementation details:
   - Use Transport.execute() for sync operations
   - Use ATransport.aexecute() for async operations
   - Handle multipart/form-data requests properly
   - Support various image formats (png, jpg, jpeg, webp, gif)
   - Implement file size limit checks
   - Proper error handling for HTTP status codes:
     * 400: Bad Request (no_file_uploaded, too_many_files, unsupported_preview)
     * 413: File Too Large (file_too_large)
     * 415: Unsupported Media Type (unsupported_file_type)
     * 503: Service Unavailable (s3_connection_failed, s3_permission_denied)

5. Follow existing resource class patterns
6. Ensure proper integration with Transport layer
```

**Testing Prompt:**
```
Create comprehensive tests for File resource class.

Requirements:
1. Create `tests/completion/v1/resource/test_file_resource.py`
2. Implement TestFileResource class with fixtures:
   - file_resource fixture with mocked config
   - Mock Transport.execute and ATransport.aexecute

3. Test methods:
   - test_upload_file - Test successful file upload
   - test_async_upload_file - Test async file upload
   - test_file_type_validation - Test supported image formats
   - test_file_size_limits - Test file size validation
   - test_error_handling_400 - Test bad request errors
   - test_error_handling_413 - Test file too large error
   - test_error_handling_415 - Test unsupported file type
   - test_error_handling_503 - Test service unavailable errors
   - test_method_signatures - Verify methods exist and callable

4. Use pytest.mock for Transport layer mocking
5. Create mock file data with BytesIO
6. Test various error scenarios and status codes
7. Achieve 100% test coverage
```

### Step 7: Implement Feedback API Models (2 APIs)

**Implementation Prompt:**
```
Implement all request and response models for Feedback API (2 APIs).

Requirements:
1. Create Message Feedback API models in `dify_oapi/api/completion/v1/model/feedback/`:
   - `message_feedback_request.py`:
     * Inherit from BaseRequest
     * HTTP method: POST, URI: "/v1/messages/{message_id}/feedbacks"
     * Path parameter: message_id
   - `message_feedback_request_body.py`:
     * Fields: rating (optional, "like" | "dislike" | null), user (required), content (optional)
     * rating: Optional[Rating] - can be null to revoke feedback
   - `message_feedback_response.py`:
     * Inherit from BaseResponse
     * Fields: result ("success")

2. Create Get Feedbacks API models:
   - `get_feedbacks_request.py`:
     * Inherit from BaseRequest
     * HTTP method: GET, URI: "/v1/app/feedbacks"
     * Query parameters: page (optional, default 1), limit (optional, default 20)
   - `get_feedbacks_response.py`:
     * Inherit from BaseResponse
     * Fields: data (List[FeedbackInfo])
     * Support pagination information

3. All models must:
   - Implement Builder pattern
   - Use proper type annotations with Literal types
   - Include field validation
   - Support optional rating field (nullable)
   - Handle pagination parameters properly

4. Integration requirements:
   - Use FeedbackInfo common model for response data
   - Support null rating for feedback revocation
```

**Testing Prompt:**
```
Create comprehensive tests for Feedback API models.

Requirements:
1. Create `tests/completion/v1/model/test_feedback_models.py`
2. Implement test classes:
   - TestMessageFeedbackModels - Test message feedback request/response models
   - TestGetFeedbacksModels - Test get feedbacks request/response models

3. Test coverage:
   - Builder pattern functionality for all models
   - BaseRequest/BaseResponse inheritance
   - HTTP method and URI configuration
   - Path parameter handling (message_id)
   - Query parameter handling (page, limit)
   - Rating validation (like/dislike/null)
   - Required vs optional field handling
   - Pagination parameter validation
   - Integration with FeedbackInfo model
   - Null rating handling for feedback revocation

4. Use pytest fixtures for test data
5. Test edge cases (null rating, pagination limits)
6. Achieve 100% test coverage
```

### Step 8: Implement Feedback Resource Class

**Implementation Prompt:**
```
Implement Feedback resource class to handle feedback management functionality.

Requirements:
1. Create `dify_oapi/api/completion/v1/resource/feedback.py`
2. Implement Feedback class with methods:
   - `message_feedback()` - Submit message feedback
   - `get_feedbacks()` - Get feedback list
   - `amessage_feedback()` - Async submit message feedback
   - `aget_feedbacks()` - Async get feedback list

3. Method signatures:
   - message_feedback(request: MessageFeedbackRequest, request_option: RequestOption) -> MessageFeedbackResponse
   - get_feedbacks(request: GetFeedbacksRequest, request_option: RequestOption) -> GetFeedbacksResponse
   - Include proper type annotations

4. Implementation details:
   - Use Transport.execute() for sync operations
   - Use ATransport.aexecute() for async operations
   - Handle different types of feedback ratings (like/dislike/null)
   - Support pagination for feedback list
   - Proper error handling
   - Support feedback revocation (null rating)

5. Follow existing resource class patterns
6. Ensure proper integration with Transport layer
```

**Testing Prompt:**
```
Create comprehensive tests for Feedback resource class.

Requirements:
1. Create `tests/completion/v1/resource/test_feedback_resource.py`
2. Implement TestFeedbackResource class with fixtures:
   - feedback_resource fixture with mocked config
   - Mock Transport.execute and ATransport.aexecute

3. Test methods:
   - test_message_feedback - Test submit message feedback
   - test_message_feedback_revoke - Test feedback revocation (null rating)
   - test_get_feedbacks - Test get feedback list
   - test_get_feedbacks_pagination - Test pagination functionality
   - test_async_message_feedback - Test async submit feedback
   - test_async_get_feedbacks - Test async get feedbacks
   - test_rating_validation - Test rating validation (like/dislike/null)
   - test_method_signatures - Verify methods exist and callable
   - test_error_handling - Test exception propagation

4. Use pytest.mock for Transport layer mocking
5. Test pagination scenarios (different page/limit values)
6. Test all rating types including null for revocation
7. Achieve 100% test coverage
```

### Step 9: Implement Audio API Models (1 API)

**Implementation Prompt:**
```
Implement request and response models for Audio API.

Requirements:
1. Create Text-to-Audio API models in `dify_oapi/api/completion/v1/model/audio/`:
   - `text_to_audio_request.py`:
     * Inherit from BaseRequest
     * HTTP method: POST, URI: "/v1/text-to-audio"
     * Content-Type: application/json
   - `text_to_audio_request_body.py`:
     * Fields: message_id (optional), text (optional), user (required)
     * At least one of message_id or text is required
     * message_id takes priority over text if both provided
   - `text_to_audio_response.py`:
     * Inherit from BaseResponse
     * Returns binary audio data (wav or mp3)
     * Content-Type: audio/wav or audio/mp3

2. Special handling requirements:
   - Support two input methods: message_id (UUID) or text (string)
   - message_id has higher priority than text
   - Return binary audio formats: wav or mp3
   - Proper handling of binary response data
   - User field is always required

3. All models must:
   - Implement Builder pattern
   - Use proper type annotations
   - Include field validation
   - Handle binary response data properly
   - Validate that at least one of message_id or text is provided

4. Integration requirements:
   - Follow existing audio processing patterns
   - Handle binary data with proper content types
```

**Testing Prompt:**
```
Create comprehensive tests for Audio API models.

Requirements:
1. Create `tests/completion/v1/model/test_audio_models.py`
2. Implement TestTextToAudioModels test class

3. Test coverage:
   - Builder pattern functionality
   - BaseRequest/BaseResponse inheritance
   - HTTP method and URI configuration
   - Field validation (message_id, text, user)
   - Required field checks (user always required)
   - Input parameter priority logic (message_id over text)
   - Binary response data handling
   - Content-Type validation (audio/wav, audio/mp3)
   - At least one input validation (message_id or text)

4. Test scenarios:
   - Test with message_id only
   - Test with text only
   - Test with both message_id and text (priority)
   - Test with neither (should fail validation)
   - Test binary response handling

5. Use pytest fixtures for test data
6. Mock binary audio data for testing
7. Achieve 100% test coverage
```

### Step 10: Implement Audio Resource Class

**Implementation Prompt:**
```
Implement Audio resource class to handle audio processing functionality.

Requirements:
1. Create `dify_oapi/api/completion/v1/resource/audio.py`
2. Implement Audio class with methods:
   - `text_to_audio()` - Text to audio conversion
   - `atext_to_audio()` - Async text to audio conversion

3. Method signatures:
   - text_to_audio(request: TextToAudioRequest, request_option: RequestOption) -> TextToAudioResponse
   - atext_to_audio(request: TextToAudioRequest, request_option: RequestOption) -> TextToAudioResponse
   - Include proper type annotations

4. Implementation details:
   - Use Transport.execute() for sync operations
   - Use ATransport.aexecute() for async operations
   - Handle binary audio responses properly
   - Support both message_id and text input methods
   - Proper error handling for audio processing
   - Handle different audio formats (wav, mp3)
   - Validate input parameters (at least one of message_id or text)

5. Special handling:
   - Binary response data processing
   - Audio format detection from Content-Type headers
   - Input parameter priority (message_id over text)

6. Follow existing resource class patterns
7. Ensure proper integration with Transport layer
```

**Testing Prompt:**
```
Create comprehensive tests for Audio resource class.

Requirements:
1. Create `tests/completion/v1/resource/test_audio_resource.py`
2. Implement TestAudioResource class with fixtures:
   - audio_resource fixture with mocked config
   - Mock Transport.execute and ATransport.aexecute

3. Test methods:
   - test_text_to_audio_with_message_id - Test with message_id input
   - test_text_to_audio_with_text - Test with text input
   - test_text_to_audio_priority - Test message_id priority over text
   - test_async_text_to_audio - Test async text to audio conversion
   - test_binary_response_handling - Test binary audio response
   - test_audio_format_detection - Test wav/mp3 format handling
   - test_input_validation - Test input parameter validation
   - test_method_signatures - Verify methods exist and callable
   - test_error_handling - Test exception propagation

4. Use pytest.mock for Transport layer mocking
5. Mock binary audio data for response testing
6. Test different audio formats and content types
7. Test input parameter combinations and validation
8. Achieve 100% test coverage
```

### Step 11: Implement Info API Models (3 APIs)

**Implementation Prompt:**
```
Implement all request and response models for Info API (3 APIs).

Requirements:
1. Create Get Info API models in `dify_oapi/api/completion/v1/model/info/`:
   - `get_info_request.py`:
     * Inherit from BaseRequest
     * HTTP method: GET, URI: "/v1/info"
     * No request parameters
   - `get_info_response.py`:
     * Inherit from BaseResponse
     * Fields: name, description, tags

2. Create Get Parameters API models:
   - `get_parameters_request.py`:
     * Inherit from BaseRequest
     * HTTP method: GET, URI: "/v1/parameters"
     * No request parameters
   - `get_parameters_response.py`:
     * Inherit from BaseResponse
     * Fields: opening_statement, suggested_questions, suggested_questions_after_answer,
       speech_to_text, retriever_resource, annotation_reply, user_input_form, file_upload, system_parameters

3. Create Get Site API models:
   - `get_site_request.py`:
     * Inherit from BaseRequest
     * HTTP method: GET, URI: "/v1/site"
     * No request parameters
   - `get_site_response.py`:
     * Inherit from BaseResponse
     * Fields: title, chat_color_theme, chat_color_theme_inverted, icon_type, icon,
       icon_background, icon_url, description, copyright, privacy_policy, custom_disclaimer,
       default_language, show_workflow_steps, use_icon_as_answer_icon

4. All models must:
   - Implement Builder pattern
   - Use proper type annotations with Literal types
   - Include field validation
   - Support complex nested objects (user_input_form, file_upload, etc.)

5. Integration requirements:
   - Use UserInputForm, SystemParameters, FileUploadConfig common models
   - Support IconType Literal ("emoji" | "image")
   - Handle boolean and string fields properly
```

**Testing Prompt:**
```
Create comprehensive tests for Info API models.

Requirements:
1. Create `tests/completion/v1/model/test_info_models.py`
2. Implement test classes:
   - TestGetInfoModels - Test get info request/response models
   - TestGetParametersModels - Test get parameters request/response models
   - TestGetSiteModels - Test get site request/response models

3. Test coverage:
   - Builder pattern functionality for all models
   - BaseRequest/BaseResponse inheritance
   - HTTP method and URI configuration
   - Field validation and type constraints
   - Complex nested object handling
   - Integration with common models (UserInputForm, SystemParameters, etc.)
   - IconType Literal validation ("emoji" | "image")
   - Boolean and string field validation
   - Optional vs required field handling

4. Test scenarios:
   - Test all response fields with various data types
   - Test nested object serialization/deserialization
   - Test Literal type constraints
   - Test optional field behavior

5. Use pytest fixtures for complex test data
6. Test integration with common models
7. Achieve 100% test coverage
```

### Step 12: Implement Info Resource Class

**Implementation Prompt:**
```
Implement Info resource class containing all application information related API methods.

Requirements:
1. Create `dify_oapi/api/completion/v1/resource/info.py`
2. Implement Info class with methods:
   - `get_info()` - Get application basic information
   - `get_parameters()` - Get application parameters information
   - `get_site()` - Get application WebApp settings
   - `aget_info()` - Async get application basic information
   - `aget_parameters()` - Async get application parameters information
   - `aget_site()` - Async get application WebApp settings

3. Method signatures:
   - get_info(request: GetInfoRequest, request_option: RequestOption) -> GetInfoResponse
   - get_parameters(request: GetParametersRequest, request_option: RequestOption) -> GetParametersResponse
   - get_site(request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse
   - Include proper type annotations for all methods

4. Implementation details:
   - Use Transport.execute() for sync operations
   - Use ATransport.aexecute() for async operations
   - Proper error handling
   - Complete type annotations
   - Handle complex response objects with nested data

5. Follow existing resource class patterns
6. Ensure proper integration with Transport layer
```

**Testing Prompt:**
```
Create comprehensive tests for Info resource class.

Requirements:
1. Create `tests/completion/v1/resource/test_info_resource.py`
2. Implement TestInfoResource class with fixtures:
   - info_resource fixture with mocked config
   - Mock Transport.execute and ATransport.aexecute

3. Test methods:
   - test_get_info - Test get application basic information
   - test_get_parameters - Test get application parameters information
   - test_get_site - Test get application WebApp settings
   - test_async_get_info - Test async get info
   - test_async_get_parameters - Test async get parameters
   - test_async_get_site - Test async get site
   - test_method_signatures - Verify all methods exist and callable
   - test_error_handling - Test exception propagation

4. Use pytest.mock for Transport layer mocking
5. Mock complex response data with nested objects
6. Verify return types match method specifications
7. Test both sync and async method variants
8. Achieve 100% test coverage
```

### Step 13: Implement Version Integration

**Implementation Prompt:**
```
Implement Completion V1 version integration, integrating all resource classes into a unified version interface.

Requirements:
1. Update `dify_oapi/api/completion/v1/version.py`
2. Implement V1 class containing all resources:
   - completion: Completion resource
   - file: File resource
   - feedback: Feedback resource
   - audio: Audio resource
   - info: Info resource

3. Class structure:
   ```python
   class V1:
       def __init__(self, config: Config):
           self.completion = Completion(config)
           self.file = File(config)
           self.feedback = Feedback(config)
           self.audio = Audio(config)
           self.info = Info(config)
   ```

4. Requirements:
   - Proper dependency injection and configuration passing
   - Maintain consistency with existing architecture
   - Provide clear resource access interface
   - Follow existing version integration patterns from chat/knowledge APIs

5. Ensure all resources are properly initialized with config
6. Maintain backward compatibility if any existing code depends on this
```

**Testing Prompt:**
```
Create comprehensive tests for Version integration.

Requirements:
1. Create `tests/completion/v1/integration/test_version_integration.py`
2. Implement TestV1Integration class

3. Test coverage:
   - test_all_resources_available - Test all 5 resources are available
   - test_resource_initialization - Test all resources are properly initialized
   - test_config_propagation - Test configuration is passed to all resources
   - test_resource_method_access - Test all resource methods are accessible
   - test_resource_types - Verify resource types are correct
   - test_version_interface - Test V1 class interface

4. Verification points:
   - All 5 resources (completion, file, feedback, audio, info) are present
   - Each resource is properly initialized with config
   - All resource methods are accessible through V1 interface
   - Configuration is properly propagated to all resources

5. Use pytest fixtures for config mocking
6. Test resource accessibility and method availability
7. Achieve 100% test coverage
```

### Step 14: Implement Complete API Integration Tests

**Implementation Prompt:**
```
Implement complete integration tests for Completion API, verifying end-to-end functionality of all 9 APIs.

Requirements:
1. Create `tests/completion/v1/integration/test_completion_api_integration.py`
2. Implement TestCompletionAPIIntegration class

3. Test all 9 APIs with comprehensive scenarios:
   - test_send_message_api - Test send completion message (both streaming/blocking)
   - test_stop_response_api - Test stop response generation
   - test_upload_file_api - Test file upload functionality
   - test_message_feedback_api - Test message feedback submission
   - test_get_feedbacks_api - Test get application feedbacks
   - test_text_to_audio_api - Test text to audio conversion
   - test_get_info_api - Test get application basic information
   - test_get_parameters_api - Test get application parameters
   - test_get_site_api - Test get application WebApp settings

4. Integration test requirements:
   - Test complete request-response workflow for each API
   - Verify all request models can be built successfully
   - Test both sync and async operations where applicable
   - Test error handling and edge cases
   - Verify streaming and blocking modes for completion API
   - Test file upload with different formats
   - Test feedback with different rating types
   - Test audio conversion with both message_id and text inputs

5. Mock external dependencies but test internal integrations
6. Use realistic test data that matches API specifications
7. Ensure all API integrations work correctly together
```

**Testing Prompt:**
```
Create validation for complete API integration tests.

Requirements:
1. Verify all 9 API integration tests pass successfully
2. Check comprehensive test coverage across all APIs:
   - Completion APIs (2): send_message, stop_response
   - File API (1): upload_file
   - Feedback APIs (2): message_feedback, get_feedbacks
   - Audio API (1): text_to_audio
   - Info APIs (3): get_info, get_parameters, get_site

3. Validation points:
   - All request models are buildable and valid
   - All response models inherit from BaseResponse correctly
   - Both streaming and blocking modes work for completion
   - File upload handles multipart/form-data correctly
   - Feedback supports all rating types (like/dislike/null)
   - Audio conversion works with both input methods
   - Info APIs return proper application configuration

4. Error handling validation:
   - Test error scenarios for each API
   - Verify proper HTTP status code handling
   - Test exception propagation

5. Performance validation:
   - Ensure tests run efficiently
   - Verify no memory leaks in streaming operations
   - Test concurrent operations where applicable

6. Coverage validation:
   - Achieve minimum 95% test coverage
   - Cover all major code paths
   - Test both success and failure scenarios
```

### Step 15: Create Usage Examples

**Implementation Prompt:**
```
Create complete usage examples for all Completion APIs.

Requirements:
1. Create resource-categorized examples in `examples/completion/` directory:
   - completion/send_message.py - Send message examples (streaming & blocking)
   - completion/stop_response.py - Stop response examples
   - file/upload_file.py - File upload examples
   - feedback/message_feedback.py - Message feedback examples
   - feedback/get_feedbacks.py - Get feedbacks examples
   - audio/text_to_audio.py - Text to audio examples
   - info/get_info.py - Get application info examples
   - info/get_parameters.py - Get parameters info examples
   - info/get_site.py - Get site info examples

2. Each example file must contain:
   - Complete working code examples
   - Both synchronous and asynchronous usage examples
   - Proper error handling examples
   - Clear explanatory comments
   - Realistic parameter configurations
   - Environment variable usage for API keys

3. Example structure for each file:
   ```python
   # Sync example
   def example_sync():
       # Implementation with error handling
       pass

   # Async example  
   async def example_async():
       # Implementation with error handling
       pass

   if __name__ == "__main__":
       # Run examples
       pass
   ```

4. Special requirements:
   - Completion examples: Show both streaming and blocking modes
   - File examples: Show different image formats and error handling
   - Feedback examples: Show all rating types including revocation
   - Audio examples: Show both message_id and text inputs
   - Info examples: Show how to access nested configuration data

5. Create `examples/completion/README.md` with:
   - Overview of all examples
   - Setup instructions
   - Environment variable configuration
   - Usage guidelines
```

**Testing Prompt:**
```
Verify correctness of all usage examples.

Requirements:
1. Syntax and import validation:
   - Check syntax correctness of all example files
   - Verify all import statements are correct
   - Ensure type annotations are accurate
   - Validate example code matches actual API interfaces

2. Functionality validation:
   - Verify examples cover all major use cases
   - Check error handling logic is complete and correct
   - Ensure both sync and async examples are provided
   - Validate realistic parameter usage

3. Documentation validation:
   - Check README.md accuracy and completeness
   - Verify setup instructions are clear
   - Ensure environment variable documentation is correct
   - Validate usage guidelines are helpful

4. Code quality validation:
   - Ensure examples follow Python best practices
   - Check for proper resource cleanup (async contexts)
   - Verify error handling patterns are consistent
   - Ensure examples are educational and clear

5. Coverage validation:
   - Verify all 9 APIs have corresponding examples
   - Check both streaming and blocking modes are covered
   - Ensure all major features are demonstrated
   - Validate edge cases and error scenarios are shown

6. Runnable validation:
   - Ensure examples can be executed (with proper API keys)
   - Check that examples handle missing environment variables gracefully
   - Verify examples provide helpful output and logging
```

## Implementation Verification Checklist

### Model Verification
- [ ] All Request classes inherit from BaseRequest
- [ ] All Response classes inherit from BaseResponse
- [ ] All models implement Builder pattern
- [ ] Use strict Literal type definitions
- [ ] Proper field validation and type constraints

### Resource Verification
- [ ] All resource classes properly implement synchronous and asynchronous methods
- [ ] Proper error handling and type annotations
- [ ] Proper integration with Transport layer
- [ ] Support streaming and blocking modes (applicable APIs)
- [ ] Properly handle file upload and binary responses

### Integration Verification
- [ ] V1 version properly integrates all 5 resources
- [ ] All 9 APIs can be called correctly
- [ ] Configuration and dependency injection work properly
- [ ] Maintain consistency with existing architecture

### Testing Verification
- [ ] All model tests pass
- [ ] All resource tests pass
- [ ] Integration tests cover all APIs
- [ ] Test coverage meets expected standards
- [ ] Error handling scenarios are thoroughly tested

### Example Verification
- [ ] All 9 APIs have corresponding examples
- [ ] Example code is syntactically correct and runnable
- [ ] Include both synchronous and asynchronous usage
- [ ] Complete error handling examples
- [ ] README documentation is accurate and complete

## Summary

This implementation plan breaks down Completion API development into 15 specific steps, each containing detailed implementation requirements and corresponding test validation. This approach ensures:

1. **Code Quality**: Each step has corresponding tests to ensure code quality
2. **Type Safety**: Use strict Literal type definitions for complete type safety
3. **Architecture Consistency**: Follow existing design patterns and architectural specifications
4. **Functional Completeness**: Cover complete functionality of all 9 Completion APIs
5. **Usability**: Provide clear usage examples and documentation

Each step's prompts can be directly given to AI for execution, ensuring implementation consistency and quality.