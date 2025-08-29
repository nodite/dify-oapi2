"""Tests for dataset API models."""

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse
from dify_oapi.api.knowledge.v1.model.dataset_info import DatasetInfo
from dify_oapi.api.knowledge.v1.model.delete_dataset_request import DeleteDatasetRequest
from dify_oapi.api.knowledge.v1.model.delete_dataset_response import DeleteDatasetResponse
from dify_oapi.api.knowledge.v1.model.get_dataset_request import GetDatasetRequest
from dify_oapi.api.knowledge.v1.model.get_dataset_response import GetDatasetResponse
from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest
from dify_oapi.api.knowledge.v1.model.list_datasets_response import ListDatasetsResponse
from dify_oapi.api.knowledge.v1.model.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request_body import RetrieveFromDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_response import RetrieveFromDatasetResponse
from dify_oapi.api.knowledge.v1.model.update_dataset_request import UpdateDatasetRequest
from dify_oapi.api.knowledge.v1.model.update_dataset_request_body import UpdateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.update_dataset_response import UpdateDatasetResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestCreateModels:
    """Test Create API models."""

    def test_request_builder(self) -> None:
        """Test CreateDatasetRequest builder pattern."""
        retrieval_model = RetrievalModel(search_method="semantic_search")
        request_body = (
            CreateDatasetRequestBody.builder()
            .name("test_dataset")
            .description("test description")
            .indexing_technique("high_quality")
            .permission("only_me")
            .provider("vendor")
            .model("text-embedding-3")
            .retrieval_model(retrieval_model)
            .build()
        )

        request = CreateDatasetRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.name == "test_dataset"
        assert request.request_body.description == "test description"
        assert request.request_body.indexing_technique == "high_quality"
        assert request.request_body.permission == "only_me"
        assert request.request_body.provider == "vendor"
        assert request.request_body.model == "text-embedding-3"
        assert request.request_body.retrieval_model is not None
        assert request.request_body.retrieval_model.search_method == "semantic_search"

    def test_request_validation(self) -> None:
        """Test CreateDatasetRequest validation."""
        request = CreateDatasetRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets"

    def test_request_body_builder(self) -> None:
        """Test CreateDatasetRequestBody builder pattern."""
        request_body = CreateDatasetRequestBody.builder().name("test").build()
        assert request_body.name == "test"

    def test_request_body_validation(self) -> None:
        """Test CreateDatasetRequestBody validation."""
        request_body = CreateDatasetRequestBody(name="test_dataset")
        assert request_body.name == "test_dataset"

    def test_response_inheritance(self) -> None:
        """Test CreateDatasetResponse inherits from BaseResponse."""
        response = CreateDatasetResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test CreateDatasetResponse data access."""
        response = CreateDatasetResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"


class TestListModels:
    """Test List API models."""

    def test_request_builder(self) -> None:
        """Test ListDatasetsRequest builder pattern."""
        request = ListDatasetsRequest.builder().page(2).limit(10).build()
        query_keys = [key for key, value in request.queries]
        assert "page" in query_keys
        assert "limit" in query_keys

    def test_request_validation(self) -> None:
        """Test ListDatasetsRequest validation."""
        request = ListDatasetsRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets"

    def test_response_inheritance(self) -> None:
        """Test ListDatasetsResponse inherits from BaseResponse."""
        response = ListDatasetsResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test ListDatasetsResponse data access."""
        dataset1 = DatasetInfo(id="id1", name="name1")
        dataset2 = DatasetInfo(id="id2", name="name2")
        response = ListDatasetsResponse(data=[dataset1, dataset2], has_more=True, limit=20, total=50, page=1)

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
        """Test GetDatasetRequest builder pattern."""
        request = GetDatasetRequest.builder().dataset_id("test_id").build()
        assert request.dataset_id == "test_id"
        assert request.paths["dataset_id"] == "test_id"

    def test_request_validation(self) -> None:
        """Test GetDatasetRequest validation."""
        request = GetDatasetRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id"

    def test_response_inheritance(self) -> None:
        """Test GetDatasetResponse inherits from BaseResponse."""
        response = GetDatasetResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetDatasetResponse data access."""
        response = GetDatasetResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"


class TestUpdateModels:
    """Test Update API models."""

    def test_request_builder(self) -> None:
        """Test UpdateDatasetRequest builder pattern."""
        retrieval_model = RetrievalModel(search_method="hybrid_search")
        request_body = (
            UpdateDatasetRequestBody.builder()
            .name("updated_name")
            .indexing_technique("economy")
            .permission("all_team_members")
            .model("new_model")
            .retrieval_model(retrieval_model)
            .build()
        )

        request = UpdateDatasetRequest.builder().dataset_id("test_id").request_body(request_body).build()
        assert request.dataset_id == "test_id"
        assert request.paths["dataset_id"] == "test_id"
        assert request.request_body is not None
        assert request.request_body.name == "updated_name"
        assert request.request_body.indexing_technique == "economy"
        assert request.request_body.permission == "all_team_members"
        assert request.request_body.model == "new_model"
        assert request.request_body.retrieval_model is not None
        assert request.request_body.retrieval_model.search_method == "hybrid_search"

    def test_request_validation(self) -> None:
        """Test UpdateDatasetRequest validation."""
        request = UpdateDatasetRequest.builder().build()
        assert request.http_method == HttpMethod.PATCH
        assert request.uri == "/v1/datasets/:dataset_id"

    def test_request_body_builder(self) -> None:
        """Test UpdateDatasetRequestBody builder pattern."""
        request_body = UpdateDatasetRequestBody.builder().name("updated").build()
        assert request_body.name == "updated"

    def test_request_body_validation(self) -> None:
        """Test UpdateDatasetRequestBody validation."""
        request_body = UpdateDatasetRequestBody(name="updated_name")
        assert request_body.name == "updated_name"

    def test_response_inheritance(self) -> None:
        """Test UpdateDatasetResponse inherits from BaseResponse."""
        response = UpdateDatasetResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UpdateDatasetResponse data access."""
        response = UpdateDatasetResponse(id="test_id", name="test_name")
        assert response.id == "test_id"
        assert response.name == "test_name"


class TestDeleteModels:
    """Test Delete API models."""

    def test_request_builder(self) -> None:
        """Test DeleteDatasetRequest builder pattern."""
        request = DeleteDatasetRequest.builder().dataset_id("test_id").build()
        assert request.dataset_id == "test_id"
        assert request.paths["dataset_id"] == "test_id"

    def test_request_validation(self) -> None:
        """Test DeleteDatasetRequest validation."""
        request = DeleteDatasetRequest.builder().build()
        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/datasets/:dataset_id"

    def test_response_inheritance(self) -> None:
        """Test DeleteDatasetResponse inherits from BaseResponse."""
        response = DeleteDatasetResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test DeleteDatasetResponse data access."""
        response = DeleteDatasetResponse()
        assert isinstance(response, DeleteDatasetResponse)


class TestRetrieveModels:
    """Test Retrieve API models."""

    def test_request_builder(self) -> None:
        """Test RetrieveFromDatasetRequest builder pattern."""
        retrieval_model = RetrievalModel(search_method="full_text_search", top_k=5)
        request_body = (
            RetrieveFromDatasetRequestBody.builder().query("test query").retrieval_model(retrieval_model).build()
        )

        request = RetrieveFromDatasetRequest.builder().dataset_id("test_id").request_body(request_body).build()
        assert request.dataset_id == "test_id"
        assert request.paths["dataset_id"] == "test_id"
        assert request.request_body is not None
        assert request.request_body.query == "test query"
        assert request.request_body.retrieval_model is not None
        assert request.request_body.retrieval_model.search_method == "full_text_search"
        assert request.request_body.retrieval_model.top_k == 5

    def test_request_validation(self) -> None:
        """Test RetrieveFromDatasetRequest validation."""
        request = RetrieveFromDatasetRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/retrieve"

    def test_request_body_builder(self) -> None:
        """Test RetrieveFromDatasetRequestBody builder pattern."""
        request_body = RetrieveFromDatasetRequestBody.builder().query("test").build()
        assert request_body.query == "test"

    def test_request_body_validation(self) -> None:
        """Test RetrieveFromDatasetRequestBody validation."""
        request_body = RetrieveFromDatasetRequestBody(query="test query")
        assert request_body.query == "test query"

    def test_response_inheritance(self) -> None:
        """Test RetrieveFromDatasetResponse inherits from BaseResponse."""
        response = RetrieveFromDatasetResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test RetrieveFromDatasetResponse data access."""
        response = RetrieveFromDatasetResponse(query="test query", records=[])
        assert response.query == "test query"
        assert response.records == []
