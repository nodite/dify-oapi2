"""Completion service tests."""

import pytest

from dify_oapi.api.completion.service import CompletionService
from dify_oapi.api.completion.v1.version import V1


class TestCompletionService:
    """Test Completion service."""

    @pytest.fixture
    def service(self, mock_config):
        """Create CompletionService instance."""
        return CompletionService(mock_config)

    def test_service_has_v1(self, service):
        """Test service has v1."""
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_resources(self, service):
        """Test v1 resources."""
        v1 = service.v1
        assert hasattr(v1, "completion")
        assert hasattr(v1, "annotation")
