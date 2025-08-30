"""Integration tests for Document API functionality."""

from __future__ import annotations

from unittest.mock import Mock, patch

from dify_oapi.api.knowledge.v1.model.create_document_by_file_request import (
    CreateDocumentByFileRequest as CreateByFileRequest,
)
from dify_oapi.api.knowledge.v1.model.create_document_by_file_request_body import (
    CreateDocumentByFileRequestBody as CreateByFileRequestBody,
)
from dify_oapi.api.knowledge.v1.model.create_document_by_file_response import (
    CreateDocumentByFileResponse as CreateByFileResponse,
)
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import (
    CreateDocumentByTextRequest as CreateByTextRequest,
)
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import (
    CreateDocumentByTextRequestBody as CreateByTextRequestBody,
)
from dify_oapi.api.knowledge.v1.model.create_document_by_text_response import (
    CreateDocumentByTextResponse as CreateByTextResponse,
)
from dify_oapi.api.knowledge.v1.model.delete_document_request import DeleteDocumentRequest as DeleteRequest
from dify_oapi.api.knowledge.v1.model.delete_document_response import DeleteDocumentResponse as DeleteResponse
from dify_oapi.api.knowledge.v1.model.document_info import DocumentInfo
from dify_oapi.api.knowledge.v1.model.get_document_request import GetDocumentRequest as GetRequest
from dify_oapi.api.knowledge.v1.model.get_document_response import GetDocumentResponse as GetResponse
from dify_oapi.api.knowledge.v1.model.get_upload_file_info_request import (
    GetUploadFileInfoRequest as GetUploadFileRequest,
)
from dify_oapi.api.knowledge.v1.model.get_upload_file_info_response import (
    GetUploadFileInfoResponse as GetUploadFileResponse,
)
from dify_oapi.api.knowledge.v1.resource.document import Document
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestDocumentAPIIntegration:
    """Integration tests for Document API functionality."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.config = Config()
        self.document = Document(self.config)
        self.request_option = RequestOption.builder().api_key("test-api-key").build()
        self.dataset_id = "test-dataset-id"
        self.document_id = "test-document-id"
        self.batch_id = "test-batch-id"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_complete_document_lifecycle_sync(self, mock_execute: Mock) -> None:
        """Test complete document lifecycle with sync operations."""
        # Mock responses for each step
        create_response = CreateByTextResponse(
            document=DocumentInfo(id=self.document_id, name="Test Document"), batch=self.batch_id
        )
        get_response = GetResponse(id=self.document_id, name="Test Document")
        delete_response = DeleteResponse()

        mock_execute.side_effect = [create_response, get_response, delete_response]

        # 1. Create document by text
        create_request = (
            CreateByTextRequest.builder()
            .dataset_id(self.dataset_id)
            .request_body(CreateByTextRequestBody.builder().name("Test Document").text("Test content").build())
            .build()
        )
        result = self.document.create_by_text(create_request, self.request_option)
        assert result.document.id == self.document_id

        # 2. Get document details
        get_request = GetRequest.builder().dataset_id(self.dataset_id).document_id(self.document_id).build()
        result = self.document.get(get_request, self.request_option)
        assert result.id == self.document_id

        # 3. Delete document
        delete_request = DeleteRequest.builder().dataset_id(self.dataset_id).document_id(self.document_id).build()
        self.document.delete(delete_request, self.request_option)

        assert mock_execute.call_count == 3

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_file_operations_sync(self, mock_execute: Mock) -> None:
        """Test file operations with sync methods."""
        # Mock responses
        create_response = CreateByFileResponse(
            document=DocumentInfo(id=self.document_id, name="Test File"), batch=self.batch_id
        )
        upload_file_response = GetUploadFileResponse(id="file-id", name="test.pdf", size=1024, extension="pdf")

        mock_execute.side_effect = [create_response, upload_file_response]

        # 1. Create document by file
        create_request = (
            CreateByFileRequest.builder()
            .dataset_id(self.dataset_id)
            .request_body(CreateByFileRequestBody.builder().file("test.pdf").build())
            .build()
        )
        result = self.document.create_by_file(create_request, self.request_option)
        assert result.document.name == "Test File"

        # 2. Get upload file information
        upload_file_request = (
            GetUploadFileRequest.builder().dataset_id(self.dataset_id).document_id(self.document_id).build()
        )
        result = self.document.get_upload_file(upload_file_request, self.request_option)
        assert result.extension == "pdf"

        assert mock_execute.call_count == 2
