"""Tests for tag API models."""

from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request_body import BindTagsToDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_response import BindTagsToDatasetResponse
from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody
from dify_oapi.api.knowledge.v1.model.create_tag_response import CreateTagResponse
from dify_oapi.api.knowledge.v1.model.delete_tag_request import DeleteTagRequest
from dify_oapi.api.knowledge.v1.model.delete_tag_request_body import DeleteTagRequestBody
from dify_oapi.api.knowledge.v1.model.delete_tag_response import DeleteTagResponse
from dify_oapi.api.knowledge.v1.model.get_dataset_tags_request import GetDatasetTagsRequest
from dify_oapi.api.knowledge.v1.model.get_dataset_tags_response import GetDatasetTagsResponse
from dify_oapi.api.knowledge.v1.model.list_tags_request import ListTagsRequest
from dify_oapi.api.knowledge.v1.model.list_tags_response import ListTagsResponse
from dify_oapi.api.knowledge.v1.model.tag_info import TagInfo
from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_request import UnbindTagsFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_request_body import UnbindTagsFromDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_response import UnbindTagsFromDatasetResponse
from dify_oapi.api.knowledge.v1.model.update_tag_request import UpdateTagRequest
from dify_oapi.api.knowledge.v1.model.update_tag_request_body import UpdateTagRequestBody
from dify_oapi.api.knowledge.v1.model.update_tag_response import UpdateTagResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestCreateTagModels:
    """Test Create Tag API models."""

    def test_request_builder(self) -> None:
        """Test CreateTagRequest builder pattern."""
        request_body = CreateTagRequestBody.builder().name("test-tag").type("knowledge").build()
        request = CreateTagRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.name == "test-tag"
        assert request.request_body.type == "knowledge"

    def test_request_validation(self) -> None:
        """Test CreateTagRequest validation."""
        request = CreateTagRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/tags"

    def test_request_body_builder(self) -> None:
        """Test CreateTagRequestBody builder pattern."""
        request_body = CreateTagRequestBody.builder().name("test-tag").type("custom").build()
        assert request_body.name == "test-tag"
        assert request_body.type == "custom"

    def test_request_body_validation(self) -> None:
        """Test CreateTagRequestBody validation."""
        request_body = CreateTagRequestBody(name="test-tag", type="knowledge")
        assert request_body.name == "test-tag"
        assert request_body.type == "knowledge"

    def test_response_inheritance(self) -> None:
        """Test CreateTagResponse inherits from BaseResponse."""
        response = CreateTagResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test CreateTagResponse data access."""
        response = CreateTagResponse(id="tag-123", name="test-tag", type="knowledge", binding_count=5)
        assert response.id == "tag-123"
        assert response.name == "test-tag"
        assert response.type == "knowledge"
        assert response.binding_count == 5


class TestListTagsModels:
    """Test List Tags API models."""

    def test_request_builder(self) -> None:
        """Test ListTagsRequest builder pattern."""
        request = ListTagsRequest.builder().type("knowledge").build()
        query_keys = [key for key, value in request.queries]
        assert "type" in query_keys

    def test_request_validation(self) -> None:
        """Test ListTagsRequest validation."""
        request = ListTagsRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/tags"

    def test_response_inheritance(self) -> None:
        """Test ListTagsResponse inherits from BaseResponse."""
        response = ListTagsResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test ListTagsResponse data access."""
        tag1 = TagInfo(id="tag1", name="Tag 1", type="knowledge", binding_count=3)
        tag2 = TagInfo(id="tag2", name="Tag 2", type="custom", binding_count=1)
        response = ListTagsResponse(data=[tag1, tag2])
        assert response.data is not None
        assert len(response.data) == 2
        assert response.data[0].id == "tag1"
        assert response.data[1].id == "tag2"


class TestUpdateTagModels:
    """Test Update Tag API models."""

    def test_request_builder(self) -> None:
        """Test UpdateTagRequest builder pattern."""
        request_body = UpdateTagRequestBody.builder().name("updated-tag").tag_id("tag-123").build()
        request = UpdateTagRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.name == "updated-tag"
        assert request.request_body.tag_id == "tag-123"

    def test_request_validation(self) -> None:
        """Test UpdateTagRequest validation."""
        request = UpdateTagRequest.builder().build()
        assert request.http_method == HttpMethod.PATCH
        assert request.uri == "/v1/datasets/tags"

    def test_request_body_builder(self) -> None:
        """Test UpdateTagRequestBody builder pattern."""
        request_body = UpdateTagRequestBody.builder().name("updated-tag").tag_id("tag-123").build()
        assert request_body.name == "updated-tag"
        assert request_body.tag_id == "tag-123"

    def test_request_body_validation(self) -> None:
        """Test UpdateTagRequestBody validation."""
        request_body = UpdateTagRequestBody(name="updated-tag", tag_id="tag-123")
        assert request_body.name == "updated-tag"
        assert request_body.tag_id == "tag-123"

    def test_response_inheritance(self) -> None:
        """Test UpdateTagResponse inherits from BaseResponse."""
        response = UpdateTagResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UpdateTagResponse data access."""
        response = UpdateTagResponse(id="tag-123", name="updated-tag", type="knowledge", binding_count=3)
        assert response.id == "tag-123"
        assert response.name == "updated-tag"
        assert response.type == "knowledge"
        assert response.binding_count == 3


class TestDeleteTagModels:
    """Test Delete Tag API models."""

    def test_request_builder(self) -> None:
        """Test DeleteTagRequest builder pattern."""
        request_body = DeleteTagRequestBody.builder().tag_id("tag-123").build()
        request = DeleteTagRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.tag_id == "tag-123"

    def test_request_validation(self) -> None:
        """Test DeleteTagRequest validation."""
        request = DeleteTagRequest.builder().build()
        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/datasets/tags"

    def test_request_body_builder(self) -> None:
        """Test DeleteTagRequestBody builder pattern."""
        request_body = DeleteTagRequestBody.builder().tag_id("tag-123").build()
        assert request_body.tag_id == "tag-123"

    def test_request_body_validation(self) -> None:
        """Test DeleteTagRequestBody validation."""
        request_body = DeleteTagRequestBody(tag_id="tag-123")
        assert request_body.tag_id == "tag-123"

    def test_response_inheritance(self) -> None:
        """Test DeleteTagResponse inherits from BaseResponse."""
        response = DeleteTagResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test DeleteTagResponse data access."""
        response = DeleteTagResponse(result="success")
        assert response.result == "success"


class TestBindTagsToDatasetModels:
    """Test Bind Tags to Dataset API models."""

    def test_request_builder(self) -> None:
        """Test BindTagsToDatasetRequest builder pattern."""
        request_body = (
            BindTagsToDatasetRequestBody.builder().tag_ids(["tag-1", "tag-2"]).target_id("dataset-123").build()
        )
        request = BindTagsToDatasetRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.tag_ids == ["tag-1", "tag-2"]
        assert request.request_body.target_id == "dataset-123"

    def test_request_validation(self) -> None:
        """Test BindTagsToDatasetRequest validation."""
        request = BindTagsToDatasetRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/tags/binding"

    def test_request_body_builder(self) -> None:
        """Test BindTagsToDatasetRequestBody builder pattern."""
        request_body = (
            BindTagsToDatasetRequestBody.builder().tag_ids(["tag-1", "tag-2"]).target_id("dataset-123").build()
        )
        assert request_body.tag_ids == ["tag-1", "tag-2"]
        assert request_body.target_id == "dataset-123"

    def test_request_body_validation(self) -> None:
        """Test BindTagsToDatasetRequestBody validation."""
        request_body = BindTagsToDatasetRequestBody(tag_ids=["tag-1", "tag-2"], target_id="dataset-123")
        assert request_body.tag_ids == ["tag-1", "tag-2"]
        assert request_body.target_id == "dataset-123"

    def test_response_inheritance(self) -> None:
        """Test BindTagsToDatasetResponse inherits from BaseResponse."""
        response = BindTagsToDatasetResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test BindTagsToDatasetResponse data access."""
        response = BindTagsToDatasetResponse(result="success")
        assert response.result == "success"


class TestUnbindTagsFromDatasetModels:
    """Test Unbind Tags from Dataset API models."""

    def test_request_builder(self) -> None:
        """Test UnbindTagsFromDatasetRequest builder pattern."""
        request_body = UnbindTagsFromDatasetRequestBody.builder().tag_id("tag-123").target_id("dataset-123").build()
        request = UnbindTagsFromDatasetRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.request_body.tag_id == "tag-123"
        assert request.request_body.target_id == "dataset-123"

    def test_request_validation(self) -> None:
        """Test UnbindTagsFromDatasetRequest validation."""
        request = UnbindTagsFromDatasetRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/tags/unbinding"

    def test_request_body_builder(self) -> None:
        """Test UnbindTagsFromDatasetRequestBody builder pattern."""
        request_body = UnbindTagsFromDatasetRequestBody.builder().tag_id("tag-123").target_id("dataset-123").build()
        assert request_body.tag_id == "tag-123"
        assert request_body.target_id == "dataset-123"

    def test_request_body_validation(self) -> None:
        """Test UnbindTagsFromDatasetRequestBody validation."""
        request_body = UnbindTagsFromDatasetRequestBody(tag_id="tag-123", target_id="dataset-123")
        assert request_body.tag_id == "tag-123"
        assert request_body.target_id == "dataset-123"

    def test_response_inheritance(self) -> None:
        """Test UnbindTagsFromDatasetResponse inherits from BaseResponse."""
        response = UnbindTagsFromDatasetResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UnbindTagsFromDatasetResponse data access."""
        response = UnbindTagsFromDatasetResponse(result="success")
        assert response.result == "success"


class TestGetDatasetTagsModels:
    """Test Get Dataset Tags API models."""

    def test_request_builder(self) -> None:
        """Test GetDatasetTagsRequest builder pattern."""
        request = GetDatasetTagsRequest.builder().dataset_id("dataset-123").build()
        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"

    def test_request_validation(self) -> None:
        """Test GetDatasetTagsRequest validation."""
        request = GetDatasetTagsRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/tags"

    def test_response_inheritance(self) -> None:
        """Test GetDatasetTagsResponse inherits from BaseResponse."""
        response = GetDatasetTagsResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetDatasetTagsResponse data access."""
        tag1 = TagInfo(id="tag1", name="Tag 1", type="knowledge")
        tag2 = TagInfo(id="tag2", name="Tag 2", type="custom")
        response = GetDatasetTagsResponse(data=[tag1, tag2])
        assert response.data is not None
        assert len(response.data) == 2
        assert response.data[0].id == "tag1"
        assert response.data[1].id == "tag2"
