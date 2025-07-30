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


# ===== CREATE BY FILE API MODELS TESTS =====


def test_create_by_file_request_builder() -> None:
    """Test CreateByFileRequest builder pattern."""
    from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_request import CreateByFileRequest
    from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_request_body import CreateByFileRequestBody
    from dify_oapi.core.enum import HttpMethod

    request_body = CreateByFileRequestBody.builder().file("test.pdf").indexing_technique("high_quality").build()

    request = CreateByFileRequest.builder().dataset_id("dataset-123").request_body(request_body).build()

    assert request.dataset_id == "dataset-123"
    assert request.request_body is not None
    assert request.request_body.file == "test.pdf"
    assert request.request_body.indexing_technique == "high_quality"
    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/datasets/:dataset_id/document/create-by-file"
    assert request.paths["dataset_id"] == "dataset-123"


def test_create_by_file_request_body_validation() -> None:
    """Test CreateByFileRequestBody validation and builder."""
    from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_request_body import CreateByFileRequestBody
    from dify_oapi.api.knowledge_base.v1.model.document.process_rule import ProcessRule
    from dify_oapi.api.knowledge_base.v1.model.document.retrieval_model import RetrievalModel

    process_rule = ProcessRule.builder().mode("automatic").build()
    retrieval_model = RetrievalModel.builder().search_method("hybrid_search").top_k(10).build()

    request_body = (
        CreateByFileRequestBody.builder()
        .data('{"name": "test.pdf"}')
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

    assert request_body.data == '{"name": "test.pdf"}'
    assert request_body.file == "test.pdf"
    assert request_body.original_document_id == "doc-456"
    assert request_body.indexing_technique == "high_quality"
    assert request_body.doc_form == "text_model"
    assert request_body.doc_language == "English"
    assert request_body.process_rule is not None
    assert request_body.process_rule.mode == "automatic"
    assert request_body.retrieval_model is not None
    assert request_body.retrieval_model.search_method == "hybrid_search"
    assert request_body.embedding_model == "text-embedding-ada-002"
    assert request_body.embedding_model_provider == "openai"


def test_create_by_file_request_body_optional_fields() -> None:
    """Test CreateByFileRequestBody with optional fields."""
    from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_request_body import CreateByFileRequestBody

    request_body = CreateByFileRequestBody.builder().file("test.pdf").build()

    assert request_body.file == "test.pdf"
    assert request_body.data is None
    assert request_body.original_document_id is None
    assert request_body.indexing_technique is None
    assert request_body.doc_form is None
    assert request_body.doc_language is None
    assert request_body.process_rule is None
    assert request_body.retrieval_model is None
    assert request_body.embedding_model is None
    assert request_body.embedding_model_provider is None


def test_create_by_file_response_model() -> None:
    """Test CreateByFileResponse model."""
    from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_response import CreateByFileResponse
    from dify_oapi.api.knowledge_base.v1.model.document.document_info import DocumentInfo

    doc_info = DocumentInfo.builder().id("doc-789").name("test.pdf").enabled(True).build()
    response = CreateByFileResponse(document=doc_info, batch="batch-123")

    assert response.document is not None
    assert response.document.id == "doc-789"
    assert response.document.name == "test.pdf"
    assert response.document.enabled is True
    assert response.batch == "batch-123"


def test_create_by_file_multipart_handling() -> None:
    """Test multipart/form-data handling in CreateByFileRequestBody."""
    from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_request_body import CreateByFileRequestBody

    # Test with multipart data field
    request_body = (
        CreateByFileRequestBody.builder()
        .data('{"indexing_technique": "high_quality", "doc_form": "text_model"}')
        .file("/path/to/document.pdf")
        .build()
    )

    assert request_body.data == '{"indexing_technique": "high_quality", "doc_form": "text_model"}'
    assert request_body.file == "/path/to/document.pdf"


def test_create_by_file_original_document_id_handling() -> None:
    """Test original_document_id handling for document updates."""
    from dify_oapi.api.knowledge_base.v1.model.document.create_by_file_request_body import CreateByFileRequestBody

    # Test update scenario with original_document_id
    request_body = (
        CreateByFileRequestBody.builder()
        .file("updated_document.pdf")
        .original_document_id("original-doc-123")
        .indexing_technique("economy")
        .build()
    )

    assert request_body.file == "updated_document.pdf"
    assert request_body.original_document_id == "original-doc-123"
    assert request_body.indexing_technique == "economy"


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


# ===== UPDATE BY TEXT API MODELS TESTS =====


def test_update_by_text_request_builder() -> None:
    """Test UpdateByTextRequest builder pattern."""
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_request import UpdateByTextRequest
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_request_body import UpdateByTextRequestBody
    from dify_oapi.core.enum import HttpMethod

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
    assert request.request_body.name == "Updated Document"
    assert request.request_body.text == "Updated content"
    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/update-by-text"
    assert request.paths["dataset_id"] == "dataset-123"
    assert request.paths["document_id"] == "doc-456"


def test_update_by_text_request_body_validation() -> None:
    """Test UpdateByTextRequestBody validation and builder."""
    from dify_oapi.api.knowledge_base.v1.model.document.process_rule import ProcessRule
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_request_body import UpdateByTextRequestBody

    process_rule = ProcessRule.builder().mode("custom").rules({"key": "value"}).build()

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
    assert request_body.process_rule.rules == {"key": "value"}


def test_update_by_text_request_body_optional_fields() -> None:
    """Test UpdateByTextRequestBody with optional fields."""
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_request_body import UpdateByTextRequestBody

    # Test with minimal fields
    request_body = UpdateByTextRequestBody.builder().name("Minimal Update").build()

    assert request_body.name == "Minimal Update"
    assert request_body.text is None
    assert request_body.process_rule is None

    # Test with only text
    text_only_body = UpdateByTextRequestBody.builder().text("Only text update").build()

    assert text_only_body.name is None
    assert text_only_body.text == "Only text update"
    assert text_only_body.process_rule is None


def test_update_by_text_response_model() -> None:
    """Test UpdateByTextResponse model."""
    from dify_oapi.api.knowledge_base.v1.model.document.document_info import DocumentInfo
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_response import UpdateByTextResponse

    doc_info = DocumentInfo.builder().id("doc-updated").name("Updated Document").enabled(True).build()
    response = UpdateByTextResponse(document=doc_info, batch="batch-update-123")

    assert response.document is not None
    assert response.document.id == "doc-updated"
    assert response.document.name == "Updated Document"
    assert response.document.enabled is True
    assert response.batch == "batch-update-123"


def test_update_by_text_dual_path_parameters() -> None:
    """Test dual path parameter handling in UpdateByTextRequest."""
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_request import UpdateByTextRequest

    request = UpdateByTextRequest.builder().dataset_id("test-dataset-789").document_id("test-document-101").build()

    assert request.dataset_id == "test-dataset-789"
    assert request.document_id == "test-document-101"
    assert request.paths["dataset_id"] == "test-dataset-789"
    assert request.paths["document_id"] == "test-document-101"


def test_update_by_text_builder_method_chaining() -> None:
    """Test builder method chaining for UpdateByTextRequestBody."""
    from dify_oapi.api.knowledge_base.v1.model.document.process_rule import ProcessRule
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_text_request_body import UpdateByTextRequestBody

    builder = UpdateByTextRequestBody.builder()
    process_rule = ProcessRule.builder().mode("automatic").build()

    # Test that each method returns the builder instance
    assert builder.name("test") is builder
    assert builder.text("test content") is builder
    assert builder.process_rule(process_rule) is builder

    # Test final build
    request_body = builder.build()
    assert isinstance(request_body, UpdateByTextRequestBody)
    assert request_body.name == "test"
    assert request_body.text == "test content"
    assert request_body.process_rule == process_rule


# ===== UPDATE BY FILE API MODELS TESTS =====


def test_update_by_file_request_builder() -> None:
    """Test UpdateByFileRequest builder pattern."""
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request import UpdateByFileRequest
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request_body import UpdateByFileRequestBody
    from dify_oapi.core.enum import HttpMethod

    request_body = UpdateByFileRequestBody.builder().name("Updated File Document").file("updated_file.pdf").build()

    request = (
        UpdateByFileRequest.builder()
        .dataset_id("dataset-123")
        .document_id("doc-456")
        .request_body(request_body)
        .build()
    )

    assert request.dataset_id == "dataset-123"
    assert request.document_id == "doc-456"
    assert request.request_body is not None
    assert request.request_body.name == "Updated File Document"
    assert request.request_body.file == "updated_file.pdf"
    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/update-by-file"
    assert request.paths["dataset_id"] == "dataset-123"
    assert request.paths["document_id"] == "doc-456"


def test_update_by_file_request_body_validation() -> None:
    """Test UpdateByFileRequestBody validation and builder."""
    from dify_oapi.api.knowledge_base.v1.model.document.process_rule import ProcessRule
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request_body import UpdateByFileRequestBody

    process_rule = ProcessRule.builder().mode("custom").rules({"key": "value"}).build()

    request_body = (
        UpdateByFileRequestBody.builder()
        .name("Updated File Test Document")
        .file("test_file.docx")
        .process_rule(process_rule)
        .build()
    )

    assert request_body.name == "Updated File Test Document"
    assert request_body.file == "test_file.docx"
    assert request_body.process_rule is not None
    assert request_body.process_rule.mode == "custom"
    assert request_body.process_rule.rules == {"key": "value"}


def test_update_by_file_request_body_optional_fields() -> None:
    """Test UpdateByFileRequestBody with optional fields."""
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request_body import UpdateByFileRequestBody

    # Test with minimal fields
    request_body = UpdateByFileRequestBody.builder().name("Minimal File Update").build()

    assert request_body.name == "Minimal File Update"
    assert request_body.file is None
    assert request_body.process_rule is None

    # Test with only file
    file_only_body = UpdateByFileRequestBody.builder().file("only_file.txt").build()

    assert file_only_body.name is None
    assert file_only_body.file == "only_file.txt"
    assert file_only_body.process_rule is None


def test_update_by_file_response_model() -> None:
    """Test UpdateByFileResponse model."""
    from dify_oapi.api.knowledge_base.v1.model.document.document_info import DocumentInfo
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_response import UpdateByFileResponse

    doc_info = DocumentInfo.builder().id("doc-file-updated").name("Updated File Document").enabled(True).build()
    response = UpdateByFileResponse(document=doc_info, batch="batch-file-update-123")

    assert response.document is not None
    assert response.document.id == "doc-file-updated"
    assert response.document.name == "Updated File Document"
    assert response.document.enabled is True
    assert response.batch == "batch-file-update-123"


def test_update_by_file_dual_path_parameters() -> None:
    """Test dual path parameter handling in UpdateByFileRequest."""
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request import UpdateByFileRequest

    request = (
        UpdateByFileRequest.builder().dataset_id("test-dataset-file-789").document_id("test-document-file-101").build()
    )

    assert request.dataset_id == "test-dataset-file-789"
    assert request.document_id == "test-document-file-101"
    assert request.paths["dataset_id"] == "test-dataset-file-789"
    assert request.paths["document_id"] == "test-document-file-101"


def test_update_by_file_builder_method_chaining() -> None:
    """Test builder method chaining for UpdateByFileRequestBody."""
    from dify_oapi.api.knowledge_base.v1.model.document.process_rule import ProcessRule
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request_body import UpdateByFileRequestBody

    builder = UpdateByFileRequestBody.builder()
    process_rule = ProcessRule.builder().mode("automatic").build()

    # Test that each method returns the builder instance
    assert builder.name("test") is builder
    assert builder.file("test_file.pdf") is builder
    assert builder.process_rule(process_rule) is builder

    # Test final build
    request_body = builder.build()
    assert isinstance(request_body, UpdateByFileRequestBody)
    assert request_body.name == "test"
    assert request_body.file == "test_file.pdf"
    assert request_body.process_rule == process_rule


def test_update_by_file_multipart_handling() -> None:
    """Test multipart/form-data handling for UpdateByFileRequestBody."""
    from dify_oapi.api.knowledge_base.v1.model.document.update_by_file_request_body import UpdateByFileRequestBody

    request_body = (
        UpdateByFileRequestBody.builder().name("Multipart Test Document").file("/path/to/test_file.pdf").build()
    )

    assert request_body.name == "Multipart Test Document"
    assert request_body.file == "/path/to/test_file.pdf"
    assert request_body.process_rule is None


# ===== INDEXING STATUS API MODELS TESTS =====


def test_indexing_status_request_builder() -> None:
    """Test IndexingStatusRequest builder pattern."""
    from dify_oapi.api.knowledge_base.v1.model.document.indexing_status_request import IndexingStatusRequest
    from dify_oapi.core.enum import HttpMethod

    request = IndexingStatusRequest.builder().dataset_id("dataset-123").batch("batch-456").build()

    assert request.dataset_id == "dataset-123"
    assert request.batch == "batch-456"
    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/datasets/:dataset_id/documents/:batch/indexing-status"
    assert request.paths["dataset_id"] == "dataset-123"
    assert request.paths["batch"] == "batch-456"


def test_indexing_status_response_model() -> None:
    """Test IndexingStatusResponse model."""
    from dify_oapi.api.knowledge_base.v1.model.document.indexing_status_info import IndexingStatusInfo
    from dify_oapi.api.knowledge_base.v1.model.document.indexing_status_response import IndexingStatusResponse

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


def test_indexing_status_batch_parameter_handling() -> None:
    """Test batch parameter handling in IndexingStatusRequest."""
    from dify_oapi.api.knowledge_base.v1.model.document.indexing_status_request import IndexingStatusRequest

    request = IndexingStatusRequest.builder().dataset_id("test-dataset-789").batch("test-batch-101").build()

    assert request.dataset_id == "test-dataset-789"
    assert request.batch == "test-batch-101"
    assert request.paths["dataset_id"] == "test-dataset-789"
    assert request.paths["batch"] == "test-batch-101"


def test_indexing_status_builder_method_chaining() -> None:
    """Test builder method chaining for IndexingStatusRequest."""
    from dify_oapi.api.knowledge_base.v1.model.document.indexing_status_request import IndexingStatusRequest

    builder = IndexingStatusRequest.builder()

    # Test that each method returns the builder instance
    assert builder.dataset_id("test") is builder
    assert builder.batch("test-batch") is builder

    # Test final build
    request = builder.build()
    assert isinstance(request, IndexingStatusRequest)
    assert request.dataset_id == "test"
    assert request.batch == "test-batch"


# ===== DELETE API MODELS TESTS =====


def test_delete_request_builder() -> None:
    """Test DeleteRequest builder pattern."""
    from dify_oapi.api.knowledge_base.v1.model.document.delete_request import DeleteRequest
    from dify_oapi.core.enum import HttpMethod

    request = DeleteRequest.builder().dataset_id("dataset-123").document_id("doc-456").build()

    assert request.dataset_id == "dataset-123"
    assert request.document_id == "doc-456"
    assert request.http_method == HttpMethod.DELETE
    assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id"
    assert request.paths["dataset_id"] == "dataset-123"
    assert request.paths["document_id"] == "doc-456"


def test_delete_response_model() -> None:
    """Test DeleteResponse model for 204 No Content."""
    from dify_oapi.api.knowledge_base.v1.model.document.delete_response import DeleteResponse

    response = DeleteResponse()

    # Test that response is empty (204 No Content)
    assert response.model_dump() == {}


def test_delete_dual_path_parameters() -> None:
    """Test dual path parameter handling in DeleteRequest."""
    from dify_oapi.api.knowledge_base.v1.model.document.delete_request import DeleteRequest

    request = DeleteRequest.builder().dataset_id("test-dataset-delete").document_id("test-document-delete").build()

    assert request.dataset_id == "test-dataset-delete"
    assert request.document_id == "test-document-delete"
    assert request.paths["dataset_id"] == "test-dataset-delete"
    assert request.paths["document_id"] == "test-document-delete"


def test_delete_builder_method_chaining() -> None:
    """Test builder method chaining for DeleteRequest."""
    from dify_oapi.api.knowledge_base.v1.model.document.delete_request import DeleteRequest

    builder = DeleteRequest.builder()

    # Test that each method returns the builder instance
    assert builder.dataset_id("test") is builder
    assert builder.document_id("test-doc") is builder

    # Test final build
    request = builder.build()
    assert isinstance(request, DeleteRequest)
    assert request.dataset_id == "test"
    assert request.document_id == "test-doc"


def test_delete_http_method_configuration() -> None:
    """Test DELETE method configuration in DeleteRequest."""
    from dify_oapi.api.knowledge_base.v1.model.document.delete_request import DeleteRequest
    from dify_oapi.core.enum import HttpMethod

    request = DeleteRequest.builder().dataset_id("dataset-test").document_id("doc-test").build()

    assert request.http_method == HttpMethod.DELETE
    assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id"
