# Chatflow API Examples

The Chatflow API provides enhanced chat functionality with workflow events and advanced streaming capabilities. This directory contains examples for all chatflow operations with 15 APIs across 3 resource types.

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

**Note**: File upload, audio processing, and feedback examples are available in the [Dify Core API](../dify/) examples, as these are system-level features shared across all APIs.

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

### Chatflow Operations (3 APIs)
- **Enhanced Chat**: Advanced chat functionality with workflow integration
- **Message Control**: Send messages and stop generation
- **Suggested Questions**: AI-powered follow-up question suggestions

### Conversation Management (6 APIs)
- **Conversation CRUD**: Complete conversation lifecycle management
- **Message History**: Access to conversation message history
- **Variable Management**: Get and set conversation variables
- **Conversation Listing**: Paginated conversation retrieval
- **Rename Operations**: Update conversation titles
- **Delete Operations**: Clean up conversations

### Annotation Management (6 APIs)
- **Annotation CRUD**: Create, read, update, delete annotations
- **Reply Settings**: Configure annotation reply behavior
- **Status Monitoring**: Track annotation reply status
- **Content Management**: Rich annotation content handling

### Advanced Features
- **Enhanced Streaming**: Advanced streaming with comprehensive workflow events
- **Workflow Integration**: Seamless integration with workflow systems
- **Event Handling**: Real-time event streaming and processing
- **File Support**: Upload and process various file types (via Dify Core API)
- **Audio Processing**: Speech-to-text and text-to-speech (via Dify Core API)
- **Feedback System**: User feedback collection (via Dify Core API)
- **Type Safety**: Comprehensive type hints with strict Literal types
- **Builder Pattern**: Fluent API construction

## 📖 Environment Variables

```bash
export DOMAIN="https://api.dify.ai"
export CHATFLOW_KEY="your-chatflow-api-key"
```

## 🔗 Related APIs

- [Chat API](../chat/) - Basic chat functionality
- [Workflow API](../workflow/) - Workflow execution
- [Dify Core API](../dify/) - Core functionality