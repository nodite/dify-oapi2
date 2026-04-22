# Test Restructure Design: Co-located Unit Tests with respx

**Date:** 2026-04-22
**Status:** Approved

---

## 1. Overview

Refactor the entire test suite from a centralized `tests/` directory to co-located `__tests__` directories adjacent to source files. Simultaneously upgrade test quality by replacing `Transport.execute` mocks with HTTP-level mocking via `respx`, enabling full verification of request construction and response parsing.

**Goals:**
- Co-location: tests live next to the code they test
- No external service dependencies: all HTTP mocked at the httpx layer
- Higher test quality: verify URL, method, headers, body, and response model parsing
- Delete all low-value integration/ tests that duplicate unit test coverage

---

## 2. Directory Structure

The `tests/` directory is **deleted entirely**. Tests move into `__tests__` subdirectories alongside source files.

```
dify_oapi/
├── conftest.py                                 # Global shared fixtures
├── __tests__/
│   └── test_client.py
├── core/
│   └── __tests__/
│       ├── test_config.py
│       ├── test_error_handling.py
│       └── test_streaming.py
└── api/
    ├── chat/
    │   ├── __tests__/
    │   │   └── test_service.py
    │   └── v1/
    │       ├── __tests__/
    │       │   └── test_async.py
    │       └── resource/
    │           └── __tests__/
    │               ├── test_annotation.py
    │               ├── test_chat.py
    │               ├── test_conversation.py
    │               └── test_message.py
    ├── chatflow/
    │   ├── __tests__/
    │   │   └── test_service.py
    │   └── v1/
    │       ├── __tests__/
    │       │   └── test_integration.py
    │       ├── model/
    │       │   └── __tests__/
    │       │       └── test_models.py
    │       └── resource/
    │           └── __tests__/
    │               ├── test_annotation.py
    │               ├── test_chatflow.py
    │               └── test_conversation.py
    ├── completion/
    │   ├── __tests__/
    │   │   └── test_service.py
    │   └── v1/
    │       └── resource/
    │           └── __tests__/
    │               ├── test_annotation.py
    │               └── test_completion.py
    ├── dify/
    │   ├── __tests__/
    │   │   └── test_service.py
    │   └── v1/
    │       └── resource/
    │           └── __tests__/
    │               ├── test_audio.py
    │               ├── test_feedback.py
    │               ├── test_file.py
    │               └── test_info.py
    ├── knowledge/
    │   ├── __tests__/
    │   │   └── test_service.py
    │   └── v1/
    │       ├── __tests__/
    │       │   ├── test_async.py
    │       │   └── test_integration.py
    │       ├── model/
    │       │   └── __tests__/
    │       │       └── test_models.py
    │       └── resource/
    │           └── __tests__/
    │               ├── test_chunk.py
    │               ├── test_dataset.py
    │               ├── test_document.py
    │               ├── test_model.py
    │               ├── test_segment.py
    │               └── test_tag.py
    └── workflow/
        ├── __tests__/
        │   └── test_service.py
        └── v1/
            └── resource/
                └── __tests__/
                    └── test_workflow.py
```

**Files deleted (not migrated):**
- `tests/integration/test_edge_cases.py`
- `tests/integration/test_end_to_end.py`
- `tests/integration/test_performance.py`

These are mock-based tests that duplicate unit test coverage with no additional value.

Note: `tests/chatflow/v1/test_integration.py` and `tests/knowledge/v1/test_integration.py` are **not** the same as the `tests/integration/` files. They are service-specific tests that exercise multi-step workflows. These are migrated and rewritten with respx mocks (see Section 5).

---

## 3. Infrastructure Changes

### 3.1 New Dependency

Add `respx` to dev dependencies in `pyproject.toml`:

```toml
[tool.poetry.group.dev.dependencies]
respx = "^0.21"
```

### 3.2 Packaging & Tooling Exclusions

Because `__tests__` directories live inside `dify_oapi/`, they fall under the `packages = [{include = "dify_oapi"}]` directive and would be shipped in the published wheel by default. Three config sections must exclude them:

**pyproject.toml `[tool.poetry]`** — add both patterns to exclude (directory entry + contents):
```toml
exclude = [".vscode", "docs", "examples", "tests", "dify_oapi/**/__tests__", "dify_oapi/**/__tests__/**"]
```

**pyproject.toml `[tool.mypy]`** — add `"__tests__"` to exclude list:
```toml
exclude = [".venv", "venv", "examples", "tests", "docs", "__tests__"]
```

**pyproject.toml `[tool.pylint.main]`** — add `"__tests__"` to ignore list:
```toml
ignore = [".venv", "venv", "examples", "tests", "build", "dist", "docs", "__tests__"]
```

### 3.3 pytest Configuration

Update `[tool.pytest.ini_options]` in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
testpaths = ["dify_oapi"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "-ra",
    "--import-mode=importlib"
]
```

Key changes from current config:
- `testpaths`: `["tests"]` → `["dify_oapi"]`
- `addopts`: added `"--import-mode=importlib"` — allows `__tests__` directories to contain test files without `__init__.py`

`__tests__` directories do **not** get `__init__.py` files. `importlib` mode handles imports correctly without them.

### 3.4 conftest.py

The existing `tests/conftest.py` is deleted. A new `dify_oapi/conftest.py` replaces it with real objects instead of MagicMocks:

```python
import pytest
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


@pytest.fixture
def domain() -> str:
    return "https://api.dify.ai"


@pytest.fixture
def request_option() -> RequestOption:
    return RequestOption.builder().api_key("test-key").build()


@pytest.fixture
def config(domain: str) -> Config:
    c = Config()
    c.domain = domain
    return c
```

Removed fixtures (not migrated):
- `mock_config()` — `MagicMock(spec=Config)` replaced by real `Config` object
- `mock_response()` — was never used anywhere in the test suite

---

## 4. Test Quality Standard

### 4.0 respx + ConnectionPoolManager Isolation

`respx.mock` patches `httpx.Client.send` and `httpx.AsyncClient.send` at the class method level (not instance level), so it covers both newly created and cached clients. The `ConnectionPoolManager` creates `httpx.Client` instances lazily on first request — `Dataset(config)` in `setup` does not create any client. Client creation only happens when `Transport.execute` is called, which is inside the `@respx.mock` scope. Test isolation is safe.

### 4.1 What Each Test Must Verify

| Verification | Description |
|---|---|
| HTTP method | Correct verb (GET, POST, DELETE, PATCH) |
| URL path | Correct path including path parameters (e.g., `/v1/datasets/{id}`) |
| Authorization header | `Bearer test-key` present in every request |
| Request body | JSON fields correctly serialized from request model |
| Response model | Pydantic model fields correctly populated from JSON response |

### 4.2 Resource Test Template (sync)

```python
import httpx
import pytest
import respx

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.api.knowledge.v1.resource.dataset import Dataset


class TestDataset:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Dataset(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get("https://api.dify.ai/v1/datasets").mock(
            return_value=httpx.Response(200, json={
                "data": [], "total": 0, "page": 1, "limit": 20, "has_more": False
            })
        )
        result = self.resource.list(self.option)
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create(self):
        route = respx.post("https://api.dify.ai/v1/datasets").mock(
            return_value=httpx.Response(200, json={"id": "ds-123", "name": "Test"})
        )
        body = CreateDatasetRequestBody.builder().name("Test").build()
        result = self.resource.create(
            CreateDatasetRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "ds-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete("https://api.dify.ai/v1/datasets/ds-123").mock(
            return_value=httpx.Response(200, json={"result": "success"})
        )
        result = self.resource.delete("ds-123", self.option)
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

### 4.3 Async Test Template

```python
import httpx
import pytest
import respx

from dify_oapi.api.knowledge.v1.resource.dataset import Dataset


class TestDatasetAsync:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Dataset(config)
        self.option = request_option

    @respx.mock
    async def test_alist(self):
        route = respx.get("https://api.dify.ai/v1/datasets").mock(
            return_value=httpx.Response(200, json={
                "data": [], "total": 0, "page": 1, "limit": 20, "has_more": False
            })
        )
        result = await self.resource.alist(self.option)
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

No `@pytest.mark.asyncio` decorators — redundant under `asyncio_mode = "auto"`.

The sync `autouse` `setup` fixture setting `self.resource` and `self.option` is safe in both sync and async test methods: pytest creates a fresh class instance per test item, and the async method sees the same instance that the sync fixture ran on.

### 4.4 Streaming Test Template

The SDK streaming generator yields raw bytes from `httpx.Response.iter_bytes()` — not parsed SSE lines. Chunk boundaries are not guaranteed, so assertions should use `in` on the fully joined bytes:

```python
@respx.mock
def test_chat_stream(self):
    chunks = b"data: hello\n\ndata: world\n\n"
    respx.post("https://api.dify.ai/v1/chat-messages").mock(
        return_value=httpx.Response(200, content=chunks)
    )
    gen = self.resource.chat(
        ChatRequest.builder().query("hi").user("u1").build(), self.option, stream=True
    )
    collected = b"".join(gen)
    assert b"hello" in collected
```

### 4.5 URL Parameters

For endpoints with path parameters, use `respx` pattern matching:

```python
respx.delete(url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+").mock(...)
# or exact match:
respx.delete("https://api.dify.ai/v1/datasets/ds-123").mock(...)
```

---

## 5. Migration File Map

36 test files are migrated and rewritten. 3 integration files are deleted. Total source files: 39.

| Original Path | New Path | Action |
|---|---|---|
| `tests/test_client.py` | `dify_oapi/__tests__/test_client.py` | migrate + rewrite |
| `tests/core/test_config.py` | `dify_oapi/core/__tests__/test_config.py` | migrate + rewrite |
| `tests/core/test_error_handling.py` | `dify_oapi/core/__tests__/test_error_handling.py` | migrate + rewrite |
| `tests/core/test_streaming.py` | `dify_oapi/core/__tests__/test_streaming.py` | migrate + rewrite |
| `tests/chat/test_service.py` | `dify_oapi/api/chat/__tests__/test_service.py` | migrate + rewrite |
| `tests/chat/v1/test_async.py` | `dify_oapi/api/chat/v1/__tests__/test_async.py` | migrate + rewrite |
| `tests/chat/v1/resource/test_annotation.py` | `dify_oapi/api/chat/v1/resource/__tests__/test_annotation.py` | migrate + rewrite |
| `tests/chat/v1/resource/test_chat.py` | `dify_oapi/api/chat/v1/resource/__tests__/test_chat.py` | migrate + rewrite |
| `tests/chat/v1/resource/test_conversation.py` | `dify_oapi/api/chat/v1/resource/__tests__/test_conversation.py` | migrate + rewrite |
| `tests/chat/v1/resource/test_message.py` | `dify_oapi/api/chat/v1/resource/__tests__/test_message.py` | migrate + rewrite |
| `tests/chatflow/test_service.py` | `dify_oapi/api/chatflow/__tests__/test_service.py` | migrate + rewrite |
| `tests/chatflow/v1/test_integration.py` | `dify_oapi/api/chatflow/v1/__tests__/test_integration.py` | migrate + rewrite |
| `tests/chatflow/v1/model/test_models.py` | `dify_oapi/api/chatflow/v1/model/__tests__/test_models.py` | migrate + rewrite |
| `tests/chatflow/v1/resource/test_annotation.py` | `dify_oapi/api/chatflow/v1/resource/__tests__/test_annotation.py` | migrate + rewrite |
| `tests/chatflow/v1/resource/test_chatflow.py` | `dify_oapi/api/chatflow/v1/resource/__tests__/test_chatflow.py` | migrate + rewrite |
| `tests/chatflow/v1/resource/test_conversation.py` | `dify_oapi/api/chatflow/v1/resource/__tests__/test_conversation.py` | migrate + rewrite |
| `tests/completion/test_service.py` | `dify_oapi/api/completion/__tests__/test_service.py` | migrate + rewrite |
| `tests/completion/v1/resource/test_annotation.py` | `dify_oapi/api/completion/v1/resource/__tests__/test_annotation.py` | migrate + rewrite |
| `tests/completion/v1/resource/test_completion.py` | `dify_oapi/api/completion/v1/resource/__tests__/test_completion.py` | migrate + rewrite |
| `tests/dify/test_service.py` | `dify_oapi/api/dify/__tests__/test_service.py` | migrate + rewrite |
| `tests/dify/v1/resource/test_audio.py` | `dify_oapi/api/dify/v1/resource/__tests__/test_audio.py` | migrate + rewrite |
| `tests/dify/v1/resource/test_feedback.py` | `dify_oapi/api/dify/v1/resource/__tests__/test_feedback.py` | migrate + rewrite |
| `tests/dify/v1/resource/test_file.py` | `dify_oapi/api/dify/v1/resource/__tests__/test_file.py` | migrate + rewrite |
| `tests/dify/v1/resource/test_info.py` | `dify_oapi/api/dify/v1/resource/__tests__/test_info.py` | migrate + rewrite |
| `tests/knowledge/test_service.py` | `dify_oapi/api/knowledge/__tests__/test_service.py` | migrate + rewrite |
| `tests/knowledge/v1/test_async.py` | `dify_oapi/api/knowledge/v1/__tests__/test_async.py` | migrate + rewrite |
| `tests/knowledge/v1/test_integration.py` | `dify_oapi/api/knowledge/v1/__tests__/test_integration.py` | migrate + rewrite |
| `tests/knowledge/v1/model/test_models.py` | `dify_oapi/api/knowledge/v1/model/__tests__/test_models.py` | migrate + rewrite |
| `tests/knowledge/v1/resource/test_chunk.py` | `dify_oapi/api/knowledge/v1/resource/__tests__/test_chunk.py` | migrate + rewrite |
| `tests/knowledge/v1/resource/test_dataset.py` | `dify_oapi/api/knowledge/v1/resource/__tests__/test_dataset.py` | migrate + rewrite |
| `tests/knowledge/v1/resource/test_document.py` | `dify_oapi/api/knowledge/v1/resource/__tests__/test_document.py` | migrate + rewrite |
| `tests/knowledge/v1/resource/test_model.py` | `dify_oapi/api/knowledge/v1/resource/__tests__/test_model.py` | migrate + rewrite |
| `tests/knowledge/v1/resource/test_segment.py` | `dify_oapi/api/knowledge/v1/resource/__tests__/test_segment.py` | migrate + rewrite |
| `tests/knowledge/v1/resource/test_tag.py` | `dify_oapi/api/knowledge/v1/resource/__tests__/test_tag.py` | migrate + rewrite |
| `tests/workflow/test_service.py` | `dify_oapi/api/workflow/__tests__/test_service.py` | migrate + rewrite |
| `tests/workflow/v1/resource/test_workflow.py` | `dify_oapi/api/workflow/v1/resource/__tests__/test_workflow.py` | migrate + rewrite |
| `tests/integration/test_edge_cases.py` | — | **delete** |
| `tests/integration/test_end_to_end.py` | — | **delete** |
| `tests/integration/test_performance.py` | — | **delete** |

---

## 6. CLAUDE.md Updates

Three sections require updates:

### 6.1 Testing Commands

```bash
make test               # Run all tests (now discovers from dify_oapi/)
make test-cov           # Run tests with coverage report

# Run specific service tests
poetry run pytest dify_oapi/api/knowledge/ -v
poetry run pytest dify_oapi/api/chat/ -v

# Run specific test patterns
poetry run pytest dify_oapi/ -k "test_create" -v
```

### 6.2 Testing Strategy Section

Replace current structure description with:

```
Tests live adjacent to source files in __tests__ directories:

dify_oapi/
├── __tests__/
│   └── test_client.py
├── conftest.py                          # Shared fixtures (config, request_option, domain)
└── api/
    └── {service}/
        ├── __tests__/
        │   └── test_service.py
        └── v1/
            └── resource/
                └── __tests__/
                    └── test_{resource}.py   # HTTP-level tests with respx
```

Co-location rule: `a/b/c.py` → `a/b/__tests__/c.py`

### 6.3 Adding a New API Method — Step 3

Change from:
> **Add Tests** (tests/{service}/v1/resource/test_{resource}.py)

To:
> **Add Tests** (api/{service}/v1/resource/\_\_tests\_\_/test_{resource}.py):
> - Use `@respx.mock` to mock HTTP responses
> - Verify URL, method, Authorization header, response model fields
> - Add async variant test using `async def`
