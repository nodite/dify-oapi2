"""Integration tests for Document API functionality."""

from typing import Any
from unittest.mock import Mock

import pytest

from dify_oapi.api.knowledge.v1.model.create_document_by_file_request import CreateDocumentByFileRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_file_request_body import CreateDocumentByFileRequestBody
from dify_oapi.api.knowledge.v1.model.create_document_by_file_response import CreateDocumentByFileResponse
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import CreateDocumentByTextRequestBody
from dify_oapi.api.knowledge.v1.model.create_document_by_text_response import CreateDocumentByTextResponse
from dify_oapi.api.knowledge.v1.model.delete_document_request import DeleteDocumentRequest
from dify_oapi.api.knowledge.v1.model.delete_document_response import DeleteDocumentResponse
from dify_oapi.api.knowledge.v1.model.document_info import DocumentInfo
from dify_oapi.api.knowledge.v1.model.get_batch_indexing_status_request import GetBatchIndexingStatusRequest
from dify_oapi.api.knowledge.v1.model.get_batch_indexing_status_response import GetBatchIndexingStatusResponse
from dify_oapi.api.knowledge.v1.model.get_document_request import GetDocumentRequest
from dify_oapi.api.knowledge.v1.model.get_document_response import GetDocumentResponse
from dify_oapi.api.knowledge.v1.model.get_upload_file_info_request import GetUploadFileInfoRequest
from dify_oapi.api.knowledge.v1.model.get_upload_file_info_response import GetUploadFileInfoResponse
from dify_oapi.api.knowledge.v1.model.list_documents_request import ListDocumentsRequest
from dify_oapi.api.knowledge.v1.model.list_documents_response import ListDocumentsResponse
from dify_oapi.api.knowledge.v1.model.update_document_by_file_request import UpdateDocumentByFileRequest
from dify_oapi.api.knowledge.v1.model.update_document_by_file_request_body import UpdateDocumentByFileRequestBody
from dify_oapi.api.knowledge.v1.model.update_document_by_file_response import UpdateDocumentByFileResponse
from dify_oapi.api.knowledge.v1.model.update_document_by_text_request import UpdateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.update_document_by_text_request_body import UpdateDocumentByTextRequestBody
from dify_oapi.api.knowledge.v1.model.update_document_by_text_response import UpdateDocumentByTextResponse
from dify_oapi.api.knowledge.v1.model.update_document_status_request import UpdateDocumentStatusRequest
from dify_oapi.api.knowledge.v1.model.update_document_status_request_body import UpdateDocumentStatusRequestBody
from dify_oapi.api.knowledge.v1.model.update_document_status_response import UpdateDocumentStatusResponse
from dify_oapi.api.knowledge.v1.resource.document import Document
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestDocumentIntegration:
    """Test all 10 Document Resource APIs."""

    @pytest.fixture
    def document_resource(self) -> Document:
        return Document(Config())

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_create_document_by_file(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test POST /v1/datasets/{dataset_id}/document/create-by-file"""
        response = CreateDocumentByFileResponse(document=DocumentInfo(id="doc-id", name="test.pdf"), batch="batch-id")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        from io import BytesIO

        file_content = BytesIO(b"test file content")
        request_body = CreateDocumentByFileRequestBody.builder().name("test.pdf").build()
        request = (
            CreateDocumentByFileRequest.builder()
            .dataset_id("dataset-id")
            .file(file_content, "test.pdf")
            .request_body(request_body)
            .build()
        )
        result = document_resource.create_by_file(request, request_option)

        assert result.document.id == "doc-id"
        assert result.batch == "batch-id"

    def test_create_document_by_text(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test POST /v1/datasets/{dataset_id}/document/create-by-text"""
        response = CreateDocumentByTextResponse(
            document=DocumentInfo(id="doc-id", name="Text Document"), batch="batch-id"
        )
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateDocumentByTextRequestBody.builder().name("Text Document").text("Document content").build()
        request = CreateDocumentByTextRequest.builder().dataset_id("dataset-id").request_body(request_body).build()
        result = document_resource.create_by_text(request, request_option)

        assert result.document.id == "doc-id"

    def test_list_documents(self, document_resource: Document, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents"""
        response = ListDocumentsResponse(data=[], has_more=False, limit=20, total=0, page=1)
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListDocumentsRequest.builder().dataset_id("dataset-id").build()
        result = document_resource.list(request, request_option)

        assert result.total == 0

    def test_get_document(self, document_resource: Document, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents/{document_id}"""
        response = GetDocumentResponse(id="doc-id", name="Test Document")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetDocumentRequest.builder().dataset_id("dataset-id").document_id("doc-id").build()
        result = document_resource.get(request, request_option)

        assert result.id == "doc-id"

    def test_update_document_by_file(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test POST /v1/datasets/{dataset_id}/documents/{document_id}/update-by-file"""
        response = UpdateDocumentByFileResponse(
            document=DocumentInfo(id="doc-id", name="updated.pdf"), batch="batch-id"
        )
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        from io import BytesIO

        file_content = BytesIO(b"updated file content")
        request_body = UpdateDocumentByFileRequestBody.builder().name("updated.pdf").build()
        request = (
            UpdateDocumentByFileRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .file(file_content, "updated.pdf")
            .request_body(request_body)
            .build()
        )
        result = document_resource.update_by_file(request, request_option)

        assert result.document.name == "updated.pdf"

    def test_update_document_by_text(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test POST /v1/datasets/{dataset_id}/documents/{document_id}/update-by-text"""
        response = UpdateDocumentByTextResponse(
            document=DocumentInfo(id="doc-id", name="Updated Text Document"), batch="batch-id"
        )
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = (
            UpdateDocumentByTextRequestBody.builder().name("Updated Text Document").text("Updated content").build()
        )
        request = (
            UpdateDocumentByTextRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .request_body(request_body)
            .build()
        )
        result = document_resource.update_by_text(request, request_option)

        assert result.document.name == "Updated Text Document"

    def test_delete_document(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test DELETE /v1/datasets/{dataset_id}/documents/{document_id}"""
        response = DeleteDocumentResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = DeleteDocumentRequest.builder().dataset_id("dataset-id").document_id("doc-id").build()
        result = document_resource.delete(request, request_option)

        assert result.result == "success"

    def test_update_document_status(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test PATCH /v1/datasets/{dataset_id}/documents/status/{action}"""
        response = UpdateDocumentStatusResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UpdateDocumentStatusRequestBody.builder().document_ids(["doc-id"]).build()
        request = (
            UpdateDocumentStatusRequest.builder()
            .dataset_id("dataset-id")
            .action("enable")
            .request_body(request_body)
            .build()
        )
        result = document_resource.update_status(request, request_option)

        assert result.result == "success"

    def test_get_batch_indexing_status(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents/{batch}/indexing-status"""
        response = GetBatchIndexingStatusResponse(id="batch-id", indexing_status="completed")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetBatchIndexingStatusRequest.builder().dataset_id("dataset-id").batch("batch-id").build()
        result = document_resource.get_batch_status(request, request_option)

        assert result.indexing_status == "completed"

    def test_get_upload_file_info(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents/{document_id}/upload-file"""
        response = GetUploadFileInfoResponse(id="file-id", name="test.pdf", size=1024)
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetUploadFileInfoRequest.builder().dataset_id("dataset-id").document_id("doc-id").build()
        result = document_resource.file_info(request, request_option)

        assert result.name == "test.pdf"

    def test_complete_document_lifecycle_sync(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test complete document lifecycle with sync operations."""
        dataset_id = "test-dataset-id"
        document_id = "test-document-id"
        batch_id = "test-batch-id"

        # Mock responses for each step
        create_response = CreateDocumentByTextResponse(
            document=DocumentInfo(id=document_id, name="Test Document"), batch=batch_id
        )
        get_response = GetDocumentResponse(id=document_id, name="Test Document")
        delete_response = DeleteDocumentResponse(result="success")

        mock_execute = Mock()
        mock_execute.side_effect = [create_response, get_response, delete_response]
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # 1. Create document by text
        create_request = (
            CreateDocumentByTextRequest.builder()
            .dataset_id(dataset_id)
            .request_body(CreateDocumentByTextRequestBody.builder().name("Test Document").text("Test content").build())
            .build()
        )
        result = document_resource.create_by_text(create_request, request_option)
        assert result.document.id == document_id

        # 2. Get document details
        get_request = GetDocumentRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
        result = document_resource.get(get_request, request_option)
        assert result.id == document_id

        # 3. Delete document
        delete_request = DeleteDocumentRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
        document_resource.delete(delete_request, request_option)

        assert mock_execute.call_count == 3

    def test_file_operations_sync(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test file operations with sync methods."""
        dataset_id = "test-dataset-id"
        document_id = "test-document-id"
        batch_id = "test-batch-id"

        # Mock responses
        create_response = CreateDocumentByFileResponse(
            document=DocumentInfo(id=document_id, name="Test File"), batch=batch_id
        )
        upload_file_response = GetUploadFileInfoResponse(id="file-id", name="test.pdf", size=1024, extension="pdf")

        mock_execute = Mock()
        mock_execute.side_effect = [create_response, upload_file_response]
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # 1. Create document by file
        from io import BytesIO

        file_content = BytesIO(b"test file content")
        create_request = (
            CreateDocumentByFileRequest.builder()
            .dataset_id(dataset_id)
            .file(file_content, "test.pdf")
            .request_body(CreateDocumentByFileRequestBody.builder().name("test.pdf").build())
            .build()
        )
        result = document_resource.create_by_file(create_request, request_option)
        assert result.document.name == "Test File"

        # 2. Get upload file information
        upload_file_request = GetUploadFileInfoRequest.builder().dataset_id(dataset_id).document_id(document_id).build()
        result = document_resource.file_info(upload_file_request, request_option)
        assert result.extension == "pdf"

        assert mock_execute.call_count == 2
