"""Tests for document API models."""

from io import BytesIO

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
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestCreateDocumentByFileModels:
    """Test CreateDocumentByFile API models."""

    def test_request_builder(self) -> None:
        """Test CreateDocumentByFileRequest builder pattern."""
        request_body = CreateDocumentByFileRequestBody.builder().name("test.pdf").build()
        request = CreateDocumentByFileRequest.builder().dataset_id("dataset-123").request_body(request_body).build()

        assert request.dataset_id == "dataset-123"
        assert request.request_body is not None
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/document/create-by-file"
        assert request.paths["dataset_id"] == "dataset-123"

    def test_request_validation(self) -> None:
        """Test CreateDocumentByFileRequest validation."""
        request = CreateDocumentByFileRequest.builder().dataset_id("test-dataset").build()
        assert request.dataset_id == "test-dataset"
        assert request.paths["dataset_id"] == "test-dataset"

    def test_request_body_builder(self) -> None:
        """Test CreateDocumentByFileRequestBody builder pattern."""
        request_body = (
            CreateDocumentByFileRequestBody.builder()
            .name("test.pdf")
            .indexing_technique("high_quality")
            .doc_form("text_model")
            .build()
        )

        assert request_body.name == "test.pdf"
        assert request_body.indexing_technique == "high_quality"
        assert request_body.doc_form == "text_model"

    def test_response_inheritance(self) -> None:
        """Test CreateDocumentByFileResponse inherits from BaseResponse."""
        response = CreateDocumentByFileResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test CreateDocumentByFileResponse data access."""
        doc_info = DocumentInfo(id="doc-789", name="test.pdf")
        response = CreateDocumentByFileResponse(document=doc_info, batch="batch-123")

        assert response.document is not None
        assert response.document.id == "doc-789"
        assert response.document.name == "test.pdf"
        assert response.batch == "batch-123"


class TestCreateDocumentByTextModels:
    """Test CreateDocumentByText API models."""

    def test_request_builder(self) -> None:
        """Test CreateDocumentByTextRequest builder pattern."""
        request_body = CreateDocumentByTextRequestBody.builder().name("Test Document").text("Sample text").build()
        request = CreateDocumentByTextRequest.builder().dataset_id("dataset-123").request_body(request_body).build()

        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/document/create-by-text"
        assert request.request_body is not None

    def test_request_body_builder(self) -> None:
        """Test CreateDocumentByTextRequestBody builder pattern."""
        request_body = (
            CreateDocumentByTextRequestBody.builder()
            .name("Builder Test")
            .text("Builder text")
            .indexing_technique("high_quality")
            .doc_form("text_model")
            .doc_language("English")
            .build()
        )

        assert request_body.name == "Builder Test"
        assert request_body.text == "Builder text"
        assert request_body.indexing_technique == "high_quality"
        assert request_body.doc_form == "text_model"
        assert request_body.doc_language == "English"

    def test_response_inheritance(self) -> None:
        """Test CreateDocumentByTextResponse inherits from BaseResponse."""
        response = CreateDocumentByTextResponse()
        assert isinstance(response, BaseResponse)

    def test_response_data_access(self) -> None:
        """Test CreateDocumentByTextResponse data access."""
        document_info = DocumentInfo(id="doc-123", name="Test Document")
        response = CreateDocumentByTextResponse(document=document_info, batch="batch-456")

        assert response.document == document_info
        assert response.batch == "batch-456"
        assert response.document.id == "doc-123"
        assert response.document.name == "Test Document"


class TestListDocumentsModels:
    """Test ListDocuments API models."""

    def test_request_builder(self) -> None:
        """Test ListDocumentsRequest builder pattern."""
        request = ListDocumentsRequest.builder().dataset_id("dataset-123").build()

        assert request.dataset_id == "dataset-123"
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents"
        assert request.paths["dataset_id"] == "dataset-123"

    def test_request_validation(self) -> None:
        """Test ListDocumentsRequest validation."""
        request = (
            ListDocumentsRequest.builder()
            .dataset_id("test-dataset-789")
            .keyword("search-term")
            .page(2)
            .limit(50)
            .build()
        )
        assert request.dataset_id == "test-dataset-789"
        query_dict = dict(request.queries)
        assert query_dict["keyword"] == "search-term"
        assert query_dict["page"] == "2"
        assert query_dict["limit"] == "50"

    def test_response_inheritance(self) -> None:
        """Test ListDocumentsResponse inherits from BaseResponse."""
        response = ListDocumentsResponse()
        assert isinstance(response, BaseResponse)

    def test_response_data_access(self) -> None:
        """Test ListDocumentsResponse data access."""
        doc_info = DocumentInfo(id="doc-123", name="Test Document")
        response = ListDocumentsResponse(data=[doc_info], has_more=False, limit=20, total=1, page=1)

        assert response.data is not None
        assert len(response.data) == 1
        assert response.data[0].id == "doc-123"
        assert response.data[0].name == "Test Document"
        assert response.has_more is False
        assert response.limit == 20
        assert response.total == 1
        assert response.page == 1


class TestGetDocumentModels:
    """Test GetDocument API models."""

    def test_request_builder(self) -> None:
        """Test GetDocumentRequest builder pattern."""
        request = GetDocumentRequest.builder().dataset_id("dataset-123").document_id("doc-456").build()

        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"

    def test_response_inheritance(self) -> None:
        """Test GetDocumentResponse inherits from BaseResponse."""
        response = GetDocumentResponse()
        assert isinstance(response, BaseResponse)

    def test_response_data_access(self) -> None:
        """Test GetDocumentResponse data access."""
        response = GetDocumentResponse(id="doc-123", name="Test Document")
        assert response.id == "doc-123"
        assert response.name == "Test Document"


class TestUpdateDocumentByTextModels:
    """Test UpdateDocumentByText API models."""

    def test_request_builder(self) -> None:
        """Test UpdateDocumentByTextRequest builder pattern."""
        request_body = (
            UpdateDocumentByTextRequestBody.builder().name("Updated Document").text("Updated content").build()
        )
        request = (
            UpdateDocumentByTextRequest.builder()
            .dataset_id("dataset-123")
            .document_id("doc-456")
            .request_body(request_body)
            .build()
        )

        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.request_body is not None
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/update-by-text"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"

    def test_response_inheritance(self) -> None:
        """Test UpdateDocumentByTextResponse inherits from BaseResponse."""
        response = UpdateDocumentByTextResponse()
        assert isinstance(response, BaseResponse)


class TestUpdateDocumentByFileModels:
    """Test UpdateDocumentByFile API models."""

    def test_request_builder(self) -> None:
        """Test UpdateDocumentByFileRequest builder pattern."""
        request_body = UpdateDocumentByFileRequestBody.builder().name("Updated File Document").build()
        file_content = BytesIO(b"test file content")

        request = (
            UpdateDocumentByFileRequest.builder()
            .dataset_id("dataset-123")
            .document_id("doc-456")
            .request_body(request_body)
            .file(file_content, "updated_file.pdf")
            .build()
        )

        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.request_body is not None
        assert request.file is not None
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/update-by-file"

    def test_response_inheritance(self) -> None:
        """Test UpdateDocumentByFileResponse inherits from BaseResponse."""
        response = UpdateDocumentByFileResponse()
        assert isinstance(response, BaseResponse)


class TestDeleteDocumentModels:
    """Test DeleteDocument API models."""

    def test_request_builder(self) -> None:
        """Test DeleteDocumentRequest builder pattern."""
        request = DeleteDocumentRequest.builder().dataset_id("dataset-123").document_id("doc-456").build()

        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"

    def test_response_inheritance(self) -> None:
        """Test DeleteDocumentResponse inherits from BaseResponse."""
        response = DeleteDocumentResponse()
        assert isinstance(response, BaseResponse)


class TestUpdateDocumentStatusModels:
    """Test UpdateDocumentStatus API models."""

    def test_request_builder(self) -> None:
        """Test UpdateDocumentStatusRequest builder pattern."""
        request_body = UpdateDocumentStatusRequestBody.builder().document_ids(["doc-123", "doc-456"]).build()
        request = (
            UpdateDocumentStatusRequest.builder()
            .dataset_id("dataset-123")
            .action("enable")
            .request_body(request_body)
            .build()
        )

        assert request.dataset_id == "dataset-123"
        assert request.action == "enable"
        assert request.request_body is not None
        assert request.request_body.document_ids == ["doc-123", "doc-456"]
        assert request.http_method == HttpMethod.PATCH
        assert request.uri == "/v1/datasets/:dataset_id/documents/status/:action"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["action"] == "enable"

    def test_response_inheritance(self) -> None:
        """Test UpdateDocumentStatusResponse inherits from BaseResponse."""
        response = UpdateDocumentStatusResponse()
        assert isinstance(response, BaseResponse)


class TestGetBatchIndexingStatusModels:
    """Test GetBatchIndexingStatus API models."""

    def test_request_builder(self) -> None:
        """Test GetBatchIndexingStatusRequest builder pattern."""
        request = GetBatchIndexingStatusRequest.builder().dataset_id("dataset-123").batch("batch-456").build()

        assert request.dataset_id == "dataset-123"
        assert request.batch == "batch-456"
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents/:batch/indexing-status"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["batch"] == "batch-456"

    def test_response_inheritance(self) -> None:
        """Test GetBatchIndexingStatusResponse inherits from BaseResponse."""
        response = GetBatchIndexingStatusResponse()
        assert isinstance(response, BaseResponse)


class TestGetUploadFileInfoModels:
    """Test GetUploadFileInfo API models."""

    def test_request_builder(self) -> None:
        """Test GetUploadFileInfoRequest builder pattern."""
        request = GetUploadFileInfoRequest.builder().dataset_id("dataset-123").document_id("doc-456").build()

        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/upload-file"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"

    def test_response_inheritance(self) -> None:
        """Test GetUploadFileInfoResponse inherits from BaseResponse."""
        response = GetUploadFileInfoResponse()
        assert isinstance(response, BaseResponse)

    def test_response_data_access(self) -> None:
        """Test GetUploadFileInfoResponse data access."""
        response = GetUploadFileInfoResponse(
            id="file-123",
            name="test.pdf",
            size=2048,
            extension="pdf",
            mime_type="application/pdf",
            created_by="user-123",
            created_at=1681623639,
        )

        assert response.id == "file-123"
        assert response.name == "test.pdf"
        assert response.size == 2048
        assert response.extension == "pdf"
        assert response.mime_type == "application/pdf"
        assert response.created_by == "user-123"
        assert response.created_at == 1681623639
