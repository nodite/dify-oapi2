# Dify-OAPI

[![PyPI version](https://badge.fury.io/py/dify-oapi2.svg)](https://badge.fury.io/py/dify-oapi2)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern Python SDK for interacting with the Dify Service-API. This library provides a fluent, type-safe interface for building AI-powered applications using Dify's comprehensive API services including chat, completion, knowledge base, workflow, and chatflow features.

> This project is based on https://github.com/QiMington/dify-oapi, completely refactored with modern Python practices and full support for the latest Dify API.

## ✨ Features

-   **Complete API Coverage**: Chat (18 APIs), Chatflow (15 APIs), Completion (10 APIs), Knowledge Base (33 APIs), Workflow (4 APIs), and Core Dify (9 APIs)
-   **Builder Pattern**: Fluent, chainable interface for constructing requests
-   **Sync & Async Support**: Both synchronous and asynchronous operations
-   **Streaming Responses**: Real-time streaming for chat and completion
-   **Type Safety**: Comprehensive type hints with Pydantic 2.x validation
-   **File Upload**: Support for images and documents
-   **Modern HTTP Client**: Built on httpx for reliable API communication
-   **Connection Pool Optimization**: Efficient TCP connection reuse to reduce resource overhead

## 📦 Installation

```bash
pip install dify-oapi2
```

**Requirements**: Python 3.10+

**Core Dependencies**:

-   `pydantic` (^2) - Data validation and settings management with type safety
-   `httpx` (^0) - Modern async HTTP client

**Development Dependencies**:

-   `ruff` (^0) - Fast Python linter and formatter
-   `mypy` (^1) - Static type checking
-   `pytest` (^8) - Testing framework
-   `pre-commit` (^4) - Git hooks for code quality
-   `commitizen` (^4) - Semantic versioning and changelog generation
-   `poetry` - Dependency management and packaging

## 🛠️ Technology Stack

-   **Language**: Python 3.10+
-   **HTTP Client**: httpx with connection pooling optimization
-   **Type System**: Pydantic 2.x with comprehensive type validation
-   **Architecture**: Builder pattern with fluent API design + Service layer pattern
-   **Async Support**: Full async/await support with AsyncGenerator streaming
-   **Code Quality**: Ruff (linting + formatting) + MyPy (type checking)
-   **Testing**: pytest with async support and comprehensive coverage
-   **Packaging**: Poetry with modern Python packaging standards
-   **Total Coverage**: 89 API methods across 6 services with complete examples

## 🚀 Quick Start

### Basic Usage

```python
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest

# Initialize client with builder pattern
client = (
    Client.builder()
    .domain("https://api.dify.ai")
    .max_connections(100)
    .keepalive_expiry(30.0)
    .build()
)

# Create request options
req_option = RequestOption.builder().api_key("your-api-key").build()

# Use the chat API
response = client.chat.chat(
    request=ChatRequest.builder()
    .query("Hello, how are you?")
    .user("user-123")
    .build(),
    request_option=req_option
)

print(response.answer)
```

### Comprehensive Examples

Ready to build AI-powered applications? Check out our comprehensive examples:

-   **[Chat Examples](./examples/chat/)** - Interactive conversations and streaming responses
-   **[Chatflow Examples](./examples/chatflow/)** - Enhanced chat with workflow events
-   **[Knowledge Base Examples](./examples/knowledge/)** - Build and query knowledge bases
-   **[Workflow Examples](./examples/workflow/)** - Automate complex AI workflows
-   **[Complete Examples Collection](./examples/)** - All API services with detailed usage patterns

Each example includes complete, runnable code with detailed explanations.

## 🔧 API Services

### Chat API (18 APIs)

**Resources**: annotation (6), chat (3), conversation (6), message (3)

-   **Interactive Chat**: Send messages with blocking/streaming responses
-   **Conversation Management**: Complete conversation lifecycle operations
-   **Annotation System**: Create, update, delete annotations with reply settings
-   **Message Operations**: Basic message handling and history retrieval
-   **Streaming Support**: Real-time streaming for chat responses
-   **Type Safety**: Comprehensive type hints with strict Literal types

### Chatflow API (15 APIs)

**Resources**: annotation (6), chatflow (3), conversation (6)

-   **Enhanced Chat**: Advanced chat functionality with workflow events
-   **Conversation Management**: Complete conversation operations with variables
-   **Annotation System**: Full annotation management and reply configuration
-   **Workflow Integration**: Seamless integration with workflow events
-   **Event Streaming**: Real-time streaming with comprehensive event handling
-   **Type Safety**: Strict Literal types for all predefined values

### Completion API (10 APIs)

**Resources**: annotation (6), completion (4)

-   **Text Generation**: Advanced text completion and generation
-   **Message Processing**: Send messages and control text generation
-   **Annotation Management**: Create, update, and manage annotations
-   **Generation Control**: Stop ongoing text generation processes
-   **Streaming Support**: Real-time text generation with streaming responses
-   **Type Safety**: Full type validation with Pydantic models

### Knowledge Base API (33 APIs)

**Resources**: chunk (4), dataset (6), document (10), model (1), segment (5), tag (7)

-   **Dataset Management**: Complete dataset CRUD operations and content retrieval
-   **Document Processing**: File upload, text processing, and batch management
-   **Content Organization**: Fine-grained segmentation and chunk management
-   **Tag System**: Flexible tagging and categorization system
-   **Model Integration**: Embedding model information and configuration
-   **Search & Retrieval**: Advanced search with multiple retrieval strategies

### Workflow API (4 APIs)

**Resources**: workflow (4)

-   **Workflow Execution**: Run workflows with blocking or streaming responses
-   **Execution Control**: Stop running workflows and monitor progress
-   **Log Management**: Retrieve detailed execution logs and run details
-   **Parameter Support**: Flexible workflow parameter configuration

### Dify Core API (9 APIs)

**Resources**: audio (2), feedback (2), file (1), info (4)

-   **Audio Processing**: Speech-to-text and text-to-speech conversion
-   **Feedback System**: Submit and retrieve user feedback
-   **File Management**: Unified file upload and processing
-   **Application Info**: App configuration, parameters, and metadata access

## 💡 Examples

Explore comprehensive examples in the [examples directory](./examples):

### Chat Examples

-   [**Chat Messages**](./examples/chat/chat/) - Send messages, stop generation, get suggestions
-   [**Conversation Management**](./examples/chat/conversation/) - Complete conversation operations
-   [**Message Operations**](./examples/chat/message/) - Basic message operations
-   [**Annotation Management**](./examples/chat/annotation/) - Annotation CRUD and reply settings

_Note: File upload and feedback examples are available in [Dify Core API](./examples/dify/) as shared services._

### Completion Examples

-   [**Completion Operations**](./examples/completion/completion/) - Text generation and completion
-   [**Annotation Management**](./examples/completion/annotation/) - Annotation operations

### Knowledge Base Examples

-   [**Dataset Management**](./examples/knowledge/dataset/) - Complete dataset operations
-   [**Document Processing**](./examples/knowledge/document/) - File upload and text processing
-   [**Content Organization**](./examples/knowledge/segment/) - Segment and chunk management
-   [**Tag Management**](./examples/knowledge/tag/) - Metadata and tagging system

### Chatflow Examples

-   [**Advanced Chat**](./examples/chatflow/chatflow/) - Enhanced chat with streaming and workflow events
-   [**Conversation Management**](./examples/chatflow/conversation/) - Complete conversation operations
-   [**Annotation Management**](./examples/chatflow/annotation/) - Annotation CRUD and reply settings

### Dify Core Examples

-   [**Audio Processing**](./examples/dify/audio/) - Speech-to-text and text-to-speech
-   [**Feedback Management**](./examples/dify/feedback/) - User feedback collection
-   [**File Management**](./examples/dify/file/) - File upload and processing
-   [**Application Info**](./examples/dify/info/) - App configuration and metadata

### Workflow Examples

-   [**Workflow Operations**](./examples/workflow/workflow/) - Workflow execution and management
-   [**File Upload**](./examples/workflow/file/) - File upload for workflows

For detailed examples and usage patterns, see the [examples README](./examples/README.md).

## 🛠️ Development

### Prerequisites

-   Python 3.10+
-   Poetry (for dependency management)
-   Git (for version control)

### Setup

```bash
# Clone repository
git clone https://github.com/nodite/dify-oapi2.git
cd dify-oapi2

# Setup development environment (installs dependencies and pre-commit hooks)
make dev-setup
```

### Code Quality Tools

This project uses modern Python tooling for code quality:

-   **Ruff**: Fast Python linter and formatter (replaces Black + isort + flake8)
-   **MyPy**: Static type checking for type safety
-   **Pre-commit**: Git hooks for automated code quality checks
-   **Poetry**: Modern dependency management and packaging

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
# Set environment variables for integration tests
export DOMAIN="https://api.dify.ai"
export CHAT_KEY="your-chat-api-key"
export CHATFLOW_KEY="your-chatflow-api-key"
export COMPLETION_KEY="your-completion-api-key"
export DIFY_KEY="your-dify-api-key"
export WORKFLOW_KEY="your-workflow-api-key"
export KNOWLEDGE_KEY="your-knowledge-api-key"

# Run tests
make test

# Run tests with coverage
make test-cov

# Run specific test module
poetry run pytest tests/knowledge/ -v
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
dify-oapi2/
├── dify_oapi/           # Main SDK package
│   ├── api/             # API service modules
│   │   ├── chat/        # Chat API (18 APIs)
│   │   │   └── v1/      # Version 1 implementation
│   │   ├── chatflow/    # Chatflow API (15 APIs)
│   │   │   └── v1/      # Version 1 implementation
│   │   ├── completion/  # Completion API (10 APIs)
│   │   │   └── v1/      # Version 1 implementation
│   │   ├── dify/        # Core Dify API (9 APIs)
│   │   │   └── v1/      # Version 1 implementation
│   │   ├── knowledge/   # Knowledge Base API (33 APIs)
│   │   │   └── v1/      # Version 1 implementation
│   │   └── workflow/    # Workflow API (6 APIs)
│   │       └── v1/      # Version 1 implementation
│   ├── core/            # Core functionality
│   │   ├── http/        # HTTP transport layer with connection pooling
│   │   ├── model/       # Base models and configurations
│   │   └── utils/       # Utility functions
│   └── client.py        # Main client interface with builder pattern
├── docs/                # Comprehensive documentation
├── examples/            # Complete usage examples for all APIs
├── tests/               # Comprehensive test suite
├── pyproject.toml       # Project configuration (Poetry + tools)
├── Makefile            # Development automation
└── DEVELOPMENT.md      # Development guide
```

## 📖 Documentation

-   [**Development Guide**](./DEVELOPMENT.md) - Setup, workflow, and contribution guidelines
-   [**Project Overview**](./docs/overview.md) - Architecture and technical details
-   [**API Documentation**](./docs/) - Complete API documentation by service
-   [**Examples**](./examples/README.md) - Comprehensive usage examples and patterns

## 🤝 Contributing

Contributions are welcome! Please follow our development workflow:

1. Fork the repository
2. Clone and checkout the `main` branch (`git checkout main`)
3. Create a feature branch from `main` (`git checkout -b feature/amazing-feature`)
4. Make your changes with comprehensive tests
5. Ensure code quality passes (`make check`)
6. Run the full test suite (`make test`)
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to the branch (`git push origin feature/amazing-feature`)
9. Submit a pull request to the `main` branch

### Branch Strategy

-   `main` - Main development branch, **all development and PRs are based on this branch**
-   `feature/*` - Feature branches, created from and merged back to `main`
-   `bugfix/*` - Bug fix branches, created from and merged back to `main`
-   `hotfix/*` - Urgent fixes, created from and merged back to `main`

See [DEVELOPMENT.md](./DEVELOPMENT.md) for detailed development guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🔗 Links

-   **PyPI Package**: https://pypi.org/project/dify-oapi2/
-   **Source Code**: https://github.com/nodite/dify-oapi2
-   **Dify Platform**: https://dify.ai/
-   **Dify API Docs**: https://docs.dify.ai/

---

**Keywords**: dify, ai, nlp, language-processing, python-sdk, async, type-safe, api-client
