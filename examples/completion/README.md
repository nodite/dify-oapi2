# Completion API Examples

The Completion API provides text generation and completion capabilities with 10 APIs across 2 resource types. This directory contains examples for all completion-related operations.

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

**Note**: File upload, audio processing, and feedback examples are available in the [Dify Core API](../dify/) examples, as these are system-level features shared across all APIs.

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

### Core Completion (6 APIs)
- **Text Generation**: Advanced text completion and generation
- **Multiple Response Modes**: Blocking and streaming responses
- **Parameter Control**: Flexible completion parameter configuration
- **Stop Generation**: Control over ongoing text generation
- **Application Info**: Access to completion app configuration

### Annotation Management (4 APIs)
- **Annotation CRUD**: Create, read, update, delete annotations
- **Reply Settings**: Configure annotation reply behavior
- **Status Monitoring**: Track annotation reply status
- **Content Management**: Rich annotation content handling

### Advanced Features
- **File Support**: Process documents and media files (via Dify Core API)
- **Audio Output**: Convert text responses to speech (via Dify Core API)
- **Feedback System**: User feedback collection (via Dify Core API)
- **Type Safety**: Comprehensive type hints with strict Literal types
- **Builder Pattern**: Fluent API construction
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
