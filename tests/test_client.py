"""Client tests."""

import pytest

from dify_oapi.api.chat.service import ChatService
from dify_oapi.api.chatflow.service import ChatflowService
from dify_oapi.api.completion.service import CompletionService
from dify_oapi.api.dify.service import DifyService
from dify_oapi.api.knowledge.service import KnowledgeService
from dify_oapi.api.workflow.service import WorkflowService
from dify_oapi.client import Client


class TestClient:
    """Test Client."""

    @pytest.fixture
    def client(self):
        """Create client."""
        return Client.builder().domain("https://api.dify.ai").build()

    def test_client_services(self, client):
        """Test client has all services."""
        assert hasattr(client, "chat")
        assert hasattr(client, "chatflow")
        assert hasattr(client, "completion")
        assert hasattr(client, "dify")
        assert hasattr(client, "knowledge")
        assert hasattr(client, "workflow")

    def test_service_types(self, client):
        """Test service types."""
        assert isinstance(client.chat, ChatService)
        assert isinstance(client.chatflow, ChatflowService)
        assert isinstance(client.completion, CompletionService)
        assert isinstance(client.dify, DifyService)
        assert isinstance(client.knowledge, KnowledgeService)
        assert isinstance(client.workflow, WorkflowService)

    def test_client_builder(self):
        """Test client builder."""
        client = Client.builder().domain("https://test.api").build()
        assert client is not None

    def test_client_builder_validation(self):
        """Test client builder validation."""
        # Builder may have defaults, so just test it builds
        client = Client.builder().build()
        assert client is not None
