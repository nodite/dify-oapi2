import pytest
from typing import List

from dify_oapi.api.knowledge_base.v1.model.tag.create_request import CreateTagRequest
from dify_oapi.api.knowledge_base.v1.model.tag.create_response import CreateTagResponse
from dify_oapi.api.knowledge_base.v1.model.tag.list_request import ListTagsRequest
from dify_oapi.api.knowledge_base.v1.model.tag.list_response import ListTagsResponse
from dify_oapi.api.knowledge_base.v1.model.tag.update_request import UpdateTagRequest
from dify_oapi.api.knowledge_base.v1.model.tag.update_response import UpdateTagResponse
from dify_oapi.api.knowledge_base.v1.model.tag.delete_request import DeleteTagRequest
from dify_oapi.api.knowledge_base.v1.model.tag.delete_response import DeleteTagResponse
from dify_oapi.api.knowledge_base.v1.model.tag.bind_request import BindTagsRequest
from dify_oapi.api.knowledge_base.v1.model.tag.bind_response import BindTagsResponse
from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request import UnbindTagRequest
from dify_oapi.api.knowledge_base.v1.model.tag.unbind_response import UnbindTagResponse
from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_request import QueryBoundTagsRequest
from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_response import QueryBoundTagsResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.tag_info import TagInfo
from dify_oapi.core.enum import HttpMethod


class TestCreateTagRequest:
    def test_builder_pattern(self) -> None:
        request = (
            CreateTagRequest.builder()
            .name("test-tag")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.name == "test-tag"
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/tags"

    def test_request_body_serialization(self) -> None:
        request = (
            CreateTagRequest.builder()
            .name("test-tag")
            .build()
        )
        
        assert request.body == {"name": "test-tag"}

    def test_empty_name(self) -> None:
        request = (
            CreateTagRequest.builder()
            .name("")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.name == ""


class TestCreateTagResponse:
    def test_builder_pattern(self) -> None:
        response = (
            CreateTagResponse.builder()
            .id("tag-123")
            .name("test-tag")
            .type("knowledge")
            .binding_count(5)
            .build()
        )
        
        assert response.id == "tag-123"
        assert response.name == "test-tag"
        assert response.type == "knowledge"
        assert response.binding_count == 5

    def test_to_tag_info(self) -> None:
        response = CreateTagResponse(
            id="tag-123",
            name="test-tag",
            type="knowledge",
            binding_count=5
        )
        tag_info = response.to_tag_info()
        
        assert isinstance(tag_info, TagInfo)
        assert tag_info.id == "tag-123"
        assert tag_info.name == "test-tag"
        assert tag_info.type == "knowledge"
        assert tag_info.binding_count == 5

    def test_zero_binding_count(self) -> None:
        response = CreateTagResponse(
            id="tag-123",
            name="test-tag",
            type="knowledge",
            binding_count=0
        )
        
        assert response.binding_count == 0


class TestListTagsRequest:
    def test_builder_pattern(self) -> None:
        request = ListTagsRequest.builder().build()
        
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/tags"

    def test_no_parameters_required(self) -> None:
        request = ListTagsRequest()
        assert isinstance(request, ListTagsRequest)


class TestListTagsResponse:
    def test_builder_pattern(self) -> None:
        tag_info = TagInfo(id="tag-123", name="test-tag", type="knowledge", binding_count=5)
        response = (
            ListTagsResponse.builder()
            .data([tag_info])
            .build()
        )
        
        assert len(response.data) == 1
        assert response.data[0].id == "tag-123"
        assert response.data[0].name == "test-tag"

    def test_add_tag_method(self) -> None:
        tag_info = TagInfo(id="tag-123", name="test-tag", type="knowledge", binding_count=5)
        response = (
            ListTagsResponse.builder()
            .add_tag(tag_info)
            .build()
        )
        
        assert len(response.data) == 1
        assert response.data[0].id == "tag-123"

    def test_empty_data_list(self) -> None:
        response = ListTagsResponse(data=[])
        assert response.data == []

    def test_multiple_tags(self) -> None:
        tag1 = TagInfo(id="tag-1", name="tag-1", type="knowledge", binding_count=1)
        tag2 = TagInfo(id="tag-2", name="tag-2", type="knowledge", binding_count=2)
        
        response = (
            ListTagsResponse.builder()
            .add_tag(tag1)
            .add_tag(tag2)
            .build()
        )
        
        assert len(response.data) == 2
        assert response.data[0].id == "tag-1"
        assert response.data[1].id == "tag-2"


class TestUpdateTagRequest:
    def test_builder_pattern(self) -> None:
        request = (
            UpdateTagRequest.builder()
            .name("updated-tag")
            .tag_id("tag-123")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.name == "updated-tag"
        assert request.request_body.tag_id == "tag-123"
        assert request.http_method == HttpMethod.PATCH
        assert request.uri == "/v1/datasets/tags"

    def test_request_body_serialization(self) -> None:
        request = (
            UpdateTagRequest.builder()
            .name("updated-tag")
            .tag_id("tag-123")
            .build()
        )
        
        assert request.body == {"name": "updated-tag", "tag_id": "tag-123"}

    def test_partial_update(self) -> None:
        request = (
            UpdateTagRequest.builder()
            .name("updated-tag")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.name == "updated-tag"
        assert request.request_body.tag_id == ""


class TestUpdateTagResponse:
    def test_builder_pattern(self) -> None:
        response = (
            UpdateTagResponse.builder()
            .id("tag-123")
            .name("updated-tag")
            .type("knowledge")
            .binding_count(3)
            .build()
        )
        
        assert response.id == "tag-123"
        assert response.name == "updated-tag"
        assert response.type == "knowledge"
        assert response.binding_count == 3

    def test_to_tag_info(self) -> None:
        response = UpdateTagResponse(
            id="tag-123",
            name="updated-tag",
            type="knowledge",
            binding_count=3
        )
        tag_info = response.to_tag_info()
        
        assert isinstance(tag_info, TagInfo)
        assert tag_info.id == "tag-123"
        assert tag_info.name == "updated-tag"
        assert tag_info.type == "knowledge"
        assert tag_info.binding_count == 3


class TestDeleteTagRequest:
    def test_builder_pattern(self) -> None:
        request = (
            DeleteTagRequest.builder()
            .tag_id("tag-123")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.tag_id == "tag-123"
        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/datasets/tags"

    def test_request_body_serialization(self) -> None:
        request = (
            DeleteTagRequest.builder()
            .tag_id("tag-123")
            .build()
        )
        
        assert request.body == {"tag_id": "tag-123"}

    def test_empty_tag_id(self) -> None:
        request = (
            DeleteTagRequest.builder()
            .tag_id("")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.tag_id == ""


class TestDeleteTagResponse:
    def test_builder_pattern(self) -> None:
        response = (
            DeleteTagResponse.builder()
            .result("success")
            .build()
        )
        
        assert response.result == "success"

    def test_result_field(self) -> None:
        response = DeleteTagResponse(result="success")
        assert response.result == "success"

    def test_empty_result(self) -> None:
        response = DeleteTagResponse(result="")
        assert response.result == ""


class TestBindTagsRequest:
    def test_builder_pattern(self) -> None:
        request = (
            BindTagsRequest.builder()
            .tag_ids(["tag-1", "tag-2"])
            .target_id("dataset-123")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.tag_ids == ["tag-1", "tag-2"]
        assert request.request_body.target_id == "dataset-123"
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/tags/binding"

    def test_request_body_serialization(self) -> None:
        request = (
            BindTagsRequest.builder()
            .tag_ids(["tag-1", "tag-2"])
            .target_id("dataset-123")
            .build()
        )
        
        assert request.body == {"tag_ids": ["tag-1", "tag-2"], "target_id": "dataset-123"}

    def test_empty_tag_ids(self) -> None:
        request = (
            BindTagsRequest.builder()
            .tag_ids([])
            .target_id("dataset-123")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.tag_ids == []
        assert request.request_body.target_id == "dataset-123"

    def test_single_tag_id(self) -> None:
        request = (
            BindTagsRequest.builder()
            .tag_ids(["tag-1"])
            .target_id("dataset-123")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.tag_ids == ["tag-1"]


class TestBindTagsResponse:
    def test_builder_pattern(self) -> None:
        response = (
            BindTagsResponse.builder()
            .result("success")
            .build()
        )
        
        assert response.result == "success"

    def test_result_field(self) -> None:
        response = BindTagsResponse(result="success")
        assert response.result == "success"


class TestUnbindTagRequest:
    def test_builder_pattern(self) -> None:
        request = (
            UnbindTagRequest.builder()
            .tag_id("tag-123")
            .target_id("dataset-123")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.tag_id == "tag-123"
        assert request.request_body.target_id == "dataset-123"
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/tags/unbinding"

    def test_request_body_serialization(self) -> None:
        request = (
            UnbindTagRequest.builder()
            .tag_id("tag-123")
            .target_id("dataset-123")
            .build()
        )
        
        assert request.body == {"tag_id": "tag-123", "target_id": "dataset-123"}

    def test_empty_fields(self) -> None:
        request = (
            UnbindTagRequest.builder()
            .tag_id("")
            .target_id("")
            .build()
        )
        
        assert request.request_body is not None
        assert request.request_body.tag_id == ""
        assert request.request_body.target_id == ""


class TestUnbindTagResponse:
    def test_builder_pattern(self) -> None:
        response = (
            UnbindTagResponse.builder()
            .result("success")
            .build()
        )
        
        assert response.result == "success"

    def test_result_field(self) -> None:
        response = UnbindTagResponse(result="success")
        assert response.result == "success"


class TestQueryBoundTagsRequest:
    def test_builder_pattern(self) -> None:
        request = (
            QueryBoundTagsRequest.builder()
            .dataset_id("dataset-123")
            .build()
        )
        
        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/tags"

    def test_path_parameter_handling(self) -> None:
        request = (
            QueryBoundTagsRequest.builder()
            .dataset_id("dataset-456")
            .build()
        )
        
        assert request.dataset_id == "dataset-456"
        assert request.paths["dataset_id"] == "dataset-456"

    def test_empty_dataset_id(self) -> None:
        request = (
            QueryBoundTagsRequest.builder()
            .dataset_id("")
            .build()
        )
        
        assert request.dataset_id == ""
        assert request.paths["dataset_id"] == ""


class TestQueryBoundTagsResponse:
    def test_builder_pattern(self) -> None:
        tag_info = TagInfo(id="tag-123", name="test-tag", type="knowledge", binding_count=5)
        response = (
            QueryBoundTagsResponse.builder()
            .data([tag_info])
            .total(1)
            .build()
        )
        
        assert len(response.data) == 1
        assert response.data[0].id == "tag-123"
        assert response.total == 1

    def test_add_tag_method(self) -> None:
        tag_info = TagInfo(id="tag-123", name="test-tag", type="knowledge", binding_count=5)
        response = (
            QueryBoundTagsResponse.builder()
            .add_tag(tag_info)
            .total(1)
            .build()
        )
        
        assert len(response.data) == 1
        assert response.data[0].id == "tag-123"
        assert response.total == 1

    def test_empty_data_list(self) -> None:
        response = QueryBoundTagsResponse(data=[], total=0)
        assert response.data == []
        assert response.total == 0

    def test_multiple_tags_with_total(self) -> None:
        tag1 = TagInfo(id="tag-1", name="tag-1", type="knowledge", binding_count=1)
        tag2 = TagInfo(id="tag-2", name="tag-2", type="knowledge", binding_count=2)
        
        response = (
            QueryBoundTagsResponse.builder()
            .data([tag1, tag2])
            .total(2)
            .build()
        )
        
        assert len(response.data) == 2
        assert response.total == 2
        assert response.data[0].id == "tag-1"
        assert response.data[1].id == "tag-2"

    def test_total_mismatch_with_data_length(self) -> None:
        tag_info = TagInfo(id="tag-123", name="test-tag", type="knowledge", binding_count=5)
        response = (
            QueryBoundTagsResponse.builder()
            .data([tag_info])
            .total(10)  # Total can be different from data length (pagination)
            .build()
        )
        
        assert len(response.data) == 1
        assert response.total == 10


class TestTagModelsIntegration:
    def test_create_to_list_integration(self) -> None:
        # Test that create response can be used in list response
        create_response = CreateTagResponse(
            id="tag-123",
            name="test-tag",
            type="knowledge",
            binding_count=5
        )
        tag_info = create_response.to_tag_info()
        
        list_response = ListTagsResponse(data=[tag_info])
        
        assert len(list_response.data) == 1
        assert list_response.data[0].id == "tag-123"
        assert list_response.data[0].name == "test-tag"

    def test_update_to_tag_info_integration(self) -> None:
        # Test that update response can be converted to tag info
        update_response = UpdateTagResponse(
            id="tag-123",
            name="updated-tag",
            type="knowledge",
            binding_count=3
        )
        tag_info = update_response.to_tag_info()
        
        assert isinstance(tag_info, TagInfo)
        assert tag_info.id == "tag-123"
        assert tag_info.name == "updated-tag"

    def test_bind_unbind_workflow(self) -> None:
        # Test bind and unbind request workflow
        bind_request = (
            BindTagsRequest.builder()
            .tag_ids(["tag-1", "tag-2"])
            .target_id("dataset-123")
            .build()
        )
        
        unbind_request = (
            UnbindTagRequest.builder()
            .tag_id("tag-1")
            .target_id("dataset-123")
            .build()
        )
        
        assert bind_request.request_body.tag_ids == ["tag-1", "tag-2"]
        assert bind_request.request_body.target_id == "dataset-123"
        assert unbind_request.request_body.tag_id == "tag-1"
        assert unbind_request.request_body.target_id == "dataset-123"

    def test_query_bound_with_tag_info(self) -> None:
        # Test query bound response with tag info
        tag_info = TagInfo(id="tag-123", name="bound-tag", type="knowledge", binding_count=1)
        
        query_response = (
            QueryBoundTagsResponse.builder()
            .add_tag(tag_info)
            .total(1)
            .build()
        )
        
        assert len(query_response.data) == 1
        assert query_response.data[0].name == "bound-tag"
        assert query_response.total == 1

    def test_complete_tag_lifecycle(self) -> None:
        # Test complete tag management lifecycle
        
        # 1. Create tag
        create_request = (
            CreateTagRequest.builder()
            .name("lifecycle-tag")
            .build()
        )
        
        create_response = CreateTagResponse(
            id="tag-123",
            name="lifecycle-tag",
            type="knowledge",
            binding_count=0
        )
        
        # 2. Update tag
        update_request = (
            UpdateTagRequest.builder()
            .name("updated-lifecycle-tag")
            .tag_id("tag-123")
            .build()
        )
        
        # 3. Bind tag to dataset
        bind_request = (
            BindTagsRequest.builder()
            .tag_ids(["tag-123"])
            .target_id("dataset-456")
            .build()
        )
        
        # 4. Query bound tags
        query_request = (
            QueryBoundTagsRequest.builder()
            .dataset_id("dataset-456")
            .build()
        )
        
        # 5. Unbind tag
        unbind_request = (
            UnbindTagRequest.builder()
            .tag_id("tag-123")
            .target_id("dataset-456")
            .build()
        )
        
        # 6. Delete tag
        delete_request = (
            DeleteTagRequest.builder()
            .tag_id("tag-123")
            .build()
        )
        
        # Verify all requests are properly constructed
        assert create_request.request_body.name == "lifecycle-tag"
        assert update_request.request_body.name == "updated-lifecycle-tag"
        assert bind_request.request_body.tag_ids == ["tag-123"]
        assert query_request.dataset_id == "dataset-456"
        assert unbind_request.request_body.tag_id == "tag-123"
        assert delete_request.request_body.tag_id == "tag-123"
        
        # Verify response conversion
        tag_info = create_response.to_tag_info()
        assert tag_info.id == "tag-123"
        assert tag_info.name == "lifecycle-tag"

    def test_http_methods_and_uris(self) -> None:
        # Test that all requests have correct HTTP methods and URIs
        create_request = CreateTagRequest.builder().name("test").build()
        list_request = ListTagsRequest.builder().build()
        update_request = UpdateTagRequest.builder().name("test").tag_id("123").build()
        delete_request = DeleteTagRequest.builder().tag_id("123").build()
        bind_request = BindTagsRequest.builder().tag_ids(["123"]).target_id("456").build()
        unbind_request = UnbindTagRequest.builder().tag_id("123").target_id("456").build()
        query_request = QueryBoundTagsRequest.builder().dataset_id("456").build()
        
        assert create_request.http_method == HttpMethod.POST
        assert create_request.uri == "/v1/datasets/tags"
        
        assert list_request.http_method == HttpMethod.GET
        assert list_request.uri == "/v1/datasets/tags"
        
        assert update_request.http_method == HttpMethod.PATCH
        assert update_request.uri == "/v1/datasets/tags"
        
        assert delete_request.http_method == HttpMethod.DELETE
        assert delete_request.uri == "/v1/datasets/tags"
        
        assert bind_request.http_method == HttpMethod.POST
        assert bind_request.uri == "/v1/datasets/tags/binding"
        
        assert unbind_request.http_method == HttpMethod.POST
        assert unbind_request.uri == "/v1/datasets/tags/unbinding"
        
        assert query_request.http_method == HttpMethod.POST
        assert query_request.uri == "/v1/datasets/:dataset_id/tags"