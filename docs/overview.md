# Dify-OAPI2 Project Overview

## Project Introduction

Dify-OAPI2 is a Python SDK for interacting with the Dify Service-API, providing a fluent, type-safe interface for building AI-powered applications.

## Technology Stack

### Core Technologies
- **Python**: 3.10+
- **HTTP Client**: httpx (modern async HTTP client)
- **Data Validation**: Pydantic v2 (data validation and settings management)
- **Build Tool**: Poetry (dependency management and packaging)

### Development Tools
- **Code Formatting**: Ruff (fast Python linter and formatter)
- **Type Checking**: MyPy (static type checking)
- **Code Quality**: Pylint (code analysis)
- **Git Hooks**: Pre-commit (code quality checks)
- **Testing Framework**: Pytest (unit and integration testing)
- **Version Management**: Commitizen (semantic versioning)

## Project Structure

```
dify-oapi2/
├── dify_oapi/              # Main SDK package
│   ├── api/                # API service modules
│   │   ├── chat/           # Chat API (22 APIs)
│   │   ├── chatflow/       # Chatflow API (17 APIs)
│   │   ├── completion/     # Completion API (15 APIs)
│   │   ├── knowledge/      # Knowledge Base API (33 APIs)
│   │   ├── workflow/       # Workflow API
│   │   └── dify/           # Core Dify API
│   ├── core/               # Core functionality
│   │   ├── http/           # HTTP transport layer
│   │   ├── model/          # Base models
│   │   └── utils/          # Utility functions
│   └── client.py           # Main client interface
├── docs/                   # Documentation
├── examples/               # Usage examples
├── tests/                  # Test suite
└── Configuration files
```

## Core Module Details

### 1. API Service Modules (`dify_oapi/api/`)

#### Chat API (`chat/`)
- **Features**: Interactive conversations, file management, feedback collection, conversation management, audio processing
- **API Count**: 22 APIs
- **Capabilities**: Streaming responses, type safety

#### Chatflow API (`chatflow/`)
- **Features**: Enhanced chat functionality, workflow event handling
- **API Count**: 17 APIs
- **Capabilities**: Real-time streaming, event processing

#### Completion API (`completion/`)
- **Features**: Text generation, annotation management, audio processing
- **API Count**: 15 APIs

#### Knowledge API (`knowledge/`)
- **Features**: Dataset management, document processing, content segmentation, tag management
- **API Count**: 33 APIs
- **Capabilities**: Complete knowledge base lifecycle management

#### Workflow API (`workflow/`)
- **Features**: Automated workflow execution, parameter configuration, status monitoring

#### Dify Core API (`dify/`)
- **Features**: Essential Dify service functionality

### 2. Core Functionality Modules (`dify_oapi/core/`)

#### HTTP Transport Layer (`http/`)
- **Connection Pool**: Optimized TCP connection reuse
- **Transport**: Synchronous and asynchronous transport support
- **Configuration**: Configurable connection pool parameters

#### Model Layer (`model/`)
- **Base Request/Response**: BaseRequest, BaseResponse
- **Configuration Management**: Config class
- **Request Options**: RequestOption

#### Utility Functions (`utils/`)
- **String Processing**: String utility functions

### 3. Client Interface (`client.py`)

#### Client Class
- **Service Access**: Unified service access point
- **Connection Management**: HTTP connection pool management
- **Configuration**: Flexible client configuration

#### ClientBuilder Class
- **Builder Pattern**: Fluent client construction interface
- **Configuration Options**: Domain, log level, retry count, connection pool settings

## Dependencies

### Production Dependencies
```toml
python = ">=3.10"
pydantic = "^2"      # Data validation and settings management
httpx = "^0"         # Modern HTTP client
```

### Development Dependencies
```toml
# Testing
pytest = "^8"
pytest-env = "^1"
pytest-asyncio = "^1"

# Code Quality
pre-commit = "^4"
mypy = "^1"
ruff = "^0"
black = "^25"

# Version Management
commitizen = "^4"
```

## Design Patterns

### 1. Builder Pattern
- **Application**: All request objects and client construction
- **Advantages**: Fluent API interface, optional parameter handling

### 2. Service Layer Pattern
- **Application**: API service organization
- **Advantages**: Clear separation of concerns, easy maintenance

### 3. Transport Layer Abstraction
- **Application**: HTTP communication layer
- **Advantages**: Sync/async operation support, connection pool optimization

## Key Features

### 1. Type Safety
- Comprehensive type hints
- Pydantic data validation
- Strict Literal types

### 2. Performance Optimization
- HTTP connection pool reuse
- Configurable connection parameters
- Async operation support

### 3. Developer Experience
- Fluent builder API
- Complete example code
- Modern development toolchain

### 4. Extensibility
- Modular API design
- Clear abstraction layers
- Easy to add new API services

## Configuration Options

### Client Configuration
- **Domain**: API service address
- **Timeout**: Request timeout settings
- **Retry**: Failure retry count
- **Logging**: Log level control

### Connection Pool Configuration
- **Max Connections**: Maximum connections per pool
- **Keepalive Connections**: Active connection count
- **Connection Expiry**: Connection lifetime
- **SSL Verification**: SSL certificate verification settings

## Testing Strategy

### Test Types
- **Unit Tests**: Core functionality testing
- **Integration Tests**: API service integration testing
- **Module Tests**: Module structure validation

### Test Coverage
- Chat API testing
- Chatflow API testing
- Knowledge API testing
- Client integration testing

## Build and Release

### Build Tools
- **Poetry**: Dependency management and packaging
- **GitHub Actions**: CI/CD pipeline
- **PyPI**: Package publishing platform

### Release Process
1. Code quality checks (Ruff, MyPy)
2. Test execution (Pytest)
3. Version management (Commitizen)
4. Package building (Poetry)
5. Publishing to PyPI

## Version Information

- **Current Version**: 0.5.0
- **Python Requirements**: 3.10+
- **License**: MIT
- **Maintenance Status**: Active development