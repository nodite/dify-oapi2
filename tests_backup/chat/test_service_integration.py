"""Tests for Chat service integration."""

import pytest

from dify_oapi.api.chat.service import ChatService
from dify_oapi.api.chat.v1.version import V1
from dify_oapi.core.model.config import Config


class TestChatServiceIntegration:
    """Test Chat service class integration."""

    @pytest.fixture
    def config(self):
        """Create test config."""
        return Config()

    @pytest.fixture
    def chat_service(self, config):
        """Create ChatService instance."""
        return ChatService(config)

    def test_chat_service_initialization(self, chat_service):
        """Test ChatService initialization."""
        assert chat_service is not None
        assert hasattr(chat_service, "v1")
        assert isinstance(chat_service.v1, V1)

    def test_v1_version_accessibility(self, chat_service):
        """Test v1 version accessibility."""
        v1 = chat_service.v1
        assert v1 is not None
        assert isinstance(v1, V1)

    def test_configuration_propagation(self, config):
        """Test configuration propagation to service."""
        config.domain = "https://test.api.dify.ai"
        config.max_retry_count = 5

        service = ChatService(config)

        # Verify service is initialized with config
        assert service.v1 is not None

        # Check that all resources are properly initialized
        assert service.v1.chat is not None
        assert service.v1.file is not None
        assert service.v1.feedback is not None
        assert service.v1.conversation is not None
        assert service.v1.audio is not None
        assert service.v1.app is not None
        assert service.v1.annotation is not None
        assert service.v1.message is not None  # Backward compatibility

    def test_service_consistency(self, chat_service):
        """Test service consistency with other API services."""
        # Verify service follows same pattern as other services
        assert hasattr(chat_service, "v1")
        assert chat_service.v1 is not None

        # Verify v1 has all expected resources
        v1 = chat_service.v1
        expected_resources = ["chat", "file", "feedback", "conversation", "audio", "app", "annotation", "message"]

        for resource in expected_resources:
            assert hasattr(v1, resource), f"Missing resource: {resource}"
            assert getattr(v1, resource) is not None

    def test_all_resources_have_config(self, config):
        """Test all resources receive configuration."""
        service = ChatService(config)
        v1 = service.v1

        # All resources should have config attribute
        resources = [v1.chat, v1.file, v1.feedback, v1.conversation, v1.audio, v1.app, v1.annotation, v1.message]

        for resource in resources:
            assert hasattr(resource, "config")
            assert resource.config is config

    def test_service_type_annotations(self, chat_service):
        """Test service has proper type annotations."""
        # Check that v1 attribute has proper type
        assert hasattr(ChatService, "__annotations__")

        # Verify v1 is properly typed
        v1 = chat_service.v1
        assert isinstance(v1, V1)
