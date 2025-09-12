"""
Segment Resource Tests

Test segment resources of the knowledge module
"""

from unittest.mock import Mock, patch

import pytest

from dify_oapi.api.knowledge.v1.resource.segment import Segment
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestSegmentResource:
    """Segment Resource Tests"""

    @pytest.fixture
    def config(self):
        return Config()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def segment_resource(self, config):
        return Segment(config)

    def test_segment_resource_init(self, segment_resource):
        """Test Segment resource initialization"""
        assert segment_resource.config is not None

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_create_method(self, mock_execute, segment_resource, request_option):
        """Test create segment method"""
        from dify_oapi.api.knowledge.v1.model.create_segment_request import CreateSegmentRequest

        mock_response = Mock()
        mock_response.data = Mock()
        mock_response.data.id = "seg-123"
        mock_execute.return_value = mock_response

        request = CreateSegmentRequest.builder().build()
        response = segment_resource.create(request, request_option)

        assert response.data.id == "seg-123"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_list_method(self, mock_execute, segment_resource, request_option):
        """Test list segments method"""
        from dify_oapi.api.knowledge.v1.model.list_segments_request import ListSegmentsRequest

        mock_response = Mock()
        mock_response.data = [Mock(id="seg-1"), Mock(id="seg-2")]
        mock_execute.return_value = mock_response

        request = ListSegmentsRequest.builder().build()
        response = segment_resource.list(request, request_option)

        assert len(response.data) == 2
        assert response.data[0].id == "seg-1"
        mock_execute.assert_called_once()

    def test_segment_resource_methods_exist(self, segment_resource):
        """Test Segment resource methods exist"""
        methods = ["create", "acreate", "list", "alist", "get", "aget", "update", "aupdate", "delete", "adelete"]

        for method in methods:
            assert hasattr(segment_resource, method)
            assert callable(getattr(segment_resource, method))


if __name__ == "__main__":
    pytest.main([__file__])
