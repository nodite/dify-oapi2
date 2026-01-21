# Dify Core API Examples

The Dify Core API provides essential system-level functionality across all Dify services. This directory contains examples for unified core operations with 9 APIs across 4 resource types.

## 📁 Resources

### [audio/](./audio/) - Audio Processing (2 APIs)
Speech-to-text and text-to-speech capabilities.

**Available Examples:**
- `audio_to_text.py` - Convert audio files to text
- `text_to_audio.py` - Convert text to audio files

### [feedback/](./feedback/) - Feedback Management (2 APIs)
User feedback collection and analysis.

**Available Examples:**
- `submit_feedback.py` - Submit user feedback (like/dislike)
- `get_feedbacks.py` - Retrieve feedback data and statistics

### [file/](./file/) - File Management (1 API)
Unified file upload and processing.

**Available Examples:**
- `upload_file.py` - Upload files for various Dify services

### [info/](./info/) - Application Information (4 APIs)
Application configuration and metadata retrieval.

**Available Examples:**
- `get_app_info.py` - Get basic application information
- `get_app_parameters.py` - Get application configuration parameters
- `get_app_meta.py` - Get application metadata
- `get_site_settings.py` - Get site configuration settings

## 🚀 Quick Start

### File Upload Example

```python
from dify_oapi.api.dify.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.dify.v1.model.upload_file_request_body import UploadFileRequestBody

with open("document.pdf", "rb") as file:
    req_body = (
        UploadFileRequestBody.builder()
        .file(file)
        .user("user-123")
        .build()
    )

req = UploadFileRequest.builder().request_body(req_body).build()
response = client.dify.v1.file.upload_file(req, req_option)
print(f"File ID: {response.id}")
```

### Audio Processing Example

```python
from dify_oapi.api.dify.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.dify.v1.model.audio_to_text_request_body import AudioToTextRequestBody

with open("audio.mp3", "rb") as audio_file:
    req_body = (
        AudioToTextRequestBody.builder()
        .file(audio_file)
        .user("user-123")
        .build()
    )

req = AudioToTextRequest.builder().request_body(req_body).build()
response = client.dify.v1.audio.audio_to_text(req, req_option)
print(f"Transcription: {response.text}")
```

### Application Info Example

```python
from dify_oapi.api.dify.v1.model.get_application_info_request import GetApplicationInfoRequest

req = GetApplicationInfoRequest.builder().build()
response = client.dify.v1.info.get_application_info(req, req_option)
print(f"App Name: {response.name}")
print(f"Description: {response.description}")
```

## 🔧 Features

### Unified Interface
- **Consistent API**: All core functionality through unified dify module
- **Cross-Service Support**: Used by Chat, Completion, Chatflow, and Workflow APIs
- **Standardized Responses**: Consistent response formats across all services

### File Management
- **Multiple Formats**: Support for images, documents, audio, and video files
- **Secure Upload**: Built-in file validation and security checks
- **Metadata Extraction**: Automatic file metadata processing

### Audio Processing
- **Speech Recognition**: High-quality audio-to-text conversion
- **Text-to-Speech**: Natural voice synthesis from text
- **Multiple Formats**: Support for various audio formats

### Application Configuration
- **Runtime Info**: Get application status and configuration
- **Parameter Management**: Access and manage app parameters
- **Metadata Access**: Retrieve comprehensive app metadata
- **Site Settings**: Access global site configuration

### Feedback System
- **User Feedback**: Collect likes, dislikes, and ratings
- **Analytics**: Comprehensive feedback statistics
- **Quality Improvement**: Data-driven service enhancement

## 📖 Environment Variables

```bash
export DOMAIN="https://api.dify.ai"
export DIFY_KEY="your-dify-api-key"
```

## 🔧 Running Examples

```bash
# File management
python examples/dify/file/upload_file.py

# Audio processing
python examples/dify/audio/audio_to_text.py
python examples/dify/audio/text_to_audio.py

# Application information
python examples/dify/info/get_app_info.py
python examples/dify/info/get_app_parameters.py
python examples/dify/info/get_app_meta.py
python examples/dify/info/get_site_settings.py

# Feedback management
python examples/dify/feedback/submit_feedback.py
python examples/dify/feedback/get_feedbacks.py
```

## 🔗 Integration with Other APIs

The Dify Core API is used by all other Dify services:

- **Chat API**: File upload, audio processing, feedback collection
- **Completion API**: File management, application info
- **Chatflow API**: Audio processing, feedback management
- **Workflow API**: File upload, application configuration
- **Knowledge Base API**: File processing for document upload

## 📚 Best Practices

1. **Use Core APIs Directly**: For new projects, use `client.dify.v1.*` interfaces
2. **Handle File Resources**: Properly close file handles and manage memory
3. **Error Handling**: Implement consistent exception handling patterns
4. **Async Operations**: Use async versions for high-concurrency scenarios
5. **Configuration Management**: Use environment variables for API keys and domains
6. **File Validation**: Validate file types and sizes before upload

## 🔗 Related APIs

- [Chat API](../chat/) - Interactive conversations
- [Completion API](../completion/) - Text generation
- [Chatflow API](../chatflow/) - Enhanced chat with workflows
- [Workflow API](../workflow/) - Automated workflow execution
- [Knowledge Base API](../knowledge/) - Knowledge management
