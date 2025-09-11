"""Tests for Completion API client integration."""

import pytest

from dify_oapi.api.completion.service import CompletionService
from dify_oapi.client import Client


class TestCompletionClientIntegration:
    """Test cases for Completion API integration with main Client."""

    def test_client_initialization_with_completion_service(self):
        """Test client initialization includes completion service."""
        client = Client.builder().domain("https://api.dify.ai").build()

        assert client is not None
        assert hasattr(client, "completion")
        assert isinstance(client.completion, CompletionService)

    def test_completion_api_accessibility_through_client(self):
        """Test completion API accessibility through client."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Verify completion service is accessible
        assert client.completion is not None
        assert isinstance(client.completion, CompletionService)

        # Verify v1 version is accessible
        assert client.completion.v1 is not None

        # Verify all resources are accessible
        assert hasattr(client.completion.v1, "completion")
        assert hasattr(client.completion.v1, "file")
        assert hasattr(client.completion.v1, "feedback")
        assert hasattr(client.completion.v1, "audio")
        assert hasattr(client.completion.v1, "info")
        assert hasattr(client.completion.v1, "annotation")

    def test_end_to_end_api_access_patterns(self):
        """Test end-to-end API access patterns through client."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Test completion operations access
        assert hasattr(client.completion.v1.completion, "send")
        assert hasattr(client.completion.v1.completion, "stop")

        # Test file operations access
        assert hasattr(client.completion.v1.file, "upload")

        # Test feedback operations access
        assert hasattr(client.completion.v1.feedback, "message")
        assert hasattr(client.completion.v1.feedback, "list")

        # Test audio operations access
        assert hasattr(client.completion.v1.audio, "text_to_audio")

        # Test info operations access
        assert hasattr(client.completion.v1.info, "get")
        assert hasattr(client.completion.v1.info, "parameters")
        assert hasattr(client.completion.v1.info, "site")

        # Test annotation operations access
        assert hasattr(client.completion.v1.annotation, "list")
        assert hasattr(client.completion.v1.annotation, "create")
        assert hasattr(client.completion.v1.annotation, "update")
        assert hasattr(client.completion.v1.annotation, "delete")
        assert hasattr(client.completion.v1.annotation, "reply_settings")
        assert hasattr(client.completion.v1.annotation, "reply_status")

    def test_configuration_propagation_through_all_layers(self):
        """Test configuration propagation through all layers."""
        domain = "https://test.api.dify.ai"
        client = Client.builder().domain(domain).build()

        # Verify completion service is accessible
        assert client.completion.v1 is not None

        # Verify all resources are accessible
        resources = [
            client.completion.v1.completion,
            client.completion.v1.file,
            client.completion.v1.feedback,
            client.completion.v1.audio,
            client.completion.v1.info,
            client.completion.v1.annotation,
        ]

        for resource in resources:
            assert resource is not None

    def test_completion_service_not_initialized_error(self):
        """Test error when completion service is not initialized."""
        client = Client()

        with pytest.raises(RuntimeError, match="Completion service has not been initialized"):
            _ = client.completion

    def test_client_builder_pattern_with_completion(self):
        """Test client builder pattern includes completion service."""
        client = Client.builder().domain("https://api.dify.ai").max_retry_count(3).max_keepalive_connections(10).build()

        # Verify client is properly built
        assert client is not None

        # Verify completion service is initialized
        assert client.completion is not None
        assert isinstance(client.completion, CompletionService)

        # Verify completion service is properly configured
        assert client.completion.v1 is not None

    def test_all_services_coexist(self):
        """Test that completion service coexists with other services."""
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

    def test_completion_service_independence(self):
        """Test that completion service operates independently of other services."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Get completion service
        completion_service = client.completion

        # Verify it's independent
        assert completion_service is not None
        assert completion_service.v1 is not None

        # Verify it's a different service instance
        assert id(completion_service) != id(client.chat)
        assert id(completion_service) != id(client.chatflow)
        assert id(completion_service) != id(client.dify)

    def test_async_methods_accessibility(self):
        """Test that async methods are accessible through client."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Test async completion methods
        assert hasattr(client.completion.v1.completion, "asend")
        assert hasattr(client.completion.v1.completion, "astop")

        # Test async file methods
        assert hasattr(client.completion.v1.file, "aupload")

        # Test async feedback methods
        assert hasattr(client.completion.v1.feedback, "amessage")
        assert hasattr(client.completion.v1.feedback, "alist")

        # Test async audio methods
        assert hasattr(client.completion.v1.audio, "atext_to_audio")

        # Test async info methods
        assert hasattr(client.completion.v1.info, "aget")
        assert hasattr(client.completion.v1.info, "aparameters")
        assert hasattr(client.completion.v1.info, "asite")

        # Test async annotation methods
        assert hasattr(client.completion.v1.annotation, "alist")
        assert hasattr(client.completion.v1.annotation, "acreate")
        assert hasattr(client.completion.v1.annotation, "aupdate")
        assert hasattr(client.completion.v1.annotation, "adelete")
        assert hasattr(client.completion.v1.annotation, "areply_settings")
        assert hasattr(client.completion.v1.annotation, "areply_status")

    def test_client_close_methods_with_completion(self):
        """Test client close methods work with completion service."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Verify completion service is accessible before close
        assert client.completion is not None

        # Test synchronous close
        client.close()

        # Service should still be accessible after close
        assert client.completion is not None

    async def test_client_async_close_with_completion(self):
        """Test client async close methods work with completion service."""
        client = Client.builder().domain("https://api.dify.ai").build()

        # Verify completion service is accessible before close
        assert client.completion is not None

        # Test asynchronous close
        await client.aclose()

        # Service should still be accessible after close
        assert client.completion is not None
