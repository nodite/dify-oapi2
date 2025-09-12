# Dify-OAPI Examples

This directory contains comprehensive examples for all Dify-OAPI services. The examples are organized by API service and resource type to match the SDK structure.

## 📁 Directory Structure

```
examples/
├── chat/                    # Chat API Examples (22 APIs)
├── chatflow/               # Chatflow API Examples (17 APIs)
├── completion/             # Completion API Examples (15 APIs)
├── dify/                   # Dify Core API Examples
├── knowledge/              # Knowledge Base API Examples (33 APIs)
├── workflow/               # Workflow API Examples
└── connection_pool_example.py  # Connection pool optimization
```

## 🚀 Quick Start

### Environment Setup

Set your environment variables:

```bash
export DOMAIN="https://api.dify.ai"
export CHAT_KEY="your-chat-api-key"
export CHATFLOW_KEY="your-chatflow-api-key"
export COMPLETION_KEY="your-completion-api-key"
export DIFY_KEY="your-dify-api-key"
export WORKFLOW_KEY="your-workflow-api-key"
export KNOWLEDGE_KEY="your-knowledge-api-key"
```

### Basic Usage

```python
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

# Initialize client
client = Client.builder().domain("https://api.dify.ai").build()
req_option = RequestOption.builder().api_key("your-api-key").build()
```

## 📚 API Services

### [Chat API](./chat/README.md)
Interactive conversations with AI assistants
- **Resources**: annotation, chat, conversation, message
- **Features**: Streaming, file upload, feedback, audio processing

### [Chatflow API](./chatflow/README.md)
Enhanced chat functionality with workflow events
- **Resources**: annotation, chatflow, conversation
- **Features**: Advanced streaming, workflow integration

### [Completion API](./completion/README.md)
Text generation and completion
- **Resources**: annotation, completion
- **Features**: Blocking/streaming responses, file support

### [Dify Core API](./dify/README.md)
Essential Dify service functionality
- **Resources**: audio, feedback, file, info
- **Features**: Audio processing, file management, app info

### [Knowledge Base API](./knowledge/README.md)
Comprehensive knowledge management (33 APIs)
- **Resources**: chunk, dataset, document, model, segment, tag
- **Features**: Full CRUD operations, content organization

### [Workflow API](./workflow/README.md)
Automated workflow execution
- **Resources**: workflow
- **Features**: Blocking/streaming execution, file upload

## 🔧 Advanced Features

### Connection Pool Optimization
See [connection_pool_example.py](./connection_pool_example.py) for TCP connection optimization.

### Error Handling
All examples include proper error handling patterns.

### Async Support
Most examples can be adapted for async usage by using the `a*` methods (e.g., `achat` instead of `chat`).

## 📖 Documentation

Each directory contains:
- **README.md**: Service overview and usage guide
- **Resource directories**: Organized by API resource
- **Example files**: Complete, runnable examples

## 🤝 Contributing

When adding new examples:
1. Follow the existing directory structure
2. Include proper error handling
3. Add documentation and comments
4. Test examples before submitting

## 📄 License

MIT License - see [LICENSE](../LICENSE) file for details.
