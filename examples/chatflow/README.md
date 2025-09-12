# Chatflow API Examples

The Chatflow API provides enhanced chat functionality with workflow events and advanced streaming capabilities. This directory contains examples for all chatflow-related operations.

## 📁 Resources

### [annotation/](./annotation/) - Annotation Management
Manage annotations and reply settings for chatflow messages.

**Available Examples:**
- `annotation_reply_settings.py` - Configure annotation reply settings
- `annotation_reply_status.py` - Check annotation reply status
- `create_annotation.py` - Create new annotations
- `delete_annotation.py` - Delete existing annotations
- `get_annotations.py` - List all annotations
- `update_annotation.py` - Update annotation content

### [chatflow/](./chatflow/) - Chatflow Operations
Core chatflow functionality with enhanced streaming and workflow integration.

**Available Examples:**
- `send_chat_message.py` - Send chatflow messages
- `stop_chat_message.py` - Stop ongoing message generation
- `get_suggested_questions.py` - Get suggested follow-up questions

### [conversation/](./conversation/) - Conversation Management
Manage conversation lifecycle with enhanced features.

**Available Examples:**
- `delete_conversation.py` - Delete conversations
- `get_conversation_messages.py` - Get conversation messages
- `get_conversation_variables.py` - Get conversation variables
- `get_conversations.py` - List conversations
- `rename_conversation.py` - Rename conversations

### [file/](./file/) - File Management
Upload and manage files for chatflow interactions.

**Available Examples:**
- `upload_file.py` - Upload files for processing

### [feedback/](./feedback/) - Feedback Management
Collect and manage user feedback on chatflow responses.

**Available Examples:**
- `get_feedbacks.py` - Retrieve feedback data
- `submit_feedback.py` - Submit user feedback

### [audio/](./audio/) - Audio Processing
Speech-to-text and text-to-speech capabilities.

**Available Examples:**
- `audio_to_text.py` - Convert audio to text
- `text_to_audio.py` - Convert text to audio

## 🚀 Quick Start

### Basic Chatflow Message

```python
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody

req_body = (
    SendChatMessageRequestBody.builder()
    .inputs({})
    .query("Hello, how can you help me?")
    .response_mode("streaming")
    .user("user-123")
    .build()
)

req = SendChatMessageRequest.builder().request_body(req_body).build()
response = client.chatflow.v1.chatflow.send_chat_message(req, req_option, True)

for chunk in response:
    print(chunk, end="", flush=True)
```

## 🔧 Features

- **Enhanced Streaming**: Advanced streaming with workflow events
- **Workflow Integration**: Seamless integration with workflow systems
- **File Support**: Upload and process various file types
- **Event Handling**: Comprehensive event streaming and handling
- **Annotation System**: Rich annotation and reply management

## 📖 Environment Variables

```bash
export DOMAIN="https://api.dify.ai"
export CHATFLOW_KEY="your-chatflow-api-key"
```

## 🔗 Related APIs

- [Chat API](../chat/) - Basic chat functionality
- [Workflow API](../workflow/) - Workflow execution
- [Dify Core API](../dify/) - Core functionality