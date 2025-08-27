"""Tests for document public models."""

from dify_oapi.api.knowledge_base.v1.model.document.data_source_info import DataSourceInfo
from dify_oapi.api.knowledge_base.v1.model.document.document_info import DocumentInfo
from dify_oapi.api.knowledge_base.v1.model.document.indexing_status_info import IndexingStatusInfo
from dify_oapi.api.knowledge_base.v1.model.document.pre_processing_rule import PreProcessingRule
from dify_oapi.api.knowledge_base.v1.model.document.process_rule import ProcessRule
from dify_oapi.api.knowledge_base.v1.model.document.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge_base.v1.model.document.rules import Rules
from dify_oapi.api.knowledge_base.v1.model.document.segmentation import Segmentation
from dify_oapi.api.knowledge_base.v1.model.document.subchunk_segmentation import SubchunkSegmentation
from dify_oapi.api.knowledge_base.v1.model.document.upload_file_info import UploadFileInfo


class TestDocumentInfo:
    """Test DocumentInfo model."""

    def test_builder_pattern(self) -> None:
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

    def test_field_validation(self) -> None:
        """Test DocumentInfo field validation."""
        doc_info = DocumentInfo(
            id="doc-123", name="Test Document", indexing_status="completed", enabled=True, word_count=1000
        )

        assert doc_info.id == "doc-123"
        assert doc_info.name == "Test Document"
        assert doc_info.indexing_status == "completed"
        assert doc_info.enabled is True
        assert doc_info.word_count == 1000

    def test_serialization(self) -> None:
        """Test DocumentInfo serialization."""
        doc_info = DocumentInfo(id="doc-serialize", name="Serialization Test", enabled=True)
        data = doc_info.model_dump()
        assert data["id"] == "doc-serialize"
        assert data["name"] == "Serialization Test"
        assert data["enabled"] is True

    def test_direct_instantiation(self) -> None:
        """Test DocumentInfo direct instantiation alongside builder."""
        direct = DocumentInfo(id="direct-123", name="Direct Test", enabled=True)
        builder = DocumentInfo.builder().id("direct-123").name("Direct Test").enabled(True).build()

        assert direct.id == builder.id
        assert direct.name == builder.name
        assert direct.enabled == builder.enabled


class TestProcessRule:
    """Test ProcessRule model."""

    def test_builder_pattern(self) -> None:
        """Test ProcessRule builder pattern functionality."""
        rules = Rules.builder().build()
        process_rule = ProcessRule.builder().mode("custom").rules(rules).build()

        assert process_rule.mode == "custom"
        assert process_rule.rules == rules

    def test_field_validation(self) -> None:
        """Test ProcessRule field validation."""
        segmentation = Segmentation.builder().separator("\n").max_tokens(1000).build()
        rules = Rules.builder().segmentation(segmentation).build()
        process_rule = ProcessRule(mode="automatic", rules=rules)

        assert process_rule.mode == "automatic"
        assert process_rule.rules == rules
        assert process_rule.rules.segmentation == segmentation

    def test_serialization(self) -> None:
        """Test ProcessRule serialization."""
        process_rule = ProcessRule.builder().mode("automatic").build()
        data = process_rule.model_dump()
        assert data["mode"] == "automatic"

    def test_direct_instantiation(self) -> None:
        """Test ProcessRule direct instantiation alongside builder."""
        direct = ProcessRule(mode="automatic")
        builder = ProcessRule.builder().mode("automatic").build()

        assert direct.mode == builder.mode


class TestPreProcessingRule:
    """Test PreProcessingRule model."""

    def test_builder_pattern(self) -> None:
        """Test PreProcessingRule builder pattern functionality."""
        pre_rule = PreProcessingRule.builder().id("remove_urls_emails").enabled(False).build()

        assert pre_rule.id == "remove_urls_emails"
        assert pre_rule.enabled is False

    def test_field_validation(self) -> None:
        """Test PreProcessingRule field validation."""
        pre_rule = PreProcessingRule(id="remove_extra_spaces", enabled=True)

        assert pre_rule.id == "remove_extra_spaces"
        assert pre_rule.enabled is True

    def test_serialization(self) -> None:
        """Test PreProcessingRule serialization."""
        pre_rule = PreProcessingRule(id="remove_extra_spaces", enabled=True)
        data = pre_rule.model_dump()
        assert data["id"] == "remove_extra_spaces"
        assert data["enabled"] is True

    def test_direct_instantiation(self) -> None:
        """Test PreProcessingRule direct instantiation alongside builder."""
        direct = PreProcessingRule(id="remove_extra_spaces", enabled=True)
        builder = PreProcessingRule.builder().id("remove_extra_spaces").enabled(True).build()

        assert direct.id == builder.id
        assert direct.enabled == builder.enabled


class TestSegmentation:
    """Test Segmentation model."""

    def test_builder_pattern(self) -> None:
        """Test Segmentation builder pattern functionality."""
        segmentation = Segmentation.builder().separator("***").max_tokens(512).chunk_overlap(50).build()

        assert segmentation.separator == "***"
        assert segmentation.max_tokens == 512
        assert segmentation.chunk_overlap == 50

    def test_field_validation(self) -> None:
        """Test Segmentation field validation."""
        segmentation = Segmentation(separator="\n", max_tokens=1000, chunk_overlap=100)

        assert segmentation.separator == "\n"
        assert segmentation.max_tokens == 1000
        assert segmentation.chunk_overlap == 100

    def test_serialization(self) -> None:
        """Test Segmentation serialization."""
        segmentation = Segmentation(separator="\n", max_tokens=1000)
        data = segmentation.model_dump()
        assert data["separator"] == "\n"
        assert data["max_tokens"] == 1000

    def test_direct_instantiation(self) -> None:
        """Test Segmentation direct instantiation alongside builder."""
        direct = Segmentation(separator="\n", max_tokens=1000)
        builder = Segmentation.builder().separator("\n").max_tokens(1000).build()

        assert direct.separator == builder.separator
        assert direct.max_tokens == builder.max_tokens


class TestSubchunkSegmentation:
    """Test SubchunkSegmentation model."""

    def test_builder_pattern(self) -> None:
        """Test SubchunkSegmentation builder pattern functionality."""
        subchunk = SubchunkSegmentation.builder().separator("---").max_tokens(128).chunk_overlap(10).build()

        assert subchunk.separator == "---"
        assert subchunk.max_tokens == 128
        assert subchunk.chunk_overlap == 10

    def test_field_validation(self) -> None:
        """Test SubchunkSegmentation field validation."""
        subchunk = SubchunkSegmentation(separator="\n", max_tokens=256, chunk_overlap=25)

        assert subchunk.separator == "\n"
        assert subchunk.max_tokens == 256
        assert subchunk.chunk_overlap == 25

    def test_serialization(self) -> None:
        """Test SubchunkSegmentation serialization."""
        subchunk = SubchunkSegmentation(separator="\n", max_tokens=256)
        data = subchunk.model_dump()
        assert data["separator"] == "\n"
        assert data["max_tokens"] == 256

    def test_direct_instantiation(self) -> None:
        """Test SubchunkSegmentation direct instantiation alongside builder."""
        direct = SubchunkSegmentation(separator="\n", max_tokens=256)
        builder = SubchunkSegmentation.builder().separator("\n").max_tokens(256).build()

        assert direct.separator == builder.separator
        assert direct.max_tokens == builder.max_tokens


class TestDataSourceInfo:
    """Test DataSourceInfo model."""

    def test_builder_pattern(self) -> None:
        """Test DataSourceInfo builder pattern functionality."""
        data_source = DataSourceInfo.builder().upload_file_id("file-456").upload_file({"size": 1024}).build()

        assert data_source.upload_file_id == "file-456"
        assert data_source.upload_file == {"size": 1024}

    def test_field_validation(self) -> None:
        """Test DataSourceInfo field validation."""
        data_source = DataSourceInfo(upload_file_id="file-123", upload_file={"name": "test.txt"})

        assert data_source.upload_file_id == "file-123"
        assert data_source.upload_file == {"name": "test.txt"}

    def test_serialization(self) -> None:
        """Test DataSourceInfo serialization."""
        data_source = DataSourceInfo(upload_file_id="file-test")
        data = data_source.model_dump()
        assert data["upload_file_id"] == "file-test"

    def test_direct_instantiation(self) -> None:
        """Test DataSourceInfo direct instantiation alongside builder."""
        direct = DataSourceInfo(upload_file_id="test")
        builder = DataSourceInfo.builder().upload_file_id("test").build()

        assert direct.upload_file_id == builder.upload_file_id


class TestUploadFileInfo:
    """Test UploadFileInfo model."""

    def test_builder_pattern(self) -> None:
        """Test UploadFileInfo builder pattern functionality."""
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

    def test_field_validation(self) -> None:
        """Test UploadFileInfo field validation."""
        file_info = UploadFileInfo(
            id="file-789", name="document.pdf", size=2048, extension="pdf", mime_type="application/pdf"
        )

        assert file_info.id == "file-789"
        assert file_info.name == "document.pdf"
        assert file_info.size == 2048
        assert file_info.extension == "pdf"
        assert file_info.mime_type == "application/pdf"

    def test_serialization(self) -> None:
        """Test UploadFileInfo serialization."""
        file_info = UploadFileInfo(id="file-test", name="test.pdf")
        data = file_info.model_dump()
        assert data["id"] == "file-test"
        assert data["name"] == "test.pdf"

    def test_direct_instantiation(self) -> None:
        """Test UploadFileInfo direct instantiation alongside builder."""
        direct = UploadFileInfo(id="test", name="test.pdf")
        builder = UploadFileInfo.builder().id("test").name("test.pdf").build()

        assert direct.id == builder.id
        assert direct.name == builder.name


class TestIndexingStatusInfo:
    """Test IndexingStatusInfo model."""

    def test_builder_pattern(self) -> None:
        """Test IndexingStatusInfo builder pattern functionality."""
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

    def test_field_validation(self) -> None:
        """Test IndexingStatusInfo field validation."""
        status_info = IndexingStatusInfo(
            id="status-123", indexing_status="indexing", completed_segments=24, total_segments=100
        )

        assert status_info.id == "status-123"
        assert status_info.indexing_status == "indexing"
        assert status_info.completed_segments == 24
        assert status_info.total_segments == 100

    def test_serialization(self) -> None:
        """Test IndexingStatusInfo serialization."""
        status_info = IndexingStatusInfo(id="status-test", indexing_status="waiting")
        data = status_info.model_dump()
        assert data["id"] == "status-test"
        assert data["indexing_status"] == "waiting"

    def test_direct_instantiation(self) -> None:
        """Test IndexingStatusInfo direct instantiation alongside builder."""
        direct = IndexingStatusInfo(id="test", indexing_status="waiting")
        builder = IndexingStatusInfo.builder().id("test").indexing_status("waiting").build()

        assert direct.id == builder.id
        assert direct.indexing_status == builder.indexing_status


class TestRetrievalModel:
    """Test RetrievalModel model."""

    def test_builder_pattern(self) -> None:
        """Test RetrievalModel builder pattern functionality."""
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

    def test_field_validation(self) -> None:
        """Test RetrievalModel field validation."""
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

    def test_serialization(self) -> None:
        """Test RetrievalModel serialization."""
        retrieval_model = RetrievalModel(search_method="hybrid_search", top_k=10)
        data = retrieval_model.model_dump()
        assert data["search_method"] == "hybrid_search"
        assert data["top_k"] == 10

    def test_direct_instantiation(self) -> None:
        """Test RetrievalModel direct instantiation alongside builder."""
        direct = RetrievalModel(search_method="hybrid_search", top_k=10)
        builder = RetrievalModel.builder().search_method("hybrid_search").top_k(10).build()

        assert direct.search_method == builder.search_method
        assert direct.top_k == builder.top_k
