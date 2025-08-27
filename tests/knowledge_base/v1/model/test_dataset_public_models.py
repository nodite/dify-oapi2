"""Tests for dataset public models."""

from dify_oapi.api.knowledge_base.v1.model.dataset.dataset_info import DatasetInfo
from dify_oapi.api.knowledge_base.v1.model.dataset.external_knowledge_info import ExternalKnowledgeInfo
from dify_oapi.api.knowledge_base.v1.model.dataset.filter_condition import FilterCondition
from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_filtering_conditions import MetadataFilteringConditions
from dify_oapi.api.knowledge_base.v1.model.dataset.reranking_model import RerankingModel
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge_base.v1.model.metadata.metadata_info import MetadataInfo
from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo


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
        tag = TagInfo(id="tag_id", name="tag_name")
        external_info = ExternalKnowledgeInfo(external_knowledge_id="ext_id")
        retrieval_model = RetrievalModel(search_method="semantic_search")

        dataset = DatasetInfo(
            id="dataset_id",
            name="dataset_name",
            description="test description",
            provider="vendor",
            permission="only_me",
            indexing_technique="high_quality",
            app_count=2,
            document_count=10,
            word_count=1000,
            embedding_model="text-embedding-3",
            embedding_model_provider="openai",
            embedding_available=True,
            tags=[tag],
            external_knowledge_info=external_info,
            retrieval_model_dict=retrieval_model,
        )

        assert dataset.id == "dataset_id"
        assert dataset.name == "dataset_name"
        assert dataset.description == "test description"
        assert dataset.provider == "vendor"
        assert dataset.permission == "only_me"
        assert dataset.indexing_technique == "high_quality"
        assert dataset.app_count == 2
        assert dataset.document_count == 10
        assert dataset.word_count == 1000
        assert dataset.embedding_model == "text-embedding-3"
        assert dataset.embedding_model_provider == "openai"
        assert dataset.embedding_available is True
        assert dataset.tags is not None
        assert len(dataset.tags) == 1
        assert dataset.tags[0].id == "tag_id"
        assert dataset.external_knowledge_info is not None
        assert dataset.external_knowledge_info.external_knowledge_id == "ext_id"
        assert dataset.retrieval_model_dict is not None
        assert dataset.retrieval_model_dict.search_method == "semantic_search"

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
        reranking = RerankingModel(reranking_provider_name="provider", reranking_model_name="model")
        filtering = MetadataFilteringConditions(logical_operator="and", conditions=[])

        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import KeywordSetting, VectorSetting, Weights

        keyword_setting = KeywordSetting(keyword_weight=0.7)
        vector_setting = VectorSetting(vector_weight=0.3)
        weights = Weights(keyword_setting=keyword_setting, vector_setting=vector_setting)

        model = RetrievalModel(
            search_method="hybrid_search",
            reranking_enable=True,
            reranking_mode="reranking_model",
            reranking_model=reranking,
            weights=weights,
            top_k=10,
            score_threshold_enabled=True,
            score_threshold=0.8,
            metadata_filtering_conditions=filtering,
        )

        assert model.search_method == "hybrid_search"
        assert model.reranking_enable is True
        assert model.reranking_mode == "reranking_model"
        assert model.weights is not None
        assert model.weights.keyword_setting is not None
        assert model.weights.keyword_setting.keyword_weight == 0.7
        assert model.weights.vector_setting is not None
        assert model.weights.vector_setting.vector_weight == 0.3
        assert model.top_k == 10
        assert model.score_threshold == 0.8
        assert model.metadata_filtering_conditions is not None

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


class TestFilterCondition:
    """Test FilterCondition model."""

    def test_builder_pattern(self) -> None:
        """Test FilterCondition builder pattern functionality."""
        condition = (
            FilterCondition.builder().name("test_field").comparison_operator("contains").value("test_value").build()
        )

        assert condition.name == "test_field"
        assert condition.comparison_operator == "contains"
        assert condition.value == "test_value"

    def test_field_validation(self) -> None:
        """Test FilterCondition field validation."""
        condition = FilterCondition(name="test_field", comparison_operator="contains", value="test_value")
        assert condition.name == "test_field"
        assert condition.comparison_operator == "contains"
        assert condition.value == "test_value"

    def test_serialization(self) -> None:
        """Test FilterCondition serialization."""
        condition = FilterCondition(name="field", comparison_operator="=", value=42)
        data = condition.model_dump()
        assert data["name"] == "field"
        assert data["comparison_operator"] == "="
        assert data["value"] == 42

    def test_direct_instantiation(self) -> None:
        """Test FilterCondition direct instantiation alongside builder."""
        direct = FilterCondition(name="field", comparison_operator="empty")
        builder = FilterCondition.builder().name("field").comparison_operator("empty").build()

        assert direct.name == builder.name
        assert direct.comparison_operator == builder.comparison_operator


class TestMetadataFilteringConditions:
    """Test MetadataFilteringConditions model."""

    def test_builder_pattern(self) -> None:
        """Test MetadataFilteringConditions builder pattern functionality."""
        condition1 = FilterCondition(name="field1", comparison_operator="contains", value="value1")
        condition2 = FilterCondition(name="field2", comparison_operator="=", value=42)

        filtering = (
            MetadataFilteringConditions.builder().logical_operator("or").conditions([condition1, condition2]).build()
        )

        assert filtering.logical_operator == "or"
        assert len(filtering.conditions) == 2
        assert filtering.conditions[0].name == "field1"
        assert filtering.conditions[1].value == 42

    def test_field_validation(self) -> None:
        """Test MetadataFilteringConditions field validation."""
        condition1 = FilterCondition(name="field1", comparison_operator="contains", value="value1")
        condition2 = FilterCondition(name="field2", comparison_operator="=", value=42)

        filtering = MetadataFilteringConditions(logical_operator="or", conditions=[condition1, condition2])
        assert filtering.logical_operator == "or"
        assert len(filtering.conditions) == 2
        assert filtering.conditions[0].name == "field1"
        assert filtering.conditions[1].value == 42

    def test_serialization(self) -> None:
        """Test MetadataFilteringConditions serialization."""
        filtering = MetadataFilteringConditions(logical_operator="and", conditions=[])
        data = filtering.model_dump()
        assert data["logical_operator"] == "and"
        assert data["conditions"] == []

    def test_direct_instantiation(self) -> None:
        """Test MetadataFilteringConditions direct instantiation alongside builder."""
        direct = MetadataFilteringConditions(logical_operator="and", conditions=[])
        builder = MetadataFilteringConditions.builder().logical_operator("and").conditions([]).build()

        assert direct.logical_operator == builder.logical_operator
        assert direct.conditions == builder.conditions


class TestExternalKnowledgeInfo:
    """Test ExternalKnowledgeInfo model."""

    def test_builder_pattern(self) -> None:
        """Test ExternalKnowledgeInfo builder pattern functionality."""
        info = (
            ExternalKnowledgeInfo.builder()
            .external_knowledge_id("ext_id")
            .external_knowledge_api_id("api_id")
            .external_knowledge_api_name("api_name")
            .external_knowledge_api_endpoint("https://api.example.com")
            .build()
        )

        assert info.external_knowledge_id == "ext_id"
        assert info.external_knowledge_api_id == "api_id"
        assert info.external_knowledge_api_name == "api_name"
        assert info.external_knowledge_api_endpoint == "https://api.example.com"

    def test_field_validation(self) -> None:
        """Test ExternalKnowledgeInfo field validation."""
        info = ExternalKnowledgeInfo(
            external_knowledge_id="ext_id",
            external_knowledge_api_id="api_id",
            external_knowledge_api_name="api_name",
            external_knowledge_api_endpoint="https://api.example.com",
        )

        assert info.external_knowledge_id == "ext_id"
        assert info.external_knowledge_api_id == "api_id"
        assert info.external_knowledge_api_name == "api_name"
        assert info.external_knowledge_api_endpoint == "https://api.example.com"

    def test_serialization(self) -> None:
        """Test ExternalKnowledgeInfo serialization."""
        info = ExternalKnowledgeInfo(external_knowledge_id="ext_id")
        data = info.model_dump()
        assert data["external_knowledge_id"] == "ext_id"

    def test_direct_instantiation(self) -> None:
        """Test ExternalKnowledgeInfo direct instantiation alongside builder."""
        direct = ExternalKnowledgeInfo()
        builder = ExternalKnowledgeInfo.builder().build()

        assert direct.external_knowledge_id == builder.external_knowledge_id


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
        tag = TagInfo(id="id", name="name")
        data = tag.model_dump()
        assert data["id"] == "id"
        assert data["name"] == "name"

    def test_direct_instantiation(self) -> None:
        """Test TagInfo direct instantiation alongside builder."""
        direct = TagInfo(id="id", name="name")
        builder = TagInfo.builder().id("id").name("name").build()

        assert direct.id == builder.id
        assert direct.name == builder.name


class TestMetadataInfo:
    """Test MetadataInfo model."""

    def test_builder_pattern(self) -> None:
        """Test MetadataInfo builder pattern functionality."""
        metadata = MetadataInfo.builder().id("meta_id").name("meta_name").type("string").use_count(10).build()

        assert metadata.id == "meta_id"
        assert metadata.name == "meta_name"
        assert metadata.type == "string"
        assert metadata.use_count == 10

    def test_field_validation(self) -> None:
        """Test MetadataInfo field validation."""
        metadata = MetadataInfo(id="meta_id", name="meta_name", type="string", use_count=10)
        assert metadata.id == "meta_id"
        assert metadata.name == "meta_name"
        assert metadata.type == "string"
        assert metadata.use_count == 10

    def test_serialization(self) -> None:
        """Test MetadataInfo serialization."""
        metadata = MetadataInfo(id="id", name="name", type="string")
        data = metadata.model_dump()
        assert data["id"] == "id"
        assert data["name"] == "name"
        assert data["type"] == "string"

    def test_direct_instantiation(self) -> None:
        """Test MetadataInfo direct instantiation alongside builder."""
        direct = MetadataInfo(id="id", name="name", type="string")
        builder = MetadataInfo.builder().id("id").name("name").type("string").build()

        assert direct.id == builder.id
        assert direct.name == builder.name
        assert direct.type == builder.type
