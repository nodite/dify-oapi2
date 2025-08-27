"""Unit tests for tag API models."""

from __future__ import annotations

from dify_oapi.api.knowledge_base.v1.model.tag.bind_request import BindRequest
from dify_oapi.api.knowledge_base.v1.model.tag.bind_request_body import BindRequestBody
from dify_oapi.api.knowledge_base.v1.model.tag.bind_response import BindResponse
from dify_oapi.api.knowledge_base.v1.model.tag.create_request import CreateRequest
from dify_oapi.api.knowledge_base.v1.model.tag.create_request_body import CreateRequestBody
from dify_oapi.api.knowledge_base.v1.model.tag.create_response import CreateResponse
from dify_oapi.api.knowledge_base.v1.model.tag.delete_request import DeleteRequest
from dify_oapi.api.knowledge_base.v1.model.tag.delete_request_body import DeleteRequestBody
from dify_oapi.api.knowledge_base.v1.model.tag.delete_response import DeleteResponse
from dify_oapi.api.knowledge_base.v1.model.tag.list_request import ListRequest
from dify_oapi.api.knowledge_base.v1.model.tag.list_response import ListResponse
from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_request import QueryBoundRequest
from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_response import QueryBoundResponse
from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request import UnbindRequest
from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request_body import UnbindRequestBody
from dify_oapi.api.knowledge_base.v1.model.tag.unbind_response import UnbindResponse
from dify_oapi.api.knowledge_base.v1.model.tag.update_request import UpdateRequest
from dify_oapi.api.knowledge_base.v1.model.tag.update_request_body import UpdateRequestBody
from dify_oapi.api.knowledge_base.v1.model.tag.update_response import UpdateResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestCreateModels:
    """Test Create API models."""

    def test_request_builder(self) -> None:
        """Test CreateRequest builder pattern."""
        request_body = CreateRequestBody.builder().name("test-tag").build()
        request = CreateRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.name == "test-tag"

    def test_request_validation(self) -> None:
        """Test CreateRequest validation."""
        request = CreateRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/tags"

    def test_request_body_builder(self) -> None:
        """Test CreateRequestBody builder pattern."""
        request_body = CreateRequestBody.builder().name("test-tag").build()
        assert request_body.name == "test-tag"

    def test_request_body_validation(self) -> None:
        """Test CreateRequestBody validation."""
        request_body = CreateRequestBody(name="test-tag")
        assert request_body.name == "test-tag"

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
        response = CreateResponse(id="tag-123", name="test-tag", type="knowledge", binding_count=5)
        assert response.id == "tag-123"
        assert response.name == "test-tag"
        assert response.type == "knowledge"
        assert response.binding_count == 5


class TestListModels:
    """Test List API models."""

    def test_request_builder(self) -> None:
        """Test ListRequest builder pattern."""
        request = ListRequest.builder().build()
        assert isinstance(request, ListRequest)

    def test_request_validation(self) -> None:
        """Test ListRequest validation."""
        request = ListRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/tags"

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
        response = ListResponse(data=[])
        assert response.data == []


class TestUpdateModels:
    """Test Update API models."""

    def test_request_builder(self) -> None:
        """Test UpdateRequest builder pattern."""
        request_body = UpdateRequestBody.builder().name("updated-tag").tag_id("tag-123").build()
        request = UpdateRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.name == "updated-tag"
        assert request.request_body.tag_id == "tag-123"

    def test_request_validation(self) -> None:
        """Test UpdateRequest validation."""
        request = UpdateRequest.builder().build()
        assert request.http_method == HttpMethod.PATCH
        assert request.uri == "/v1/datasets/tags"

    def test_request_body_builder(self) -> None:
        """Test UpdateRequestBody builder pattern."""
        request_body = UpdateRequestBody.builder().name("updated-tag").tag_id("tag-123").build()
        assert request_body.name == "updated-tag"
        assert request_body.tag_id == "tag-123"

    def test_request_body_validation(self) -> None:
        """Test UpdateRequestBody validation."""
        request_body = UpdateRequestBody(name="updated-tag", tag_id="tag-123")
        assert request_body.name == "updated-tag"
        assert request_body.tag_id == "tag-123"

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
        response = UpdateResponse(id="tag-123", name="updated-tag", type="knowledge", binding_count=3)
        assert response.id == "tag-123"
        assert response.name == "updated-tag"
        assert response.type == "knowledge"
        assert response.binding_count == 3


class TestDeleteModels:
    """Test Delete API models."""

    def test_request_builder(self) -> None:
        """Test DeleteRequest builder pattern."""
        request_body = DeleteRequestBody.builder().tag_id("tag-123").build()
        request = DeleteRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.tag_id == "tag-123"

    def test_request_validation(self) -> None:
        """Test DeleteRequest validation."""
        request = DeleteRequest.builder().build()
        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/datasets/tags"

    def test_request_body_builder(self) -> None:
        """Test DeleteRequestBody builder pattern."""
        request_body = DeleteRequestBody.builder().tag_id("tag-123").build()
        assert request_body.tag_id == "tag-123"

    def test_request_body_validation(self) -> None:
        """Test DeleteRequestBody validation."""
        request_body = DeleteRequestBody(tag_id="tag-123")
        assert request_body.tag_id == "tag-123"

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
        response = DeleteResponse(result="success")
        assert response.result == "success"


class TestBindModels:
    """Test Bind API models."""

    def test_request_builder(self) -> None:
        """Test BindRequest builder pattern."""
        request_body = BindRequestBody.builder().tag_ids(["tag-1", "tag-2"]).target_id("dataset-123").build()
        request = BindRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.tag_ids == ["tag-1", "tag-2"]
        assert request.request_body.target_id == "dataset-123"

    def test_request_validation(self) -> None:
        """Test BindRequest validation."""
        request = BindRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/tags/binding"

    def test_request_body_builder(self) -> None:
        """Test BindRequestBody builder pattern."""
        request_body = BindRequestBody.builder().tag_ids(["tag-1", "tag-2"]).target_id("dataset-123").build()
        assert request_body.tag_ids == ["tag-1", "tag-2"]
        assert request_body.target_id == "dataset-123"

    def test_request_body_validation(self) -> None:
        """Test BindRequestBody validation."""
        request_body = BindRequestBody(tag_ids=["tag-1", "tag-2"], target_id="dataset-123")
        assert request_body.tag_ids == ["tag-1", "tag-2"]
        assert request_body.target_id == "dataset-123"

    def test_response_inheritance(self) -> None:
        """Test BindResponse inherits from BaseResponse."""
        response = BindResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test BindResponse data access."""
        response = BindResponse(result="success")
        assert response.result == "success"


class TestUnbindModels:
    """Test Unbind API models."""

    def test_request_builder(self) -> None:
        """Test UnbindRequest builder pattern."""
        request_body = UnbindRequestBody.builder().tag_id("tag-123").target_id("dataset-123").build()
        request = UnbindRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.tag_id == "tag-123"
        assert request.request_body.target_id == "dataset-123"

    def test_request_validation(self) -> None:
        """Test UnbindRequest validation."""
        request = UnbindRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/tags/unbinding"

    def test_request_body_builder(self) -> None:
        """Test UnbindRequestBody builder pattern."""
        request_body = UnbindRequestBody.builder().tag_id("tag-123").target_id("dataset-123").build()
        assert request_body.tag_id == "tag-123"
        assert request_body.target_id == "dataset-123"

    def test_request_body_validation(self) -> None:
        """Test UnbindRequestBody validation."""
        request_body = UnbindRequestBody(tag_id="tag-123", target_id="dataset-123")
        assert request_body.tag_id == "tag-123"
        assert request_body.target_id == "dataset-123"

    def test_response_inheritance(self) -> None:
        """Test UnbindResponse inherits from BaseResponse."""
        response = UnbindResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UnbindResponse data access."""
        response = UnbindResponse(result="success")
        assert response.result == "success"


class TestQueryBoundModels:
    """Test QueryBound API models."""

    def test_request_builder(self) -> None:
        """Test QueryBoundRequest builder pattern."""
        request = QueryBoundRequest.builder().dataset_id("dataset-123").build()
        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"

    def test_request_validation(self) -> None:
        """Test QueryBoundRequest validation."""
        request = QueryBoundRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/tags"

    def test_response_inheritance(self) -> None:
        """Test QueryBoundResponse inherits from BaseResponse."""
        response = QueryBoundResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test QueryBoundResponse data access."""
        response = QueryBoundResponse(data=[], total=0)
        assert response.data == []
        assert response.total == 0
