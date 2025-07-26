import pytest
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge_base.v1.model.dataset.reranking_model import RerankingModel
from dify_oapi.api.knowledge_base.v1.model.dataset.external_knowledge_info import ExternalKnowledgeInfo
from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_filtering_conditions import MetadataFilteringConditions
from dify_oapi.api.knowledge_base.v1.model.dataset.filter_condition import FilterCondition
from dify_oapi.api.knowledge_base.v1.model.dataset.dataset_info import DatasetInfo
from dify_oapi.api.knowledge_base.v1.model.dataset.tag_info import TagInfo
from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_info import MetadataInfo


class TestRerankingModel:
    def test_builder_pattern(self):
        model = (
            RerankingModel.builder()
            .reranking_provider_name("test_provider")
            .reranking_model_name("test_model")
            .build()
        )
        assert model.reranking_provider_name == "test_provider"
        assert model.reranking_model_name == "test_model"

    def test_serialization(self):
        model = RerankingModel(reranking_provider_name="provider", reranking_model_name="model")
        data = model.model_dump()
        assert data["reranking_provider_name"] == "provider"
        assert data["reranking_model_name"] == "model"


class TestFilterCondition:
    def test_builder_pattern(self):
        condition = (
            FilterCondition.builder()
            .name("test_field")
            .comparison_operator("contains")
            .value("test_value")
            .build()
        )
        assert condition.name == "test_field"
        assert condition.comparison_operator == "contains"
        assert condition.value == "test_value"

    def test_optional_value(self):
        condition = (
            FilterCondition.builder()
            .name("test_field")
            .comparison_operator("empty")
            .build()
        )
        assert condition.name == "test_field"
        assert condition.comparison_operator == "empty"
        assert condition.value is None


class TestMetadataFilteringConditions:
    def test_builder_pattern(self):
        condition1 = FilterCondition(name="field1", comparison_operator="contains", value="value1")
        condition2 = FilterCondition(name="field2", comparison_operator="=", value=42)
        
        filtering = (
            MetadataFilteringConditions.builder()
            .logical_operator("or")
            .conditions([condition1, condition2])
            .build()
        )
        assert filtering.logical_operator == "or"
        assert len(filtering.conditions) == 2
        assert filtering.conditions[0].name == "field1"
        assert filtering.conditions[1].value == 42

    def test_add_condition(self):
        condition = FilterCondition(name="field", comparison_operator="is", value="test")
        filtering = (
            MetadataFilteringConditions.builder()
            .add_condition(condition)
            .build()
        )
        assert len(filtering.conditions) == 1
        assert filtering.conditions[0].name == "field"


class TestRetrievalModel:
    def test_builder_pattern(self):
        reranking = RerankingModel(reranking_provider_name="provider", reranking_model_name="model")
        filtering = MetadataFilteringConditions(logical_operator="and", conditions=[])
        
        model = (
            RetrievalModel.builder()
            .search_method("hybrid_search")
            .reranking_enable(True)
            .reranking_model(reranking)
            .top_k(10)
            .score_threshold_enabled(True)
            .score_threshold(0.8)
            .metadata_filtering_conditions(filtering)
            .build()
        )
        assert model.search_method == "hybrid_search"
        assert model.reranking_enable is True
        assert model.top_k == 10
        assert model.score_threshold == 0.8
        assert model.metadata_filtering_conditions is not None

    def test_default_search_method(self):
        model = RetrievalModel.builder().build()
        assert model.search_method == "semantic_search"


class TestExternalKnowledgeInfo:
    def test_builder_pattern(self):
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

    def test_all_optional_fields(self):
        info = ExternalKnowledgeInfo.builder().build()
        assert info.external_knowledge_id is None
        assert info.external_knowledge_api_id is None
        assert info.external_knowledge_api_name is None
        assert info.external_knowledge_api_endpoint is None


class TestTagInfo:
    def test_builder_pattern(self):
        tag = (
            TagInfo.builder()
            .id("tag_id")
            .name("tag_name")
            .type("knowledge")
            .binding_count(5)
            .build()
        )
        assert tag.id == "tag_id"
        assert tag.name == "tag_name"
        assert tag.type == "knowledge"
        assert tag.binding_count == 5

    def test_required_fields(self):
        tag = TagInfo(id="id", name="name")
        assert tag.id == "id"
        assert tag.name == "name"
        assert tag.type is None
        assert tag.binding_count is None


class TestMetadataInfo:
    def test_builder_pattern(self):
        metadata = (
            MetadataInfo.builder()
            .id("meta_id")
            .name("meta_name")
            .type("string")
            .use_count(10)
            .build()
        )
        assert metadata.id == "meta_id"
        assert metadata.name == "meta_name"
        assert metadata.type == "string"
        assert metadata.use_count == 10

    def test_required_fields(self):
        metadata = MetadataInfo(id="id", name="name", type="string")
        assert metadata.id == "id"
        assert metadata.name == "name"
        assert metadata.type == "string"
        assert metadata.use_count is None


class TestDatasetInfo:
    def test_builder_pattern(self):
        tag = TagInfo(id="tag_id", name="tag_name")
        external_info = ExternalKnowledgeInfo(external_knowledge_id="ext_id")
        retrieval_model = RetrievalModel(search_method="semantic_search")
        
        dataset = (
            DatasetInfo.builder()
            .id("dataset_id")
            .name("dataset_name")
            .description("test description")
            .provider("vendor")
            .permission("only_me")
            .indexing_technique("high_quality")
            .app_count(2)
            .document_count(10)
            .word_count(1000)
            .embedding_model("text-embedding-3")
            .embedding_model_provider("openai")
            .embedding_available(True)
            .tags([tag])
            .external_knowledge_info(external_info)
            .retrieval_model_dict(retrieval_model)
            .build()
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
        assert len(dataset.tags) == 1
        assert dataset.tags[0].id == "tag_id"
        assert dataset.external_knowledge_info.external_knowledge_id == "ext_id"
        assert dataset.retrieval_model_dict.search_method == "semantic_search"

    def test_required_fields_only(self):
        dataset = DatasetInfo(id="id", name="name")
        assert dataset.id == "id"
        assert dataset.name == "name"
        assert dataset.description is None
        assert dataset.tags is None

    def test_serialization_deserialization(self):
        dataset = DatasetInfo(
            id="test_id",
            name="test_name",
            description="test_desc",
            app_count=5
        )
        data = dataset.model_dump()
        assert data["id"] == "test_id"
        assert data["name"] == "test_name"
        assert data["description"] == "test_desc"
        assert data["app_count"] == 5
        
        # Test deserialization
        new_dataset = DatasetInfo.model_validate(data)
        assert new_dataset.id == "test_id"
        assert new_dataset.name == "test_name"
        assert new_dataset.description == "test_desc"
        assert new_dataset.app_count == 5