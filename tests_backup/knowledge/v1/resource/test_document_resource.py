"""
Document Resource Tests

Test document resources of the knowledge module
"""

from unittest.mock import Mock, patch

import pytest

from dify_oapi.api.knowledge.v1.resource.document import Document
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestDocumentResource:
    """Document Resource Tests"""

    @pytest.fixture
    def config(self):
        return Config()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def document_resource(self, config):
        return Document(config)

    def test_document_resource_init(self, document_resource):
        """Test Document resource initialization"""
        assert document_resource.config is not None

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_create_by_file_method(self, mock_execute, document_resource, request_option):
        """Test create document by file method"""
        from dify_oapi.api.knowledge.v1.model.create_document_by_file_request import CreateDocumentByFileRequest

        mock_response = Mock()
        mock_response.document = Mock()
        mock_response.document.id = "doc-123"
        mock_execute.return_value = mock_response

        request = CreateDocumentByFileRequest.builder().build()
        response = document_resource.create_by_file(request, request_option)

        assert response.document.id == "doc-123"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_create_by_text_method(self, mock_execute, document_resource, request_option):
        """Test create document by text method"""
        from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest

        mock_response = Mock()
        mock_response.document = Mock()
        mock_response.document.id = "doc-text-123"
        mock_execute.return_value = mock_response

        request = CreateDocumentByTextRequest.builder().build()
        response = document_resource.create_by_text(request, request_option)

        assert response.document.id == "doc-text-123"
        mock_execute.assert_called_once()

    def test_document_resource_methods_exist(self, document_resource):
        """Test Document resource methods exist"""
        methods = [
            "create_by_file",
            "acreate_by_file",
            "create_by_text",
            "acreate_by_text",
            "list",
            "alist",
            "get",
            "aget",
            "update_by_file",
            "aupdate_by_file",
            "update_by_text",
            "aupdate_by_text",
            "delete",
            "adelete",
            "update_status",
            "aupdate_status",
            "get_batch_status",
            "aget_batch_status",
            "file_info",
            "afile_info",
        ]

        for method in methods:
            assert hasattr(document_resource, method)
            assert callable(getattr(document_resource, method))


if __name__ == "__main__":
    pytest.main([__file__])
