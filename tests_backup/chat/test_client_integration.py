"""Tests for Chat client integration."""

import pytest

from dify_oapi.api.chat.service import ChatService
from dify_oapi.client import Client


class TestChatClientIntegration:
    """Test Chat client integration."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return Client.builder().domain("https://api.dify.ai").build()

    def test_client_initialization(self, client):
        """Test client initialization includes chat service."""
        assert client is not None
        assert hasattr(client, "chat")
        assert isinstance(client.chat, ChatService)

    def test_chat_service_accessibility(self, client):
        """Test chat service accessibility through client."""
        chat_service = client.chat
        assert chat_service is not None
        assert isinstance(chat_service, ChatService)

    def test_all_chat_resources_accessible_through_client(self, client):
        """Test all chat resources accessible through client."""
        chat = client.chat
        v1 = chat.v1

        # Test all 7 main resources are accessible
        assert v1.chat is not None
        assert v1.file is not None
        assert v1.feedback is not None
        assert v1.conversation is not None
        assert v1.audio is not None
        assert v1.app is not None
        assert v1.annotation is not None

        # Test backward compatibility resource
        assert v1.message is not None

    def test_complete_api_access_path(self, client):
        """Test complete API access path works properly."""
        # Test access path: client.chat.v1.resource.method
        assert hasattr(client.chat.v1.chat, "chat")
        assert hasattr(client.chat.v1.chat, "stop")
        assert hasattr(client.chat.v1.chat, "suggested")

        assert hasattr(client.chat.v1.file, "upload")

        assert hasattr(client.chat.v1.feedback, "submit")
        assert hasattr(client.chat.v1.feedback, "list")

        assert hasattr(client.chat.v1.conversation, "list")
        assert hasattr(client.chat.v1.conversation, "delete")
        assert hasattr(client.chat.v1.conversation, "rename")
        assert hasattr(client.chat.v1.conversation, "history")
        assert hasattr(client.chat.v1.conversation, "variables")

        assert hasattr(client.chat.v1.audio, "to_text")
        assert hasattr(client.chat.v1.audio, "to_audio")

        assert hasattr(client.chat.v1.app, "info")
        assert hasattr(client.chat.v1.app, "parameters")
        assert hasattr(client.chat.v1.app, "meta")
        assert hasattr(client.chat.v1.app, "site")

        assert hasattr(client.chat.v1.annotation, "list")
        assert hasattr(client.chat.v1.annotation, "create")
        assert hasattr(client.chat.v1.annotation, "update")
        assert hasattr(client.chat.v1.annotation, "delete")
        assert hasattr(client.chat.v1.annotation, "configure")
        assert hasattr(client.chat.v1.annotation, "status")

    def test_client_configuration_propagation(self):
        """Test client configuration propagates to chat service."""
        domain = "https://test.api.dify.ai"
        max_retry = 5

        client = Client.builder().domain(domain).max_retry_count(max_retry).build()

        # Verify configuration propagated to chat service
        chat_service = client.chat
        assert chat_service is not None

        # Check that configuration reached the resources
        v1 = chat_service.v1
        assert v1.chat.config.domain == domain
        assert v1.chat.config.max_retry_count == max_retry

    def test_client_consistency_with_other_services(self, client):
        """Test chat service consistency with other client services."""
        # Verify client has all expected services
        expected_services = ["chat", "completion", "dify", "workflow", "knowledge"]

        for service_name in expected_services:
            assert hasattr(client, service_name), f"Missing service: {service_name}"
            service = getattr(client, service_name)
            assert service is not None

    def test_client_resource_cleanup(self, client):
        """Test client resource cleanup methods."""
        # Test synchronous cleanup
        assert hasattr(client, "close")

        # Test asynchronous cleanup
        assert hasattr(client, "aclose")

        # Cleanup should not raise errors
        client.close()

    async def test_async_client_cleanup(self):
        """Test async client cleanup."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Async cleanup should not raise errors
        await client.aclose()

    def test_client_builder_pattern(self):
        """Test client builder pattern works correctly."""
        builder = Client.builder()
        assert builder is not None

        # Test method chaining
        client = (
            builder.domain("https://api.dify.ai")
            .max_retry_count(3)
            .max_keepalive_connections(10)
            .max_connections(100)
            .keepalive_expiry(30.0)
            .build()
        )

        assert client is not None
        assert isinstance(client.chat, ChatService)

    def test_client_error_handling(self):
        """Test client error handling for uninitialized services."""
        client = Client()  # Not built through builder

        # Should raise RuntimeError for uninitialized services
        with pytest.raises(RuntimeError, match="Chat service has not been initialized"):
            _ = client.chat
