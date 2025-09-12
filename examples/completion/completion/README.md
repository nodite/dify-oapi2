# Completion Operations Examples

This directory contains examples for core completion functionality including text generation and response handling.

## 📋 Available Examples

### Message Operations
- **`send_message.py`** - Send completion requests
- **`stop_response.py`** - Stop ongoing text generation

### Response Modes
- **`blocking_completion.py`** - Synchronous completion example
- **`streaming_completion.py`** - Real-time streaming completion

## 🚀 Quick Start

### Basic Completion

```python
from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody

req_body = (
    SendMessageRequestBody.builder()
    .inputs({})
    .query("Write a short story")
    .response_mode("blocking")
    .user("user-123")
    .build()
)

req = SendMessageRequest.builder().request_body(req_body).build()
response = client.completion.v1.completion.send_message(req, req_option, False)
print(response.answer)
```

## 🔧 Features

- **Text Generation**: AI-powered text completion
- **Multiple Modes**: Blocking and streaming responses
- **Input Variables**: Dynamic input parameter support
- **Stop Control**: Ability to stop long-running generations