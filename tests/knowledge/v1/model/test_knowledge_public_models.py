"""Tests for Knowledge Base foundation models."""

from dify_oapi.api.knowledge.v1.model.batch_info import BatchInfo
from dify_oapi.api.knowledge.v1.model.child_chunk_info import ChildChunkInfo
from dify_oapi.api.knowledge.v1.model.dataset_info import DatasetInfo
from dify_oapi.api.knowledge.v1.model.document_info import DocumentInfo
from dify_oapi.api.knowledge.v1.model.embedding_model_parameters import EmbeddingModelParameters
from dify_oapi.api.knowledge.v1.model.file_info import FileInfo
from dify_oapi.api.knowledge.v1.model.knowledge_types import (
    DataSourceType,
    DocumentStatus,
    FileType,
    IndexingTechnique,
    Permission,
    ProcessingMode,
    SearchMethod,
    SegmentStatus,
    TagType,
)
from dify_oapi.api.knowledge.v1.model.model_info import ModelInfo
from dify_oapi.api.knowledge.v1.model.pagination_info import PaginationInfo
from dify_oapi.api.knowledge.v1.model.process_rule import ProcessRule
from dify_oapi.api.knowledge.v1.model.reranking_model import RerankingModel
from dify_oapi.api.knowledge.v1.model.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge.v1.model.retrieval_record import RetrievalRecord
from dify_oapi.api.knowledge.v1.model.segment_info import SegmentInfo
from dify_oapi.api.knowledge.v1.model.tag_info import TagInfo


class TestDatasetInfo:
    """Test DatasetInfo model."""

    def test_builder_pattern(self) -> None:
        """Test DatasetInfo builder pattern functionality."""
        dataset = (
            DatasetInfo.builder()
            .id("dataset_id")
            .name("dataset_name")
            .description("test description")
            .indexing_technique("high_quality")
            .permission("only_me")
            .build()
        )

        assert dataset.id == "dataset_id"
        assert dataset.name == "dataset_name"
        assert dataset.description == "test description"
        assert dataset.indexing_technique == "high_quality"
        assert dataset.permission == "only_me"

    def test_field_validation(self) -> None:
        """Test DatasetInfo field validation."""
        dataset = DatasetInfo(
            id="dataset_id",
            name="dataset_name",
            description="test description",
            indexing_technique="high_quality",
            permission="only_me",
            data_source_type="upload_file",
            provider="vendor",
            document_count=10,
            word_count=1000,
        )

        assert dataset.id == "dataset_id"
        assert dataset.name == "dataset_name"
        assert dataset.description == "test description"
        assert dataset.indexing_technique == "high_quality"
        assert dataset.permission == "only_me"
        assert dataset.data_source_type == "upload_file"
        assert dataset.provider == "vendor"
        assert dataset.document_count == 10
        assert dataset.word_count == 1000

    def test_type_safety(self) -> None:
        """Test DatasetInfo type safety with Literal types."""
        dataset = DatasetInfo(
            indexing_technique="high_quality",
            permission="all_team_members",
            data_source_type="notion_import",
        )
        assert dataset.indexing_technique == "high_quality"
        assert dataset.permission == "all_team_members"
        assert dataset.data_source_type == "notion_import"

    def test_serialization(self) -> None:
        """Test DatasetInfo serialization."""
        dataset = DatasetInfo(id="test_id", name="test_name", description="test_desc", document_count=5)
        data = dataset.model_dump()
        assert data["id"] == "test_id"
        assert data["name"] == "test_name"
        assert data["description"] == "test_desc"
        assert data["document_count"] == 5

    def test_direct_instantiation(self) -> None:
        """Test DatasetInfo direct instantiation alongside builder."""
        direct = DatasetInfo(id="id", name="name")
        builder = DatasetInfo.builder().id("id").name("name").build()

        assert direct.id == builder.id
        assert direct.name == builder.name


class TestDocumentInfo:
    """Test DocumentInfo model."""

    def test_builder_pattern(self) -> None:
        """Test DocumentInfo builder pattern functionality."""
        document = (
            DocumentInfo.builder()
            .id("doc_id")
            .name("doc_name")
            .status("completed")
            .enabled(True)
            .word_count(500)
            .build()
        )

        assert document.id == "doc_id"
        assert document.name == "doc_name"
        assert document.status == "completed"
        assert document.enabled is True
        assert document.word_count == 500

    def test_field_validation(self) -> None:
        """Test DocumentInfo field validation."""
        document = DocumentInfo(
            id="doc_id",
            name="doc_name",
            character_count=1000,
            tokens=250,
            status="indexing",
            enabled=True,
            archived=False,
            word_count=500,
            hit_count=10,
            data_source_type="upload_file",
        )

        assert document.id == "doc_id"
        assert document.name == "doc_name"
        assert document.character_count == 1000
        assert document.tokens == 250
        assert document.status == "indexing"
        assert document.enabled is True
        assert document.archived is False
        assert document.word_count == 500
        assert document.hit_count == 10
        assert document.data_source_type == "upload_file"

    def test_type_safety(self) -> None:
        """Test DocumentInfo type safety with Literal types."""
        document = DocumentInfo(
            status="completed",
            data_source_type="website_crawl",
        )
        assert document.status == "completed"
        assert document.data_source_type == "website_crawl"

    def test_serialization(self) -> None:
        """Test DocumentInfo serialization."""
        document = DocumentInfo(id="test_id", name="test_name", tokens=100)
        data = document.model_dump()
        assert data["id"] == "test_id"
        assert data["name"] == "test_name"
        assert data["tokens"] == 100

    def test_direct_instantiation(self) -> None:
        """Test DocumentInfo direct instantiation alongside builder."""
        direct = DocumentInfo(id="id", name="name")
        builder = DocumentInfo.builder().id("id").name("name").build()

        assert direct.id == builder.id
        assert direct.name == builder.name


class TestSegmentInfo:
    """Test SegmentInfo model."""

    def test_builder_pattern(self) -> None:
        """Test SegmentInfo builder pattern functionality."""
        segment = (
            SegmentInfo.builder()
            .id("seg_id")
            .position(1)
            .document_id("doc_id")
            .content("segment content")
            .status("completed")
            .build()
        )

        assert segment.id == "seg_id"
        assert segment.position == 1
        assert segment.document_id == "doc_id"
        assert segment.content == "segment content"
        assert segment.status == "completed"

    def test_field_validation(self) -> None:
        """Test SegmentInfo field validation."""
        segment = SegmentInfo(
            id="seg_id",
            position=1,
            document_id="doc_id",
            content="segment content",
            answer="segment answer",
            word_count=50,
            tokens=12,
            keywords=["keyword1", "keyword2"],
            enabled=True,
            status="completed",
        )

        assert segment.id == "seg_id"
        assert segment.position == 1
        assert segment.document_id == "doc_id"
        assert segment.content == "segment content"
        assert segment.answer == "segment answer"
        assert segment.word_count == 50
        assert segment.tokens == 12
        assert segment.keywords == ["keyword1", "keyword2"]
        assert segment.enabled is True
        assert segment.status == "completed"

    def test_type_safety(self) -> None:
        """Test SegmentInfo type safety with Literal types."""
        segment = SegmentInfo(status="indexing")
        assert segment.status == "indexing"

    def test_serialization(self) -> None:
        """Test SegmentInfo serialization."""
        segment = SegmentInfo(id="test_id", content="test content", word_count=25)
        data = segment.model_dump()
        assert data["id"] == "test_id"
        assert data["content"] == "test content"
        assert data["word_count"] == 25

    def test_direct_instantiation(self) -> None:
        """Test SegmentInfo direct instantiation alongside builder."""
        direct = SegmentInfo(id="id", content="content")
        builder = SegmentInfo.builder().id("id").content("content").build()

        assert direct.id == builder.id
        assert direct.content == builder.content


class TestChildChunkInfo:
    """Test ChildChunkInfo model."""

    def test_builder_pattern(self) -> None:
        """Test ChildChunkInfo builder pattern functionality."""
        chunk = (
            ChildChunkInfo.builder()
            .id("chunk_id")
            .content("chunk content")
            .keywords(["key1", "key2"])
            .created_at(1234567890)
            .build()
        )

        assert chunk.id == "chunk_id"
        assert chunk.content == "chunk content"
        assert chunk.keywords == ["key1", "key2"]
        assert chunk.created_at == 1234567890

    def test_field_validation(self) -> None:
        """Test ChildChunkInfo field validation."""
        chunk = ChildChunkInfo(
            id="chunk_id",
            content="chunk content",
            keywords=["keyword1"],
            created_at=1234567890,
        )

        assert chunk.id == "chunk_id"
        assert chunk.content == "chunk content"
        assert chunk.keywords == ["keyword1"]
        assert chunk.created_at == 1234567890

    def test_serialization(self) -> None:
        """Test ChildChunkInfo serialization."""
        chunk = ChildChunkInfo(id="test_id", content="test content")
        data = chunk.model_dump()
        assert data["id"] == "test_id"
        assert data["content"] == "test content"

    def test_direct_instantiation(self) -> None:
        """Test ChildChunkInfo direct instantiation alongside builder."""
        direct = ChildChunkInfo(id="id", content="content")
        builder = ChildChunkInfo.builder().id("id").content("content").build()

        assert direct.id == builder.id
        assert direct.content == builder.content


class TestTagInfo:
    """Test TagInfo model."""

    def test_builder_pattern(self) -> None:
        """Test TagInfo builder pattern functionality."""
        tag = TagInfo.builder().id("tag_id").name("tag_name").type("knowledge_type").build()

        assert tag.id == "tag_id"
        assert tag.name == "tag_name"
        assert tag.type == "knowledge_type"

    def test_field_validation(self) -> None:
        """Test TagInfo field validation."""
        tag = TagInfo(
            id="tag_id",
            name="tag_name",
            type="custom",
        )

        assert tag.id == "tag_id"
        assert tag.name == "tag_name"
        assert tag.type == "custom"

    def test_type_safety(self) -> None:
        """Test TagInfo type safety with Literal types."""
        tag = TagInfo(type="knowledge_type")
        assert tag.type == "knowledge_type"

    def test_serialization(self) -> None:
        """Test TagInfo serialization."""
        tag = TagInfo(id="test_id", name="test_name", type="custom")
        data = tag.model_dump()
        assert data["id"] == "test_id"
        assert data["name"] == "test_name"
        assert data["type"] == "custom"

    def test_direct_instantiation(self) -> None:
        """Test TagInfo direct instantiation alongside builder."""
        direct = TagInfo(id="id", name="name")
        builder = TagInfo.builder().id("id").name("name").build()

        assert direct.id == builder.id
        assert direct.name == builder.name


class TestModelInfo:
    """Test ModelInfo model."""

    def test_builder_pattern(self) -> None:
        """Test ModelInfo builder pattern functionality."""
        model = ModelInfo.builder().provider("openai").status("active").label({"en": "OpenAI"}).build()

        assert model.provider == "openai"
        assert model.status == "active"
        assert model.label == {"en": "OpenAI"}

    def test_field_validation(self) -> None:
        """Test ModelInfo field validation."""
        from dify_oapi.api.knowledge.v1.model.model_info import EmbeddingModelDetails

        model_details = EmbeddingModelDetails(model="text-embedding-3", model_type="text-embedding", status="active")

        model = ModelInfo(
            provider="openai",
            status="active",
            label={"en": "OpenAI"},
            models=[model_details],
        )

        assert model.provider == "openai"
        assert model.status == "active"
        assert model.label == {"en": "OpenAI"}
        assert len(model.models) == 1
        assert model.models[0].model == "text-embedding-3"

    def test_type_safety(self) -> None:
        """Test ModelInfo type safety with Literal types."""
        model = ModelInfo(
            provider="openai",
            status="active",
        )
        assert model.provider == "openai"
        assert model.status == "active"

    def test_serialization(self) -> None:
        """Test ModelInfo serialization."""
        model = ModelInfo(provider="test_provider", status="active")
        data = model.model_dump()
        assert data["provider"] == "test_provider"
        assert data["status"] == "active"

    def test_direct_instantiation(self) -> None:
        """Test ModelInfo direct instantiation alongside builder."""
        direct = ModelInfo(provider="provider", status="active")
        builder = ModelInfo.builder().provider("provider").status("active").build()

        assert direct.provider == builder.provider
        assert direct.status == builder.status


class TestFileInfo:
    """Test FileInfo model."""

    def test_builder_pattern(self) -> None:
        """Test FileInfo builder pattern functionality."""
        file = (
            FileInfo.builder()
            .id("file_id")
            .name("test.pdf")
            .size(1024)
            .extension("pdf")
            .mime_type("application/pdf")
            .type("document")
            .build()
        )

        assert file.id == "file_id"
        assert file.name == "test.pdf"
        assert file.size == 1024
        assert file.extension == "pdf"
        assert file.mime_type == "application/pdf"
        assert file.type == "document"

    def test_field_validation(self) -> None:
        """Test FileInfo field validation."""
        file = FileInfo(
            id="file_id",
            name="test.pdf",
            size=1024,
            extension="pdf",
            mime_type="application/pdf",
            type="document",
            upload_file_id="upload_123",
        )

        assert file.id == "file_id"
        assert file.name == "test.pdf"
        assert file.size == 1024
        assert file.extension == "pdf"
        assert file.mime_type == "application/pdf"
        assert file.type == "document"
        assert file.upload_file_id == "upload_123"

    def test_type_safety(self) -> None:
        """Test FileInfo type safety with Literal types."""
        file = FileInfo(type="image")
        assert file.type == "image"

    def test_serialization(self) -> None:
        """Test FileInfo serialization."""
        file = FileInfo(id="test_id", name="test.txt", size=512)
        data = file.model_dump()
        assert data["id"] == "test_id"
        assert data["name"] == "test.txt"
        assert data["size"] == 512

    def test_direct_instantiation(self) -> None:
        """Test FileInfo direct instantiation alongside builder."""
        direct = FileInfo(id="id", name="name")
        builder = FileInfo.builder().id("id").name("name").build()

        assert direct.id == builder.id
        assert direct.name == builder.name


class TestProcessRule:
    """Test ProcessRule model."""

    def test_builder_pattern(self) -> None:
        """Test ProcessRule builder pattern functionality."""
        rule = (
            ProcessRule.builder()
            .mode("automatic")
            .rules({"max_tokens": 1000})
            .segmentation({"separator": "\n"})
            .build()
        )

        assert rule.mode == "automatic"
        assert rule.rules == {"max_tokens": 1000}
        assert rule.segmentation == {"separator": "\n"}

    def test_field_validation(self) -> None:
        """Test ProcessRule field validation."""
        rule = ProcessRule(
            mode="custom",
            rules={"max_tokens": 500, "overlap": 50},
            segmentation={"separator": "\n\n", "max_tokens": 1000},
        )

        assert rule.mode == "custom"
        assert rule.rules == {"max_tokens": 500, "overlap": 50}
        assert rule.segmentation == {"separator": "\n\n", "max_tokens": 1000}

    def test_type_safety(self) -> None:
        """Test ProcessRule type safety with Literal types."""
        rule = ProcessRule(mode="automatic")
        assert rule.mode == "automatic"

    def test_serialization(self) -> None:
        """Test ProcessRule serialization."""
        rule = ProcessRule(mode="custom", rules={"test": "value"})
        data = rule.model_dump()
        assert data["mode"] == "custom"
        assert data["rules"] == {"test": "value"}

    def test_direct_instantiation(self) -> None:
        """Test ProcessRule direct instantiation alongside builder."""
        direct = ProcessRule(mode="automatic")
        builder = ProcessRule.builder().mode("automatic").build()

        assert direct.mode == builder.mode


class TestRetrievalModel:
    """Test RetrievalModel model."""

    def test_builder_pattern(self) -> None:
        """Test RetrievalModel builder pattern functionality."""
        model = (
            RetrievalModel.builder()
            .search_method("hybrid_search")
            .reranking_enable(True)
            .top_k(10)
            .score_threshold(0.8)
            .build()
        )

        assert model.search_method == "hybrid_search"
        assert model.reranking_enable is True
        assert model.top_k == 10
        assert model.score_threshold == 0.8

    def test_field_validation(self) -> None:
        """Test RetrievalModel field validation."""
        model = RetrievalModel(
            search_method="semantic_search",
            reranking_enable=False,
            top_k=5,
            score_threshold_enabled=True,
            score_threshold=0.7,
            reranking_model={"provider": "test", "model": "test_model"},
        )

        assert model.search_method == "semantic_search"
        assert model.reranking_enable is False
        assert model.top_k == 5
        assert model.score_threshold_enabled is True
        assert model.score_threshold == 0.7
        assert model.reranking_model == {"provider": "test", "model": "test_model"}

    def test_type_safety(self) -> None:
        """Test RetrievalModel type safety with Literal types."""
        model = RetrievalModel(search_method="full_text_search")
        assert model.search_method == "full_text_search"

    def test_serialization(self) -> None:
        """Test RetrievalModel serialization."""
        model = RetrievalModel(search_method="semantic_search", top_k=5)
        data = model.model_dump()
        assert data["search_method"] == "semantic_search"
        assert data["top_k"] == 5

    def test_direct_instantiation(self) -> None:
        """Test RetrievalModel direct instantiation alongside builder."""
        direct = RetrievalModel(search_method="semantic_search")
        builder = RetrievalModel.builder().search_method("semantic_search").build()

        assert direct.search_method == builder.search_method


class TestRerankingModel:
    """Test RerankingModel model."""

    def test_builder_pattern(self) -> None:
        """Test RerankingModel builder pattern functionality."""
        model = (
            RerankingModel.builder()
            .model("rerank-model")
            .provider("test_provider")
            .credentials({"api_key": "test"})
            .build()
        )

        assert model.model == "rerank-model"
        assert model.provider == "test_provider"
        assert model.credentials == {"api_key": "test"}

    def test_field_validation(self) -> None:
        """Test RerankingModel field validation."""
        model = RerankingModel(
            model="rerank-model",
            provider="test_provider",
            credentials={"api_key": "test_key"},
            model_parameters={"temperature": 0.7},
        )

        assert model.model == "rerank-model"
        assert model.provider == "test_provider"
        assert model.credentials == {"api_key": "test_key"}
        assert model.model_parameters == {"temperature": 0.7}

    def test_serialization(self) -> None:
        """Test RerankingModel serialization."""
        model = RerankingModel(model="test_model", provider="test_provider")
        data = model.model_dump()
        assert data["model"] == "test_model"
        assert data["provider"] == "test_provider"

    def test_direct_instantiation(self) -> None:
        """Test RerankingModel direct instantiation alongside builder."""
        direct = RerankingModel(model="model", provider="provider")
        builder = RerankingModel.builder().model("model").provider("provider").build()

        assert direct.model == builder.model
        assert direct.provider == builder.provider


class TestEmbeddingModelParameters:
    """Test EmbeddingModelParameters model."""

    def test_builder_pattern(self) -> None:
        """Test EmbeddingModelParameters builder pattern functionality."""
        params = (
            EmbeddingModelParameters.builder()
            .model("text-embedding-3")
            .provider("openai")
            .credentials({"api_key": "test"})
            .build()
        )

        assert params.model == "text-embedding-3"
        assert params.provider == "openai"
        assert params.credentials == {"api_key": "test"}

    def test_field_validation(self) -> None:
        """Test EmbeddingModelParameters field validation."""
        params = EmbeddingModelParameters(
            model="text-embedding-3",
            provider="openai",
            credentials={"api_key": "test_key"},
            model_parameters={"dimensions": 1536},
        )

        assert params.model == "text-embedding-3"
        assert params.provider == "openai"
        assert params.credentials == {"api_key": "test_key"}
        assert params.model_parameters == {"dimensions": 1536}

    def test_serialization(self) -> None:
        """Test EmbeddingModelParameters serialization."""
        params = EmbeddingModelParameters(model="test_model", provider="test_provider")
        data = params.model_dump()
        assert data["model"] == "test_model"
        assert data["provider"] == "test_provider"

    def test_direct_instantiation(self) -> None:
        """Test EmbeddingModelParameters direct instantiation alongside builder."""
        direct = EmbeddingModelParameters(model="model", provider="provider")
        builder = EmbeddingModelParameters.builder().model("model").provider("provider").build()

        assert direct.model == builder.model
        assert direct.provider == builder.provider


class TestBatchInfo:
    """Test BatchInfo model."""

    def test_builder_pattern(self) -> None:
        """Test BatchInfo builder pattern functionality."""
        batch = (
            BatchInfo.builder()
            .id("batch_123")
            .indexing_status("completed")
            .completed_segments(80)
            .total_segments(100)
            .build()
        )

        assert batch.id == "batch_123"
        assert batch.indexing_status == "completed"
        assert batch.completed_segments == 80
        assert batch.total_segments == 100

    def test_field_validation(self) -> None:
        """Test BatchInfo field validation."""
        batch = BatchInfo(
            id="batch_123",
            indexing_status="indexing",
            processing_started_at=1234567890.0,
            completed_segments=40,
            total_segments=50,
            error=None,
        )

        assert batch.id == "batch_123"
        assert batch.indexing_status == "indexing"
        assert batch.processing_started_at == 1234567890.0
        assert batch.completed_segments == 40
        assert batch.total_segments == 50
        assert batch.error is None

    def test_serialization(self) -> None:
        """Test BatchInfo serialization."""
        batch = BatchInfo(id="test_batch", total_segments=10)
        data = batch.model_dump()
        assert data["id"] == "test_batch"
        assert data["total_segments"] == 10

    def test_direct_instantiation(self) -> None:
        """Test BatchInfo direct instantiation alongside builder."""
        direct = BatchInfo(id="batch", total_segments=10)
        builder = BatchInfo.builder().id("batch").total_segments(10).build()

        assert direct.id == builder.id
        assert direct.total_segments == builder.total_segments


class TestPaginationInfo:
    """Test PaginationInfo model."""

    def test_builder_pattern(self) -> None:
        """Test PaginationInfo builder pattern functionality."""
        pagination = PaginationInfo.builder().page(1).limit(20).total(100).has_more(True).build()

        assert pagination.page == 1
        assert pagination.limit == 20
        assert pagination.total == 100
        assert pagination.has_more is True

    def test_field_validation(self) -> None:
        """Test PaginationInfo field validation."""
        pagination = PaginationInfo(
            page=2,
            limit=50,
            total=200,
            has_more=False,
        )

        assert pagination.page == 2
        assert pagination.limit == 50
        assert pagination.total == 200
        assert pagination.has_more is False

    def test_serialization(self) -> None:
        """Test PaginationInfo serialization."""
        pagination = PaginationInfo(page=1, limit=10, total=50)
        data = pagination.model_dump()
        assert data["page"] == 1
        assert data["limit"] == 10
        assert data["total"] == 50

    def test_direct_instantiation(self) -> None:
        """Test PaginationInfo direct instantiation alongside builder."""
        direct = PaginationInfo(page=1, limit=10)
        builder = PaginationInfo.builder().page(1).limit(10).build()

        assert direct.page == builder.page
        assert direct.limit == builder.limit


class TestRetrievalRecord:
    """Test RetrievalRecord model."""

    def test_builder_pattern(self) -> None:
        """Test RetrievalRecord builder pattern functionality."""
        segment = SegmentInfo(id="seg_id", content="test content")
        record = RetrievalRecord.builder().segment(segment).score(0.95).build()

        assert record.segment is not None
        assert record.segment.id == "seg_id"
        assert record.segment.content == "test content"
        assert record.score == 0.95

    def test_field_validation(self) -> None:
        """Test RetrievalRecord field validation."""
        segment = SegmentInfo(id="seg_id", content="test content", word_count=10)
        record = RetrievalRecord(segment=segment, score=0.85)

        assert record.segment is not None
        assert record.segment.id == "seg_id"
        assert record.segment.content == "test content"
        assert record.segment.word_count == 10
        assert record.score == 0.85

    def test_serialization(self) -> None:
        """Test RetrievalRecord serialization."""
        segment = SegmentInfo(id="test_id", content="test content")
        record = RetrievalRecord(segment=segment, score=0.9)
        data = record.model_dump()
        assert data["segment"]["id"] == "test_id"
        assert data["segment"]["content"] == "test content"
        assert data["score"] == 0.9

    def test_direct_instantiation(self) -> None:
        """Test RetrievalRecord direct instantiation alongside builder."""
        segment = SegmentInfo(id="id", content="content")
        direct = RetrievalRecord(segment=segment, score=0.8)
        builder = RetrievalRecord.builder().segment(segment).score(0.8).build()

        assert direct.segment.id == builder.segment.id
        assert direct.score == builder.score


class TestKnowledgeTypes:
    """Test Knowledge types for type safety."""

    def test_indexing_technique_values(self) -> None:
        """Test IndexingTechnique literal values."""
        # These should be valid
        technique1: IndexingTechnique = "high_quality"
        technique2: IndexingTechnique = "economy"
        assert technique1 == "high_quality"
        assert technique2 == "economy"

    def test_permission_values(self) -> None:
        """Test Permission literal values."""
        perm1: Permission = "only_me"
        perm2: Permission = "all_team_members"
        perm3: Permission = "partial_members"
        assert perm1 == "only_me"
        assert perm2 == "all_team_members"
        assert perm3 == "partial_members"

    def test_search_method_values(self) -> None:
        """Test SearchMethod literal values."""
        method1: SearchMethod = "hybrid_search"
        method2: SearchMethod = "semantic_search"
        method3: SearchMethod = "full_text_search"
        method4: SearchMethod = "keyword_search"
        assert method1 == "hybrid_search"
        assert method2 == "semantic_search"
        assert method3 == "full_text_search"
        assert method4 == "keyword_search"

    def test_document_status_values(self) -> None:
        """Test DocumentStatus literal values."""
        status1: DocumentStatus = "indexing"
        status2: DocumentStatus = "completed"
        status3: DocumentStatus = "error"
        status4: DocumentStatus = "paused"
        assert status1 == "indexing"
        assert status2 == "completed"
        assert status3 == "error"
        assert status4 == "paused"

    def test_processing_mode_values(self) -> None:
        """Test ProcessingMode literal values."""
        mode1: ProcessingMode = "automatic"
        mode2: ProcessingMode = "custom"
        assert mode1 == "automatic"
        assert mode2 == "custom"

    def test_file_type_values(self) -> None:
        """Test FileType literal values."""
        type1: FileType = "document"
        type2: FileType = "image"
        type3: FileType = "audio"
        type4: FileType = "video"
        type5: FileType = "custom"
        assert type1 == "document"
        assert type2 == "image"
        assert type3 == "audio"
        assert type4 == "video"
        assert type5 == "custom"

    def test_tag_type_values(self) -> None:
        """Test TagType literal values."""
        tag1: TagType = "knowledge_type"
        tag2: TagType = "custom"
        assert tag1 == "knowledge_type"
        assert tag2 == "custom"

    def test_segment_status_values(self) -> None:
        """Test SegmentStatus literal values."""
        status1: SegmentStatus = "waiting"
        status2: SegmentStatus = "parsing"
        status3: SegmentStatus = "cleaning"
        status4: SegmentStatus = "splitting"
        status5: SegmentStatus = "indexing"
        status6: SegmentStatus = "completed"
        status7: SegmentStatus = "error"
        status8: SegmentStatus = "paused"
        assert status1 == "waiting"
        assert status2 == "parsing"
        assert status3 == "cleaning"
        assert status4 == "splitting"
        assert status5 == "indexing"
        assert status6 == "completed"
        assert status7 == "error"
        assert status8 == "paused"

    def test_data_source_type_values(self) -> None:
        """Test DataSourceType literal values."""
        source1: DataSourceType = "upload_file"
        source2: DataSourceType = "notion_import"
        source3: DataSourceType = "website_crawl"
        assert source1 == "upload_file"
        assert source2 == "notion_import"
        assert source3 == "website_crawl"
