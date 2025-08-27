"""Tests for document API models."""

from io import BytesIO

from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_request import CreateByFileRequest
from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_request_body import CreateByFileRequestBody
from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_request_body_data import CreateByFileRequestBodyData
from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_response import CreateByFileResponse
from dify_oapi.api.knowledge_base.v1.model.document.create_by_text_request import CreateByTextRequest
from dify_oapi.api.knowledge_base.v1.model.document.create_by_text_request_body import CreateByTextRequestBody
from dify_oapi.api.knowledge_base.v1.model.document.create_by_text_response import CreateByTextResponse
from dify_oapi.api.knowledge_base.v1.model.document.delete_request import DeleteRequest
from dify_oapi.api.knowledge_base.v1.model.document.delete_response import DeleteResponse
from dify_oapi.api.knowledge_base.v1.model.document.document_info import DocumentInfo
from dify_oapi.api.knowledge_base.v1.model.document.get_request import GetRequest
from dify_oapi.api.knowledge_base.v1.model.document.get_response import GetResponse
from dify_oapi.api.knowledge_base.v1.model.document.get_upload_file_request import GetUploadFileRequest
from dify_oapi.api.knowledge_base.v1.model.document.get_upload_file_response import GetUploadFileResponse
from dify_oapi.api.knowledge_base.v1.model.document.indexing_status_info import IndexingStatusInfo
from dify_oapi.api.knowledge_base.v1.model.document.indexing_status_request import IndexingStatusRequest
from dify_oapi.api.knowledge_base.v1.model.document.indexing_status_response import IndexingStatusResponse
from dify_oapi.api.knowledge_base.v1.model.document.list_request import ListRequest
from dify_oapi.api.knowledge_base.v1.model.document.list_response import ListResponse
from dify_oapi.api.knowledge_base.v1.model.document.process_rule import ProcessRule
from dify_oapi.api.knowledge_base.v1.model.document.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request import UpdateByFileRequest
from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request_body import UpdateByFileRequestBody
from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request_body_data import UpdateByFileRequestBodyData
from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_response import UpdateByFileResponse
from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_request import UpdateByTextRequest
from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_request_body import UpdateByTextRequestBody
from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_response import UpdateByTextResponse
from dify_oapi.api.knowledge_base.v1.model.document.update_status_request import UpdateStatusRequest
from dify_oapi.api.knowledge_base.v1.model.document.update_status_request_body import UpdateStatusRequestBody
from dify_oapi.api.knowledge_base.v1.model.document.update_status_response import UpdateStatusResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestCreateByFileModels:
    """Test CreateByFile API models."""

    def test_request_builder(self) -> None:
        """Test CreateByFileRequest builder pattern."""
        data = CreateByFileRequestBodyData.builder().file("test.pdf").indexing_technique("high_quality").build()
        request_body = CreateByFileRequestBody.builder().data(data).build()
        request = CreateByFileRequest.builder().dataset_id("dataset-123").request_body(request_body).build()

        assert request.dataset_id == "dataset-123"
        assert request.request_body is not None
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/document/create-by-file"
        assert request.paths["dataset_id"] == "dataset-123"

    def test_request_validation(self) -> None:
        """Test CreateByFileRequest validation."""
        request = CreateByFileRequest.builder().dataset_id("test-dataset").build()
        assert request.dataset_id == "test-dataset"
        assert request.paths["dataset_id"] == "test-dataset"

    def test_request_body_builder(self) -> None:
        """Test CreateByFileRequestBody builder pattern."""
        process_rule = ProcessRule.builder().mode("automatic").build()
        retrieval_model = RetrievalModel.builder().search_method("hybrid_search").top_k(10).build()

        data = (
            CreateByFileRequestBodyData.builder()
            .file("test.pdf")
            .original_document_id("doc-456")
            .indexing_technique("high_quality")
            .doc_form("text_model")
            .doc_language("English")
            .process_rule(process_rule)
            .retrieval_model(retrieval_model)
            .embedding_model("text-embedding-ada-002")
            .embedding_model_provider("openai")
            .build()
        )

        request_body = CreateByFileRequestBody.builder().data(data).build()
        assert request_body.data is not None

    def test_request_body_validation(self) -> None:
        """Test CreateByFileRequestBody validation."""
        data = CreateByFileRequestBodyData.builder().file("test.pdf").build()
        request_body = CreateByFileRequestBody.builder().data(data).build()
        assert request_body.data is not None

    def test_response_inheritance(self) -> None:
        """Test CreateByFileResponse inherits from BaseResponse."""
        response = CreateByFileResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test CreateByFileResponse data access."""
        doc_info = DocumentInfo.builder().id("doc-789").name("test.pdf").enabled(True).build()
        response = CreateByFileResponse(document=doc_info, batch="batch-123")

        assert response.document is not None
        assert response.document.id == "doc-789"
        assert response.document.name == "test.pdf"
        assert response.document.enabled is True
        assert response.batch == "batch-123"


class TestCreateByTextModels:
    """Test CreateByText API models."""

    def test_request_builder(self) -> None:
        """Test CreateByTextRequest builder pattern."""
        request_body = CreateByTextRequestBody(name="Test Document", text="Sample text")
        request = CreateByTextRequest.builder().dataset_id("dataset-123").request_body(request_body).build()

        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/document/create-by-text"
        assert request.request_body is not None

    def test_request_validation(self) -> None:
        """Test CreateByTextRequest validation."""
        request = CreateByTextRequest.builder().dataset_id("test-dataset-id").build()
        assert request.dataset_id == "test-dataset-id"
        assert request.paths["dataset_id"] == "test-dataset-id"

    def test_request_body_builder(self) -> None:
        """Test CreateByTextRequestBody builder pattern."""
        request_body = (
            CreateByTextRequestBody.builder()
            .name("Builder Test")
            .text("Builder text")
            .indexing_technique("economy")
            .doc_form("qa_model")
            .doc_language("Chinese")
            .build()
        )

        assert request_body.name == "Builder Test"
        assert request_body.text == "Builder text"
        assert request_body.indexing_technique == "economy"
        assert request_body.doc_form == "qa_model"
        assert request_body.doc_language == "Chinese"

    def test_request_body_validation(self) -> None:
        """Test CreateByTextRequestBody validation."""
        request_body = CreateByTextRequestBody(
            name="Test Document",
            text="Sample text content",
            indexing_technique="high_quality",
            doc_form="text_model",
            doc_language="English",
        )

        assert request_body.name == "Test Document"
        assert request_body.text == "Sample text content"
        assert request_body.indexing_technique == "high_quality"
        assert request_body.doc_form == "text_model"
        assert request_body.doc_language == "English"

    def test_response_inheritance(self) -> None:
        """Test CreateByTextResponse inherits from BaseResponse."""
        response = CreateByTextResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test CreateByTextResponse data access."""
        document_info = DocumentInfo(id="doc-123", name="Test Document", indexing_status="waiting")
        response = CreateByTextResponse(document=document_info, batch="batch-456")

        assert response.document == document_info
        assert response.batch == "batch-456"
        assert response.document.id == "doc-123"
        assert response.document.name == "Test Document"
        assert response.document.indexing_status == "waiting"


class TestUpdateByTextModels:
    """Test UpdateByText API models."""

    def test_request_builder(self) -> None:
        """Test UpdateByTextRequest builder pattern."""
        request_body = UpdateByTextRequestBody.builder().name("Updated Document").text("Updated content").build()
        request = (
            UpdateByTextRequest.builder()
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

    def test_request_validation(self) -> None:
        """Test UpdateByTextRequest validation."""
        request = UpdateByTextRequest.builder().dataset_id("test-dataset-789").document_id("test-document-101").build()
        assert request.dataset_id == "test-dataset-789"
        assert request.document_id == "test-document-101"
        assert request.paths["dataset_id"] == "test-dataset-789"
        assert request.paths["document_id"] == "test-document-101"

    def test_request_body_builder(self) -> None:
        """Test UpdateByTextRequestBody builder pattern."""
        from dify_oapi.api.knowledge_base.v1.model.document.rules import Rules

        rules = Rules.builder().build()
        process_rule = ProcessRule.builder().mode("custom").rules(rules).build()
        request_body = (
            UpdateByTextRequestBody.builder()
            .name("Updated Test Document")
            .text("This is updated text content")
            .process_rule(process_rule)
            .build()
        )

        assert request_body.name == "Updated Test Document"
        assert request_body.text == "This is updated text content"
        assert request_body.process_rule is not None
        assert request_body.process_rule.mode == "custom"

    def test_request_body_validation(self) -> None:
        """Test UpdateByTextRequestBody validation."""
        request_body = UpdateByTextRequestBody.builder().name("Minimal Update").build()
        assert request_body.name == "Minimal Update"
        assert request_body.text is None
        assert request_body.process_rule is None

    def test_response_inheritance(self) -> None:
        """Test UpdateByTextResponse inherits from BaseResponse."""
        response = UpdateByTextResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UpdateByTextResponse data access."""
        doc_info = DocumentInfo.builder().id("doc-updated").name("Updated Document").enabled(True).build()
        response = UpdateByTextResponse(document=doc_info, batch="batch-update-123")

        assert response.document is not None
        assert response.document.id == "doc-updated"
        assert response.document.name == "Updated Document"
        assert response.document.enabled is True
        assert response.batch == "batch-update-123"


class TestUpdateByFileModels:
    """Test UpdateByFile API models."""

    def test_request_builder(self) -> None:
        """Test UpdateByFileRequest builder pattern."""
        data = UpdateByFileRequestBodyData.builder().name("Updated File Document").indexing_technique("economy").build()
        request_body = UpdateByFileRequestBody.builder().data(data).build()
        file_content = BytesIO(b"test file content")

        request = (
            UpdateByFileRequest.builder()
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

    def test_request_validation(self) -> None:
        """Test UpdateByFileRequest validation."""
        request = (
            UpdateByFileRequest.builder()
            .dataset_id("test-dataset-file-789")
            .document_id("test-document-file-101")
            .build()
        )
        assert request.dataset_id == "test-dataset-file-789"
        assert request.document_id == "test-document-file-101"

    def test_request_body_builder(self) -> None:
        """Test UpdateByFileRequestBody builder pattern."""
        process_rule = ProcessRule.builder().mode("automatic").build()
        data = (
            UpdateByFileRequestBodyData.builder()
            .name("Builder Test")
            .indexing_technique("economy")
            .process_rule(process_rule)
            .build()
        )

        request_body = UpdateByFileRequestBody.builder().data(data).build()
        assert request_body.data is not None

    def test_request_body_validation(self) -> None:
        """Test UpdateByFileRequestBody validation."""
        data = UpdateByFileRequestBodyData.builder().name("Minimal File Update").build()
        request_body = UpdateByFileRequestBody.builder().data(data).build()
        assert request_body.data is not None

    def test_response_inheritance(self) -> None:
        """Test UpdateByFileResponse inherits from BaseResponse."""
        response = UpdateByFileResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UpdateByFileResponse data access."""
        doc_info = DocumentInfo.builder().id("doc-file-updated").name("Updated File Document").enabled(True).build()
        response = UpdateByFileResponse(document=doc_info, batch="batch-file-update-123")

        assert response.document is not None
        assert response.document.id == "doc-file-updated"
        assert response.document.name == "Updated File Document"
        assert response.document.enabled is True
        assert response.batch == "batch-file-update-123"


class TestIndexingStatusModels:
    """Test IndexingStatus API models."""

    def test_request_builder(self) -> None:
        """Test IndexingStatusRequest builder pattern."""
        request = IndexingStatusRequest.builder().dataset_id("dataset-123").batch("batch-456").build()

        assert request.dataset_id == "dataset-123"
        assert request.batch == "batch-456"
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents/:batch/indexing-status"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["batch"] == "batch-456"

    def test_request_validation(self) -> None:
        """Test IndexingStatusRequest validation."""
        request = IndexingStatusRequest.builder().dataset_id("test-dataset-789").batch("test-batch-101").build()
        assert request.dataset_id == "test-dataset-789"
        assert request.batch == "test-batch-101"

    def test_response_inheritance(self) -> None:
        """Test IndexingStatusResponse inherits from BaseResponse."""
        response = IndexingStatusResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test IndexingStatusResponse data access."""
        status_info = (
            IndexingStatusInfo.builder()
            .id("doc-123")
            .indexing_status("indexing")
            .completed_segments(24)
            .total_segments(100)
            .build()
        )
        response = IndexingStatusResponse(data=[status_info])

        assert response.data is not None
        assert len(response.data) == 1
        assert response.data[0].id == "doc-123"
        assert response.data[0].indexing_status == "indexing"
        assert response.data[0].completed_segments == 24
        assert response.data[0].total_segments == 100


class TestDeleteModels:
    """Test Delete API models."""

    def test_request_builder(self) -> None:
        """Test DeleteRequest builder pattern."""
        request = DeleteRequest.builder().dataset_id("dataset-123").document_id("doc-456").build()

        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"

    def test_request_validation(self) -> None:
        """Test DeleteRequest validation."""
        request = DeleteRequest.builder().dataset_id("test-dataset-delete").document_id("test-document-delete").build()
        assert request.dataset_id == "test-dataset-delete"
        assert request.document_id == "test-document-delete"

    def test_response_inheritance(self) -> None:
        """Test DeleteResponse inherits from BaseResponse."""
        response = DeleteResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test DeleteResponse data access."""
        response = DeleteResponse()
        model_data = response.model_dump()
        assert "raw" in model_data
        assert model_data["raw"] is None


class TestListModels:
    """Test List API models."""

    def test_request_builder(self) -> None:
        """Test ListRequest builder pattern."""
        request = ListRequest.builder().dataset_id("dataset-123").build()

        assert request.dataset_id == "dataset-123"
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents"
        assert request.paths["dataset_id"] == "dataset-123"

    def test_request_validation(self) -> None:
        """Test ListRequest validation."""
        request = ListRequest.builder().dataset_id("test-dataset-789").keyword("search-term").page(2).limit(50).build()
        assert request.dataset_id == "test-dataset-789"
        query_dict = dict(request.queries)
        assert query_dict["keyword"] == "search-term"
        assert query_dict["page"] == "2"
        assert query_dict["limit"] == "50"

    def test_response_inheritance(self) -> None:
        """Test ListResponse inherits from BaseResponse."""
        response = ListResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test ListResponse data access."""
        doc_info = DocumentInfo.builder().id("doc-123").name("Test Document").enabled(True).build()
        response = ListResponse(data=[doc_info], has_more=False, limit=20, total=1, page=1)

        assert response.data is not None
        assert len(response.data) == 1
        assert response.data[0].id == "doc-123"
        assert response.data[0].name == "Test Document"
        assert response.data[0].enabled is True
        assert response.has_more is False
        assert response.limit == 20
        assert response.total == 1
        assert response.page == 1


class TestGetModels:
    """Test Get API models."""

    def test_request_builder(self) -> None:
        """Test GetRequest builder pattern."""
        request = GetRequest.builder().dataset_id("dataset-123").document_id("doc-456").build()

        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"

    def test_request_validation(self) -> None:
        """Test GetRequest validation."""
        request = GetRequest.builder().dataset_id("test-dataset").document_id("test-doc").metadata("all").build()
        assert request.dataset_id == "test-dataset"
        assert request.document_id == "test-doc"
        query_dict = dict(request.queries)
        assert query_dict["metadata"] == "all"

    def test_response_inheritance(self) -> None:
        """Test GetResponse inherits from BaseResponse."""
        response = GetResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetResponse data access."""
        response = GetResponse(id="doc-123", name="Test Document", enabled=True)
        assert response.id == "doc-123"
        assert response.name == "Test Document"
        assert response.enabled is True


class TestUpdateStatusModels:
    """Test UpdateStatus API models."""

    def test_request_builder(self) -> None:
        """Test UpdateStatusRequest builder pattern."""
        request_body = UpdateStatusRequestBody.builder().document_ids(["doc-123", "doc-456"]).build()
        request = (
            UpdateStatusRequest.builder().dataset_id("dataset-123").action("enable").request_body(request_body).build()
        )

        assert request.dataset_id == "dataset-123"
        assert request.action == "enable"
        assert request.request_body is not None
        assert request.request_body.document_ids == ["doc-123", "doc-456"]
        assert request.http_method == HttpMethod.PATCH
        assert request.uri == "/v1/datasets/:dataset_id/documents/status/:action"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["action"] == "enable"

    def test_request_validation(self) -> None:
        """Test UpdateStatusRequest validation."""
        actions = ["enable", "disable", "archive", "un_archive"]
        for action in actions:
            request = UpdateStatusRequest.builder().dataset_id("test-dataset").action(action).build()
            assert request.action == action
            assert request.paths["action"] == action

    def test_request_body_builder(self) -> None:
        """Test UpdateStatusRequestBody builder pattern."""
        request_body = UpdateStatusRequestBody.builder().document_ids(["doc-1", "doc-2", "doc-3"]).build()
        assert request_body.document_ids == ["doc-1", "doc-2", "doc-3"]

    def test_request_body_validation(self) -> None:
        """Test UpdateStatusRequestBody validation."""
        request_body = UpdateStatusRequestBody.builder().document_ids([]).build()
        assert request_body.document_ids == []

    def test_response_inheritance(self) -> None:
        """Test UpdateStatusResponse inherits from BaseResponse."""
        response = UpdateStatusResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UpdateStatusResponse data access."""
        response = UpdateStatusResponse(result="success")
        assert response.result == "success"


class TestGetUploadFileModels:
    """Test GetUploadFile API models."""

    def test_request_builder(self) -> None:
        """Test GetUploadFileRequest builder pattern."""
        request = GetUploadFileRequest.builder().dataset_id("dataset-123").document_id("doc-456").build()

        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/upload-file"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"

    def test_request_validation(self) -> None:
        """Test GetUploadFileRequest validation."""
        request = (
            GetUploadFileRequest.builder().dataset_id("test-dataset-upload").document_id("test-document-upload").build()
        )
        assert request.dataset_id == "test-dataset-upload"
        assert request.document_id == "test-document-upload"

    def test_response_inheritance(self) -> None:
        """Test GetUploadFileResponse inherits from BaseResponse."""
        response = GetUploadFileResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetUploadFileResponse data access."""
        response = GetUploadFileResponse(
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
