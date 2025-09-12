"""Chat service tests."""

import pytest

from dify_oapi.api.chat.service import ChatService
from dify_oapi.api.chat.v1.version import V1


class TestChatService:
    """Test Chat service."""

    @pytest.fixture
    def service(self, mock_config):
        """Create ChatService instance."""
        return ChatService(mock_config)

    def test_service_has_v1(self, service):
        """Test service has v1."""
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_resources(self, service):
        """Test v1 resources."""
        v1 = service.v1
        assert hasattr(v1, "chat")
        assert hasattr(v1, "annotation")
        assert hasattr(v1, "conversation")
        assert hasattr(v1, "message")
