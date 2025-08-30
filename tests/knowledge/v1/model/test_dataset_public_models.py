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
        model = RetrievalModel(
            search_method="hybrid_search",
            reranking_enable=True,
            top_k=10,
            score_threshold_enabled=True,
            score_threshold=0.8,
        )

        assert model.search_method == "hybrid_search"
        assert model.reranking_enable is True
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
        model = RerankingModel.builder().provider("provider").model("model").build()

        assert model.provider == "provider"
        assert model.model == "model"

    def test_field_validation(self) -> None:
        """Test RerankingModel field validation."""
        model = RerankingModel(provider="test_provider", model="test_model")
        assert model.provider == "test_provider"
        assert model.model == "test_model"

    def test_serialization(self) -> None:
        """Test RerankingModel serialization."""
        model = RerankingModel(provider="provider", model="model")
        data = model.model_dump()
        assert data["provider"] == "provider"
        assert data["model"] == "model"

    def test_direct_instantiation(self) -> None:
        """Test RerankingModel direct instantiation alongside builder."""
        direct = RerankingModel(provider="provider", model="model")
        builder = RerankingModel.builder().provider("provider").model("model").build()

        assert direct.provider == builder.provider
        assert direct.model == builder.model


class TestTagInfo:
    """Test TagInfo model."""

    def test_builder_pattern(self) -> None:
        """Test TagInfo builder pattern functionality."""
        tag = TagInfo.builder().id("tag_id").name("tag_name").type("knowledge").binding_count(5).build()

        assert tag.id == "tag_id"
        assert tag.name == "tag_name"
        assert tag.type == "knowledge"
        assert tag.binding_count == 5

    def test_field_validation(self) -> None:
        """Test TagInfo field validation."""
        tag = TagInfo(id="tag_id", name="tag_name", type="knowledge", binding_count=5)
        assert tag.id == "tag_id"
        assert tag.name == "tag_name"
        assert tag.type == "knowledge"
        assert tag.binding_count == 5

    def test_serialization(self) -> None:
        """Test TagInfo serialization."""
        tag = TagInfo(id="id", name="name", type="knowledge")
        data = tag.model_dump()
        assert data["id"] == "id"
        assert data["name"] == "name"
        assert data["type"] == "knowledge"

    def test_direct_instantiation(self) -> None:
        """Test TagInfo direct instantiation alongside builder."""
        direct = TagInfo(id="id", name="name", type="knowledge")
        builder = TagInfo.builder().id("id").name("name").type("knowledge").build()

        assert direct.id == builder.id
        assert direct.name == builder.name
        assert direct.type == builder.type
