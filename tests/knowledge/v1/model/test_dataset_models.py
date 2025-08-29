"""Tests for dataset API models."""

from dify_oapi.api.knowledge.v1.model.dataset.create_request import CreateRequest
from dify_oapi.api.knowledge.v1.model.dataset.create_request_body import CreateRequestBody
from dify_oapi.api.knowledge.v1.model.dataset.create_response import CreateResponse
from dify_oapi.api.knowledge.v1.model.dataset.dataset_info import DatasetInfo
from dify_oapi.api.knowledge.v1.model.dataset.delete_request import DeleteRequest
from dify_oapi.api.knowledge.v1.model.dataset.delete_response import DeleteResponse
from dify_oapi.api.knowledge.v1.model.dataset.get_request import GetRequest
from dify_oapi.api.knowledge.v1.model.dataset.get_response import GetResponse
from dify_oapi.api.knowledge.v1.model.dataset.list_request import ListRequest
from dify_oapi.api.knowledge.v1.model.dataset.list_response import ListResponse
from dify_oapi.api.knowledge.v1.model.dataset.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge.v1.model.dataset.retrieve_request import RetrieveRequest
from dify_oapi.api.knowledge.v1.model.dataset.retrieve_request_body import RetrieveRequestBody
from dify_oapi.api.knowledge.v1.model.dataset.retrieve_response import RetrieveResponse
from dify_oapi.api.knowledge.v1.model.dataset.update_request import UpdateRequest
from dify_oapi.api.knowledge.v1.model.dataset.update_request_body import UpdateRequestBody
from dify_oapi.api.knowledge.v1.model.dataset.update_response import UpdateResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestCreateModels:
    """Test Create API models."""

    def test_request_builder(self) -> None:
        """Test CreateRequest builder pattern."""
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
        assert request.request_body is not None
        assert request.request_body.name == "test_dataset"
        assert request.request_body.description == "test description"
        assert request.request_body.indexing_technique == "high_quality"
        assert request.request_body.permission == "only_me"
        assert request.request_body.provider == "vendor"
        assert request.request_body.embedding_model == "text-embedding-3"
        assert request.request_body.embedding_model_provider == "openai"
        assert request.request_body.retrieval_model is not None
        assert request.request_body.retrieval_model.search_method == "semantic_search"

    def test_request_validation(self) -> None:
        """Test CreateRequest validation."""
        request = CreateRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets"

    def test_request_body_builder(self) -> None:
        """Test CreateRequestBody builder pattern."""
        request_body = CreateRequestBody.builder().name("test").build()
        assert request_body.name == "test"

    def test_request_body_validation(self) -> None:
        """Test CreateRequestBody validation."""
        request_body = CreateRequestBody(name="test_dataset")
        assert request_body.name == "test_dataset"

    def test_response_inheritance(self) -> None:
        """Test CreateResponse inherits from BaseResponse."""
        response = CreateResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test CreateResponse data access."""
        response = CreateResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"


class TestListModels:
    """Test List API models."""

    def test_request_builder(self) -> None:
        """Test ListRequest builder pattern."""
        request = (
            ListRequest.builder()
            .keyword("test")
            .tag_ids(["tag1", "tag2"])
            .page(2)
            .limit("10")
            .include_all(True)
            .build()
        )
        query_keys = [key for key, value in request.queries]
        assert "keyword" in query_keys
        assert "tag_ids" in query_keys
        assert "page" in query_keys
        assert "limit" in query_keys
        assert "include_all" in query_keys

    def test_request_validation(self) -> None:
        """Test ListRequest validation."""
        request = ListRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets"

    def test_response_inheritance(self) -> None:
        """Test ListResponse inherits from BaseResponse."""
        response = ListResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test ListResponse data access."""
        dataset1 = DatasetInfo(id="id1", name="name1")
        dataset2 = DatasetInfo(id="id2", name="name2")
        response = ListResponse(data=[dataset1, dataset2], has_more=True, limit=20, total=50, page=1)

        assert response.data is not None
        assert len(response.data) == 2
        assert response.data[0].id == "id1"
        assert response.data[1].id == "id2"
        assert response.has_more is True
        assert response.limit == 20
        assert response.total == 50
        assert response.page == 1


class TestGetModels:
    """Test Get API models."""

    def test_request_builder(self) -> None:
        """Test GetRequest builder pattern."""
        request = GetRequest.builder().dataset_id("test_id").build()
        assert request.dataset_id == "test_id"
        assert request.paths["dataset_id"] == "test_id"

    def test_request_validation(self) -> None:
        """Test GetRequest validation."""
        request = GetRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id"

    def test_response_inheritance(self) -> None:
        """Test GetResponse inherits from BaseResponse."""
        response = GetResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetResponse data access."""
        response = GetResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"


class TestUpdateModels:
    """Test Update API models."""

    def test_request_builder(self) -> None:
        """Test UpdateRequest builder pattern."""
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
        assert request.request_body is not None
        assert request.request_body.name == "updated_name"
        assert request.request_body.indexing_technique == "economy"
        assert request.request_body.permission == "all_team_members"
        assert request.request_body.embedding_model == "new_model"
        assert request.request_body.retrieval_model is not None
        assert request.request_body.retrieval_model.search_method == "hybrid_search"
        assert request.request_body.partial_member_list == ["user1", "user2"]

    def test_request_validation(self) -> None:
        """Test UpdateRequest validation."""
        request = UpdateRequest.builder().build()
        assert request.http_method == HttpMethod.PATCH
        assert request.uri == "/v1/datasets/:dataset_id"

    def test_request_body_builder(self) -> None:
        """Test UpdateRequestBody builder pattern."""
        request_body = UpdateRequestBody.builder().name("updated").build()
        assert request_body.name == "updated"

    def test_request_body_validation(self) -> None:
        """Test UpdateRequestBody validation."""
        request_body = UpdateRequestBody(name="updated_name")
        assert request_body.name == "updated_name"

    def test_response_inheritance(self) -> None:
        """Test UpdateResponse inherits from BaseResponse."""
        response = UpdateResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UpdateResponse data access."""
        response = UpdateResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"


class TestDeleteModels:
    """Test Delete API models."""

    def test_request_builder(self) -> None:
        """Test DeleteRequest builder pattern."""
        request = DeleteRequest.builder().dataset_id("test_id").build()
        assert request.dataset_id == "test_id"
        assert request.paths["dataset_id"] == "test_id"

    def test_request_validation(self) -> None:
        """Test DeleteRequest validation."""
        request = DeleteRequest.builder().build()
        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/datasets/:dataset_id"

    def test_response_inheritance(self) -> None:
        """Test DeleteResponse inherits from BaseResponse."""
        response = DeleteResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test DeleteResponse data access."""
        response = DeleteResponse()
        assert isinstance(response, DeleteResponse)


class TestRetrieveModels:
    """Test Retrieve API models."""

    def test_request_builder(self) -> None:
        """Test RetrieveRequest builder pattern."""
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
        assert request.request_body is not None
        assert request.request_body.query == "test query"
        assert request.request_body.retrieval_model is not None
        assert request.request_body.retrieval_model.search_method == "full_text_search"
        assert request.request_body.retrieval_model.top_k == 5
        assert request.request_body.external_retrieval_model == {"key": "value"}

    def test_request_validation(self) -> None:
        """Test RetrieveRequest validation."""
        request = RetrieveRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/retrieve"

    def test_request_body_builder(self) -> None:
        """Test RetrieveRequestBody builder pattern."""
        request_body = RetrieveRequestBody.builder().query("test").build()
        assert request_body.query == "test"

    def test_request_body_validation(self) -> None:
        """Test RetrieveRequestBody validation."""
        request_body = RetrieveRequestBody(query="test query")
        assert request_body.query == "test query"

    def test_response_inheritance(self) -> None:
        """Test RetrieveResponse inherits from BaseResponse."""
        response = RetrieveResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test RetrieveResponse data access."""
        from dify_oapi.api.knowledge.v1.model.dataset.retrieve_response import QueryInfo

        query = QueryInfo(content="test query")
        response = RetrieveResponse(query=query, records=[])
        assert response.query is not None
        assert response.query.content == "test query"
        assert response.records == []
