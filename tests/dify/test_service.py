"""Dify service tests."""

import pytest

from dify_oapi.api.dify.service import DifyService
from dify_oapi.api.dify.v1.version import V1


class TestDifyService:
    """Test Dify service."""

    @pytest.fixture
    def service(self, mock_config):
        """Create DifyService instance."""
        return DifyService(mock_config)

    def test_service_has_v1(self, service):
        """Test service has v1."""
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_resources(self, service):
        """Test v1 resources."""
        v1 = service.v1
        assert hasattr(v1, "audio")
        assert hasattr(v1, "feedback")
        assert hasattr(v1, "file")
        assert hasattr(v1, "info")
