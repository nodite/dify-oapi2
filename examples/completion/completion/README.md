# Completion Operations Examples

This directory contains examples for core completion functionality (6 APIs) including advanced text generation, response handling, and application management with comprehensive streaming support.

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

### Core Completion APIs (6 APIs)
- **Send Message**: Primary text generation interface with advanced parameters
- **Stop Response**: Interrupt ongoing text generation processes
- **Get Application Parameters**: Retrieve app configuration and parameter schemas
- **Get Application Information**: Access application metadata and settings
- **Get Application Meta**: Retrieve comprehensive application metadata
- **Get Site Information**: Access site-level configuration and settings

### Text Generation Capabilities
- **Advanced AI Models**: Access to state-of-the-art language models
- **Dual Response Modes**: Blocking (synchronous) and streaming (real-time) responses
- **Parameter Control**: Fine-tune generation with temperature, max tokens, etc.
- **Input Flexibility**: Support for complex input variables and context
- **Generation Control**: Start, stop, and manage text generation processes

### Application Management
- **Configuration Access**: Retrieve application settings and parameters
- **Metadata Management**: Access comprehensive application information
- **Site Integration**: Connect with site-level configurations
- **Parameter Schemas**: Understand available input parameters and types
- **Runtime Information**: Access real-time application status and capabilities

### Advanced Features
- **Streaming Support**: Real-time text generation with AsyncGenerator
- **Context Management**: Maintain conversation context and history
- **File Integration**: Process files through Dify Core API integration
- **Error Recovery**: Robust error handling and retry mechanisms
- **Performance Optimization**: Efficient text generation with caching
- **Type Safety**: Comprehensive type validation with Pydantic models
