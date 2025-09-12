# Chat Operations Examples

This directory contains examples for core chat functionality (3 APIs) including message sending, response handling, and conversation flow management with comprehensive streaming support.

## 📋 Available Examples

### Message Operations
- **`send_chat_message.py`** - Send chat messages with various options
- **`stop_chat_generation.py`** - Stop ongoing chat message generation
- **`get_suggested_questions.py`** - Get AI-suggested follow-up questions

### Response Handling
- **`blocking_response.py`** - Handle synchronous, blocking responses
- **`streaming_response.py`** - Handle real-time streaming responses

## 🚀 Quick Start

### Basic Chat Message

```python
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody

req_body = (
    ChatRequestBody.builder()
    .inputs({})
    .query("Hello, how are you?")
    .response_mode("blocking")
    .user("user-123")
    .build()
)

req = ChatRequest.builder().request_body(req_body).build()
response = client.chat.v1.chat.chat(req, req_option, False)
print(response.answer)
```

### Streaming Response

```python
req_body = (
    ChatRequestBody.builder()
    .query("Tell me a long story")
    .response_mode("streaming")
    .user("user-123")
    .build()
)

req = ChatRequest.builder().request_body(req_body).build()
response = client.chat.v1.chat.chat(req, req_option, True)

for chunk in response:
    print(chunk, end="", flush=True)
```

### With File Upload

```python
from dify_oapi.api.chat.v1.model.chat_file import ChatFile

req_file = (
    ChatFile.builder()
    .type("image")
    .transfer_method("remote_url")
    .url("https://example.com/image.jpg")
    .build()
)

req_body = (
    ChatRequestBody.builder()
    .query("What do you see in this image?")
    .files([req_file])
    .response_mode("blocking")
    .user("user-123")
    .build()
)
```

## 🔧 Features

### Core Chat APIs (3 APIs)
- **Send Chat Message**: Primary chat interface with blocking/streaming modes
- **Stop Chat Generation**: Interrupt ongoing message generation
- **Get Suggested Questions**: AI-powered follow-up question recommendations

### Response Modes
- **Blocking Mode**: Synchronous responses, wait for complete answer
- **Streaming Mode**: Real-time responses, receive chunks as they're generated
- **Hybrid Support**: Switch between modes based on use case

### Input Capabilities
- **Text Queries**: Plain text questions and prompts
- **File Attachments**: Images, documents, and other media (via Dify Core API)
- **Context Variables**: Pass additional context through inputs parameter
- **Conversation Continuity**: Maintain conversation history with conversation_id
- **User Tracking**: Associate messages with specific users

### Advanced Features
- **Generation Control**: Start and stop message generation dynamically
- **Intelligent Suggestions**: Context-aware follow-up question generation
- **Multi-modal Support**: Text, image, and document processing
- **Real-time Streaming**: Low-latency streaming with AsyncGenerator support
- **Type Safety**: Comprehensive type validation with strict Literal types
- **Error Recovery**: Robust error handling and retry mechanisms

## 📖 Best Practices

1. **Use Streaming for Long Responses**: Better user experience for lengthy content
2. **Handle Errors Gracefully**: Always wrap API calls in try-catch blocks
3. **Set Appropriate Timeouts**: Configure timeouts for your use case
4. **Manage Conversation State**: Use conversation_id to maintain context
5. **Optimize File Uploads**: Use appropriate transfer methods for files

## 🔗 Related Examples

- [File Management](../file/) - File upload and handling
- [Conversation Management](../conversation/) - Conversation lifecycle
- [Feedback](../feedback/) - User feedback collection