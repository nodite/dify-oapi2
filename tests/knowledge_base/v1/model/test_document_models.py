"""Tests for shared document models."""

from dify_oapi.api.knowledge_base.v1.model.document.create_by_text_request import CreateByTextRequest
from dify_oapi.api.knowledge_base.v1.model.document.create_by_text_request_body import CreateByTextRequestBody
from dify_oapi.api.knowledge_base.v1.model.document.create_by_text_response import CreateByTextResponse
from dify_oapi.api.knowledge_base.v1.model.document.data_source_info import DataSourceInfo
from dify_oapi.api.knowledge_base.v1.model.document.document_info import DocumentInfo
from dify_oapi.api.knowledge_base.v1.model.document.indexing_status_info import IndexingStatusInfo
from dify_oapi.api.knowledge_base.v1.model.document.pre_processing_rule import PreProcessingRule
from dify_oapi.api.knowledge_base.v1.model.document.process_rule import ProcessRule
from dify_oapi.api.knowledge_base.v1.model.document.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge_base.v1.model.document.segmentation import Segmentation
from dify_oapi.api.knowledge_base.v1.model.document.subchunk_segmentation import SubchunkSegmentation
from dify_oapi.api.knowledge_base.v1.model.document.upload_file_info import UploadFileInfo
from dify_oapi.core.enum import HttpMethod

# ===== SHARED DOCUMENT MODELS TESTS =====


def test_document_info_creation() -> None:
    """Test DocumentInfo model creation and field assignment."""
    doc_info = DocumentInfo(
        id="doc-123", name="Test Document", indexing_status="completed", enabled=True, word_count=1000
    )

    assert doc_info.id == "doc-123"
    assert doc_info.name == "Test Document"
    assert doc_info.indexing_status == "completed"
    assert doc_info.enabled is True
    assert doc_info.word_count == 1000


def test_document_info_builder_pattern() -> None:
    """Test DocumentInfo builder pattern functionality."""
    doc_info = (
        DocumentInfo.builder()
        .id("doc-456")
        .name("Builder Test")
        .indexing_status("waiting")
        .enabled(False)
        .word_count(500)
        .build()
    )

    assert doc_info.id == "doc-456"
    assert doc_info.name == "Builder Test"
    assert doc_info.indexing_status == "waiting"
    assert doc_info.enabled is False
    assert doc_info.word_count == 500


def test_document_info_optional_fields() -> None:
    """Test DocumentInfo with None values."""
    doc_info = DocumentInfo()

    assert doc_info.id is None
    assert doc_info.name is None
    assert doc_info.indexing_status is None
    assert doc_info.enabled is None
    assert doc_info.word_count is None


def test_process_rule_creation() -> None:
    """Test ProcessRule model creation."""
    process_rule = ProcessRule(mode="automatic", rules={"key": "value"})

    assert process_rule.mode == "automatic"
    assert process_rule.rules == {"key": "value"}


def test_process_rule_builder_pattern() -> None:
    """Test ProcessRule builder pattern."""
    process_rule = ProcessRule.builder().mode("custom").rules({"custom": "rule"}).build()

    assert process_rule.mode == "custom"
    assert process_rule.rules == {"custom": "rule"}


def test_pre_processing_rule_creation() -> None:
    """Test PreProcessingRule model creation."""
    pre_rule = PreProcessingRule(id="remove_extra_spaces", enabled=True)

    assert pre_rule.id == "remove_extra_spaces"
    assert pre_rule.enabled is True


def test_pre_processing_rule_builder_pattern() -> None:
    """Test PreProcessingRule builder pattern."""
    pre_rule = PreProcessingRule.builder().id("remove_urls_emails").enabled(False).build()

    assert pre_rule.id == "remove_urls_emails"
    assert pre_rule.enabled is False


def test_segmentation_creation() -> None:
    """Test Segmentation model creation."""
    segmentation = Segmentation(separator="\n", max_tokens=1000, chunk_overlap=100)

    assert segmentation.separator == "\n"
    assert segmentation.max_tokens == 1000
    assert segmentation.chunk_overlap == 100


def test_segmentation_builder_pattern() -> None:
    """Test Segmentation builder pattern."""
    segmentation = Segmentation.builder().separator("***").max_tokens(512).chunk_overlap(50).build()

    assert segmentation.separator == "***"
    assert segmentation.max_tokens == 512
    assert segmentation.chunk_overlap == 50


def test_subchunk_segmentation_creation() -> None:
    """Test SubchunkSegmentation model creation."""
    subchunk = SubchunkSegmentation(separator="\n", max_tokens=256, chunk_overlap=25)

    assert subchunk.separator == "\n"
    assert subchunk.max_tokens == 256
    assert subchunk.chunk_overlap == 25


def test_subchunk_segmentation_builder_pattern() -> None:
    """Test SubchunkSegmentation builder pattern."""
    subchunk = SubchunkSegmentation.builder().separator("---").max_tokens(128).chunk_overlap(10).build()

    assert subchunk.separator == "---"
    assert subchunk.max_tokens == 128
    assert subchunk.chunk_overlap == 10


def test_data_source_info_creation() -> None:
    """Test DataSourceInfo model creation."""
    data_source = DataSourceInfo(upload_file_id="file-123", upload_file={"name": "test.txt"})

    assert data_source.upload_file_id == "file-123"
    assert data_source.upload_file == {"name": "test.txt"}


def test_data_source_info_builder_pattern() -> None:
    """Test DataSourceInfo builder pattern."""
    data_source = DataSourceInfo.builder().upload_file_id("file-456").upload_file({"size": 1024}).build()

    assert data_source.upload_file_id == "file-456"
    assert data_source.upload_file == {"size": 1024}


def test_upload_file_info_creation() -> None:
    """Test UploadFileInfo model creation."""
    file_info = UploadFileInfo(
        id="file-789", name="document.pdf", size=2048, extension="pdf", mime_type="application/pdf"
    )

    assert file_info.id == "file-789"
    assert file_info.name == "document.pdf"
    assert file_info.size == 2048
    assert file_info.extension == "pdf"
    assert file_info.mime_type == "application/pdf"


def test_upload_file_info_builder_pattern() -> None:
    """Test UploadFileInfo builder pattern."""
    file_info = (
        UploadFileInfo.builder()
        .id("file-101")
        .name("test.docx")
        .size(4096)
        .extension("docx")
        .mime_type("application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        .build()
    )

    assert file_info.id == "file-101"
    assert file_info.name == "test.docx"
    assert file_info.size == 4096
    assert file_info.extension == "docx"
    assert file_info.mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"


def test_indexing_status_info_creation() -> None:
    """Test IndexingStatusInfo model creation."""
    status_info = IndexingStatusInfo(
        id="status-123", indexing_status="indexing", completed_segments=24, total_segments=100
    )

    assert status_info.id == "status-123"
    assert status_info.indexing_status == "indexing"
    assert status_info.completed_segments == 24
    assert status_info.total_segments == 100


def test_indexing_status_info_builder_pattern() -> None:
    """Test IndexingStatusInfo builder pattern."""
    status_info = (
        IndexingStatusInfo.builder()
        .id("status-456")
        .indexing_status("completed")
        .completed_segments(100)
        .total_segments(100)
        .build()
    )

    assert status_info.id == "status-456"
    assert status_info.indexing_status == "completed"
    assert status_info.completed_segments == 100
    assert status_info.total_segments == 100


def test_retrieval_model_creation() -> None:
    """Test RetrievalModel model creation."""
    retrieval_model = RetrievalModel(
        search_method="hybrid_search",
        reranking_enable=True,
        top_k=10,
        score_threshold_enabled=True,
        score_threshold=0.5,
    )

    assert retrieval_model.search_method == "hybrid_search"
    assert retrieval_model.reranking_enable is True
    assert retrieval_model.top_k == 10
    assert retrieval_model.score_threshold_enabled is True
    assert retrieval_model.score_threshold == 0.5


def test_retrieval_model_builder_pattern() -> None:
    """Test RetrievalModel builder pattern."""
    retrieval_model = (
        RetrievalModel.builder()
        .search_method("semantic_search")
        .reranking_enable(False)
        .top_k(5)
        .score_threshold_enabled(False)
        .build()
    )

    assert retrieval_model.search_method == "semantic_search"
    assert retrieval_model.reranking_enable is False
    assert retrieval_model.top_k == 5
    assert retrieval_model.score_threshold_enabled is False


def test_model_serialization() -> None:
    """Test model serialization and deserialization."""
    doc_info = DocumentInfo(id="doc-serialize", name="Serialization Test", enabled=True)

    # Test serialization
    data = doc_info.model_dump()
    assert data["id"] == "doc-serialize"
    assert data["name"] == "Serialization Test"
    assert data["enabled"] is True

    # Test deserialization
    new_doc_info = DocumentInfo(**data)
    assert new_doc_info.id == "doc-serialize"
    assert new_doc_info.name == "Serialization Test"
    assert new_doc_info.enabled is True


def test_builder_method_chaining() -> None:
    """Test that builder methods return the builder instance for chaining."""
    builder = DocumentInfo.builder()

    # Test that each method returns the builder instance
    assert builder.id("test") is builder
    assert builder.name("test") is builder
    assert builder.enabled(True) is builder

    # Test final build
    doc_info = builder.build()
    assert isinstance(doc_info, DocumentInfo)
    assert doc_info.id == "test"
    assert doc_info.name == "test"
    assert doc_info.enabled is True


def test_edge_cases_and_validation() -> None:
    """Test edge cases and validation scenarios."""
    # Test empty models
    empty_doc = DocumentInfo()
    assert empty_doc.id is None

    # Test with complex nested data
    data_source = DataSourceInfo(upload_file={"nested": {"data": "value"}})
    assert data_source.upload_file["nested"]["data"] == "value"

    # Test numeric edge cases
    file_info = UploadFileInfo(size=0)
    assert file_info.size == 0

    # Test float values
    status_info = IndexingStatusInfo(processing_started_at=1681623462.0, completed_at=1681623500.5)
    assert status_info.processing_started_at == 1681623462.0
    assert status_info.completed_at == 1681623500.5


# ===== CREATE BY TEXT API MODELS TESTS =====


def test_create_by_text_request_builder() -> None:
    """Test CreateByTextRequest builder pattern."""
    request = (
        CreateByTextRequest.builder()
        .dataset_id("dataset-123")
        .request_body(CreateByTextRequestBody(name="Test Document", text="Sample text"))
        .build()
    )

    assert request.dataset_id == "dataset-123"
    assert request.paths["dataset_id"] == "dataset-123"
    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/datasets/:dataset_id/document/create-by-text"
    assert request.request_body is not None
    assert request.body is not None


def test_create_by_text_request_body_validation() -> None:
    """Test CreateByTextRequestBody validation and builder."""
    # Test direct creation
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

    # Test builder pattern
    builder_body = (
        CreateByTextRequestBody.builder()
        .name("Builder Test")
        .text("Builder text")
        .indexing_technique("economy")
        .doc_form("qa_model")
        .doc_language("Chinese")
        .build()
    )

    assert builder_body.name == "Builder Test"
    assert builder_body.text == "Builder text"
    assert builder_body.indexing_technique == "economy"
    assert builder_body.doc_form == "qa_model"
    assert builder_body.doc_language == "Chinese"


def test_create_by_text_request_body_with_complex_fields() -> None:
    """Test CreateByTextRequestBody with complex nested fields."""
    process_rule = ProcessRule(mode="custom", rules={"key": "value"})
    retrieval_model = RetrievalModel(search_method="hybrid_search", top_k=10)

    request_body = (
        CreateByTextRequestBody.builder()
        .name("Complex Test")
        .text("Complex text")
        .process_rule(process_rule)
        .retrieval_model(retrieval_model)
        .embedding_model("text-embedding-ada-002")
        .embedding_model_provider("openai")
        .build()
    )

    assert request_body.name == "Complex Test"
    assert request_body.text == "Complex text"
    assert request_body.process_rule == process_rule
    assert request_body.retrieval_model == retrieval_model
    assert request_body.embedding_model == "text-embedding-ada-002"
    assert request_body.embedding_model_provider == "openai"


def test_create_by_text_response_model() -> None:
    """Test CreateByTextResponse model."""
    document_info = DocumentInfo(id="doc-123", name="Test Document", indexing_status="waiting")
    response = CreateByTextResponse(document=document_info, batch="batch-456")

    assert response.document == document_info
    assert response.batch == "batch-456"
    assert response.document.id == "doc-123"
    assert response.document.name == "Test Document"
    assert response.document.indexing_status == "waiting"


def test_create_by_text_request_path_parameter_handling() -> None:
    """Test path parameter handling in CreateByTextRequest."""
    request = CreateByTextRequest.builder().dataset_id("test-dataset-id").build()

    assert request.dataset_id == "test-dataset-id"
    assert request.paths["dataset_id"] == "test-dataset-id"


def test_create_by_text_request_body_serialization() -> None:
    """Test request body serialization."""
    request_body = CreateByTextRequestBody(
        name="Serialization Test", text="Test content", indexing_technique="high_quality"
    )

    request = CreateByTextRequest.builder().dataset_id("dataset-123").request_body(request_body).build()

    assert request.body is not None
    assert isinstance(request.body, dict)
    assert request.body["name"] == "Serialization Test"
    assert request.body["text"] == "Test content"
    assert request.body["indexing_technique"] == "high_quality"


def test_create_by_text_builder_method_chaining() -> None:
    """Test builder method chaining for CreateByTextRequestBody."""
    builder = CreateByTextRequestBody.builder()

    # Test that each method returns the builder instance
    assert builder.name("test") is builder
    assert builder.text("test") is builder
    assert builder.indexing_technique("high_quality") is builder
    assert builder.doc_form("text_model") is builder
    assert builder.doc_language("English") is builder

    # Test final build
    request_body = builder.build()
    assert isinstance(request_body, CreateByTextRequestBody)
    assert request_body.name == "test"
    assert request_body.text == "test"
    assert request_body.indexing_technique == "high_quality"
    assert request_body.doc_form == "text_model"
    assert request_body.doc_language == "English"
