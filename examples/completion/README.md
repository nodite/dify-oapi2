# Completion API Examples

The Completion API provides text generation and completion capabilities. This directory contains examples for all completion-related operations.

## 📁 Resources

### [annotation/](./annotation/) - Annotation Management
Manage annotations and reply settings for completion messages.

**Available Examples:**
- `annotation_reply_settings.py` - Configure annotation reply settings
- `create_annotation.py` - Create new annotations
- `delete_annotation.py` - Delete existing annotations
- `list_annotations.py` - List all annotations
- `query_annotation_reply_status.py` - Check annotation reply status
- `update_annotation.py` - Update annotation content

### [completion/](./completion/) - Completion Operations
Core text completion and generation functionality.

**Available Examples:**
- `send_message.py` - Send completion requests
- `stop_response.py` - Stop ongoing generation
- `blocking_completion.py` - Synchronous completion example
- `streaming_completion.py` - Real-time streaming completion

### [file/](./file/) - File Management
Upload and manage files for completion processing.

**Available Examples:**
- `upload_file.py` - Upload files for processing

### [feedback/](./feedback/) - Feedback Management
Collect and manage user feedback on completion responses.

**Available Examples:**
- `get_feedbacks.py` - Retrieve feedback data
- `submit_feedback.py` - Submit user feedback

### [audio/](./audio/) - Audio Processing
Text-to-speech capabilities for completion results.

**Available Examples:**
- `text_to_audio.py` - Convert completion text to audio

## 🚀 Quick Start

### Basic Completion

```python
from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody

req_body = (
    SendMessageRequestBody.builder()
    .inputs({})
    .query("Write a short story about AI.")
    .response_mode("blocking")
    .user("user-123")
    .build()
)

req = SendMessageRequest.builder().request_body(req_body).build()
response = client.completion.v1.completion.send_message(req, req_option, False)
print(response.answer)
```

### Streaming Completion

```python
req_body = (
    SendMessageRequestBody.builder()
    .query("Explain machine learning in detail")
    .response_mode("streaming")
    .user("user-123")
    .build()
)

response = client.completion.v1.completion.send_message(req, req_option, True)
for chunk in response:
    print(chunk, end="", flush=True)
```

## 🔧 Features

- **Multiple Response Modes**: Blocking and streaming responses
- **File Support**: Process documents and media files
- **Annotation System**: Rich annotation and feedback management
- **Audio Output**: Convert text responses to speech
- **Error Handling**: Comprehensive error management

## 📖 Environment Variables

```bash
export DOMAIN="https://api.dify.ai"
export COMPLETION_KEY="your-completion-api-key"
```

## 🔗 Related APIs

- [Chat API](../chat/) - Interactive conversations
- [Dify Core API](../dify/) - Core functionality
- [Workflow API](../workflow/) - Workflow integration