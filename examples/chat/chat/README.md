# Chat Operations Examples

This directory contains examples for core chat functionality including message sending, response handling, and conversation flow management.

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

### Response Modes
- **Blocking**: Synchronous responses, wait for complete answer
- **Streaming**: Real-time responses, receive chunks as they're generated

### Input Options
- **Text Queries**: Plain text questions and prompts
- **File Attachments**: Images, documents, and other media
- **Context Variables**: Pass additional context through inputs
- **Conversation Continuity**: Maintain conversation history

### Advanced Features
- **Stop Generation**: Interrupt long-running responses
- **Suggested Questions**: Get AI-generated follow-up questions
- **User Identification**: Track conversations by user ID
- **Error Handling**: Comprehensive error management

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