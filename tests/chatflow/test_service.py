"""Chatflow service tests."""

import pytest

from dify_oapi.api.chatflow.service import ChatflowService
from dify_oapi.api.chatflow.v1.version import V1


class TestChatflowService:
    """Test Chatflow service."""

    @pytest.fixture
    def service(self, mock_config):
        """Create ChatflowService instance."""
        return ChatflowService(mock_config)

    def test_service_has_v1(self, service):
        """Test service has v1."""
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_resources(self, service):
        """Test v1 resources."""
        v1 = service.v1
        assert hasattr(v1, "chatflow")
        assert hasattr(v1, "annotation")
        assert hasattr(v1, "conversation")
        assert hasattr(v1, "file")
        assert hasattr(v1, "feedback")
        assert hasattr(v1, "tts")
        assert hasattr(v1, "application")
