# Import new dataset request/response models
from dify_oapi.api.knowledge_base.v1.model.dataset.create_request import (
    CreateRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.create_response import (
    CreateResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.dataset_info import DatasetInfo
from dify_oapi.api.knowledge_base.v1.model.dataset.delete_request import (
    DeleteRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.delete_response import (
    DeleteResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.external_knowledge_info import (
    ExternalKnowledgeInfo,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.filter_condition import (
    FilterCondition,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.get_request import GetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.get_response import (
    GetResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.list_request import (
    ListRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.list_response import (
    ListResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_filtering_conditions import (
    MetadataFilteringConditions,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.reranking_model import RerankingModel
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_request import (
    RetrieveRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import (
    RetrieveResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.update_request import (
    UpdateRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.update_response import (
    UpdateResponse,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.metadata_info import MetadataInfo
from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo


class TestRerankingModel:
    def test_direct_instantiation(self):
        model = RerankingModel(reranking_provider_name="test_provider", reranking_model_name="test_model")
        assert model.reranking_provider_name == "test_provider"
        assert model.reranking_model_name == "test_model"

    def test_serialization(self):
        model = RerankingModel(reranking_provider_name="provider", reranking_model_name="model")
        data = model.model_dump()
        assert data["reranking_provider_name"] == "provider"
        assert data["reranking_model_name"] == "model"


class TestFilterCondition:
    def test_direct_instantiation(self):
        condition = FilterCondition(name="test_field", comparison_operator="contains", value="test_value")
        assert condition.name == "test_field"
        assert condition.comparison_operator == "contains"
        assert condition.value == "test_value"

    def test_optional_value(self):
        condition = FilterCondition(name="test_field", comparison_operator="empty")
        assert condition.name == "test_field"
        assert condition.comparison_operator == "empty"
        assert condition.value is None


class TestMetadataFilteringConditions:
    def test_direct_instantiation(self):
        condition1 = FilterCondition(name="field1", comparison_operator="contains", value="value1")
        condition2 = FilterCondition(name="field2", comparison_operator="=", value=42)

        filtering = MetadataFilteringConditions(logical_operator="or", conditions=[condition1, condition2])
        assert filtering.logical_operator == "or"
        assert len(filtering.conditions) == 2
        assert filtering.conditions[0].name == "field1"
        assert filtering.conditions[1].value == 42

    def test_empty_conditions(self):
        filtering = MetadataFilteringConditions(logical_operator="and", conditions=[])
        assert filtering.logical_operator == "and"
        assert len(filtering.conditions) == 0


class TestKeywordSetting:
    def test_direct_instantiation(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import KeywordSetting

        setting = KeywordSetting(keyword_weight=0.7)
        assert setting.keyword_weight == 0.7

    def test_default_values(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import KeywordSetting

        setting = KeywordSetting()
        assert setting.keyword_weight is None


class TestVectorSetting:
    def test_direct_instantiation(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import VectorSetting

        setting = VectorSetting(
            vector_weight=0.3, embedding_model_name="text-embedding-3", embedding_provider_name="openai"
        )
        assert setting.vector_weight == 0.3
        assert setting.embedding_model_name == "text-embedding-3"
        assert setting.embedding_provider_name == "openai"

    def test_default_values(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import VectorSetting

        setting = VectorSetting()
        assert setting.vector_weight is None
        assert setting.embedding_model_name is None
        assert setting.embedding_provider_name is None


class TestWeights:
    def test_direct_instantiation(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import KeywordSetting, VectorSetting, Weights

        keyword_setting = KeywordSetting(keyword_weight=0.7)
        vector_setting = VectorSetting(vector_weight=0.3, embedding_model_name="text-embedding-3")

        weights = Weights(keyword_setting=keyword_setting, vector_setting=vector_setting)
        assert weights.keyword_setting.keyword_weight == 0.7
        assert weights.vector_setting.vector_weight == 0.3
        assert weights.vector_setting.embedding_model_name == "text-embedding-3"

    def test_default_values(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import Weights

        weights = Weights()
        assert weights.keyword_setting is None
        assert weights.vector_setting is None


class TestRetrievalModel:
    def test_direct_instantiation(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import KeywordSetting, VectorSetting, Weights

        reranking = RerankingModel(reranking_provider_name="provider", reranking_model_name="model")
        filtering = MetadataFilteringConditions(logical_operator="and", conditions=[])
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
        assert model.weights.keyword_setting.keyword_weight == 0.7
        assert model.weights.vector_setting.vector_weight == 0.3
        assert model.top_k == 10
        assert model.score_threshold == 0.8
        assert model.metadata_filtering_conditions is not None

    def test_default_values(self):
        model = RetrievalModel()
        assert model.search_method is None
        assert model.reranking_enable is None
        assert model.reranking_mode is None
        assert model.reranking_model is None
        assert model.weights is None
        assert model.top_k is None
        assert model.score_threshold_enabled is None
        assert model.score_threshold is None
        assert model.metadata_filtering_conditions is None

    def test_with_search_method_only(self):
        model = RetrievalModel(search_method="semantic_search")
        assert model.search_method == "semantic_search"


class TestExternalKnowledgeInfo:
    def test_direct_instantiation(self):
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

    def test_all_optional_fields(self):
        info = ExternalKnowledgeInfo()
        assert info.external_knowledge_id is None
        assert info.external_knowledge_api_id is None
        assert info.external_knowledge_api_name is None
        assert info.external_knowledge_api_endpoint is None


class TestTagInfo:
    def test_direct_instantiation(self):
        tag = TagInfo(id="tag_id", name="tag_name", type="knowledge", binding_count=5)
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
    def test_direct_instantiation(self):
        metadata = MetadataInfo(id="meta_id", name="meta_name", type="string", use_count=10)
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
    def test_direct_instantiation(self):
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
        dataset = DatasetInfo(id="test_id", name="test_name", description="test_desc", app_count=5)
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
class TestCreateRequest:
    def test_builder_pattern(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.create_request_body import CreateRequestBody

        retrieval_model = RetrievalModel(search_method="semantic_search")
        request_body = (
            CreateRequestBody.builder()
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

        request = CreateRequest.builder().request_body(request_body).build()
        assert request.request_body.name == "test_dataset"
        assert request.request_body.description == "test description"
        assert request.request_body.indexing_technique == "high_quality"
        assert request.request_body.permission == "only_me"
        assert request.request_body.provider == "vendor"
        assert request.request_body.embedding_model == "text-embedding-3"
        assert request.request_body.embedding_model_provider == "openai"
        assert request.request_body.retrieval_model.search_method == "semantic_search"

    def test_http_method_and_uri(self):
        request = CreateRequest.builder().build()
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets"


class TestCreateResponse:
    def test_inheritance(self):
        response = CreateResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"
        assert hasattr(response, "description")
        assert hasattr(response, "provider")


class TestListRequest:
    def test_builder_pattern(self):
        request = (
            ListRequest.builder()
            .keyword("test")
            .tag_ids(["tag1", "tag2"])
            .page(2)
            .limit("10")
            .include_all(True)
            .build()
        )
        # Check query parameters are set (queries is a list of tuples)
        query_keys = [key for key, value in request.queries]
        assert "keyword" in query_keys
        assert "tag_ids" in query_keys
        assert "page" in query_keys
        assert "limit" in query_keys
        assert "include_all" in query_keys

    def test_http_method_and_uri(self):
        request = ListRequest.builder().build()
        assert request.http_method.name == "GET"
        assert request.uri == "/v1/datasets"


class TestListResponse:
    def test_direct_instantiation(self):
        dataset1 = DatasetInfo(id="id1", name="name1")
        dataset2 = DatasetInfo(id="id2", name="name2")

        response = ListResponse(data=[dataset1, dataset2], has_more=True, limit=20, total=50, page=1)
        assert len(response.data) == 2
        assert response.data[0].id == "id1"
        assert response.data[1].id == "id2"
        assert response.has_more is True
        assert response.limit == 20
        assert response.total == 50
        assert response.page == 1

    def test_default_values(self):
        response = ListResponse()
        assert response.data is None
        assert response.has_more is None
        assert response.limit is None
        assert response.total is None
        assert response.page is None


class TestGetRequest:
    def test_builder_pattern(self):
        request = GetRequest.builder().dataset_id("test_id").build()
        assert request.dataset_id == "test_id"
        assert request.paths["dataset_id"] == "test_id"

    def test_http_method_and_uri(self):
        request = GetRequest.builder().build()
        assert request.http_method.name == "GET"
        assert request.uri == "/v1/datasets/:dataset_id"


class TestGetResponse:
    def test_inheritance(self):
        response = GetResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"
        assert hasattr(response, "description")
        assert hasattr(response, "provider")


class TestUpdateRequest:
    def test_builder_pattern(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.update_request_body import UpdateRequestBody

        retrieval_model = RetrievalModel(search_method="hybrid_search")
        request_body = (
            UpdateRequestBody.builder()
            .name("updated_name")
            .indexing_technique("economy")
            .permission("all_team_members")
            .embedding_model("new_model")
            .retrieval_model(retrieval_model)
            .partial_member_list(["user1", "user2"])
            .build()
        )

        request = UpdateRequest.builder().dataset_id("test_id").request_body(request_body).build()
        assert request.dataset_id == "test_id"
        assert request.paths["dataset_id"] == "test_id"
        assert request.request_body.name == "updated_name"
        assert request.request_body.indexing_technique == "economy"
        assert request.request_body.permission == "all_team_members"
        assert request.request_body.embedding_model == "new_model"
        assert request.request_body.retrieval_model.search_method == "hybrid_search"
        assert request.request_body.partial_member_list == ["user1", "user2"]

    def test_http_method_and_uri(self):
        request = UpdateRequest.builder().build()
        assert request.http_method.name == "PATCH"
        assert request.uri == "/v1/datasets/:dataset_id"


class TestUpdateResponse:
    def test_inheritance(self):
        response = UpdateResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"
        assert hasattr(response, "description")
        assert hasattr(response, "provider")


class TestDeleteRequest:
    def test_builder_pattern(self):
        request = DeleteRequest.builder().dataset_id("test_id").build()
        assert request.dataset_id == "test_id"
        assert request.paths["dataset_id"] == "test_id"

    def test_http_method_and_uri(self):
        request = DeleteRequest.builder().build()
        assert request.http_method.name == "DELETE"
        assert request.uri == "/v1/datasets/:dataset_id"


class TestDeleteResponse:
    def test_empty_response(self):
        response = DeleteResponse()
        # Should be able to instantiate without any fields
        assert isinstance(response, DeleteResponse)


class TestRetrieveRequest:
    def test_builder_pattern(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_request_body import RetrieveRequestBody

        retrieval_model = RetrievalModel(search_method="full_text_search", top_k=5)
        request_body = (
            RetrieveRequestBody.builder()
            .query("test query")
            .retrieval_model(retrieval_model)
            .external_retrieval_model({"key": "value"})
            .build()
        )

        request = RetrieveRequest.builder().dataset_id("test_id").request_body(request_body).build()
        assert request.dataset_id == "test_id"
        assert request.paths["dataset_id"] == "test_id"
        assert request.request_body.query == "test query"
        assert request.request_body.retrieval_model.search_method == "full_text_search"
        assert request.request_body.retrieval_model.top_k == 5
        assert request.request_body.external_retrieval_model == {"key": "value"}

    def test_http_method_and_uri(self):
        request = RetrieveRequest.builder().build()
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/:dataset_id/retrieve"


class TestRetrieveResponse:
    def test_direct_instantiation(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import (
            DocumentInfo,
            QueryInfo,
            RetrievalRecord,
            SegmentInfo,
        )

        query = QueryInfo(content="test query")
        document = DocumentInfo(id="doc_id", data_source_type="upload_file", name="test.txt")
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

        response = RetrieveResponse(query=query, records=[record])
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
        response = RetrieveResponse(query=query, records=[])
        assert response.query.content == "test query"
        assert response.records == []

    def test_nested_models(self):
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import (
            DocumentInfo,
            QueryInfo,
        )

        query = QueryInfo(content="test")
        document = DocumentInfo(id="doc_id", data_source_type="upload", name="file.txt")

        assert query.content == "test"
        assert document.id == "doc_id"
        assert document.data_source_type == "upload"
        assert document.name == "file.txt"
