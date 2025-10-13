# Dify-OAPI2 Project Overview

## Introduction

Dify-OAPI2 is a modern Python SDK for interacting with the Dify Service-API. This project is completely refactored from [dify-oapi](https://github.com/QiMington/dify-oapi), adopting modern Python practices with full support for the latest Dify API.

- **Project Name**: dify-oapi2
- **Version**: 1.0.1
- **License**: MIT
- **Python Version**: 3.10+
- **PyPI**: https://pypi.org/project/dify-oapi2/
- **Source Code**: https://github.com/nodite/dify-oapi2

## Technology Stack

### Core Technologies

- **Programming Language**: Python 3.10+
- **HTTP Client**: httpx (sync/async support with connection pooling optimization)
- **Type System**: Pydantic 2.x (data validation and type safety)
- **Architecture Patterns**:
  - Builder Pattern (fluent API design)
  - Service Layer Pattern (service layering)
- **Async Support**: Full async/await support with AsyncGenerator streaming

### Development Tools

- **Code Quality**:
  - Ruff (^0) - Fast Python linter and formatter (replaces Black + isort + flake8)
  - MyPy (^1) - Static type checking
  - Black (^25) - Alternative code formatter

- **Testing Framework**:
  - pytest (^8) - Testing framework
  - pytest-asyncio (^1) - Async testing support
  - pytest-env (^1) - Environment variable management

- **Development Workflow**:
  - pre-commit (^4) - Git hooks for automated code quality checks
  - commitizen (^4) - Semantic versioning and changelog generation
  - Poetry - Dependency management and packaging tool

### Core Dependencies

```toml
[tool.poetry.dependencies]
python = ">=3.10"
pydantic = "^2"    # Data validation and type safety
httpx = "^0"       # Modern HTTP client
```

## Project Structure

```
dify-oapi2/
├── dify_oapi/              # Main SDK package
│   ├── __init__.py
│   ├── client.py           # Main client interface (Builder pattern)
│   ├── api/                # API service modules
│   │   ├── chat/           # Chat API (18 APIs)
│   │   │   ├── service.py  # Service layer
│   │   │   └── v1/         # v1 implementation
│   │   │       ├── resource/   # Resource layer (annotation, chat, conversation, message)
│   │   │       └── model/      # Data models
│   │   ├── chatflow/       # Chatflow API (15 APIs)
│   │   │   ├── service.py
│   │   │   └── v1/         # Resources: annotation, chatflow, conversation
│   │   ├── completion/     # Completion API (10 APIs)
│   │   │   ├── service.py
│   │   │   └── v1/         # Resources: annotation, completion
│   │   ├── dify/           # Dify Core API (9 APIs)
│   │   │   ├── service.py
│   │   │   └── v1/         # Resources: audio, feedback, file, info
│   │   ├── knowledge/      # Knowledge Base API (33 APIs)
│   │   │   ├── service.py
│   │   │   └── v1/         # Resources: chunk, dataset, document, model, segment, tag
│   │   └── workflow/       # Workflow API (4 APIs)
│   │       ├── service.py
│   │       └── v1/         # Resources: workflow
│   └── core/               # Core functionality
│       ├── http/           # HTTP transport layer
│       │   └── transport/  # Transport implementations
│       │       ├── sync_transport.py      # Synchronous transport
│       │       ├── async_transport.py     # Asynchronous transport
│       │       ├── connection_pool.py     # Connection pool management
│       │       └── _misc.py               # Helper utilities
│       ├── model/          # Base models
│       │   ├── base_request.py    # Request base class
│       │   ├── base_response.py   # Response base class
│       │   ├── config.py          # Configuration model
│       │   ├── request_option.py  # Request options
│       │   ├── raw_request.py     # Raw request
│       │   └── raw_response.py    # Raw response
│       ├── utils/          # Utility functions
│       │   └── strings.py  # String processing
│       ├── const.py        # Constants
│       ├── enum.py         # Enumerations
│       ├── json.py         # JSON handling
│       ├── log.py          # Logging configuration
│       ├── misc.py         # Miscellaneous utilities
│       └── type.py         # Type definitions
├── docs/                   # Documentation
│   ├── overview.md         # Project overview (this document)
│   ├── chat/               # Chat API documentation
│   ├── chatflow/           # Chatflow API documentation
│   ├── completion/         # Completion API documentation
│   ├── dify/               # Dify Core API documentation
│   ├── knowledge/          # Knowledge Base API documentation
│   └── workflow/           # Workflow API documentation
├── examples/               # Complete example code
│   ├── README.md           # Examples overview
│   ├── connection_pool_example.py  # Connection pool optimization example
│   ├── chat/               # Chat API examples
│   ├── chatflow/           # Chatflow API examples
│   ├── completion/         # Completion API examples
│   ├── dify/               # Dify Core API examples
│   ├── knowledge/          # Knowledge Base API examples
│   └── workflow/           # Workflow API examples
├── tests/                  # Test suite
│   ├── conftest.py         # pytest configuration
│   ├── test_client.py      # Client tests
│   ├── chat/               # Chat API tests
│   ├── chatflow/           # Chatflow API tests
│   ├── completion/         # Completion API tests
│   ├── dify/               # Dify Core API tests
│   ├── knowledge/          # Knowledge Base API tests
│   ├── workflow/           # Workflow API tests
│   ├── core/               # Core functionality tests
│   │   ├── test_config.py
│   │   ├── test_error_handling.py
│   │   └── test_streaming.py
│   └── integration/        # Integration tests
│       ├── test_edge_cases.py
│       ├── test_end_to_end.py
│       └── test_performance.py
├── pyproject.toml          # Project configuration (Poetry + tools)
├── poetry.lock             # Dependency lock file
├── poetry.toml             # Poetry configuration
├── Makefile                # Development automation
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── .editorconfig           # Editor configuration
├── .gitignore              # Git ignore file
├── README.md               # Project README
├── DEVELOPMENT.md          # Development guide
├── LICENSE                 # MIT License
└── MANIFEST.in             # Package manifest
```

## API Service Modules

### 1. Chat API (18 APIs)

**Resources**: annotation (6), chat (3), conversation (6), message (3)

**Features**:
- Interactive Chat: Send messages with blocking/streaming responses
- Conversation Management: Complete conversation lifecycle operations
- Annotation System: Create, update, delete annotations with reply settings
- Message Operations: Basic message handling and history retrieval
- Streaming Support: Real-time streaming for chat responses
- Type Safety: Comprehensive type hints with strict Literal types

### 2. Chatflow API (15 APIs)

**Resources**: annotation (6), chatflow (3), conversation (6)

**Features**:
- Enhanced Chat: Advanced chat functionality with workflow events
- Conversation Management: Complete conversation operations with variables
- Annotation System: Full annotation management and reply configuration
- Workflow Integration: Seamless integration with workflow events
- Event Streaming: Real-time streaming with comprehensive event handling
- Type Safety: Strict Literal types for all predefined values

### 3. Completion API (10 APIs)

**Resources**: annotation (6), completion (4)

**Features**:
- Text Generation: Advanced text completion and generation
- Message Processing: Send messages and control text generation
- Annotation Management: Create, update, and manage annotations
- Generation Control: Stop ongoing text generation processes
- Streaming Support: Real-time text generation with streaming responses
- Type Safety: Full type validation with Pydantic models

### 4. Knowledge Base API (33 APIs)

**Resources**: chunk (4), dataset (6), document (10), model (1), segment (5), tag (7)

**Features**:
- Dataset Management: Complete dataset CRUD operations and content retrieval
- Document Processing: File upload, text processing, and batch management
- Content Organization: Fine-grained segmentation and chunk management
- Tag System: Flexible tagging and categorization system
- Model Integration: Embedding model information and configuration
- Search & Retrieval: Advanced search with multiple retrieval strategies

### 5. Workflow API (4 APIs)

**Resources**: workflow (4)

**Features**:
- Workflow Execution: Run workflows with blocking or streaming responses
- Execution Control: Stop running workflows and monitor progress
- Log Management: Retrieve detailed execution logs and run details
- Parameter Support: Flexible workflow parameter configuration

### 6. Dify Core API (9 APIs)

**Resources**: audio (2), feedback (2), file (1), info (4)

**Features**:
- Audio Processing: Speech-to-text and text-to-speech conversion
- Feedback System: Submit and retrieve user feedback
- File Management: Unified file upload and processing
- Application Info: App configuration, parameters, and metadata access

**Total**: 89 API methods across 6 services

## Core Architecture Design

### 1. Builder Pattern

Both client and request objects use the Builder pattern, providing a fluent, chainable interface:

```python
# Client building
client = (
    Client.builder()
    .domain("https://api.dify.ai")
    .max_connections(100)
    .keepalive_expiry(30.0)
    .timeout(60.0)
    .build()
)

# Request building
request = (
    ChatRequest.builder()
    .query("Hello")
    .user("user-123")
    .build()
)
```

### 2. Connection Pool Optimization

Uses httpx's connection pooling to optimize TCP connection reuse and reduce resource overhead:

```python
# Configuration parameters
max_keepalive_connections: int = 20  # Max keepalive connections per pool
max_connections: int = 100           # Max total connections per pool
keepalive_expiry: float = 30.0      # Keepalive connection expiry time (seconds)
```

### 3. Sync/Async Support

Full support for both synchronous and asynchronous operations:

```python
# Synchronous
response = client.chat.chat(request, request_option)

# Asynchronous
response = await client.chat.achat(request, request_option)

# Streaming synchronous
for chunk in client.chat.chat_stream(request, request_option):
    print(chunk)

# Streaming asynchronous
async for chunk in client.chat.achat_stream(request, request_option):
    print(chunk)
```

### 4. Type Safety

Comprehensive type validation using Pydantic 2.x:

- All request/response models have complete type hints
- Literal types for predefined values
- MyPy static type checking ensures type safety

### 5. Error Handling

Unified error handling mechanism:

- Automatic HTTP error retry (configurable retry count)
- Detailed error messages and logging
- Exception type hierarchy

## Development Tools Configuration

### Ruff Configuration

```toml
[tool.ruff]
line-length = 120
indent-width = 4

[tool.ruff.lint]
select = ["A", "B", "F", "N", "I", "UP", "E101", "RUF019", "RUF100", "RUF101", "S506", "W191", "W605"]
ignore = ["A002", "B904", "N805", "N806"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

### MyPy Configuration

```toml
[tool.mypy]
files = ["dify_oapi"]
python_version = "3.10"
strict_optional = true
ignore_missing_imports = true
check_untyped_defs = true
warn_return_any = true
warn_unreachable = true
```

### Pytest Configuration

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = ["--strict-markers", "--strict-config", "-ra"]
```

## Development Workflow

### Environment Setup

```bash
# Clone repository
git clone https://github.com/nodite/dify-oapi2.git
cd dify-oapi2

# Setup development environment (install dependencies and pre-commit hooks)
make dev-setup
```

### Code Quality Checks

```bash
# Format code
make format

# Check code style
make lint

# Fix auto-fixable issues
make fix

# Run all checks (lint + type check)
make check

# Run pre-commit hooks
make pre-commit
```

### Testing

```bash
# Set environment variables
export DOMAIN="https://api.dify.ai"
export CHAT_KEY="your-chat-api-key"
export KNOWLEDGE_KEY="your-knowledge-api-key"

# Run tests
make test

# Run tests with coverage
make test-cov

# Run specific module tests
poetry run pytest tests/knowledge/ -v
```

### Build and Publish

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

## Key Features

### 1. Complete API Coverage

- 89 API methods
- 6 major services
- 20+ resource types
- Complete CRUD operations

### 2. Modern Python Practices

- Python 3.10+ features
- Type hints and validation
- Async/sync dual support
- Builder pattern design

### 3. Performance Optimization

- HTTP connection pooling
- TCP connection reuse
- Configurable timeout and retry
- Streaming response support

### 4. Developer Friendly

- Fluent API design
- Complete documentation and examples
- Comprehensive test coverage
- Automated development tools

### 5. Production Ready

- Strict type checking
- Comprehensive error handling
- Logging and monitoring support
- SSL/TLS support

## Usage Examples

### Basic Usage

```python
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest

# Initialize client
client = (
    Client.builder()
    .domain("https://api.dify.ai")
    .max_connections(100)
    .keepalive_expiry(30.0)
    .build()
)

# Create request options
req_option = RequestOption.builder().api_key("your-api-key").build()

# Use Chat API
response = client.chat.chat(
    request=ChatRequest.builder()
    .query("Hello, how are you?")
    .user("user-123")
    .build(),
    request_option=req_option
)

print(response.answer)
```

### Streaming Response

```python
# Synchronous streaming
for event in client.chat.chat_stream(request, req_option):
    if event.event == "message":
        print(event.answer, end="", flush=True)

# Asynchronous streaming
async for event in client.chat.achat_stream(request, req_option):
    if event.event == "message":
        print(event.answer, end="", flush=True)
```

### File Upload

```python
from dify_oapi.api.dify.v1.model.file_upload_request import FileUploadRequest

# Upload file
with open("document.pdf", "rb") as f:
    response = client.dify.file_upload(
        request=FileUploadRequest.builder()
        .file(("document.pdf", f, "application/pdf"))
        .user("user-123")
        .build(),
        request_option=req_option
    )
```

## Test Coverage

### Unit Tests

- Core functionality tests (config, error_handling, streaming)
- Service API tests
- Model validation tests

### Integration Tests

- End-to-end tests
- Edge case tests
- Performance tests

### Test Structure

```
tests/
├── chat/           # Chat API tests (18 APIs)
├── chatflow/       # Chatflow API tests (15 APIs)
├── completion/     # Completion API tests (10 APIs)
├── dify/           # Dify Core API tests (9 APIs)
├── knowledge/      # Knowledge Base API tests (33 APIs)
├── workflow/       # Workflow API tests (4 APIs)
├── core/           # Core functionality tests
└── integration/    # Integration tests
```

## Documentation Resources

- **README.md**: Project description and quick start
- **DEVELOPMENT.md**: Development guide and workflow
- **docs/**: API documentation and usage guides
- **examples/**: Complete example code collection

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Write code and tests
4. Ensure code quality passes (`make check`)
5. Run full test suite (`make test`)
6. Commit changes (`git commit -m 'Add amazing feature'`)
7. Push to branch (`git push origin feature/amazing-feature`)
8. Submit a Pull Request

## License

MIT License - see [LICENSE](../LICENSE) file for details

## Related Links

- **PyPI Package**: https://pypi.org/project/dify-oapi2/
- **Source Code**: https://github.com/nodite/dify-oapi2
- **Dify Platform**: https://dify.ai/
- **Dify API Docs**: https://docs.dify.ai/

## Keywords

dify, ai, nlp, language-processing, python-sdk, async, type-safe, api-client
