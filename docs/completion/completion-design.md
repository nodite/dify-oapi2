# Completion API Design Document

## Overview

This document outlines the design for implementing comprehensive completion functionality in the dify-oapi completion module. The implementation supports all 9 completion-related APIs covering message processing, audio processing, feedback system, file upload, and application configuration.

## Design Decisions

### 1. Module Organization
**Decision**: Extend existing `completion/v1/` module structure
- Continue using the established version-based API organization
- Maintain consistency with existing chat, knowledge, and workflow modules
- Leverage existing infrastructure and patterns

### 2. Resource Structure
**Decision**: Implement completion APIs across 5 specialized resources

**Multi-Resource Implementation**:
- `completion` - Message processing APIs (2 APIs)
  - Message operations: `send_message`, `stop_response`
- `file` - File upload APIs (1 API)
  - File operations: `upload`
- `feedback` - Feedback management APIs (2 APIs)
  - Feedback operations: `message_feedback`, `get_feedbacks`
- `audio` - Audio processing APIs (1 API)
  - Audio operations: `text_to_audio`
- `info` - Application information APIs (3 APIs)
  - Info operations: `get_info`, `get_parameters`, `get_site`

### 3. Response Model Strategy
**Decision**: Create dedicated Response models for every API
- Maintain type safety and consistency across all endpoints
- Include specific response models even for simple `{"result": "success"}` responses
- Ensure comprehensive IDE support and validation

### 4. Method Naming Convention
**Decision**: Use simple, concise method names for clarity
- Completion operations: `send_message`, `stop_response`
- File operations: `upload`
- Feedback operations: `message_feedback`, `get_feedbacks`
- Audio operations: `text_to_audio`
- Info operations: `get_info`, `get_parameters`, `get_site`

### 5. Response Model Inheritance Rules
**Decision**: ALL Response classes MUST inherit from BaseResponse for error handling
- **Rationale**: Ensures all API responses have consistent error handling capabilities
- **Properties Provided**: `success`, `code`, `msg`, `raw` for comprehensive error management

### 6. Request/Response Model Code Style Rules
**Decision**: Strict adherence to established patterns for consistency

#### HTTP Method Patterns
**GET Requests**: No RequestBody file needed
**POST Requests**: Require separate RequestBody file
**PATCH/PUT Requests**: Require separate RequestBody file
**DELETE Requests**: No RequestBody file needed

#### Multipart/Form-Data Handling
**Pattern Requirements**:
- APIs requiring file uploads MUST use multipart/form-data content type
- Request classes MUST support both `files` and `body` fields in BaseRequest

### 7. Strict Type Safety Rules
**Decision**: ALL API fields MUST use strict typing with Literal types

```python
# completion_types.py - Define all Literal types
from typing import Literal

# Response mode types
ResponseMode = Literal["streaming", "blocking"]

# File types
FileType = Literal["image"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Rating types
Rating = Literal["like", "dislike"]

# Icon types
IconType = Literal["emoji", "image"]

# Event types
EventType = Literal["message", "message_end", "tts_message", "tts_message_end", "message_replace", "error", "ping"]

# User input form types
UserInputFormType = Literal["text-input", "paragraph", "select"]
```

## API Implementation Plan

### Completion APIs (2 APIs)

#### Completion Resource Implementation
1. **POST /completion-messages** → `completion.send_message()` - Send completion message
2. **POST /completion-messages/{task_id}/stop** → `completion.stop_response()` - Stop generation



### File APIs (1 API)

#### File Resource Implementation
1. **POST /files/upload** → `file.upload()` - Upload file

### Feedback APIs (2 APIs)

#### Feedback Resource Implementation
1. **POST /messages/{message_id}/feedbacks** → `feedback.message_feedback()` - Submit message feedback
2. **GET /app/feedbacks** → `feedback.get_feedbacks()` - Get application feedbacks

### Audio APIs (1 API)

#### Audio Resource Implementation
1. **POST /text-to-audio** → `audio.text_to_audio()` - Convert text to audio

### Info APIs (3 APIs)

#### Info Resource Implementation
1. **GET /info** → `info.get_info()` - Get application basic information
2. **GET /parameters** → `info.get_parameters()` - Get application parameters
3. **GET /site** → `info.get_site()` - Get application WebApp settings

## Technical Implementation Details

### Resource Class Structure
```python
# Example: completion resource
class Completion:
    def __init__(self, config: Config):
        self.config = config

    def send_message(self, request: SendMessageRequest, request_option: RequestOption, stream: bool = False) -> SendMessageResponse:
        return Transport.execute(self.config, request, unmarshal_as=SendMessageResponse, option=request_option, stream=stream)

    async def asend_message(self, request: SendMessageRequest, request_option: RequestOption, stream: bool = False) -> SendMessageResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=SendMessageResponse, option=request_option, stream=stream)
```

### Version Integration
**Target Structure**:
```python
class V1:
    def __init__(self, config: Config):
        self.completion = Completion(config)
        self.file = File(config)
        self.feedback = Feedback(config)
        self.audio = Audio(config)
        self.info = Info(config)
```

## Examples Strategy

### Examples Organization
**Decision**: Resource-based directory structure with API-specific files
- Each resource gets its own directory under `examples/completion/`
- Each API gets its own file within the resource directory
- Each file contains both sync and async examples

### Examples Directory Structure
```
examples/completion/
├── completion/
│   ├── send_message.py              # Send completion message examples
│   └── stop_response.py             # Stop generation examples

├── file/
│   └── upload_file.py               # File upload examples
├── feedback/
│   ├── message_feedback.py          # Message feedback examples
│   └── get_feedbacks.py             # Get feedbacks examples
├── audio/
│   └── text_to_audio.py             # Text to audio examples
├── info/
│   ├── get_info.py                  # Get info examples
│   ├── get_parameters.py            # Get parameters examples
│   └── get_site.py                  # Get site examples
└── README.md                        # Examples overview and usage guide
```

## Testing Strategy

### Test File Organization
**Decision**: Test files MUST be organized by resource functionality

### Test Structure
```
tests/completion/v1/
├── model/
│   ├── test_completion_models.py    # Completion API tests (2 test classes)

│   ├── test_file_models.py          # File API tests (1 test class)
│   ├── test_feedback_models.py      # Feedback API tests (2 test classes)
│   ├── test_audio_models.py         # Audio API tests (1 test class)
│   ├── test_info_models.py          # Info API tests (3 test classes)
│   └── test_completion_public_models.py # All public models
├── resource/
│   ├── test_completion_resource.py  # Completion resource tests

│   ├── test_file_resource.py        # File resource tests
│   ├── test_feedback_resource.py    # Feedback resource tests
│   ├── test_audio_resource.py       # Audio resource tests
│   └── test_info_resource.py        # Info resource tests
├── integration/
│   ├── test_completion_api_integration.py # All 9 completion API integration tests
│   └── test_version_integration.py
└── __init__.py
```



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

## Migration Guide

### API Migration Map

#### Before (Legacy Structure)
```python
# Legacy access pattern
client.completion.v1.send_message(request, option)
client.completion.v1.upload_file(request, option)
client.completion.v1.message_feedback(request, option)
```

#### After (New Resource Structure)
```python
# New resource-based access pattern
client.completion.v1.completion.send_message(request, option)
client.completion.v1.file.upload(request, option)
client.completion.v1.feedback.message_feedback(request, option)
```

### Code Migration Examples

#### Example 1: Send Completion Message
**Before:**
```python
# Legacy access
response = client.completion.v1.send_message(request, option)
```

**After:**
```python
# New resource-based access
response = client.completion.v1.completion.send_message(request, option)
```

#### Example 2: Type Safety Migration
**Before:**
```python
class SendMessageRequestBody(BaseModel):
    response_mode: str | None = None  # Generic string
```

**After:**
```python
from .completion_types import ResponseMode

class SendMessageRequestBody(BaseModel):
    response_mode: ResponseMode | None = None  # Literal["streaming", "blocking"]
```

### Migration Checklist
- [ ] Update resource access patterns
- [ ] Migrate to new method names where applicable
- [ ] Update type annotations to use Literal types
- [ ] Update error handling to use BaseResponse
- [ ] Update import statements if needed

## Testing Guide

### Model Testing Patterns
```python
class TestSendMessageModels:
    """Test SendMessage API models."""
    
    def test_request_builder(self):
        """Test SendMessageRequest builder pattern."""
        request = SendMessageRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/completion-messages"
    
    def test_response_inheritance(self):
        """Test SendMessageResponse inherits from BaseResponse."""
        response = SendMessageResponse()
        assert hasattr(response, 'success')
        assert hasattr(response, 'code')
        assert hasattr(response, 'msg')
        assert hasattr(response, 'raw')
```

### Resource Testing Patterns
```python
class TestCompletionResource:
    """Test Completion resource methods."""
    
    @pytest.fixture
    def completion_resource(self):
        config = Config()
        config.domain = "https://api.dify.ai"
        return Completion(config)
    
    def test_send_message_method_exists(self, completion_resource):
        assert hasattr(completion_resource, 'send_message')
        assert callable(completion_resource.send_message)
```

### Integration Testing
```python
class TestCompletionAPIIntegration:
    """Integration tests for all 9 Completion APIs."""
    
    def test_all_request_models_buildable(self):
        requests = [
            SendMessageRequest.builder().build(),
            StopResponseRequest.builder().build(),
            UploadFileRequest.builder().build(),
            MessageFeedbackRequest.builder().build(),
            GetFeedbacksRequest.builder().build(),
            TextToAudioRequest.builder().build(),
            GetInfoRequest.builder().build(),
            GetParametersRequest.builder().build(),
            GetSiteRequest.builder().build(),
        ]
        
        for request in requests:
            assert request is not None
            assert hasattr(request, 'http_method')
            assert hasattr(request, 'uri')
```

## Examples Guide

### Complete API Examples

#### Send Completion Message
```python
def send_completion_message():
    client = Client.builder().domain("https://api.dify.ai").build()
    
    body = (
        SendMessageRequestBody.builder()
        .inputs({"query": "Translate 'Hello World' to French"})
        .response_mode("blocking")
        .user("user-123")
        .build()
    )
    
    request = SendMessageRequest.builder().request_body(body).build()
    option = RequestOption.builder().api_key("your-api-key").build()
    
    response = client.completion.v1.completion.send_message(request, option)
    return response.answer
```

#### File Upload
```python
def upload_file_example():
    client = Client.builder().domain("https://api.dify.ai").build()
    
    with open("example.png", "rb") as f:
        file_content = BytesIO(f.read())
    
    body = UploadFileRequestBody.builder().user("user-123").build()
    request = (
        UploadFileRequest.builder()
        .file(file_content, "example.png")
        .request_body(body)
        .build()
    )
    
    option = RequestOption.builder().api_key("your-api-key").build()
    response = client.completion.v1.file.upload(request, option)
    return response.id
```

#### Text to Audio
```python
def text_to_audio_example():
    client = Client.builder().domain("https://api.dify.ai").build()
    
    body = (
        TextToAudioRequestBody.builder()
        .text("Hello, this is a test message")
        .user("user-123")
        .build()
    )
    
    request = TextToAudioRequest.builder().request_body(body).build()
    option = RequestOption.builder().api_key("your-api-key").build()
    
    response = client.completion.v1.audio.text_to_audio(request, option)
    return response  # Binary audio content
```

### Complete Workflow Examples

#### Text Generation Workflow
```python
def complete_text_generation_workflow():
    """Complete workflow: generate text, get feedback, convert to audio."""
    
    # Step 1: Send completion message
    response = send_completion_message()
    message_id = response.message_id
    answer = response.answer
    
    # Step 2: Submit positive feedback
    feedback_success = submit_message_feedback(message_id)
    
    # Step 3: Convert response to audio
    audio_data = text_to_audio_example()
    
    return {
        "message_id": message_id,
        "answer": answer,
        "feedback_submitted": feedback_success,
        "audio_generated": audio_data is not None
    }
```

### Error Handling Examples
```python
def robust_completion_request():
    """Example with comprehensive error handling."""
    try:
        client = Client.builder().domain("https://api.dify.ai").build()
        
        body = (
            SendMessageRequestBody.builder()
            .inputs({"query": "Test query"})
            .response_mode("blocking")
            .user("user-123")
            .build()
        )
        
        request = SendMessageRequest.builder().request_body(body).build()
        option = RequestOption.builder().api_key("your-api-key").build()
        
        response = client.completion.v1.completion.send_message(request, option)
        
        # Check response success using BaseResponse properties
        if not response.success:
            print(f"API Error: {response.code} - {response.msg}")
            return None
        
        return response.answer
        
    except ValidationError as e:
        print(f"Validation Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None
```

## Summary

This design provides a comprehensive solution for completion functionality in dify-oapi, covering all 9 completion-related APIs with a clean, maintainable architecture. The implementation prioritizes type safety, consistency, and developer experience while ensuring full compatibility with the latest Dify API specifications.

The multi-resource organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for completion operations including message processing, file upload, feedback collection, audio processing, and application configuration.

### Key Features
- **Comprehensive Coverage**: Full implementation of all 9 completion APIs with consistent architecture
- **Multi-resource Organization**: Logical separation of concerns across completion, file, feedback, audio, and info resources
- **Advanced Type Safety**: Strict typing with Literal types for all predefined values
- **Streaming Support**: Complete streaming and blocking mode support for completion messages
- **File Processing**: Complete file upload and processing capabilities

- **Feedback Collection**: Complete feedback management and retrieval system
- **Audio Processing**: Text-to-speech conversion capabilities
- **Application Configuration**: Complete application information and settings management
- **Safety Features**: Comprehensive validation and error handling mechanisms
- **Educational Focus**: Examples focus purely on demonstrating API functionality
- **Consistent Patterns**: Uniform architecture and naming conventions across all resources
- **Complete Migration Guide**: Detailed migration instructions with code examples
- **Comprehensive Testing**: Full testing strategy covering all APIs and patterns
- **Practical Examples**: Real-world usage examples and workflow demonstrations