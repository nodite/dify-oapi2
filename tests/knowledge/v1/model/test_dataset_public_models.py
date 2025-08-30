"""Tests for dataset public models."""

from dify_oapi.api.knowledge.v1.model.dataset_info import DatasetInfo
from dify_oapi.api.knowledge.v1.model.reranking_model import RerankingModel
from dify_oapi.api.knowledge.v1.model.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge.v1.model.tag_info import TagInfo


class TestDatasetInfo:
    """Test DatasetInfo model."""

    def test_builder_pattern(self) -> None:
        """Test DatasetInfo builder pattern functionality."""
        dataset = DatasetInfo.builder().id("dataset_id").name("dataset_name").description("test description").build()

        assert dataset.id == "dataset_id"
        assert dataset.name == "dataset_name"
        assert dataset.description == "test description"

    def test_field_validation(self) -> None:
        """Test DatasetInfo field validation."""
        dataset = DatasetInfo(
            id="dataset_id",
            name="dataset_name",
            description="test description",
            provider="vendor",
            permission="only_me",
            indexing_technique="high_quality",
            document_count=10,
            word_count=1000,
        )

        assert dataset.id == "dataset_id"
        assert dataset.name == "dataset_name"
        assert dataset.description == "test description"
        assert dataset.provider == "vendor"
        assert dataset.permission == "only_me"
        assert dataset.indexing_technique == "high_quality"
        assert dataset.document_count == 10
        assert dataset.word_count == 1000

    def test_serialization(self) -> None:
        """Test DatasetInfo serialization."""
        dataset = DatasetInfo(id="test_id", name="test_name", description="test_desc", app_count=5)
        data = dataset.model_dump()
        assert data["id"] == "test_id"
        assert data["name"] == "test_name"
        assert data["description"] == "test_desc"
        assert data["app_count"] == 5

    def test_direct_instantiation(self) -> None:
        """Test DatasetInfo direct instantiation alongside builder."""
        direct = DatasetInfo(id="id", name="name")
        builder = DatasetInfo.builder().id("id").name("name").build()

        assert direct.id == builder.id
        assert direct.name == builder.name


class TestRetrievalModel:
    """Test RetrievalModel model."""

    def test_builder_pattern(self) -> None:
        """Test RetrievalModel builder pattern functionality."""
        model = RetrievalModel.builder().search_method("hybrid_search").top_k(10).build()

        assert model.search_method == "hybrid_search"
        assert model.top_k == 10

    def test_field_validation(self) -> None:
        """Test RetrievalModel field validation."""
        reranking_model_dict = {"reranking_provider_name": "provider", "reranking_model_name": "model"}

        model = RetrievalModel(
            search_method="hybrid_search",
            reranking_enable=True,
            reranking_model=reranking_model_dict,
            top_k=10,
            score_threshold_enabled=True,
            score_threshold=0.8,
        )

        assert model.search_method == "hybrid_search"
        assert model.reranking_enable is True
        assert model.reranking_model is not None
        assert model.reranking_model["reranking_provider_name"] == "provider"
        assert model.reranking_model["reranking_model_name"] == "model"
        assert model.top_k == 10
        assert model.score_threshold == 0.8

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
        model = RerankingModel.builder().reranking_provider_name("provider").reranking_model_name("model").build()

        assert model.reranking_provider_name == "provider"
        assert model.reranking_model_name == "model"

    def test_field_validation(self) -> None:
        """Test RerankingModel field validation."""
        model = RerankingModel(reranking_provider_name="test_provider", reranking_model_name="test_model")
        assert model.reranking_provider_name == "test_provider"
        assert model.reranking_model_name == "test_model"

    def test_serialization(self) -> None:
        """Test RerankingModel serialization."""
        model = RerankingModel(reranking_provider_name="provider", reranking_model_name="model")
        data = model.model_dump()
        assert data["reranking_provider_name"] == "provider"
        assert data["reranking_model_name"] == "model"

    def test_direct_instantiation(self) -> None:
        """Test RerankingModel direct instantiation alongside builder."""
        direct = RerankingModel(reranking_provider_name="provider", reranking_model_name="model")
        builder = RerankingModel.builder().reranking_provider_name("provider").reranking_model_name("model").build()

        assert direct.reranking_provider_name == builder.reranking_provider_name
        assert direct.reranking_model_name == builder.reranking_model_name


class TestTagInfo:
    """Test TagInfo model."""

    def test_builder_pattern(self) -> None:
        """Test TagInfo builder pattern functionality."""
        tag = TagInfo.builder().id("tag_id").name("tag_name").type("knowledge_type").binding_count(5).build()

        assert tag.id == "tag_id"
        assert tag.name == "tag_name"
        assert tag.type == "knowledge_type"
        assert tag.binding_count == 5

    def test_field_validation(self) -> None:
        """Test TagInfo field validation."""
        tag = TagInfo(id="tag_id", name="tag_name", type="knowledge_type", binding_count=5)
        assert tag.id == "tag_id"
        assert tag.name == "tag_name"
        assert tag.type == "knowledge_type"
        assert tag.binding_count == 5

    def test_serialization(self) -> None:
        """Test TagInfo serialization."""
        tag = TagInfo(id="id", name="name", type="knowledge_type")
        data = tag.model_dump()
        assert data["id"] == "id"
        assert data["name"] == "name"
        assert data["type"] == "knowledge_type"

    def test_direct_instantiation(self) -> None:
        """Test TagInfo direct instantiation alongside builder."""
        direct = TagInfo(id="id", name="name", type="knowledge_type")
        builder = TagInfo.builder().id("id").name("name").type("knowledge_type").build()

        assert direct.id == builder.id
        assert direct.name == builder.name
        assert direct.type == builder.type
