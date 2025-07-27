import pytest
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge_base.v1.model.dataset.reranking_model import RerankingModel
from dify_oapi.api.knowledge_base.v1.model.dataset.external_knowledge_info import (
    ExternalKnowledgeInfo,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_filtering_conditions import (
    MetadataFilteringConditions,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.filter_condition import (
    FilterCondition,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.dataset_info import DatasetInfo
from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo
from dify_oapi.api.knowledge_base.v1.model.metadata.metadata_info import MetadataInfo

# Import new dataset request/response models
from dify_oapi.api.knowledge_base.v1.model.dataset.create_request import (
    CreateDatasetRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.create_response import (
    CreateDatasetResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.list_request import (
    ListDatasetsRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.list_response import (
    ListDatasetsResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.get_request import GetDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.get_response import (
    GetDatasetResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.update_request import (
    UpdateDatasetRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.update_response import (
    UpdateDatasetResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.delete_request import (
    DeleteDatasetRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.delete_response import (
    DeleteDatasetResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_request import (
    RetrieveDatasetRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import (
    RetrieveDatasetResponse,
)


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
        model = RerankingModel(
            reranking_provider_name="provider", reranking_model_name="model"
        )
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
        condition1 = FilterCondition(
            name="field1", comparison_operator="contains", value="value1"
        )
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
        condition = FilterCondition(
            name="field", comparison_operator="is", value="test"
        )
        filtering = (
            MetadataFilteringConditions.builder().add_condition(condition).build()
        )
        assert len(filtering.conditions) == 1
        assert filtering.conditions[0].name == "field"


class TestRetrievalModel:
    def test_builder_pattern(self):
        reranking = RerankingModel(
            reranking_provider_name="provider", reranking_model_name="model"
        )
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
            id="test_id", name="test_name", description="test_desc", app_count=5
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


# New tests for dataset request/response models
class TestCreateDatasetRequest:
    def test_builder_pattern(self):
        retrieval_model = RetrievalModel(search_method="semantic_search")
        request = (
            CreateDatasetRequest.builder()
            .name("test_dataset")
            .description("test description")
            .indexing_technique("high_quality")
            .permission("only_me")
            .provider("vendor")
            .embedding_model("text-embedding-3")
            .embedding_model_provider("openai")
            .retrieval_model(retrieval_model)
            .build()
        )
        assert request.name == "test_dataset"
        assert request.description == "test description"
        assert request.indexing_technique == "high_quality"
        assert request.permission == "only_me"
        assert request.provider == "vendor"
        assert request.embedding_model == "text-embedding-3"
        assert request.embedding_model_provider == "openai"
        assert request.retrieval_model.search_method == "semantic_search"

    def test_required_fields_only(self):
        request = CreateDatasetRequest(name="test_dataset")
        assert request.name == "test_dataset"
        assert request.description is None
        assert request.indexing_technique is None

    def test_serialization(self):
        request = CreateDatasetRequest(name="test", description="desc")
        data = request.model_dump(exclude_none=True)
        assert data["name"] == "test"
        assert data["description"] == "desc"
        assert "indexing_technique" not in data


class TestCreateDatasetResponse:
    def test_inheritance(self):
        response = CreateDatasetResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"
        assert hasattr(response, "description")
        assert hasattr(response, "provider")


class TestListDatasetsRequest:
    def test_builder_pattern(self):
        request = (
            ListDatasetsRequest.builder()
            .keyword("test")
            .tag_ids(["tag1", "tag2"])
            .page(2)
            .limit("10")
            .include_all(True)
            .build()
        )
        assert request.keyword == "test"
        assert request.tag_ids == ["tag1", "tag2"]
        assert request.page == 2
        assert request.limit == "10"
        assert request.include_all is True

    def test_empty_request(self):
        request = ListDatasetsRequest.builder().build()
        assert request.keyword is None
        assert request.tag_ids is None
        assert request.page is None
        assert request.limit is None
        assert request.include_all is None


class TestListDatasetsResponse:
    def test_builder_pattern(self):
        dataset1 = DatasetInfo(id="id1", name="name1")
        dataset2 = DatasetInfo(id="id2", name="name2")

        response = (
            ListDatasetsResponse.builder()
            .data([dataset1, dataset2])
            .has_more(True)
            .limit(20)
            .total(50)
            .page(1)
            .build()
        )
        assert len(response.data) == 2
        assert response.data[0].id == "id1"
        assert response.data[1].id == "id2"
        assert response.has_more is True
        assert response.limit == 20
        assert response.total == 50
        assert response.page == 1

    def test_default_values(self):
        response = ListDatasetsResponse.builder().build()
        assert response.data == []
        assert response.has_more is False
        assert response.limit == 20
        assert response.total == 0
        assert response.page == 1


class TestGetDatasetRequest:
    def test_builder_pattern(self):
        request = GetDatasetRequest.builder().dataset_id("test_id").build()
        assert request.dataset_id == "test_id"

    def test_required_field(self):
        request = GetDatasetRequest(dataset_id="test_id")
        assert request.dataset_id == "test_id"


class TestGetDatasetResponse:
    def test_inheritance(self):
        response = GetDatasetResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"
        assert hasattr(response, "description")
        assert hasattr(response, "provider")


class TestUpdateDatasetRequest:
    def test_builder_pattern(self):
        retrieval_model = RetrievalModel(search_method="hybrid_search")
        request = (
            UpdateDatasetRequest.builder()
            .dataset_id("test_id")
            .name("updated_name")
            .indexing_technique("economy")
            .permission("all_team_members")
            .embedding_model("new_model")
            .retrieval_model(retrieval_model)
            .partial_member_list(["user1", "user2"])
            .build()
        )
        assert request.dataset_id == "test_id"
        assert request.name == "updated_name"
        assert request.indexing_technique == "economy"
        assert request.permission == "all_team_members"
        assert request.embedding_model == "new_model"
        assert request.retrieval_model.search_method == "hybrid_search"
        assert request.partial_member_list == ["user1", "user2"]

    def test_partial_update(self):
        request = (
            UpdateDatasetRequest.builder()
            .dataset_id("test_id")
            .name("new_name")
            .build()
        )
        assert request.dataset_id == "test_id"
        assert request.name == "new_name"
        assert request.indexing_technique is None
        assert request.permission is None


class TestUpdateDatasetResponse:
    def test_inheritance(self):
        response = UpdateDatasetResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"
        assert hasattr(response, "description")
        assert hasattr(response, "provider")


class TestDeleteDatasetRequest:
    def test_builder_pattern(self):
        request = DeleteDatasetRequest.builder().dataset_id("test_id").build()
        assert request.dataset_id == "test_id"

    def test_required_field(self):
        request = DeleteDatasetRequest(dataset_id="test_id")
        assert request.dataset_id == "test_id"


class TestDeleteDatasetResponse:
    def test_empty_response(self):
        response = DeleteDatasetResponse()
        # Should be able to instantiate without any fields
        assert isinstance(response, DeleteDatasetResponse)


class TestRetrieveDatasetRequest:
    def test_builder_pattern(self):
        retrieval_model = RetrievalModel(search_method="full_text_search", top_k=5)
        request = (
            RetrieveDatasetRequest.builder()
            .dataset_id("test_id")
            .query("test query")
            .retrieval_model(retrieval_model)
            .external_retrieval_model({"key": "value"})
            .build()
        )
        assert request.dataset_id == "test_id"
        assert request.query == "test query"
        assert request.retrieval_model.search_method == "full_text_search"
        assert request.retrieval_model.top_k == 5
        assert request.external_retrieval_model == {"key": "value"}

    def test_required_fields_only(self):
        request = RetrieveDatasetRequest(dataset_id="test_id", query="test query")
        assert request.dataset_id == "test_id"
        assert request.query == "test query"
        assert request.retrieval_model is None
        assert request.external_retrieval_model is None


class TestRetrieveDatasetResponse:
    def test_builder_pattern(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import (
            QueryInfo,
            RetrievalRecord,
            SegmentInfo,
            DocumentInfo,
        )

        query = QueryInfo(content="test query")
        document = DocumentInfo(
            id="doc_id", data_source_type="upload_file", name="test.txt"
        )
        segment = SegmentInfo(
            id="seg_id",
            position=1,
            document_id="doc_id",
            content="test content",
            word_count=10,
            tokens=5,
            keywords=["test"],
            index_node_id="node_id",
            index_node_hash="hash",
            hit_count=1,
            enabled=True,
            status="completed",
            created_by="user",
            created_at=1234567890,
            indexing_at=1234567890,
            completed_at=1234567890,
            document=document,
        )
        record = RetrievalRecord(segment=segment, score=0.95)

        response = (
            RetrieveDatasetResponse.builder().query(query).records([record]).build()
        )
        assert response.query.content == "test query"
        assert len(response.records) == 1
        assert response.records[0].segment.id == "seg_id"
        assert response.records[0].score == 0.95
        assert response.records[0].segment.document.name == "test.txt"

    def test_empty_records(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import (
            QueryInfo,
        )

        query = QueryInfo(content="test query")
        response = RetrieveDatasetResponse(query=query, records=[])
        assert response.query.content == "test query"
        assert response.records == []

    def test_nested_builders(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import (
            QueryInfo,
            DocumentInfo,
        )

        query = QueryInfo.builder().content("test").build()
        document = (
            DocumentInfo.builder()
            .id("doc_id")
            .data_source_type("upload")
            .name("file.txt")
            .build()
        )

        assert query.content == "test"
        assert document.id == "doc_id"
        assert document.data_source_type == "upload"
        assert document.name == "file.txt"
