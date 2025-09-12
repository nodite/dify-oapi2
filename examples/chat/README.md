# Chat API Examples

The Chat API provides interactive conversation capabilities with AI assistants through 18 APIs. This directory contains examples for all chat-related operations organized by resource type.

## 📁 Resources

### [annotation/](./annotation/) - Annotation Management
Manage annotations and reply settings for chat messages.

**Available Examples:**
- `configure_annotation_reply.py` - Configure annotation reply settings
- `create_annotation.py` - Create new annotations
- `delete_annotation.py` - Delete existing annotations
- `get_annotation_reply_status.py` - Check annotation reply status
- `list_annotations.py` - List all annotations
- `update_annotation.py` - Update annotation content

### [chat/](./chat/) - Chat Operations
Core chat functionality including message sending and response handling.

**Available Examples:**
- `send_chat_message.py` - Send chat messages
- `stop_chat_generation.py` - Stop ongoing chat generation
- `get_suggested_questions.py` - Get suggested follow-up questions
- `blocking_response.py` - Handle blocking responses
- `streaming_response.py` - Handle streaming responses

### [conversation/](./conversation/) - Conversation Management
Manage conversation lifecycle and metadata.

**Available Examples:**
- `delete_conversation.py` - Delete conversations
- `get_conversation_variables.py` - Get conversation variables
- `get_conversations.py` - List conversations
- `get_message_history.py` - Get message history
- `rename_conversation.py` - Rename conversations
- `conversation_management.py` - Complete conversation management

### [message/](./message/) - Message Operations
Basic message operations and handling.

**Available Examples:**
- `message_operations.py` - Basic message operations

### [file/](./file/) - File Management
Upload and manage files for chat interactions.

**Available Examples:**
- `upload_file.py` - Upload images and documents

Note: Feedback and audio processing examples are available in the [Dify Core API](../dify/) examples, as these are part of the core Dify services.

## 🚀 Quick Start

### Basic Chat Example

```python
import os
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()

req_body = (
    ChatRequestBody.builder()
    .inputs({})
    .query("Hello, how can you help me?")
    .response_mode("blocking")
    .user("user-123")
    .build()
)

req = ChatRequest.builder().request_body(req_body).build()
req_option = RequestOption.builder().api_key(os.getenv("CHAT_KEY")).build()

response = client.chat.v1.chat.chat(req, req_option, False)
print(response.answer)
```

### Streaming Chat Example

```python
# Enable streaming for real-time responses
req_body = (
    ChatRequestBody.builder()
    .query("Tell me a story")
    .response_mode("streaming")
    .user("user-123")
    .build()
)

response = client.chat.v1.chat.chat(req, req_option, True)
for chunk in response:
    print(chunk, end="", flush=True)
```

## 🔧 Features

- **Multiple Response Modes**: Blocking and streaming responses
- **File Support**: Upload images and documents
- **Conversation Management**: Full conversation lifecycle
- **Annotation System**: Rich annotation and reply management
- **Type Safety**: Comprehensive type hints with strict Literal types
- **Builder Pattern**: Fluent API construction
- **Error Handling**: Comprehensive error handling examples

## 📖 Environment Variables

```bash
export DOMAIN="https://api.dify.ai"
export CHAT_KEY="your-chat-api-key"
```

## 🔗 Related APIs

- [Chatflow API](../chatflow/) - Enhanced chat with workflow events
- [Dify Core API](../dify/) - Core functionality like file upload
- [Completion API](../completion/) - Text completion services