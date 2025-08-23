# Dify-OAPI

[![PyPI version](https://badge.fury.io/py/dify-oapi2.svg)](https://badge.fury.io/py/dify-oapi2)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python SDK for interacting with the Dify Service-API. This library provides a fluent, type-safe interface for building AI-powered applications using Dify's API services including chat, completion, knowledge base, and workflow features.

> This project is based on https://github.com/QiMington/dify-oapi, with refactoring and support for the latest Dify API.

## ✨ Features

- **Multiple API Services**: Chat, Completion, Knowledge Base (39 APIs), Workflow, and Core Dify APIs
- **Builder Pattern**: Fluent, chainable interface for constructing requests
- **Sync & Async Support**: Both synchronous and asynchronous operations
- **Streaming Responses**: Real-time streaming for chat and completion
- **Type Safety**: Comprehensive type hints with Pydantic validation
- **File Upload**: Support for images and documents
- **Modern HTTP Client**: Built on httpx for reliable API communication

## 📦 Installation

```bash
pip install dify-oapi2
```

**Requirements**: Python 3.10+

**Dependencies**:
- `pydantic` (>=1.10,<3.0.0) - Data validation and settings management
- `httpx` (>=0.24,<1.0) - Modern HTTP client

## 🚀 Quick Start

### Basic Chat Example

```python
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

# Initialize client
client = Client.builder().domain("https://api.dify.ai").build()

# Build request
req_body = (
    ChatRequestBody.builder()
    .inputs({})
    .query("What can Dify API do?")
    .response_mode("blocking")
    .user("user-123")
    .build()
)

req = ChatRequest.builder().request_body(req_body).build()
req_option = RequestOption.builder().api_key("your-api-key").build()

# Execute request
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

req = ChatRequest.builder().request_body(req_body).build()
response = client.chat.v1.chat.chat(req, req_option, True)

# Process streaming response
for chunk in response:
    print(chunk, end="", flush=True)
```

### Async Support

```python
import asyncio

async def async_chat():
    response = await client.chat.v1.chat.achat(req, req_option, False)
    print(response.answer)

asyncio.run(async_chat())
```

## 🔧 API Services

### Chat API
- Interactive conversations with AI assistants
- File upload support (images, documents)
- Conversation and message history management
- Streaming and blocking response modes

### Completion API (15 APIs)
- **Message Processing**: Send messages and control responses
- **Annotation Management**: Create, update, and manage annotations
- **Audio Processing**: Text-to-audio conversion
- **Feedback System**: Collect and analyze user feedback
- **File Upload**: Support for document and media files
- **Application Info**: Configuration and metadata retrieval

### Knowledge Base API (39 APIs)
- **Dataset Management**: CRUD operations for datasets
- **Document Management**: Upload, process, and manage documents
- **Segment Management**: Fine-grained content segmentation
- **Metadata & Tags**: Custom metadata and knowledge type tags
- **Retrieval**: Advanced search and retrieval functionality

### Workflow API
- Automated workflow execution
- Parameter configuration
- Status monitoring

### Dify Core API
- Essential Dify service functionality

## 💡 Examples

Explore comprehensive examples in the [examples directory](./examples):

### Chat Examples
- [**Blocking Response**](./examples/chat/blocking_response.py) - Standard chat interactions
- [**Streaming Response**](./examples/chat/streaming_response.py) - Real-time streaming chat
- [**Conversation Management**](./examples/chat/conversation_management.py) - Managing chat history

### Completion Examples
- [**Basic Completion**](./examples/completion/basic_completion.py) - Text generation

### Knowledge Base Examples
- [**List Datasets**](./examples/knowledge_base/list_datasets.py) - Dataset management

For detailed examples and usage patterns, see the [examples README](./examples/README.md).

## 🛠️ Development

### Prerequisites
- Python 3.10+
- Poetry

### Setup

```bash
# Clone repository
git clone https://github.com/nodite/dify-oapi2.git
cd dify-oapi

# Setup development environment (installs dependencies and pre-commit hooks)
make dev-setup
```

### Code Quality Tools

This project uses modern Python tooling:

- **Ruff**: Fast Python linter and formatter
- **MyPy**: Static type checking
- **Pre-commit**: Git hooks for code quality
- **Pylint**: Additional code analysis

```bash
# Format code
make format

# Lint code
make lint

# Fix linting issues
make fix

# Run all checks (lint + type check)
make check

# Install pre-commit hooks
make install-hooks

# Run pre-commit hooks manually
make pre-commit
```

### Testing

```bash
# Set environment variables
export DOMAIN="https://api.dify.ai"
export CHAT_KEY="your-api-key"

# Run tests
make test

# Run tests with coverage
make test-cov
```

### Build & Publish

```bash
# Configure PyPI tokens (one-time setup)
poetry config http-basic.testpypi __token__ <your-testpypi-token>
poetry config http-basic.pypi __token__ <your-pypi-token>

# Build package
make build

# Publish to TestPyPI (for testing)
make publish-test

# Publish to PyPI (maintainers only)
make publish
```

### Project Structure

```
dify-oapi/
├── dify_oapi/           # Main SDK package
│   ├── api/             # API service modules
│   │   ├── chat/        # Chat API
│   │   ├── completion/  # Completion API
│   │   ├── dify/        # Core Dify API
│   │   ├── knowledge_base/ # Knowledge Base API (39 APIs)
│   │   └── workflow/    # Workflow API
│   ├── core/            # Core functionality
│   │   ├── http/        # HTTP transport layer
│   │   ├── model/       # Base models
│   │   └── utils/       # Utilities
│   └── client.py        # Main client interface
├── docs/                # Documentation
├── examples/            # Usage examples
├── tests/               # Test suite
└── pyproject.toml       # Project configuration
```

## 📖 Documentation

- [**Project Overview**](./docs/overview.md) - Architecture and technical details
- [**Completion APIs**](./docs/completion/apis.md) - Complete completion API documentation
- [**Knowledge Base APIs**](./docs/datasets/apis.md) - Complete dataset API documentation
- [**Examples**](./examples/README.md) - Usage examples and patterns

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Ensure code quality (`ruff format`, `ruff check`, `mypy`)
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🔗 Links

- **PyPI Package**: https://pypi.org/project/dify-oapi2/
- **Source Code**: https://github.com/nodite/dify-oapi2
- **Dify Platform**: https://dify.ai/
- **Dify API Docs**: https://docs.dify.ai/

## 📄 License

MIT License - see [LICENSE](./LICENSE) file for details.

---

**Keywords**: dify, nlp, ai, language-processing
