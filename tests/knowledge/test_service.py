"""Knowledge service tests."""

import pytest

from dify_oapi.api.knowledge.service import KnowledgeService
from dify_oapi.api.knowledge.v1.version import V1


class TestKnowledgeService:
    """Test Knowledge service."""

    @pytest.fixture
    def service(self, mock_config):
        """Create KnowledgeService instance."""
        return KnowledgeService(mock_config)

    def test_service_has_v1(self, service):
        """Test service has v1."""
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_resources(self, service):
        """Test v1 resources."""
        v1 = service.v1
        assert hasattr(v1, "dataset")
        assert hasattr(v1, "document")
        assert hasattr(v1, "segment")
        assert hasattr(v1, "chunk")
        assert hasattr(v1, "tag")
        assert hasattr(v1, "model")
