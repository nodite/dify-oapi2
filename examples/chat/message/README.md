# Chat Message Operations Examples

This directory contains examples for basic message operations in the Chat API.

## 📋 Available Examples

- **`message_operations.py`** - Basic message sending and handling operations

## 🚀 Quick Start

### Basic Message Operation

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
print(f"Response: {response.answer}")
```

## 🔧 Features

- **Message Sending**: Send text messages to AI assistant
- **Response Handling**: Process AI responses
- **User Management**: Associate messages with specific users
- **Error Handling**: Robust error management

## 🔗 Related Examples

- [Chat Operations](../chat/) - Advanced chat functionality
- [Conversation Management](../conversation/) - Conversation lifecycle
