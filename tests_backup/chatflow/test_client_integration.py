"""Tests for Chatflow API client integration."""

import pytest

from dify_oapi.api.chatflow.service import ChatflowService
from dify_oapi.client import Client


class TestChatflowClientIntegration:
    """Test cases for Chatflow API integration with main Client."""

    def test_client_initialization_with_chatflow_service(self):
        """Test client initialization includes chatflow service."""
        client = Client.builder().domain("https://api.dify.ai").build()

        assert client is not None
        assert hasattr(client, "chatflow")
        assert isinstance(client.chatflow, ChatflowService)

    def test_chatflow_api_accessibility_through_client(self):
        """Test chatflow API accessibility through client."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Verify chatflow service is accessible
        assert client.chatflow is not None
        assert isinstance(client.chatflow, ChatflowService)

        # Verify v1 version is accessible
        assert client.chatflow.v1 is not None

        # Verify all resources are accessible
        assert hasattr(client.chatflow.v1, "chatflow")
        assert hasattr(client.chatflow.v1, "file")
        assert hasattr(client.chatflow.v1, "feedback")
        assert hasattr(client.chatflow.v1, "conversation")
        assert hasattr(client.chatflow.v1, "tts")
        assert hasattr(client.chatflow.v1, "application")
        assert hasattr(client.chatflow.v1, "annotation")

    def test_end_to_end_api_access_patterns(self):
        """Test end-to-end API access patterns through client."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Test chatflow operations access
        assert hasattr(client.chatflow.v1.chatflow, "send")
        assert hasattr(client.chatflow.v1.chatflow, "stop")
        assert hasattr(client.chatflow.v1.chatflow, "suggested")

        # Test file operations access
        assert hasattr(client.chatflow.v1.file, "upload")

        # Test feedback operations access
        assert hasattr(client.chatflow.v1.feedback, "message")
        assert hasattr(client.chatflow.v1.feedback, "list")

        # Test conversation operations access
        assert hasattr(client.chatflow.v1.conversation, "messages")
        assert hasattr(client.chatflow.v1.conversation, "list")
        assert hasattr(client.chatflow.v1.conversation, "delete")
        assert hasattr(client.chatflow.v1.conversation, "rename")
        assert hasattr(client.chatflow.v1.conversation, "variables")

        # Test TTS operations access
        assert hasattr(client.chatflow.v1.tts, "speech_to_text")
        assert hasattr(client.chatflow.v1.tts, "text_to_audio")

        # Test application operations access
        assert hasattr(client.chatflow.v1.application, "info")
        assert hasattr(client.chatflow.v1.application, "parameters")
        assert hasattr(client.chatflow.v1.application, "meta")
        assert hasattr(client.chatflow.v1.application, "site")

        # Test annotation operations access
        assert hasattr(client.chatflow.v1.annotation, "list")
        assert hasattr(client.chatflow.v1.annotation, "create")
        assert hasattr(client.chatflow.v1.annotation, "update")
        assert hasattr(client.chatflow.v1.annotation, "delete")
        assert hasattr(client.chatflow.v1.annotation, "reply_settings")
        assert hasattr(client.chatflow.v1.annotation, "reply_status")

    def test_configuration_propagation_through_all_layers(self):
        """Test configuration propagation through all layers."""
        domain = "https://test.api.dify.ai"
        client = Client.builder().domain(domain).build()

        # Verify chatflow service is accessible
        assert client.chatflow.v1 is not None

        # Verify all resources are accessible
        resources = [
            client.chatflow.v1.chatflow,
            client.chatflow.v1.file,
            client.chatflow.v1.feedback,
            client.chatflow.v1.conversation,
            client.chatflow.v1.tts,
            client.chatflow.v1.application,
            client.chatflow.v1.annotation,
        ]

        for resource in resources:
            assert resource is not None

    def test_chatflow_service_not_initialized_error(self):
        """Test error when chatflow service is not initialized."""
        client = Client()

        with pytest.raises(RuntimeError, match="Chatflow service has not been initialized"):
            _ = client.chatflow

    def test_client_builder_pattern_with_chatflow(self):
        """Test client builder pattern includes chatflow service."""
        client = Client.builder().domain("https://api.dify.ai").max_retry_count(3).max_keepalive_connections(10).build()

        # Verify client is properly built
        assert client is not None

        # Verify chatflow service is initialized
        assert client.chatflow is not None
        assert isinstance(client.chatflow, ChatflowService)

        # Verify chatflow service is properly configured
        assert client.chatflow.v1 is not None

    def test_all_services_coexist(self):
        """Test that chatflow service coexists with other services."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Verify all services are available
        assert hasattr(client, "chat")
        assert hasattr(client, "chatflow")
        assert hasattr(client, "completion")
        assert hasattr(client, "dify")
        assert hasattr(client, "workflow")
        assert hasattr(client, "knowledge")

        # Verify all services are properly initialized
        assert client.chat is not None
        assert client.chatflow is not None
        assert client.completion is not None
        assert client.dify is not None
        assert client.workflow is not None
        assert client.knowledge is not None

    def test_chatflow_service_independence(self):
        """Test that chatflow service operates independently of other services."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Get chatflow service
        chatflow_service = client.chatflow

        # Verify it's independent
        assert chatflow_service is not None
        assert chatflow_service.v1 is not None

        # Verify it's a different service instance
        assert id(chatflow_service) != id(client.chat)
        assert id(chatflow_service) != id(client.completion)
        assert id(chatflow_service) != id(client.dify)

    def test_async_methods_accessibility(self):
        """Test that async methods are accessible through client."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Test async chatflow methods
        assert hasattr(client.chatflow.v1.chatflow, "asend")
        assert hasattr(client.chatflow.v1.chatflow, "astop")
        assert hasattr(client.chatflow.v1.chatflow, "asuggested")

        # Test async file methods
        assert hasattr(client.chatflow.v1.file, "aupload")

        # Test async feedback methods
        assert hasattr(client.chatflow.v1.feedback, "amessage")
        assert hasattr(client.chatflow.v1.feedback, "alist")

        # Test async conversation methods
        assert hasattr(client.chatflow.v1.conversation, "amessages")
        assert hasattr(client.chatflow.v1.conversation, "alist")
        assert hasattr(client.chatflow.v1.conversation, "adelete")
        assert hasattr(client.chatflow.v1.conversation, "arename")
        assert hasattr(client.chatflow.v1.conversation, "avariables")

        # Test async TTS methods
        assert hasattr(client.chatflow.v1.tts, "aspeech_to_text")
        assert hasattr(client.chatflow.v1.tts, "atext_to_audio")

        # Test async application methods
        assert hasattr(client.chatflow.v1.application, "ainfo")
        assert hasattr(client.chatflow.v1.application, "aparameters")
        assert hasattr(client.chatflow.v1.application, "ameta")
        assert hasattr(client.chatflow.v1.application, "asite")

        # Test async annotation methods
        assert hasattr(client.chatflow.v1.annotation, "alist")
        assert hasattr(client.chatflow.v1.annotation, "acreate")
        assert hasattr(client.chatflow.v1.annotation, "aupdate")
        assert hasattr(client.chatflow.v1.annotation, "adelete")
        assert hasattr(client.chatflow.v1.annotation, "areply_settings")
        assert hasattr(client.chatflow.v1.annotation, "areply_status")

    def test_client_close_methods_with_chatflow(self):
        """Test client close methods work with chatflow service."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Verify chatflow service is accessible before close
        assert client.chatflow is not None

        # Test synchronous close
        client.close()

        # Service should still be accessible after close
        assert client.chatflow is not None

    async def test_client_async_close_with_chatflow(self):
        """Test client async close methods work with chatflow service."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Verify chatflow service is accessible before close
        assert client.chatflow is not None

        # Test asynchronous close
        await client.aclose()

        # Service should still be accessible after close
        assert client.chatflow is not None
