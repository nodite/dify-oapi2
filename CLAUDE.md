# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**dify-oapi2** is a modern Python SDK for the Dify Service-API that provides type-safe, async-capable interfaces for AI-powered applications. The SDK uses builder patterns, comprehensive type hints with Pydantic 2.x validation, and supports both synchronous and asynchronous operations with streaming capabilities.

**Total API Coverage**: 89 API methods across 6 services (Chat, Chatflow, Completion, Knowledge Base, Workflow, Dify Core)

## Development Commands

### Setup
```bash
make dev-setup          # Initial setup: install dependencies + pre-commit hooks
make install            # Install/update dependencies only
```

### Code Quality
```bash
make format             # Format code with ruff
make lint               # Check for linting issues
make fix                # Auto-fix linting issues
make check              # Run all checks (ruff + mypy)
make pre-commit         # Run pre-commit hooks manually
```

### Testing
```bash
# Set environment variables first
export DOMAIN="https://api.dify.ai"
export CHAT_KEY="your-chat-api-key"
export CHATFLOW_KEY="your-chatflow-api-key"
export COMPLETION_KEY="your-completion-api-key"
export DIFY_KEY="your-dify-api-key"
export WORKFLOW_KEY="your-workflow-api-key"
export KNOWLEDGE_KEY="your-knowledge-api-key"

make test               # Run all tests
make test-cov           # Run tests with coverage report

# Run specific service tests
poetry run pytest tests/knowledge/ -v
poetry run pytest tests/chat/ -v

# Run specific test patterns
poetry run pytest tests/ -k "test_create" -v
```

### Build & Publish
```bash
make clean              # Clean build artifacts
make build              # Build package
make publish-test       # Publish to TestPyPI (requires token setup)
make publish            # Publish to PyPI (maintainers only)
```

## Architecture Overview

### Core Design Patterns

**Builder Pattern**: All clients, requests, and configuration objects use fluent builder pattern for construction:
```python
client = Client.builder().domain("https://api.dify.ai").build()
request = ChatRequest.builder().query("Hello").user("user-123").build()
option = RequestOption.builder().api_key("key").build()
```

**Service Layer Pattern**: API organized as `Client → Service → Version → Resource`:
- `Client` (client.py): Main entry point with service properties
- `Service` (*/service.py): Version routing (e.g., ChatService → V1)
- `Version` (*/v1/version.py): Resource initialization
- `Resource` (*/v1/resource/*.py): Individual API implementations

**Connection Pool Management**: HTTP transport uses singleton `ConnectionPoolManager` (core/http/transport/connection_pool.py) for efficient TCP connection reuse with configurable limits.

### Directory Structure

```
dify_oapi/
├── client.py                    # Client + ClientBuilder classes
├── api/                         # API service modules
│   ├── chat/                    # Chat API (18 APIs: annotation, chat, conversation, message)
│   ├── chatflow/                # Chatflow API (15 APIs: annotation, chatflow, conversation)
│   ├── completion/              # Completion API (10 APIs: annotation, completion)
│   ├── dify/                    # Core Dify API (9 APIs: audio, feedback, file, info)
│   ├── knowledge/               # Knowledge Base API (33 APIs: chunk, dataset, document, model, segment, tag)
│   └── workflow/                # Workflow API (4 APIs: workflow)
├── core/                        # Core functionality
│   ├── http/transport/          # HTTP transport with connection pooling
│   ├── model/                   # Base models (Config, RequestOption, BaseRequest/Response)
│   └── utils/                   # Utility functions

# Each API service follows this pattern:
api/{service}/
├── service.py                   # Service class (routes to v1)
└── v1/
    ├── version.py               # V1 class (initializes resources)
    ├── model/                   # Request/response models with builder patterns
    └── resource/                # Resource implementations (API methods)
```

### Type Safety & Validation

- **Pydantic 2.x**: All models use Pydantic BaseModel for validation
- **Type Hints**: Comprehensive type hints throughout (Python 3.10+)
- **Literal Types**: Strict Literal types for predefined values (e.g., retrieval_model: Literal["single", "multiple"])
- **Overloads**: @overload decorators for streaming vs non-streaming responses
- **MyPy**: Static type checking enforced (run `make check`)

### Request/Response Flow

1. **Build Request**: Use builder pattern to construct typed request model
2. **Execute**: Pass to resource method → Transport.execute() or ATransport.execute()
3. **Transport Layer**: ConnectionPoolManager provides reusable httpx.Client/AsyncClient
4. **Unmarshal**: Response parsed to typed response model or streamed as Generator/AsyncGenerator

### Async Support

All resource methods have async counterparts (prefix with `a`):
- `chat()` → `achat()`
- `create_dataset()` → `acreate_dataset()`

Streaming returns `Generator[bytes, None, None]` (sync) or `AsyncGenerator[bytes, None]` (async).

## Code Style Guidelines

**Enforced by Ruff + MyPy** (configured in pyproject.toml):

- **Line Length**: 120 characters
- **Quotes**: Double quotes for strings
- **Indentation**: 4 spaces
- **Target**: Python 3.10+
- **Naming**: PEP 8 conventions
- **Type Hints**: Required for all public functions/methods
- **Imports**: Auto-sorted by ruff (isort rules)

**Ruff Rules**: `E` (pycodestyle errors), `F` (pyflakes), `I` (isort), `N` (naming), `UP` (pyupgrade), `B` (bugbear), `A` (builtins), `RUF` (ruff-specific)

**Ignored Rules**: `B904` (raise-without-from), `N805`/`N806` (method/variable naming flexibility)

## Testing Strategy

Tests mirror the `dify_oapi/api` structure exactly:

```
tests/
├── {service}/
│   ├── v1/
│   │   ├── resource/
│   │   │   └── test_{resource}.py      # Resource method tests
│   │   ├── model/
│   │   │   └── test_models.py          # Model validation tests
│   │   └── test_integration.py         # Integration tests
│   └── test_service.py                  # Service-level tests
├── core/                                # Core functionality tests
└── test_client.py                       # Client tests
```

**Test Fixtures** (tests/conftest.py):
- `mock_config()`: Mock Config object
- `request_option()`: Test RequestOption with "test-key"
- `mock_response()`: Mock response object

**Running Specific Tests**:
```bash
# Single resource
poetry run pytest tests/knowledge/v1/resource/test_dataset.py -v

# Single test
poetry run pytest tests/chat/v1/resource/test_chat.py::test_chat -v
```

## Common Development Patterns

### Adding a New API Method

1. **Define Models** (api/{service}/v1/model/):
   - Create `{method}_request.py` with builder pattern
   - Create `{method}_response.py` with Pydantic model
   - Use Literal types for predefined values

2. **Implement Resource Method** (api/{service}/v1/resource/{resource}.py):
   - Add method with @overload for streaming variants
   - Call Transport.execute() with appropriate unmarshal_as
   - Add async variant (prefix with `a`)

3. **Add Tests** (tests/{service}/v1/resource/test_{resource}.py):
   - Unit tests for method logic
   - Integration tests if environment variables set

4. **Update Documentation**: Add example to examples/{service}/{resource}/

### Accessing Nested Resources

Services expose resources through version:
```python
client.chat.v1.chat.chat(...)           # Chat service → v1 → chat resource → chat method
client.knowledge.v1.dataset.create(...)  # Knowledge service → v1 → dataset resource → create method
```

For convenience, some services may expose common resources directly (check the Version class).

### Environment Variables for Testing

The SDK requires API keys per service for integration tests. Set these before running tests:
- `DOMAIN`: Dify API endpoint
- `{SERVICE}_KEY`: API key for each service (CHAT_KEY, KNOWLEDGE_KEY, etc.)

## Pre-commit Hooks

Auto-runs on `git commit`:
1. **ruff format**: Format code
2. **ruff check --fix**: Lint and auto-fix
3. **mypy**: Type checking
4. **pylint**: Additional linting (max 50 statements per function)
5. **commitizen**: Enforce conventional commit messages
6. **Standard hooks**: trailing-whitespace, end-of-file-fixer, check-yaml, etc.

If hooks fail, fix issues and commit again. To bypass (not recommended): `git commit --no-verify`

## Branch Strategy

- **main**: Primary development branch (all PRs target this)
- **feature/***: New features (branch from main)
- **bugfix/***: Bug fixes (branch from main)
- **hotfix/***: Urgent fixes (branch from main)

**Workflow**:
1. Checkout main: `git checkout main && git pull`
2. Create branch: `git checkout -b feature/my-feature`
3. Make changes, ensure `make check` and `make test` pass
4. Commit with conventional message (enforced by commitizen)
5. Push and create PR to main

## Important Notes

- **Never commit** without passing `make check` (ruff + mypy)
- **Builder Pattern**: Always use `.builder()` for constructing requests/responses
- **Async Cleanup**: Call `client.aclose()` or `client.close()` to properly cleanup connections
- **Connection Pooling**: Configured via ClientBuilder (max_connections, max_keepalive_connections, keepalive_expiry)
- **Streaming**: Set `stream=True` parameter for streaming responses (returns Generator/AsyncGenerator)
- **Version Routing**: Access APIs via service.v1.resource (prepared for future API versions)

## Publishing Workflow

**One-time setup**:
```bash
poetry config http-basic.testpypi __token__ <testpypi-token>
poetry config http-basic.pypi __token__ <pypi-token>
```

**Release Process** (maintainers only):
1. Update version: `poetry version patch|minor|major`
2. Update CHANGELOG (commitizen auto-generates on bump)
3. Test build: `make build`
4. Test publish: `make publish-test` (verify on test.pypi.org)
5. Publish: `make publish`
6. Tag release: `git tag v$(poetry version -s) && git push --tags`
