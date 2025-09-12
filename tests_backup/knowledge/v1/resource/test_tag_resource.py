"""
Tag Resource Tests

Test tag resources of the knowledge module
"""

from unittest.mock import Mock, patch

import pytest

from dify_oapi.api.knowledge.v1.resource.tag import Tag
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestTagResource:
    """Tag Resource Tests"""

    @pytest.fixture
    def config(self):
        return Config()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def tag_resource(self, config):
        return Tag(config)

    def test_tag_resource_init(self, tag_resource):
        """Test Tag resource initialization"""
        assert tag_resource.config is not None

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_create_method(self, mock_execute, tag_resource, request_option):
        """Test create tag method"""
        from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest

        mock_response = Mock()
        mock_response.id = "tag-123"
        mock_response.name = "test-tag"
        mock_execute.return_value = mock_response

        request = CreateTagRequest.builder().build()
        response = tag_resource.create(request, request_option)

        assert response.id == "tag-123"
        assert response.name == "test-tag"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_list_method(self, mock_execute, tag_resource, request_option):
        """Test list tags method"""
        from dify_oapi.api.knowledge.v1.model.list_tags_request import ListTagsRequest

        mock_response = Mock()
        mock_response.data = [Mock(id="tag-1", name="tag1"), Mock(id="tag-2", name="tag2")]
        mock_execute.return_value = mock_response

        request = ListTagsRequest.builder().build()
        response = tag_resource.list(request, request_option)

        assert len(response.data) == 2
        assert response.data[0].id == "tag-1"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_bind_method(self, mock_execute, tag_resource, request_option):
        """Test bind tag method"""
        from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest

        mock_response = Mock()
        mock_response.result = "success"
        mock_execute.return_value = mock_response

        request = BindTagsToDatasetRequest.builder().build()
        response = tag_resource.bind(request, request_option)

        assert response.result == "success"
        mock_execute.assert_called_once()

    def test_tag_resource_methods_exist(self, tag_resource):
        """Test Tag resource methods exist"""
        methods = [
            "create",
            "acreate",
            "list",
            "alist",
            "update",
            "aupdate",
            "delete",
            "adelete",
            "bind",
            "abind",
            "unbind",
            "aunbind",
            "get_dataset_tags",
            "aget_dataset_tags",
        ]

        for method in methods:
            assert hasattr(tag_resource, method)
            assert callable(getattr(tag_resource, method))


if __name__ == "__main__":
    pytest.main([__file__])
