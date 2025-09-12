"""Tests for Knowledge Base foundation models."""

from dify_oapi.api.knowledge.v1.model.batch_info import BatchInfo
from dify_oapi.api.knowledge.v1.model.child_chunk_info import ChildChunkInfo
from dify_oapi.api.knowledge.v1.model.document_info import DocumentInfo
from dify_oapi.api.knowledge.v1.model.embedding_model_parameters import EmbeddingModelParameters
from dify_oapi.api.knowledge.v1.model.model_info import ModelInfo
from dify_oapi.api.knowledge.v1.model.process_rule import ProcessRule
from dify_oapi.api.knowledge.v1.model.reranking_model import RerankingModel
from dify_oapi.api.knowledge.v1.model.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge.v1.model.retrieval_record import RetrievalRecord
from dify_oapi.api.knowledge.v1.model.tag_info import TagInfo


class TestDocumentInfo:
    """Test DocumentInfo model."""

    def test_builder_pattern(self) -> None:
        """Test DocumentInfo builder pattern functionality."""
        document = (
            DocumentInfo.builder()
            .id("doc_id")
            .name("doc_name")
            .indexing_status("completed")
            .display_status("available")
            .doc_form("text_model")
            .enabled(True)
            .word_count(500)
            .build()
        )

        assert document.id == "doc_id"
        assert document.name == "doc_name"
        assert document.indexing_status == "completed"
        assert document.display_status == "available"
        assert document.doc_form == "text_model"
        assert document.enabled is True
        assert document.word_count == 500

    def test_field_validation(self) -> None:
        """Test DocumentInfo field validation."""
        document = DocumentInfo(
            id="doc_id",
            name="doc_name",
            tokens=250,
            indexing_status="indexing",
            display_status="indexing",
            doc_form="hierarchical_model",
            enabled=True,
            archived=False,
            word_count=500,
            hit_count=10,
            data_source_type="upload_file",
        )

        assert document.id == "doc_id"
        assert document.name == "doc_name"
        assert document.tokens == 250
        assert document.indexing_status == "indexing"
        assert document.display_status == "indexing"
        assert document.doc_form == "hierarchical_model"
        assert document.enabled is True
        assert document.archived is False
        assert document.word_count == 500
        assert document.hit_count == 10
        assert document.data_source_type == "upload_file"

    def test_type_safety(self) -> None:
        """Test DocumentInfo type safety with Literal types."""
        document = DocumentInfo(
            indexing_status="completed",
            display_status="available",
            doc_form="qa_model",
            data_source_type="website_crawl",
        )
        assert document.indexing_status == "completed"
        assert document.display_status == "available"
        assert document.doc_form == "qa_model"
        assert document.data_source_type == "website_crawl"


class TestTagInfo:
    """Test TagInfo model."""

    def test_type_safety(self) -> None:
        """Test TagInfo type safety with Literal types."""
        tag = TagInfo(type="knowledge")
        assert tag.type == "knowledge"


class TestModelInfo:
    """Test ModelInfo model."""

    def test_field_validation(self) -> None:
        """Test ModelInfo field validation."""
        from dify_oapi.api.knowledge.v1.model.model_info import ModelLabel

        label = ModelLabel(en_US="OpenAI")
        model = ModelInfo(
            provider="openai",
            status="active",
            label=label,
        )

        assert model.provider == "openai"
        assert model.status == "active"
        assert model.label.en_US == "OpenAI"


class TestProcessRule:
    """Test ProcessRule model."""

    def test_field_validation(self) -> None:
        """Test ProcessRule field validation."""
        rule = ProcessRule(
            mode="custom",
        )

        assert rule.mode == "custom"

    def test_serialization(self) -> None:
        """Test ProcessRule serialization."""
        rule = ProcessRule(mode="custom")
        data = rule.model_dump()
        assert data["mode"] == "custom"


class TestRetrievalModel:
    """Test RetrievalModel model."""

    def test_field_validation(self) -> None:
        """Test RetrievalModel field validation."""
        model = RetrievalModel(
            search_method="semantic_search",
            reranking_enable=False,
            top_k=5,
            score_threshold_enabled=True,
            score_threshold=0.7,
        )

        assert model.search_method == "semantic_search"
        assert model.reranking_enable is False
        assert model.top_k == 5
        assert model.score_threshold_enabled is True
        assert model.score_threshold == 0.7


class TestRerankingModel:
    """Test RerankingModel model."""

    def test_field_validation(self) -> None:
        """Test RerankingModel field validation."""
        model = RerankingModel(
            model="rerank-model",
            provider="test_provider",
        )

        assert model.model == "rerank-model"
        assert model.provider == "test_provider"


class TestEmbeddingModelParameters:
    """Test EmbeddingModelParameters model."""

    def test_field_validation(self) -> None:
        """Test EmbeddingModelParameters field validation."""
        params = EmbeddingModelParameters(
            model="text-embedding-3",
            provider="openai",
        )

        assert params.model == "text-embedding-3"
        assert params.provider == "openai"


class TestChildChunkInfo:
    """Test ChildChunkInfo model."""

    def test_builder_pattern(self) -> None:
        """Test ChildChunkInfo builder pattern functionality."""
        chunk = (
            ChildChunkInfo.builder()
            .id("chunk_id")
            .segment_id("seg_id")
            .content("chunk content")
            .word_count(100)
            .tokens(50)
            .status("completed")
            .build()
        )

        assert chunk.id == "chunk_id"
        assert chunk.segment_id == "seg_id"
        assert chunk.content == "chunk content"
        assert chunk.word_count == 100
        assert chunk.tokens == 50
        assert chunk.status == "completed"

    def test_field_validation(self) -> None:
        """Test ChildChunkInfo field validation."""
        chunk = ChildChunkInfo(
            id="chunk_id",
            segment_id="seg_id",
            content="test content",
            word_count=150,
            tokens=75,
            keywords=["test", "chunk"],
            status="processing",
            created_by="user_id",
        )

        assert chunk.id == "chunk_id"
        assert chunk.segment_id == "seg_id"
        assert chunk.content == "test content"
        assert chunk.word_count == 150
        assert chunk.tokens == 75
        assert chunk.keywords == ["test", "chunk"]
        assert chunk.status == "processing"
        assert chunk.created_by == "user_id"


class TestBatchInfo:
    """Test BatchInfo model."""

    def test_builder_pattern(self) -> None:
        """Test BatchInfo builder pattern functionality."""
        batch = (
            BatchInfo.builder()
            .id("batch_id")
            .indexing_status("completed")
            .completed_segments(10)
            .total_segments(10)
            .build()
        )

        assert batch.id == "batch_id"
        assert batch.indexing_status == "completed"
        assert batch.completed_segments == 10
        assert batch.total_segments == 10

    def test_field_validation(self) -> None:
        """Test BatchInfo field validation."""
        batch = BatchInfo(
            id="batch_id",
            indexing_status="indexing",
            completed_segments=5,
            total_segments=10,
        )

        assert batch.id == "batch_id"
        assert batch.indexing_status == "indexing"
        assert batch.completed_segments == 5
        assert batch.total_segments == 10


class TestRetrievalRecord:
    """Test RetrievalRecord model."""

    def test_field_validation(self) -> None:
        """Test RetrievalRecord field validation."""
        from dify_oapi.api.knowledge.v1.model.retrieval_segment_info import RetrievalSegmentInfo

        segment = RetrievalSegmentInfo(id="seg_id", content="test content")
        record = RetrievalRecord(segment=segment, score=0.85)

        assert record.segment is not None
        assert record.segment.id == "seg_id"
        assert record.segment.content == "test content"
        assert record.score == 0.85

    def test_serialization(self) -> None:
        """Test RetrievalRecord serialization."""
        from dify_oapi.api.knowledge.v1.model.retrieval_segment_info import RetrievalSegmentInfo

        segment = RetrievalSegmentInfo(id="test_id", content="test content")
        record = RetrievalRecord(segment=segment, score=0.9)
        data = record.model_dump()
        assert data["segment"]["id"] == "test_id"
        assert data["segment"]["content"] == "test content"
        assert data["score"] == 0.9

    def test_direct_instantiation(self) -> None:
        """Test RetrievalRecord direct instantiation alongside builder."""
        from dify_oapi.api.knowledge.v1.model.retrieval_segment_info import RetrievalSegmentInfo

        segment = RetrievalSegmentInfo(id="id", content="content")
        direct = RetrievalRecord(segment=segment, score=0.8)
        builder = RetrievalRecord.builder().segment(segment).score(0.8).build()

        assert direct.segment.id == builder.segment.id
        assert direct.score == builder.score
