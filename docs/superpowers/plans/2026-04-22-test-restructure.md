# Test Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate all tests from `tests/` into co-located `__tests__` directories inside `dify_oapi/`, rewriting them to mock HTTP at the httpx layer via `respx` instead of patching `Transport.execute`.

**Architecture:** Delete the `tests/` directory entirely. Place test files adjacent to source using `__tests__/` subdirectories. Use `respx.mock` to intercept HTTP requests at the `httpx.Client.send` level, enabling full verification of URL, HTTP method, headers, and response parsing. A shared `dify_oapi/conftest.py` provides `config`, `domain`, and `request_option` fixtures.

**Tech Stack:** pytest ≥ 8, pytest-asyncio ≥ 1 (`asyncio_mode = "auto"`), respx ^0.21, httpx, pydantic 2.x

**Reference spec:** `docs/superpowers/specs/2026-04-22-test-restructure-design.md`

## respx Pattern Reference

Every resource test follows this pattern:

```python
import httpx
import pytest
import respx

from dify_oapi.api.{service}.v1.resource.{resource} import {ResourceClass}
from dify_oapi.api.{service}.v1.model.{request_file} import {RequestClass}
# (add RequestBody import where needed)


class Test{ResourceClass}:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = {ResourceClass}(config)
        self.option = request_option

    @respx.mock
    def test_{method}(self):
        route = respx.{http_verb}("https://api.dify.ai{path}").mock(
            return_value=httpx.Response(200, json={...})
        )
        result = self.resource.{method}(request, self.option)
        assert result.{field} == expected
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

Async tests: same pattern but `async def test_...` and `await self.resource.a{method}(...)`. No `@pytest.mark.asyncio` needed — `asyncio_mode = "auto"` handles it.

Streaming tests: `respx.{verb}(...).mock(return_value=httpx.Response(200, content=b"data: chunk\n\n"))`, then `b"".join(gen)`.

---

## File Map

| Create | Purpose |
|---|---|
| `dify_oapi/conftest.py` | Shared fixtures: `domain`, `request_option`, `config` |
| `dify_oapi/__tests__/test_client.py` | Client builder and service property tests |
| `dify_oapi/core/__tests__/test_config.py` | Config and RequestOption construction |
| `dify_oapi/core/__tests__/test_error_handling.py` | HTTP error propagation tests |
| `dify_oapi/core/__tests__/test_streaming.py` | Streaming generator behavior |
| `dify_oapi/api/chat/__tests__/test_service.py` | ChatService structural tests |
| `dify_oapi/api/chat/v1/__tests__/test_async.py` | Chat async methods |
| `dify_oapi/api/chat/v1/resource/__tests__/test_annotation.py` | Chat Annotation resource |
| `dify_oapi/api/chat/v1/resource/__tests__/test_chat.py` | Chat resource (incl. streaming) |
| `dify_oapi/api/chat/v1/resource/__tests__/test_conversation.py` | Chat Conversation resource |
| `dify_oapi/api/chat/v1/resource/__tests__/test_message.py` | Chat Message resource |
| `dify_oapi/api/chatflow/__tests__/test_service.py` | ChatflowService structural tests |
| `dify_oapi/api/chatflow/v1/__tests__/test_integration.py` | Chatflow multi-step workflow |
| `dify_oapi/api/chatflow/v1/model/__tests__/test_models.py` | Chatflow model builder patterns |
| `dify_oapi/api/chatflow/v1/resource/__tests__/test_annotation.py` | Chatflow Annotation resource |
| `dify_oapi/api/chatflow/v1/resource/__tests__/test_chatflow.py` | Chatflow resource (incl. streaming) |
| `dify_oapi/api/chatflow/v1/resource/__tests__/test_conversation.py` | Chatflow Conversation resource |
| `dify_oapi/api/completion/__tests__/test_service.py` | CompletionService structural tests |
| `dify_oapi/api/completion/v1/resource/__tests__/test_annotation.py` | Completion Annotation resource |
| `dify_oapi/api/completion/v1/resource/__tests__/test_completion.py` | Completion resource (incl. streaming) |
| `dify_oapi/api/dify/__tests__/test_service.py` | DifyService structural tests |
| `dify_oapi/api/dify/v1/resource/__tests__/test_audio.py` | Dify Audio resource |
| `dify_oapi/api/dify/v1/resource/__tests__/test_feedback.py` | Dify Feedback resource |
| `dify_oapi/api/dify/v1/resource/__tests__/test_file.py` | Dify File upload |
| `dify_oapi/api/dify/v1/resource/__tests__/test_info.py` | Dify Info resource |
| `dify_oapi/api/knowledge/__tests__/test_service.py` | KnowledgeService structural tests |
| `dify_oapi/api/knowledge/v1/__tests__/test_async.py` | Knowledge async methods |
| `dify_oapi/api/knowledge/v1/__tests__/test_integration.py` | Knowledge multi-step workflow |
| `dify_oapi/api/knowledge/v1/model/__tests__/test_models.py` | Knowledge model builder patterns |
| `dify_oapi/api/knowledge/v1/resource/__tests__/test_dataset.py` | Dataset resource |
| `dify_oapi/api/knowledge/v1/resource/__tests__/test_document.py` | Document resource |
| `dify_oapi/api/knowledge/v1/resource/__tests__/test_chunk.py` | Chunk resource |
| `dify_oapi/api/knowledge/v1/resource/__tests__/test_segment.py` | Segment resource |
| `dify_oapi/api/knowledge/v1/resource/__tests__/test_tag.py` | Tag resource |
| `dify_oapi/api/knowledge/v1/resource/__tests__/test_model.py` | Model (embedding) resource |
| `dify_oapi/api/workflow/__tests__/test_service.py` | WorkflowService structural tests |
| `dify_oapi/api/workflow/v1/resource/__tests__/test_workflow.py` | Workflow resource (incl. streaming) |

| Modify | Change |
|---|---|
| `pyproject.toml` | respx dep, exclude patterns, mypy/pylint ignore, pytest testpaths + importlib mode |
| `Makefile` | Update `test` and `test-cov` targets to use `dify_oapi/` |
| `CLAUDE.md` | Update Testing Strategy, commands, and Adding a New API Method |

| Delete | Reason |
|---|---|
| `tests/` (entire directory) | Replaced by co-located `__tests__` directories |

---

## Tasks

### Task 1: Infrastructure Setup

**Files:**
- Modify: `pyproject.toml`
- Modify: `Makefile`
- Create: `dify_oapi/conftest.py`

- [ ] **Step 1: Add respx dependency**

In `pyproject.toml`, under `[tool.poetry.group.dev.dependencies]`, add:
```toml
respx = "^0.21"
```

Run: `poetry add --group dev "respx>=0.21,<1"`

Expected: respx installed, `pyproject.toml` and `poetry.lock` updated.

- [ ] **Step 2: Update pytest configuration**

In `pyproject.toml`, replace the entire `[tool.pytest.ini_options]` block:

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

- [ ] **Step 3: Update packaging and tooling exclusions**

In `pyproject.toml`:

1. In `[tool.poetry]`, update `exclude`:
```toml
exclude = [".vscode", "docs", "examples", "tests", "dify_oapi/**/__tests__", "dify_oapi/**/__tests__/**"]
```

2. In `[tool.mypy]`, update `exclude`:
```toml
exclude = [".venv", "venv", "examples", "tests", "docs", "__tests__"]
```

3. In `[tool.pylint.main]`, update `ignore`:
```toml
ignore = [".venv", "venv", "examples", "tests", "build", "dist", "docs", "__tests__"]
```

- [ ] **Step 4: Update Makefile test targets**

In `Makefile`, replace both `test` and `test-cov` targets:

```makefile
test: ## Run tests
	poetry run pytest dify_oapi/ -v

test-cov: ## Run tests with coverage
	poetry run pytest dify_oapi/ -v --cov=dify_oapi --cov-report=html --cov-report=term
```

- [ ] **Step 5: Create dify_oapi/conftest.py**

Create `dify_oapi/conftest.py`:

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

- [ ] **Step 6: Verify configuration is parseable**

Run: `poetry run pytest --collect-only dify_oapi/ 2>&1 | head -20`

Expected: "no tests ran" or "collected 0 items" (no errors — the `__tests__` dirs don't exist yet).

- [ ] **Step 7: Commit**

```bash
git add pyproject.toml poetry.lock Makefile dify_oapi/conftest.py
git commit -m "chore: set up co-located test infrastructure with respx"
```

---

### Task 2: Client and Core Tests

**Files:**
- Create: `dify_oapi/__tests__/test_client.py`
- Create: `dify_oapi/core/__tests__/test_config.py`
- Create: `dify_oapi/core/__tests__/test_error_handling.py`
- Create: `dify_oapi/core/__tests__/test_streaming.py`

- [ ] **Step 1: Create `dify_oapi/__tests__/test_client.py`**

```python
import pytest

from dify_oapi.api.chat.service import ChatService
from dify_oapi.api.chatflow.service import ChatflowService
from dify_oapi.api.completion.service import CompletionService
from dify_oapi.api.dify.service import DifyService
from dify_oapi.api.knowledge.service import KnowledgeService
from dify_oapi.api.workflow.service import WorkflowService
from dify_oapi.client import Client


class TestClient:
    def test_builder_creates_client(self):
        client = Client.builder().domain("https://api.dify.ai").build()
        assert client is not None

    def test_client_has_all_services(self):
        client = Client.builder().domain("https://api.dify.ai").build()
        assert isinstance(client.chat, ChatService)
        assert isinstance(client.chatflow, ChatflowService)
        assert isinstance(client.completion, CompletionService)
        assert isinstance(client.dify, DifyService)
        assert isinstance(client.knowledge, KnowledgeService)
        assert isinstance(client.workflow, WorkflowService)

    def test_builder_domain_required(self):
        # A client built without domain should still build but may fail on request
        client = Client.builder().build()
        assert client is not None
```

- [ ] **Step 2: Create `dify_oapi/core/__tests__/test_config.py`**

```python
import pytest

from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestConfig:
    def test_config_defaults(self):
        c = Config()
        assert c.max_connections == 100
        assert c.max_keepalive_connections == 20
        assert c.max_retry_count == 3
        assert c.verify_ssl is True

    def test_config_domain_assignment(self, domain):
        c = Config()
        c.domain = domain
        assert c.domain == "https://api.dify.ai"


class TestRequestOption:
    def test_builder_sets_api_key(self, request_option):
        assert request_option.api_key == "test-key"

    def test_builder_chaining(self):
        option = RequestOption.builder().api_key("my-key").build()
        assert option.api_key == "my-key"
```

- [ ] **Step 3: Create `dify_oapi/core/__tests__/test_error_handling.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.dify.v1.model.get_info_request import GetInfoRequest
from dify_oapi.api.dify.v1.resource.info import Info


class TestErrorHandling:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Info(config)
        self.option = request_option

    @respx.mock
    def test_404_response_returns_failed_result(self):
        respx.get("https://api.dify.ai/v1/info").mock(
            return_value=httpx.Response(404, json={"message": "Not found"})
        )
        result = self.resource.get(GetInfoRequest.builder().user("u1").build(), self.option)
        assert result.success is False

    @respx.mock
    def test_500_response_returns_failed_result(self):
        respx.get("https://api.dify.ai/v1/info").mock(
            return_value=httpx.Response(500, json={"message": "Internal Server Error"})
        )
        result = self.resource.get(GetInfoRequest.builder().user("u1").build(), self.option)
        assert result.success is False

    @respx.mock
    def test_connection_error_raises(self):
        respx.get("https://api.dify.ai/v1/info").mock(
            side_effect=httpx.ConnectError("Connection refused")
        )
        with pytest.raises(Exception):
            self.resource.get(GetInfoRequest.builder().user("u1").build(), self.option)
```

- [ ] **Step 4: Create `dify_oapi/core/__tests__/test_streaming.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.resource.chat import Chat


class TestStreaming:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Chat(config)
        self.option = request_option

    @respx.mock
    def test_stream_returns_generator(self):
        chunks = b"data: hello\n\ndata: world\n\n"
        respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, content=chunks)
        )
        body = ChatRequestBody.builder().query("hi").user("u1").build()
        gen = self.resource.chat(
            ChatRequest.builder().request_body(body).build(), self.option, stream=True
        )
        collected = b"".join(gen)
        assert b"hello" in collected
        assert b"world" in collected

    @respx.mock
    async def test_async_stream_returns_async_generator(self):
        chunks = b"data: hello\n\ndata: world\n\n"
        respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, content=chunks)
        )
        body = ChatRequestBody.builder().query("hi").user("u1").build()
        gen = await self.resource.achat(
            ChatRequest.builder().request_body(body).build(), self.option, stream=True
        )
        collected = b""
        async for chunk in gen:
            collected += chunk
        assert b"hello" in collected
```

- [ ] **Step 5: Run all new tests**

Run: `poetry run pytest dify_oapi/__tests__/ dify_oapi/core/__tests__/ -v`

Expected: All tests pass (PASSED).

- [ ] **Step 6: Commit**

```bash
git add dify_oapi/__tests__/ dify_oapi/core/__tests__/
git commit -m "test: add client and core unit tests"
```

---

### Task 3: Chat Service Tests

**Files:**
- Create: `dify_oapi/api/chat/__tests__/test_service.py`
- Create: `dify_oapi/api/chat/v1/__tests__/test_async.py`
- Create: `dify_oapi/api/chat/v1/resource/__tests__/test_annotation.py`
- Create: `dify_oapi/api/chat/v1/resource/__tests__/test_chat.py`
- Create: `dify_oapi/api/chat/v1/resource/__tests__/test_conversation.py`
- Create: `dify_oapi/api/chat/v1/resource/__tests__/test_message.py`

- [ ] **Step 1: Create `dify_oapi/api/chat/__tests__/test_service.py`**

```python
from dify_oapi.api.chat.service import ChatService
from dify_oapi.api.chat.v1.resource.annotation import Annotation
from dify_oapi.api.chat.v1.resource.chat import Chat
from dify_oapi.api.chat.v1.resource.conversation import Conversation
from dify_oapi.api.chat.v1.resource.message import Message
from dify_oapi.api.chat.v1.version import V1


class TestChatService:
    def test_service_has_v1(self, config):
        service = ChatService(config)
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_has_resources(self, config):
        v1 = ChatService(config).v1
        assert isinstance(v1.chat, Chat)
        assert isinstance(v1.conversation, Conversation)
        assert isinstance(v1.annotation, Annotation)
        assert isinstance(v1.message, Message)
```

- [ ] **Step 2: Create `dify_oapi/api/chat/v1/__tests__/test_async.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chat.v1.model.stop_chat_request import StopChatRequest
from dify_oapi.api.chat.v1.model.stop_chat_request_body import StopChatRequestBody
from dify_oapi.api.chat.v1.resource.chat import Chat


class TestChatAsync:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Chat(config)
        self.option = request_option

    @respx.mock
    async def test_achat(self):
        route = respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, json={
                "message_id": "msg-123",
                "conversation_id": "conv-123",
                "answer": "Hello!",
                "mode": "chat",
                "created_at": 1234567890,
            })
        )
        body = ChatRequestBody.builder().query("hi").user("u1").build()
        result = await self.resource.achat(
            ChatRequest.builder().request_body(body).build(), self.option
        )
        assert result.answer == "Hello!"
        assert result.message_id == "msg-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    async def test_astop(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/chat-messages/[^/]+/stop"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = StopChatRequestBody.builder().user("u1").build()
        result = await self.resource.astop(
            StopChatRequest.builder().task_id("task-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    async def test_asuggested(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/messages/[^/]+/suggested"
        ).mock(return_value=httpx.Response(200, json={"data": ["Follow up?"]}))
        result = await self.resource.asuggested(
            GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("u1").build(),
            self.option,
        )
        assert result.data == ["Follow up?"]
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 3: Create `dify_oapi/api/chat/v1/resource/__tests__/test_annotation.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chat.v1.model.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.chat.v1.model.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.chat.v1.model.list_annotations_request import ListAnnotationsRequest
from dify_oapi.api.chat.v1.model.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.chat.v1.model.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.api.chat.v1.resource.annotation import Annotation


class TestAnnotation:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Annotation(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get("https://api.dify.ai/v1/apps/annotations").mock(
            return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "limit": 20})
        )
        result = self.resource.list(
            ListAnnotationsRequest.builder().page(1).limit(20).build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create(self):
        route = respx.post("https://api.dify.ai/v1/apps/annotations").mock(
            return_value=httpx.Response(200, json={"id": "ann-123", "question": "Q?", "answer": "A."})
        )
        body = CreateAnnotationRequestBody.builder().question("Q?").answer("A.").build()
        result = self.resource.create(
            CreateAnnotationRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "ann-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_update(self):
        route = respx.put(
            url__regex=r"https://api\.dify\.ai/v1/apps/annotations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"id": "ann-123", "question": "Q?", "answer": "A2."}))
        body = UpdateAnnotationRequestBody.builder().question("Q?").answer("A2.").build()
        result = self.resource.update(
            UpdateAnnotationRequest.builder().annotation_id("ann-123").request_body(body).build(),
            self.option,
        )
        assert result.id == "ann-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/apps/annotations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={}))
        self.resource.delete(
            DeleteAnnotationRequest.builder().annotation_id("ann-123").build(), self.option
        )
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 4: Create `dify_oapi/api/chat/v1/resource/__tests__/test_chat.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chat.v1.model.stop_chat_request import StopChatRequest
from dify_oapi.api.chat.v1.model.stop_chat_request_body import StopChatRequestBody
from dify_oapi.api.chat.v1.resource.chat import Chat


class TestChat:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Chat(config)
        self.option = request_option

    @respx.mock
    def test_chat(self):
        route = respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, json={
                "message_id": "msg-123",
                "conversation_id": "conv-123",
                "answer": "Hello!",
                "mode": "chat",
                "created_at": 1234567890,
            })
        )
        body = ChatRequestBody.builder().query("hi").user("u1").build()
        result = self.resource.chat(
            ChatRequest.builder().request_body(body).build(), self.option
        )
        assert result.answer == "Hello!"
        assert result.message_id == "msg-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_chat_stream(self):
        chunks = b"data: hello\n\ndata: world\n\n"
        route = respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, content=chunks)
        )
        body = ChatRequestBody.builder().query("hi").user("u1").build()
        gen = self.resource.chat(
            ChatRequest.builder().request_body(body).build(), self.option, stream=True
        )
        collected = b"".join(gen)
        assert b"hello" in collected
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_stop(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/chat-messages/[^/]+/stop"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = StopChatRequestBody.builder().user("u1").build()
        result = self.resource.stop(
            StopChatRequest.builder().task_id("task-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_suggested(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/messages/[^/]+/suggested"
        ).mock(
            return_value=httpx.Response(200, json={"result": "success", "data": ["Q1?", "Q2?"]})
        )
        result = self.resource.suggested(
            GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("u1").build(),
            self.option,
        )
        assert result.data == ["Q1?", "Q2?"]
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 5: Create `dify_oapi/api/chat/v1/resource/__tests__/test_conversation.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chat.v1.model.delete_conversation_request_body import DeleteConversationRequestBody
from dify_oapi.api.chat.v1.model.get_conversation_list_request import GetConversationsListRequest
from dify_oapi.api.chat.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chat.v1.model.rename_conversation_request_body import RenameConversationRequestBody
from dify_oapi.api.chat.v1.resource.conversation import Conversation


class TestConversation:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Conversation(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get("https://api.dify.ai/v1/conversations").mock(
            return_value=httpx.Response(200, json={"data": [], "has_more": False, "limit": 20})
        )
        result = self.resource.list(
            GetConversationsListRequest.builder().user("u1").limit(20).build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/conversations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = DeleteConversationRequestBody.builder().user("u1").build()
        result = self.resource.delete(
            DeleteConversationRequest.builder().conversation_id("conv-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_rename(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/conversations/[^/]+/name"
        ).mock(return_value=httpx.Response(200, json={"id": "conv-123", "result": "success"}))
        body = RenameConversationRequestBody.builder().name("New Name").build()
        result = self.resource.rename(
            RenameConversationRequest.builder().conversation_id("conv-123").request_body(body).build(),
            self.option,
        )
        assert result.id == "conv-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 6: Create `dify_oapi/api/chat/v1/resource/__tests__/test_message.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chat.v1.model.message_history_request import GetMessageHistoryRequest
from dify_oapi.api.chat.v1.resource.message import Message


class TestMessage:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Message(config)
        self.option = request_option

    @respx.mock
    def test_history(self):
        route = respx.get("https://api.dify.ai/v1/messages").mock(
            return_value=httpx.Response(200, json={"data": [], "has_more": False, "limit": 20})
        )
        result = self.resource.history(
            GetMessageHistoryRequest.builder().conversation_id("conv-123").user("u1").build(),
            self.option,
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_suggested(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/messages/[^/]+/suggested"
        ).mock(
            return_value=httpx.Response(200, json={"result": "success", "data": ["Q1?"]})
        )
        result = self.resource.suggested(
            GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("u1").build(),
            self.option,
        )
        assert result.data == ["Q1?"]
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 7: Run all chat tests**

Run: `poetry run pytest dify_oapi/api/chat/ -v`

Expected: All tests pass.

- [ ] **Step 8: Commit**

```bash
git add dify_oapi/api/chat/
git commit -m "test: add chat service unit tests"
```

---

### Task 4: Chatflow Service Tests

**Files:**
- Create: `dify_oapi/api/chatflow/__tests__/test_service.py`
- Create: `dify_oapi/api/chatflow/v1/__tests__/test_integration.py`
- Create: `dify_oapi/api/chatflow/v1/model/__tests__/test_models.py`
- Create: `dify_oapi/api/chatflow/v1/resource/__tests__/test_annotation.py`
- Create: `dify_oapi/api/chatflow/v1/resource/__tests__/test_chatflow.py`
- Create: `dify_oapi/api/chatflow/v1/resource/__tests__/test_conversation.py`

- [ ] **Step 1: Create `dify_oapi/api/chatflow/__tests__/test_service.py`**

```python
from dify_oapi.api.chatflow.service import ChatflowService
from dify_oapi.api.chatflow.v1.resource.annotation import Annotation
from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow
from dify_oapi.api.chatflow.v1.resource.conversation import Conversation
from dify_oapi.api.chatflow.v1.version import V1


class TestChatflowService:
    def test_service_has_v1(self, config):
        service = ChatflowService(config)
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_has_resources(self, config):
        v1 = ChatflowService(config).v1
        assert isinstance(v1.chatflow, Chatflow)
        assert isinstance(v1.conversation, Conversation)
        assert isinstance(v1.annotation, Annotation)
```

- [ ] **Step 2: Create `dify_oapi/api/chatflow/v1/__tests__/test_integration.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request import StopChatMessageRequest
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request_body import StopChatMessageRequestBody
from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow


class TestChatflowIntegration:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Chatflow(config)
        self.option = request_option

    @respx.mock
    def test_send_then_stop(self):
        respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, json={
                "id": "msg-123",
                "conversation_id": "conv-123",
                "task_id": "task-123",
                "answer": "Hello!",
                "created_at": 1234567890,
            })
        )
        body = SendChatMessageRequestBody.builder().query("hi").user("u1").build()
        result = self.resource.send(
            SendChatMessageRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "msg-123"
        assert result.conversation_id == "conv-123"

        respx.post(
            url__regex=r"https://api\.dify\.ai/v1/chat-messages/[^/]+/stop"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        stop_body = StopChatMessageRequestBody.builder().user("u1").build()
        stop_result = self.resource.stop(
            StopChatMessageRequest.builder().task_id("task-123").request_body(stop_body).build(),
            self.option,
        )
        assert stop_result.result == "success"

    @respx.mock
    def test_send_error_propagates(self):
        respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(400, json={"message": "Bad Request"})
        )
        body = SendChatMessageRequestBody.builder().query("").user("u1").build()
        result = self.resource.send(
            SendChatMessageRequest.builder().request_body(body).build(), self.option
        )
        assert result.success is False
```

- [ ] **Step 3: Create `dify_oapi/api/chatflow/v1/model/__tests__/test_models.py`**

```python
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody


class TestChatflowModels:
    def test_send_chat_message_request_builder(self):
        body = SendChatMessageRequestBody.builder().query("test query").user("u1").build()
        request = SendChatMessageRequest.builder().request_body(body).build()
        assert request is not None
        assert request.request_body is not None
        assert request.request_body.query == "test query"

    def test_send_chat_message_request_body_builder_fields(self):
        body = (
            SendChatMessageRequestBody.builder()
            .query("hello")
            .user("user-1")
            .conversation_id("conv-1")
            .build()
        )
        assert body.query == "hello"
        assert body.user == "user-1"
        assert body.conversation_id == "conv-1"
```

- [ ] **Step 4: Create `dify_oapi/api/chatflow/v1/resource/__tests__/test_annotation.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.chatflow.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chatflow.v1.model.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.chatflow.v1.model.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.chatflow.v1.model.get_annotations_request import GetAnnotationsRequest
from dify_oapi.api.chatflow.v1.model.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.chatflow.v1.model.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.api.chatflow.v1.resource.annotation import Annotation


class TestAnnotation:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Annotation(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get("https://api.dify.ai/v1/apps/annotations").mock(
            return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "limit": 20})
        )
        result = self.resource.list(
            GetAnnotationsRequest.builder().page(1).limit(20).build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create(self):
        route = respx.post("https://api.dify.ai/v1/apps/annotations").mock(
            return_value=httpx.Response(200, json={"id": "ann-123", "question": "Q?", "answer": "A."})
        )
        body = CreateAnnotationRequestBody.builder().question("Q?").answer("A.").build()
        result = self.resource.create(
            CreateAnnotationRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "ann-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_update(self):
        route = respx.put(
            url__regex=r"https://api\.dify\.ai/v1/apps/annotations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"id": "ann-123", "question": "Q2?", "answer": "A2."}))
        body = UpdateAnnotationRequestBody.builder().question("Q2?").answer("A2.").build()
        result = self.resource.update(
            UpdateAnnotationRequest.builder().annotation_id("ann-123").request_body(body).build(),
            self.option,
        )
        assert result.id == "ann-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/apps/annotations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={}))
        self.resource.delete(
            DeleteAnnotationRequest.builder().annotation_id("ann-123").build(), self.option
        )
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 5: Create `dify_oapi/api/chatflow/v1/resource/__tests__/test_chatflow.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.chatflow.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request import StopChatMessageRequest
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request_body import StopChatMessageRequestBody
from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow


class TestChatflow:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Chatflow(config)
        self.option = request_option

    @respx.mock
    def test_send(self):
        route = respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, json={
                "id": "msg-123",
                "conversation_id": "conv-123",
                "task_id": "task-123",
                "answer": "Hi there!",
                "created_at": 1234567890,
            })
        )
        body = SendChatMessageRequestBody.builder().query("hello").user("u1").build()
        result = self.resource.send(
            SendChatMessageRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "msg-123"
        assert result.answer == "Hi there!"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_send_stream(self):
        chunks = b"data: hello\n\ndata: world\n\n"
        route = respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, content=chunks)
        )
        body = SendChatMessageRequestBody.builder().query("hello").user("u1").build()
        gen = self.resource.send(
            SendChatMessageRequest.builder().request_body(body).build(), self.option, stream=True
        )
        collected = b"".join(gen)
        assert b"hello" in collected
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_stop(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/chat-messages/[^/]+/stop"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = StopChatMessageRequestBody.builder().user("u1").build()
        result = self.resource.stop(
            StopChatMessageRequest.builder().task_id("task-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_suggested(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/messages/[^/]+/suggested"
        ).mock(return_value=httpx.Response(200, json={"result": "success", "data": ["Q1?"]}))
        result = self.resource.suggested(
            GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("u1").build(),
            self.option,
        )
        assert result.data == ["Q1?"]
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 6: Create `dify_oapi/api/chatflow/v1/resource/__tests__/test_conversation.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.chatflow.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chatflow.v1.model.delete_conversation_request_body import DeleteConversationRequestBody
from dify_oapi.api.chatflow.v1.model.get_conversations_request import GetConversationsRequest
from dify_oapi.api.chatflow.v1.model.get_conversation_messages_request import GetConversationMessagesRequest
from dify_oapi.api.chatflow.v1.resource.conversation import Conversation


class TestConversation:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Conversation(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get("https://api.dify.ai/v1/conversations").mock(
            return_value=httpx.Response(200, json={"data": [], "has_more": False, "limit": 20})
        )
        result = self.resource.list(
            GetConversationsRequest.builder().user("u1").limit(20).build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_messages(self):
        route = respx.get("https://api.dify.ai/v1/messages").mock(
            return_value=httpx.Response(200, json={"data": [], "has_more": False, "limit": 20})
        )
        result = self.resource.messages(
            GetConversationMessagesRequest.builder().conversation_id("conv-123").user("u1").build(),
            self.option,
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/conversations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = DeleteConversationRequestBody.builder().user("u1").build()
        result = self.resource.delete(
            DeleteConversationRequest.builder().conversation_id("conv-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 7: Run all chatflow tests**

Run: `poetry run pytest dify_oapi/api/chatflow/ -v`

Expected: All tests pass.

- [ ] **Step 8: Commit**

```bash
git add dify_oapi/api/chatflow/
git commit -m "test: add chatflow service unit tests"
```

---

### Task 5: Completion Service Tests

**Files:**
- Create: `dify_oapi/api/completion/__tests__/test_service.py`
- Create: `dify_oapi/api/completion/v1/resource/__tests__/test_annotation.py`
- Create: `dify_oapi/api/completion/v1/resource/__tests__/test_completion.py`

Note: completion models live in subdirectories — `model/annotation/` and `model/completion/`.

- [ ] **Step 1: Create `dify_oapi/api/completion/__tests__/test_service.py`**

```python
from dify_oapi.api.completion.service import CompletionService
from dify_oapi.api.completion.v1.resource.annotation import Annotation
from dify_oapi.api.completion.v1.resource.completion import Completion
from dify_oapi.api.completion.v1.version import V1


class TestCompletionService:
    def test_service_has_v1(self, config):
        service = CompletionService(config)
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_has_resources(self, config):
        v1 = CompletionService(config).v1
        assert isinstance(v1.completion, Completion)
        assert isinstance(v1.annotation, Annotation)
```

- [ ] **Step 2: Create `dify_oapi/api/completion/v1/resource/__tests__/test_annotation.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.completion.v1.model.annotation.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.completion.v1.model.annotation.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.list_annotations_request import ListAnnotationsRequest
from dify_oapi.api.completion.v1.resource.annotation import Annotation


class TestAnnotation:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Annotation(config)
        self.option = request_option

    @respx.mock
    def test_list_annotations(self):
        route = respx.get("https://api.dify.ai/v1/apps/annotations").mock(
            return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "limit": 20})
        )
        result = self.resource.list_annotations(
            ListAnnotationsRequest.builder().page("1").limit("20").build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create_annotation(self):
        route = respx.post("https://api.dify.ai/v1/apps/annotations").mock(
            return_value=httpx.Response(200, json={"id": "ann-123", "question": "Q?", "answer": "A."})
        )
        body = CreateAnnotationRequestBody.builder().question("Q?").answer("A.").build()
        result = self.resource.create_annotation(
            CreateAnnotationRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "ann-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete_annotation(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/apps/annotations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={}))
        self.resource.delete_annotation(
            DeleteAnnotationRequest.builder().annotation_id("ann-123").build(), self.option
        )
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 3: Create `dify_oapi/api/completion/v1/resource/__tests__/test_completion.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
from dify_oapi.api.completion.v1.model.completion.stop_response_request import StopResponseRequest
from dify_oapi.api.completion.v1.model.completion.stop_response_request_body import StopResponseRequestBody
from dify_oapi.api.completion.v1.resource.completion import Completion


class TestCompletion:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Completion(config)
        self.option = request_option

    @respx.mock
    def test_send_message(self):
        route = respx.post("https://api.dify.ai/v1/completion-messages").mock(
            return_value=httpx.Response(200, json={
                "answer": "The answer is 42.",
                "task_id": "task-123",
                "id": "msg-123",
            })
        )
        body = SendMessageRequestBody.builder().inputs({}).user("u1").build()
        result = self.resource.send_message(
            SendMessageRequest.builder().request_body(body).build(), self.option
        )
        assert result.answer == "The answer is 42."
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_send_message_stream(self):
        chunks = b"data: hello\n\ndata: world\n\n"
        route = respx.post("https://api.dify.ai/v1/completion-messages").mock(
            return_value=httpx.Response(200, content=chunks)
        )
        body = SendMessageRequestBody.builder().inputs({}).user("u1").build()
        gen = self.resource.send_message(
            SendMessageRequest.builder().request_body(body).build(), self.option, stream=True
        )
        collected = b"".join(gen)
        assert b"hello" in collected
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_stop_response(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/completion-messages/[^/]+/stop"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = StopResponseRequestBody.builder().user("u1").build()
        result = self.resource.stop_response(
            StopResponseRequest.builder().task_id("task-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 4: Run all completion tests**

Run: `poetry run pytest dify_oapi/api/completion/ -v`

Expected: All tests pass.

- [ ] **Step 5: Commit**

```bash
git add dify_oapi/api/completion/
git commit -m "test: add completion service unit tests"
```

---

### Task 6: Dify Service Tests

**Files:**
- Create: `dify_oapi/api/dify/__tests__/test_service.py`
- Create: `dify_oapi/api/dify/v1/resource/__tests__/test_audio.py`
- Create: `dify_oapi/api/dify/v1/resource/__tests__/test_feedback.py`
- Create: `dify_oapi/api/dify/v1/resource/__tests__/test_file.py`
- Create: `dify_oapi/api/dify/v1/resource/__tests__/test_info.py`

- [ ] **Step 1: Create `dify_oapi/api/dify/__tests__/test_service.py`**

```python
from dify_oapi.api.dify.service import DifyService
from dify_oapi.api.dify.v1.resource.audio import Audio
from dify_oapi.api.dify.v1.resource.feedback import Feedback
from dify_oapi.api.dify.v1.resource.file import File
from dify_oapi.api.dify.v1.resource.info import Info
from dify_oapi.api.dify.v1.version import V1


class TestDifyService:
    def test_service_has_v1(self, config):
        service = DifyService(config)
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_has_resources(self, config):
        v1 = DifyService(config).v1
        assert isinstance(v1.audio, Audio)
        assert isinstance(v1.feedback, Feedback)
        assert isinstance(v1.file, File)
        assert isinstance(v1.info, Info)
```

- [ ] **Step 2: Create `dify_oapi/api/dify/v1/resource/__tests__/test_info.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.dify.v1.model.get_info_request import GetInfoRequest
from dify_oapi.api.dify.v1.model.get_meta_request import GetMetaRequest
from dify_oapi.api.dify.v1.model.get_parameters_request import GetParametersRequest
from dify_oapi.api.dify.v1.model.get_site_request import GetSiteRequest
from dify_oapi.api.dify.v1.resource.info import Info


class TestInfo:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Info(config)
        self.option = request_option

    @respx.mock
    def test_get(self):
        route = respx.get("https://api.dify.ai/v1/info").mock(
            return_value=httpx.Response(200, json={"name": "My App", "description": "A test app"})
        )
        result = self.resource.get(
            GetInfoRequest.builder().user("u1").build(), self.option
        )
        assert result.name == "My App"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_parameters(self):
        route = respx.get("https://api.dify.ai/v1/parameters").mock(
            return_value=httpx.Response(200, json={"user_input_form": []})
        )
        result = self.resource.parameters(
            GetParametersRequest.builder().user("u1").build(), self.option
        )
        assert result.user_input_form == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_meta(self):
        route = respx.get("https://api.dify.ai/v1/meta").mock(
            return_value=httpx.Response(200, json={"tool_icons": {"dalle2": "icon-url"}})
        )
        result = self.resource.meta(GetMetaRequest.builder().build(), self.option)
        assert result.tool_icons is not None
        assert result.tool_icons.dalle2 == "icon-url"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_site(self):
        route = respx.get("https://api.dify.ai/v1/site").mock(
            return_value=httpx.Response(200, json={"title": "Test App"})
        )
        result = self.resource.site(GetSiteRequest.builder().build(), self.option)
        assert result.title == "Test App"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 3: Create `dify_oapi/api/dify/v1/resource/__tests__/test_feedback.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.dify.v1.model.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.api.dify.v1.model.submit_feedback_request import SubmitFeedbackRequest
from dify_oapi.api.dify.v1.model.submit_feedback_request_body import SubmitFeedbackRequestBody
from dify_oapi.api.dify.v1.resource.feedback import Feedback


class TestFeedback:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Feedback(config)
        self.option = request_option

    @respx.mock
    def test_submit(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/messages/[^/]+/feedbacks"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = SubmitFeedbackRequestBody.builder().rating("like").user("u1").build()
        result = self.resource.submit(
            SubmitFeedbackRequest.builder().message_id("msg-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_list(self):
        route = respx.get("https://api.dify.ai/v1/app/feedbacks").mock(
            return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "limit": 20})
        )
        result = self.resource.list(
            GetFeedbacksRequest.builder().page(1).limit(20).build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 4: Create `dify_oapi/api/dify/v1/resource/__tests__/test_file.py`**

```python
import io

import httpx
import pytest
import respx

from dify_oapi.api.dify.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.dify.v1.resource.file import File


class TestFile:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = File(config)
        self.option = request_option

    @respx.mock
    def test_upload(self):
        route = respx.post("https://api.dify.ai/v1/files/upload").mock(
            return_value=httpx.Response(200, json={
                "id": "file-123",
                "name": "test.txt",
                "size": 12,
                "extension": "txt",
                "mime_type": "text/plain",
                "created_by": "user-1",
                "created_at": 1234567890,
            })
        )
        file_content = io.BytesIO(b"hello world!")
        request = UploadFileRequest.builder().file(file_content, "test.txt").build()
        result = self.resource.upload(request, self.option)
        assert result.id == "file-123"
        assert result.name == "test.txt"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 5: Create `dify_oapi/api/dify/v1/resource/__tests__/test_audio.py`**

```python
import io

import httpx
import pytest
import respx

from dify_oapi.api.dify.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.dify.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.dify.v1.model.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.api.dify.v1.resource.audio import Audio


class TestAudio:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Audio(config)
        self.option = request_option

    @respx.mock
    def test_to_text(self):
        route = respx.post("https://api.dify.ai/v1/audio-to-text").mock(
            return_value=httpx.Response(200, json={"text": "hello world"})
        )
        file_content = io.BytesIO(b"fake audio data")
        request = AudioToTextRequest.builder().file(file_content, "audio.mp3").build()
        result = self.resource.to_text(request, self.option)
        assert result.text == "hello world"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_from_text(self):
        route = respx.post("https://api.dify.ai/v1/text-to-audio").mock(
            return_value=httpx.Response(200, content=b"fake audio bytes")
        )
        body = TextToAudioRequestBody.builder().text("hello world").user("u1").build()
        request = TextToAudioRequest.builder().request_body(body).build()
        result = self.resource.from_text(request, self.option)
        assert result is not None
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 6: Run all dify tests**

Run: `poetry run pytest dify_oapi/api/dify/ -v`

Expected: All tests pass.

- [ ] **Step 7: Commit**

```bash
git add dify_oapi/api/dify/
git commit -m "test: add dify service unit tests"
```

---

### Task 7: Knowledge Service + Supporting Tests

**Files:**
- Create: `dify_oapi/api/knowledge/__tests__/test_service.py`
- Create: `dify_oapi/api/knowledge/v1/__tests__/test_async.py`
- Create: `dify_oapi/api/knowledge/v1/__tests__/test_integration.py`
- Create: `dify_oapi/api/knowledge/v1/model/__tests__/test_models.py`

- [ ] **Step 1: Create `dify_oapi/api/knowledge/__tests__/test_service.py`**

```python
from dify_oapi.api.knowledge.service import KnowledgeService
from dify_oapi.api.knowledge.v1.resource.chunk import Chunk
from dify_oapi.api.knowledge.v1.resource.dataset import Dataset
from dify_oapi.api.knowledge.v1.resource.document import Document
from dify_oapi.api.knowledge.v1.resource.model import Model
from dify_oapi.api.knowledge.v1.resource.segment import Segment
from dify_oapi.api.knowledge.v1.resource.tag import Tag
from dify_oapi.api.knowledge.v1.version import V1


class TestKnowledgeService:
    def test_service_has_v1(self, config):
        service = KnowledgeService(config)
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_has_resources(self, config):
        v1 = KnowledgeService(config).v1
        assert isinstance(v1.dataset, Dataset)
        assert isinstance(v1.document, Document)
        assert isinstance(v1.segment, Segment)
        assert isinstance(v1.chunk, Chunk)
        assert isinstance(v1.tag, Tag)
        assert isinstance(v1.model, Model)
```

- [ ] **Step 2: Create `dify_oapi/api/knowledge/v1/__tests__/test_async.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.get_dataset_request import GetDatasetRequest
from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest
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
                "data": [], "has_more": False, "total": 0, "page": 1, "limit": 20
            })
        )
        result = await self.resource.alist(
            ListDatasetsRequest.builder().page(1).limit(20).build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    async def test_acreate(self):
        route = respx.post("https://api.dify.ai/v1/datasets").mock(
            return_value=httpx.Response(200, json={"id": "ds-123", "name": "Async Dataset"})
        )
        body = CreateDatasetRequestBody.builder().name("Async Dataset").build()
        result = await self.resource.acreate(
            CreateDatasetRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "ds-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    async def test_aget(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"id": "ds-123", "name": "Test"}))
        result = await self.resource.aget(
            GetDatasetRequest.builder().dataset_id("ds-123").build(), self.option
        )
        assert result.id == "ds-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 3: Create `dify_oapi/api/knowledge/v1/__tests__/test_integration.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import CreateDocumentByTextRequestBody
from dify_oapi.api.knowledge.v1.resource.dataset import Dataset
from dify_oapi.api.knowledge.v1.resource.document import Document


class TestKnowledgeIntegration:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.dataset = Dataset(config)
        self.document = Document(config)
        self.option = request_option

    @respx.mock
    def test_dataset_workflow(self):
        respx.post("https://api.dify.ai/v1/datasets").mock(
            return_value=httpx.Response(200, json={"id": "ds-123", "name": "test-dataset"})
        )
        body = CreateDatasetRequestBody.builder().name("test-dataset").build()
        ds_result = self.dataset.create(
            CreateDatasetRequest.builder().request_body(body).build(), self.option
        )
        assert ds_result.id == "ds-123"
        assert ds_result.name == "test-dataset"

        respx.post(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/document/create-by-text"
        ).mock(
            return_value=httpx.Response(200, json={
                "document": {"id": "doc-123", "name": "Test Doc", "indexing_status": "waiting"}
            })
        )
        doc_body = CreateDocumentByTextRequestBody.builder().name("Test Doc").text("content").build()
        doc_result = self.document.create_by_text(
            CreateDocumentByTextRequest.builder()
            .dataset_id("ds-123")
            .request_body(doc_body)
            .build(),
            self.option,
        )
        assert doc_result.document is not None
        assert doc_result.document.id == "doc-123"

    @respx.mock
    def test_dataset_create_error(self):
        respx.post("https://api.dify.ai/v1/datasets").mock(
            return_value=httpx.Response(400, json={"message": "Bad Request"})
        )
        body = CreateDatasetRequestBody.builder().name("").build()
        result = self.dataset.create(
            CreateDatasetRequest.builder().request_body(body).build(), self.option
        )
        assert result.success is False
```

- [ ] **Step 4: Create `dify_oapi/api/knowledge/v1/model/__tests__/test_models.py`**

```python
from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest


class TestKnowledgeModels:
    def test_create_dataset_request_builder(self):
        body = CreateDatasetRequestBody.builder().name("My Dataset").build()
        request = CreateDatasetRequest.builder().request_body(body).build()
        assert request is not None
        assert request.request_body is not None
        assert request.request_body.name == "My Dataset"

    def test_create_dataset_request_body_builder_fields(self):
        body = (
            CreateDatasetRequestBody.builder()
            .name("Test")
            .description("A test dataset")
            .build()
        )
        assert body.name == "Test"
        assert body.description == "A test dataset"

    def test_list_datasets_request_builder(self):
        request = ListDatasetsRequest.builder().page(2).limit(50).build()
        assert request is not None
```

- [ ] **Step 5: Run knowledge supporting tests**

Run: `poetry run pytest dify_oapi/api/knowledge/__tests__/ dify_oapi/api/knowledge/v1/__tests__/ dify_oapi/api/knowledge/v1/model/ -v`

Expected: All tests pass.

- [ ] **Step 6: Commit**

```bash
git add dify_oapi/api/knowledge/__tests__/ dify_oapi/api/knowledge/v1/__tests__/ dify_oapi/api/knowledge/v1/model/
git commit -m "test: add knowledge service, async, integration, and model tests"
```

---

### Task 8: Knowledge Resource Tests

**Files:**
- Create: `dify_oapi/api/knowledge/v1/resource/__tests__/test_dataset.py`
- Create: `dify_oapi/api/knowledge/v1/resource/__tests__/test_document.py`
- Create: `dify_oapi/api/knowledge/v1/resource/__tests__/test_segment.py`
- Create: `dify_oapi/api/knowledge/v1/resource/__tests__/test_chunk.py`
- Create: `dify_oapi/api/knowledge/v1/resource/__tests__/test_tag.py`
- Create: `dify_oapi/api/knowledge/v1/resource/__tests__/test_model.py`

- [ ] **Step 1: Create `dify_oapi/api/knowledge/v1/resource/__tests__/test_dataset.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.delete_dataset_request import DeleteDatasetRequest
from dify_oapi.api.knowledge.v1.model.get_dataset_request import GetDatasetRequest
from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request_body import RetrieveFromDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.update_dataset_request import UpdateDatasetRequest
from dify_oapi.api.knowledge.v1.model.update_dataset_request_body import UpdateDatasetRequestBody
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
                "data": [], "has_more": False, "total": 0, "page": 1, "limit": 20
            })
        )
        result = self.resource.list(
            ListDatasetsRequest.builder().page(1).limit(20).build(), self.option
        )
        assert result.data == []
        assert result.total == 0
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create(self):
        route = respx.post("https://api.dify.ai/v1/datasets").mock(
            return_value=httpx.Response(200, json={"id": "ds-123", "name": "Test Dataset"})
        )
        body = CreateDatasetRequestBody.builder().name("Test Dataset").build()
        result = self.resource.create(
            CreateDatasetRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "ds-123"
        assert result.name == "Test Dataset"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_get(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"id": "ds-123", "name": "Test Dataset"}))
        result = self.resource.get(
            GetDatasetRequest.builder().dataset_id("ds-123").build(), self.option
        )
        assert result.id == "ds-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_update(self):
        route = respx.patch(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"id": "ds-123", "name": "Updated"}))
        body = UpdateDatasetRequestBody.builder().name("Updated").build()
        result = self.resource.update(
            UpdateDatasetRequest.builder().dataset_id("ds-123").request_body(body).build(),
            self.option,
        )
        assert result.id == "ds-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        result = self.resource.delete(
            DeleteDatasetRequest.builder().dataset_id("ds-123").build(), self.option
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_retrieve(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/retrieve"
        ).mock(return_value=httpx.Response(200, json={"records": [], "query": {"content": "test"}}))
        body = RetrieveFromDatasetRequestBody.builder().query("test").build()
        result = self.resource.retrieve(
            RetrieveFromDatasetRequest.builder().dataset_id("ds-123").request_body(body).build(),
            self.option,
        )
        assert result.records == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 2: Create `dify_oapi/api/knowledge/v1/resource/__tests__/test_document.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import CreateDocumentByTextRequestBody
from dify_oapi.api.knowledge.v1.model.delete_document_request import DeleteDocumentRequest
from dify_oapi.api.knowledge.v1.model.get_batch_indexing_status_request import GetBatchIndexingStatusRequest
from dify_oapi.api.knowledge.v1.model.get_document_request import GetDocumentRequest
from dify_oapi.api.knowledge.v1.model.list_documents_request import ListDocumentsRequest
from dify_oapi.api.knowledge.v1.resource.document import Document


class TestDocument:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Document(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/documents"
        ).mock(return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "limit": 20}))
        result = self.resource.list(
            ListDocumentsRequest.builder().dataset_id("ds-123").page(1).limit(20).build(),
            self.option,
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create_by_text(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/document/create-by-text"
        ).mock(
            return_value=httpx.Response(200, json={
                "document": {"id": "doc-123", "name": "Test Doc", "indexing_status": "waiting"}
            })
        )
        body = CreateDocumentByTextRequestBody.builder().name("Test Doc").text("content").build()
        result = self.resource.create_by_text(
            CreateDocumentByTextRequest.builder()
            .dataset_id("ds-123")
            .request_body(body)
            .build(),
            self.option,
        )
        assert result.document is not None
        assert result.document.id == "doc-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_get(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/documents/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"id": "doc-123", "name": "Test Doc"}))
        result = self.resource.get(
            GetDocumentRequest.builder().dataset_id("ds-123").document_id("doc-123").build(),
            self.option,
        )
        assert result.id == "doc-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/documents/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        result = self.resource.delete(
            DeleteDocumentRequest.builder().dataset_id("ds-123").document_id("doc-123").build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_get_batch_status(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/documents/[^/]+/indexing-status"
        ).mock(return_value=httpx.Response(200, json={"id": "doc-123", "indexing_status": "completed"}))
        result = self.resource.get_batch_status(
            GetBatchIndexingStatusRequest.builder().dataset_id("ds-123").batch("batch-123").build(),
            self.option,
        )
        assert result.id == "doc-123"
        assert result.indexing_status == "completed"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 3: Create `dify_oapi/api/knowledge/v1/resource/__tests__/test_segment.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.knowledge.v1.model.create_segment_request import CreateSegmentRequest
from dify_oapi.api.knowledge.v1.model.create_segment_request_body import CreateSegmentRequestBody
from dify_oapi.api.knowledge.v1.model.delete_segment_request import DeleteSegmentRequest
from dify_oapi.api.knowledge.v1.model.list_segments_request import ListSegmentsRequest
from dify_oapi.api.knowledge.v1.resource.segment import Segment


class TestSegment:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Segment(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/documents/[^/]+/segments"
        ).mock(return_value=httpx.Response(200, json={"data": [], "doc_form": "text_model"}))
        result = self.resource.list(
            ListSegmentsRequest.builder().dataset_id("ds-123").document_id("doc-123").build(),
            self.option,
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/documents/[^/]+/segments"
        ).mock(
            return_value=httpx.Response(200, json={
                "data": [{"id": "seg-123", "content": "test content"}]
            })
        )
        body = CreateSegmentRequestBody.builder().segments([]).build()
        result = self.resource.create(
            CreateSegmentRequest.builder()
            .dataset_id("ds-123")
            .document_id("doc-123")
            .request_body(body)
            .build(),
            self.option,
        )
        assert result.data is not None
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/documents/[^/]+/segments/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        result = self.resource.delete(
            DeleteSegmentRequest.builder()
            .dataset_id("ds-123")
            .document_id("doc-123")
            .segment_id("seg-123")
            .build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 4: Create `dify_oapi/api/knowledge/v1/resource/__tests__/test_chunk.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.knowledge.v1.model.create_child_chunk_request import CreateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import CreateChildChunkRequestBody
from dify_oapi.api.knowledge.v1.model.delete_child_chunk_request import DeleteChildChunkRequest
from dify_oapi.api.knowledge.v1.model.list_child_chunks_request import ListChildChunksRequest
from dify_oapi.api.knowledge.v1.resource.chunk import Chunk


class TestChunk:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Chunk(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/documents/[^/]+/segments/[^/]+/child_chunks"
        ).mock(return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "limit": 20}))
        result = self.resource.list(
            ListChildChunksRequest.builder()
            .dataset_id("ds-123")
            .document_id("doc-123")
            .segment_id("seg-123")
            .build(),
            self.option,
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/documents/[^/]+/segments/[^/]+/child_chunks"
        ).mock(
            return_value=httpx.Response(200, json={
                "data": [{"id": "chunk-123", "content": "chunk content"}]
            })
        )
        body = CreateChildChunkRequestBody.builder().content("chunk content").build()
        result = self.resource.create(
            CreateChildChunkRequest.builder()
            .dataset_id("ds-123")
            .document_id("doc-123")
            .segment_id("seg-123")
            .request_body(body)
            .build(),
            self.option,
        )
        assert result.data is not None
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/datasets/[^/]+/documents/[^/]+/segments/[^/]+/child_chunks/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        result = self.resource.delete(
            DeleteChildChunkRequest.builder()
            .dataset_id("ds-123")
            .document_id("doc-123")
            .segment_id("seg-123")
            .child_chunk_id("chunk-123")
            .build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 5: Create `dify_oapi/api/knowledge/v1/resource/__tests__/test_tag.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request_body import BindTagsToDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody
from dify_oapi.api.knowledge.v1.model.delete_tag_request import DeleteTagRequest
from dify_oapi.api.knowledge.v1.model.delete_tag_request_body import DeleteTagRequestBody
from dify_oapi.api.knowledge.v1.model.list_tags_request import ListTagsRequest
from dify_oapi.api.knowledge.v1.resource.tag import Tag


class TestTag:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Tag(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get("https://api.dify.ai/v1/datasets/tags").mock(
            return_value=httpx.Response(200, json={"data": []})
        )
        result = self.resource.list(
            ListTagsRequest.builder().build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create(self):
        route = respx.post("https://api.dify.ai/v1/datasets/tags").mock(
            return_value=httpx.Response(200, json={"id": "tag-123", "name": "My Tag"})
        )
        body = CreateTagRequestBody.builder().name("My Tag").build()
        result = self.resource.create(
            CreateTagRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "tag-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete("https://api.dify.ai/v1/datasets/tags").mock(
            return_value=httpx.Response(200, json={"result": "success"})
        )
        body = DeleteTagRequestBody.builder().tag_id("tag-123").build()
        result = self.resource.delete(
            DeleteTagRequest.builder().request_body(body).build(), self.option
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_bind(self):
        route = respx.post("https://api.dify.ai/v1/datasets/tags/binding").mock(
            return_value=httpx.Response(200, json={"result": "success"})
        )
        body = BindTagsToDatasetRequestBody.builder().tag_ids(["tag-123"]).target_id("ds-123").build()
        result = self.resource.bind(
            BindTagsToDatasetRequest.builder().request_body(body).build(), self.option
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 6: Create `dify_oapi/api/knowledge/v1/resource/__tests__/test_model.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest
from dify_oapi.api.knowledge.v1.resource.model import Model


class TestModel:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Model(config)
        self.option = request_option

    @respx.mock
    def test_embedding_models(self):
        route = respx.get(
            "https://api.dify.ai/v1/workspaces/current/models/model-types/text-embedding"
        ).mock(return_value=httpx.Response(200, json={"data": []}))
        result = self.resource.embedding_models(
            GetTextEmbeddingModelsRequest.builder().build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 7: Run all knowledge resource tests**

Run: `poetry run pytest dify_oapi/api/knowledge/v1/resource/ -v`

Expected: All tests pass.

- [ ] **Step 8: Commit**

```bash
git add dify_oapi/api/knowledge/v1/resource/
git commit -m "test: add knowledge resource unit tests"
```

---

### Task 9: Workflow Tests

**Files:**
- Create: `dify_oapi/api/workflow/__tests__/test_service.py`
- Create: `dify_oapi/api/workflow/v1/resource/__tests__/test_workflow.py`

- [ ] **Step 1: Write `test_service.py`**

```python
import pytest

from dify_oapi.api.workflow.service import WorkflowService
from dify_oapi.api.workflow.v1.version import V1
from dify_oapi.api.workflow.v1.resource.workflow import Workflow


class TestWorkflowService:
    def test_has_v1(self, config):
        service = WorkflowService(config)
        assert isinstance(service.v1, V1)

    def test_v1_has_workflow(self, config):
        v1 = WorkflowService(config).v1
        assert isinstance(v1.workflow, Workflow)
```

- [ ] **Step 2: Write `test_workflow.py`**

```python
import httpx
import pytest
import respx

from dify_oapi.api.workflow.v1.model.get_workflow_logs_request import GetWorkflowLogsRequest
from dify_oapi.api.workflow.v1.model.get_workflow_run_detail_request import GetWorkflowRunDetailRequest
from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.run_workflow_request_body import RunWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.stop_workflow_request import StopWorkflowRequest
from dify_oapi.api.workflow.v1.model.stop_workflow_request_body import StopWorkflowRequestBody
from dify_oapi.api.workflow.v1.resource.workflow import Workflow


class TestWorkflow:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Workflow(config)
        self.option = request_option

    @respx.mock
    def test_run(self):
        route = respx.post("https://api.dify.ai/v1/workflows/run").mock(
            return_value=httpx.Response(200, json={"workflow_run_id": "run-123", "task_id": "task-456"})
        )
        body = RunWorkflowRequestBody.builder().user("user-1").build()
        result = self.resource.run(
            RunWorkflowRequest.builder().request_body(body).build(), self.option
        )
        assert result.workflow_run_id == "run-123"
        assert result.task_id == "task-456"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_run_stream(self):
        chunks = b"data: hello\n\ndata: world\n\n"
        respx.post("https://api.dify.ai/v1/workflows/run").mock(
            return_value=httpx.Response(200, content=chunks)
        )
        body = RunWorkflowRequestBody.builder().user("user-1").build()
        gen = self.resource.run(
            RunWorkflowRequest.builder().request_body(body).build(), self.option, stream=True
        )
        collected = b"".join(gen)
        assert b"hello" in collected

    @respx.mock
    def test_detail(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/workflows/run/[^/]+"
        ).mock(
            return_value=httpx.Response(200, json={"id": "run-123", "workflow_id": "wf-456", "status": "succeeded"})
        )
        result = self.resource.detail(
            GetWorkflowRunDetailRequest.builder().workflow_run_id("run-123").build(), self.option
        )
        assert result.id == "run-123"
        assert result.status == "succeeded"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_stop(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/workflows/tasks/[^/]+/stop"
        ).mock(
            return_value=httpx.Response(200, json={"result": "success"})
        )
        body = StopWorkflowRequestBody.builder().user("user-1").build()
        result = self.resource.stop(
            StopWorkflowRequest.builder().task_id("task-456").request_body(body).build(), self.option
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_logs(self):
        route = respx.get("https://api.dify.ai/v1/workflows/logs").mock(
            return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "limit": 20, "has_more": False})
        )
        result = self.resource.logs(GetWorkflowLogsRequest.builder().build(), self.option)
        assert result.data == []
        assert result.total == 0
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    async def test_arun(self):
        route = respx.post("https://api.dify.ai/v1/workflows/run").mock(
            return_value=httpx.Response(200, json={"workflow_run_id": "run-123", "task_id": "task-456"})
        )
        body = RunWorkflowRequestBody.builder().user("user-1").build()
        result = await self.resource.arun(
            RunWorkflowRequest.builder().request_body(body).build(), self.option
        )
        assert result.workflow_run_id == "run-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
```

- [ ] **Step 3: Run workflow tests**

Run: `poetry run pytest dify_oapi/api/workflow/ -v`

Expected: All tests pass.

- [ ] **Step 4: Commit**

```bash
git add dify_oapi/api/workflow/
git commit -m "test: add workflow unit tests"
```

---

### Task 10: Cleanup and CLAUDE.md Update

**Files:**
- Delete: `tests/` directory (entire tree)
- Modify: `CLAUDE.md`

- [ ] **Step 1: Delete the old `tests/` directory**

```bash
rm -rf tests/
```

- [ ] **Step 2: Run full test suite to confirm nothing broke**

Run: `poetry run pytest dify_oapi/ -v`

Expected: All tests pass, no collection errors.

- [ ] **Step 3: Update CLAUDE.md — Testing Commands section**

In CLAUDE.md, replace the Testing section's commands block:

```markdown
### Testing
```bash
make test               # Run all tests (discovers from dify_oapi/)
make test-cov           # Run tests with coverage report

# Run specific service tests
poetry run pytest dify_oapi/api/knowledge/ -v
poetry run pytest dify_oapi/api/chat/ -v

# Run specific test patterns
poetry run pytest dify_oapi/ -k "test_create" -v
\```
```

Remove the environment variable block (`export DOMAIN=...`, `export CHAT_KEY=...`, etc.) — tests no longer require external service credentials.

- [ ] **Step 4: Update CLAUDE.md — Testing Strategy section**

Replace the current Testing Strategy section content with:

```markdown
## Testing Strategy

Tests live adjacent to source files in `__tests__` directories. All HTTP is mocked at the httpx layer via `respx` — no external service dependencies.

```
dify_oapi/
├── conftest.py                          # Shared fixtures (config, request_option, domain)
├── __tests__/
│   └── test_client.py
└── api/
    └── {service}/
        ├── __tests__/
        │   └── test_service.py
        └── v1/
            └── resource/
                └── __tests__/
                    └── test_{resource}.py   # HTTP-level tests with respx
\```

Co-location rule: `a/b/c.py` → `a/b/__tests__/test_c.py`

**Test Fixtures** (`dify_oapi/conftest.py`):
- `domain`: Returns `"https://api.dify.ai"`
- `request_option`: Test `RequestOption` with `"test-key"`
- `config`: Real `Config` object with `domain` set

**Running Specific Tests**:
```bash
# Single resource
poetry run pytest dify_oapi/api/knowledge/v1/resource/__tests__/test_dataset.py -v

# Single test
poetry run pytest dify_oapi/api/chat/v1/resource/__tests__/test_chat.py::TestChat::test_chat -v
\```
```

- [ ] **Step 5: Update CLAUDE.md — Adding a New API Method section**

In the "Adding a New API Method" section, change step 3:

From:
```
3. **Add Tests** (tests/{service}/v1/resource/test_{resource}.py):
   - Unit tests for method logic
   - Integration tests if environment variables set
```

To:
```
3. **Add Tests** (`api/{service}/v1/resource/__tests__/test_{resource}.py`):
   - Use `@respx.mock` to mock HTTP responses at the httpx layer
   - Verify URL, HTTP method, Authorization header, response model fields
   - Add async variant using `async def test_a{method}`
```

- [ ] **Step 6: Remove environment variable content from CLAUDE.md**

CLAUDE.md has two places that reference API key environment variables. Remove both:

1. In the `### Testing` commands block, the `export` lines at the top:
   ```
   # Set environment variables first
   export DOMAIN="https://api.dify.ai"
   export CHAT_KEY="your-chat-api-key"
   ...
   ```
   (Step 3 already replaces this entire section with new content, so this is handled.)

2. The `### Environment Variables for Testing` subsection (around line 204 in the current CLAUDE.md):
   ```
   ### Environment Variables for Testing
   The SDK requires API keys per service for integration tests. Set these before running tests:
   - `DOMAIN`: Dify API endpoint
   - `{SERVICE}_KEY`: API key for each service (CHAT_KEY, KNOWLEDGE_KEY, etc.)
   ```
   Delete this entire subsection — tests no longer require external service credentials.

- [ ] **Step 7: Run full suite and checks**

```bash
poetry run pytest dify_oapi/ -v
make check
```

Expected: All tests pass, no mypy or lint errors.

- [ ] **Step 8: Commit**

```bash
git add -u
git add CLAUDE.md
git commit -m "chore: remove tests/ dir and update CLAUDE.md for co-located tests"
```

---

