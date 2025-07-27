from dify_oapi.api.knowledge_base.v1.model.tag.bind_request import BindRequest
from dify_oapi.api.knowledge_base.v1.model.tag.bind_response import BindResponse
from dify_oapi.api.knowledge_base.v1.model.tag.create_request import CreateRequest
from dify_oapi.api.knowledge_base.v1.model.tag.create_response import CreateResponse
from dify_oapi.api.knowledge_base.v1.model.tag.delete_request import DeleteRequest
from dify_oapi.api.knowledge_base.v1.model.tag.delete_response import DeleteResponse
from dify_oapi.api.knowledge_base.v1.model.tag.list_request import ListRequest
from dify_oapi.api.knowledge_base.v1.model.tag.list_response import ListResponse
from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_request import (
    QueryBoundRequest,
)
from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_response import (
    QueryBoundResponse,
)
from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo
from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request import UnbindRequest
from dify_oapi.api.knowledge_base.v1.model.tag.unbind_response import UnbindResponse
from dify_oapi.api.knowledge_base.v1.model.tag.update_request import UpdateRequest
from dify_oapi.api.knowledge_base.v1.model.tag.update_response import UpdateResponse


class TestCreateRequest:
    def test_builder_pattern(self) -> None:
        from dify_oapi.api.knowledge_base.v1.model.tag.create_request_body import CreateRequestBody

        request_body = CreateRequestBody.builder().name("test-tag").build()
        request = CreateRequest.builder().request_body(request_body).build()

        assert request.request_body is not None
        assert request.request_body.name == "test-tag"
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/tags"

    def test_http_method_and_uri(self) -> None:
        request = CreateRequest.builder().build()
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/tags"


class TestCreateResponse:
    def test_direct_instantiation(self) -> None:
        response = CreateResponse(id="tag-123", name="test-tag", type="knowledge", binding_count=5)

        assert response.id == "tag-123"
        assert response.name == "test-tag"
        assert response.type == "knowledge"
        assert response.binding_count == 5


class TestListRequest:
    def test_builder_pattern(self) -> None:
        request = ListRequest.builder().build()

        assert request.http_method.name == "GET"
        assert request.uri == "/v1/datasets/tags"

    def test_no_parameters_required(self) -> None:
        request = ListRequest()
        assert isinstance(request, ListRequest)


class TestListResponse:
    def test_direct_instantiation(self) -> None:
        tag_info = TagInfo(id="tag-123", name="test-tag", type="knowledge", binding_count=5)
        response = ListResponse(data=[tag_info])

        assert len(response.data) == 1
        assert response.data[0].id == "tag-123"
        assert response.data[0].name == "test-tag"

    def test_empty_data_list(self) -> None:
        response = ListResponse(data=[])
        assert response.data == []

    def test_multiple_tags(self) -> None:
        tag1 = TagInfo(id="tag-1", name="tag-1", type="knowledge", binding_count=1)
        tag2 = TagInfo(id="tag-2", name="tag-2", type="knowledge", binding_count=2)

        response = ListResponse(data=[tag1, tag2])

        assert len(response.data) == 2
        assert response.data[0].id == "tag-1"
        assert response.data[1].id == "tag-2"


class TestUpdateRequest:
    def test_builder_pattern(self) -> None:
        from dify_oapi.api.knowledge_base.v1.model.tag.update_request_body import UpdateRequestBody

        request_body = UpdateRequestBody.builder().name("updated-tag").tag_id("tag-123").build()
        request = UpdateRequest.builder().request_body(request_body).build()

        assert request.request_body is not None
        assert request.request_body.name == "updated-tag"
        assert request.request_body.tag_id == "tag-123"
        assert request.http_method.name == "PATCH"
        assert request.uri == "/v1/datasets/tags"

    def test_http_method_and_uri(self) -> None:
        request = UpdateRequest.builder().build()
        assert request.http_method.name == "PATCH"
        assert request.uri == "/v1/datasets/tags"


class TestUpdateResponse:
    def test_direct_instantiation(self) -> None:
        response = UpdateResponse(id="tag-123", name="updated-tag", type="knowledge", binding_count=3)

        assert response.id == "tag-123"
        assert response.name == "updated-tag"
        assert response.type == "knowledge"
        assert response.binding_count == 3


class TestDeleteRequest:
    def test_builder_pattern(self) -> None:
        from dify_oapi.api.knowledge_base.v1.model.tag.delete_request_body import DeleteRequestBody

        request_body = DeleteRequestBody.builder().tag_id("tag-123").build()
        request = DeleteRequest.builder().request_body(request_body).build()

        assert request.request_body is not None
        assert request.request_body.tag_id == "tag-123"
        assert request.http_method.name == "DELETE"
        assert request.uri == "/v1/datasets/tags"

    def test_http_method_and_uri(self) -> None:
        request = DeleteRequest.builder().build()
        assert request.http_method.name == "DELETE"
        assert request.uri == "/v1/datasets/tags"


class TestDeleteResponse:
    def test_direct_instantiation(self) -> None:
        response = DeleteResponse(result="success")
        assert response.result == "success"


class TestBindRequest:
    def test_builder_pattern(self) -> None:
        from dify_oapi.api.knowledge_base.v1.model.tag.bind_request_body import BindRequestBody

        request_body = BindRequestBody.builder().tag_ids(["tag-1", "tag-2"]).target_id("dataset-123").build()
        request = BindRequest.builder().request_body(request_body).build()

        assert request.request_body is not None
        assert request.request_body.tag_ids == ["tag-1", "tag-2"]
        assert request.request_body.target_id == "dataset-123"
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/tags/binding"

    def test_http_method_and_uri(self) -> None:
        request = BindRequest.builder().build()
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/tags/binding"


class TestBindResponse:
    def test_direct_instantiation(self) -> None:
        response = BindResponse(result="success")
        assert response.result == "success"


class TestUnbindRequest:
    def test_builder_pattern(self) -> None:
        from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request_body import UnbindRequestBody

        request_body = UnbindRequestBody.builder().tag_id("tag-123").target_id("dataset-123").build()
        request = UnbindRequest.builder().request_body(request_body).build()

        assert request.request_body is not None
        assert request.request_body.tag_id == "tag-123"
        assert request.request_body.target_id == "dataset-123"
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/tags/unbinding"

    def test_http_method_and_uri(self) -> None:
        request = UnbindRequest.builder().build()
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/tags/unbinding"


class TestUnbindResponse:
    def test_direct_instantiation(self) -> None:
        response = UnbindResponse(result="success")
        assert response.result == "success"


class TestQueryBoundRequest:
    def test_builder_pattern(self) -> None:
        request = QueryBoundRequest.builder().dataset_id("dataset-123").build()

        assert request.dataset_id == "dataset-123"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/:dataset_id/tags"

    def test_http_method_and_uri(self) -> None:
        request = QueryBoundRequest.builder().build()
        assert request.http_method.name == "POST"
        assert request.uri == "/v1/datasets/:dataset_id/tags"


class TestQueryBoundResponse:
    def test_direct_instantiation(self) -> None:
        tag_info = TagInfo(id="tag-123", name="test-tag", type="knowledge", binding_count=5)
        response = QueryBoundResponse(data=[tag_info], total=1)

        assert len(response.data) == 1
        assert response.data[0].id == "tag-123"
        assert response.total == 1

    def test_empty_data_list(self) -> None:
        response = QueryBoundResponse(data=[], total=0)
        assert response.data == []
        assert response.total == 0

    def test_multiple_tags_with_total(self) -> None:
        tag1 = TagInfo(id="tag-1", name="tag-1", type="knowledge", binding_count=1)
        tag2 = TagInfo(id="tag-2", name="tag-2", type="knowledge", binding_count=2)

        response = QueryBoundResponse(data=[tag1, tag2], total=2)

        assert len(response.data) == 2
        assert response.total == 2
        assert response.data[0].id == "tag-1"
        assert response.data[1].id == "tag-2"


class TestTagModelsIntegration:
    def test_create_to_list_integration(self) -> None:
        # Test that create response can be used in list response
        create_response = CreateResponse(id="tag-123", name="test-tag", type="knowledge", binding_count=5)

        # Convert to TagInfo for list response
        tag_info = TagInfo(
            id=create_response.id,
            name=create_response.name,
            type=create_response.type,
            binding_count=create_response.binding_count,
        )

        list_response = ListResponse(data=[tag_info])

        assert len(list_response.data) == 1
        assert list_response.data[0].id == "tag-123"
        assert list_response.data[0].name == "test-tag"

    def test_update_to_tag_info_integration(self) -> None:
        # Test that update response can be converted to tag info
        update_response = UpdateResponse(id="tag-123", name="updated-tag", type="knowledge", binding_count=3)

        tag_info = TagInfo(
            id=update_response.id,
            name=update_response.name,
            type=update_response.type,
            binding_count=update_response.binding_count,
        )

        assert isinstance(tag_info, TagInfo)
        assert tag_info.id == "tag-123"
        assert tag_info.name == "updated-tag"

    def test_bind_unbind_workflow(self) -> None:
        from dify_oapi.api.knowledge_base.v1.model.tag.bind_request_body import BindRequestBody
        from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request_body import UnbindRequestBody

        # Test bind and unbind request workflow
        bind_body = BindRequestBody.builder().tag_ids(["tag-1", "tag-2"]).target_id("dataset-123").build()
        bind_request = BindRequest.builder().request_body(bind_body).build()

        unbind_body = UnbindRequestBody.builder().tag_id("tag-1").target_id("dataset-123").build()
        unbind_request = UnbindRequest.builder().request_body(unbind_body).build()

        assert bind_request.request_body.tag_ids == ["tag-1", "tag-2"]
        assert bind_request.request_body.target_id == "dataset-123"
        assert unbind_request.request_body.tag_id == "tag-1"
        assert unbind_request.request_body.target_id == "dataset-123"

    def test_query_bound_with_tag_info(self) -> None:
        # Test query bound response with tag info
        tag_info = TagInfo(id="tag-123", name="bound-tag", type="knowledge", binding_count=1)

        query_response = QueryBoundResponse(data=[tag_info], total=1)

        assert len(query_response.data) == 1
        assert query_response.data[0].name == "bound-tag"
        assert query_response.total == 1

    def test_complete_tag_lifecycle(self) -> None:
        from dify_oapi.api.knowledge_base.v1.model.tag.bind_request_body import BindRequestBody
        from dify_oapi.api.knowledge_base.v1.model.tag.create_request_body import CreateRequestBody
        from dify_oapi.api.knowledge_base.v1.model.tag.delete_request_body import DeleteRequestBody
        from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request_body import UnbindRequestBody
        from dify_oapi.api.knowledge_base.v1.model.tag.update_request_body import UpdateRequestBody

        # Test complete tag management lifecycle

        # 1. Create tag
        create_body = CreateRequestBody.builder().name("lifecycle-tag").build()
        create_request = CreateRequest.builder().request_body(create_body).build()

        create_response = CreateResponse(id="tag-123", name="lifecycle-tag", type="knowledge", binding_count=0)

        # 2. Update tag
        update_body = UpdateRequestBody.builder().name("updated-lifecycle-tag").tag_id("tag-123").build()
        update_request = UpdateRequest.builder().request_body(update_body).build()

        # 3. Bind tag to dataset
        bind_body = BindRequestBody.builder().tag_ids(["tag-123"]).target_id("dataset-456").build()
        bind_request = BindRequest.builder().request_body(bind_body).build()

        # 4. Query bound tags
        query_request = QueryBoundRequest.builder().dataset_id("dataset-456").build()

        # 5. Unbind tag
        unbind_body = UnbindRequestBody.builder().tag_id("tag-123").target_id("dataset-456").build()
        unbind_request = UnbindRequest.builder().request_body(unbind_body).build()

        # 6. Delete tag
        delete_body = DeleteRequestBody.builder().tag_id("tag-123").build()
        delete_request = DeleteRequest.builder().request_body(delete_body).build()

        # Verify all requests are properly constructed
        assert create_request.request_body.name == "lifecycle-tag"
        assert update_request.request_body.name == "updated-lifecycle-tag"
        assert bind_request.request_body.tag_ids == ["tag-123"]
        assert query_request.dataset_id == "dataset-456"
        assert unbind_request.request_body.tag_id == "tag-123"
        assert delete_request.request_body.tag_id == "tag-123"

        # Verify response conversion
        tag_info = TagInfo(
            id=create_response.id,
            name=create_response.name,
            type=create_response.type,
            binding_count=create_response.binding_count,
        )
        assert tag_info.id == "tag-123"
        assert tag_info.name == "lifecycle-tag"

    def test_http_methods_and_uris(self) -> None:
        # Test that all requests have correct HTTP methods and URIs
        create_request = CreateRequest.builder().build()
        list_request = ListRequest.builder().build()
        update_request = UpdateRequest.builder().build()
        delete_request = DeleteRequest.builder().build()
        bind_request = BindRequest.builder().build()
        unbind_request = UnbindRequest.builder().build()
        query_request = QueryBoundRequest.builder().build()

        assert create_request.http_method.name == "POST"
        assert create_request.uri == "/v1/datasets/tags"

        assert list_request.http_method.name == "GET"
        assert list_request.uri == "/v1/datasets/tags"

        assert update_request.http_method.name == "PATCH"
        assert update_request.uri == "/v1/datasets/tags"

        assert delete_request.http_method.name == "DELETE"
        assert delete_request.uri == "/v1/datasets/tags"

        assert bind_request.http_method.name == "POST"
        assert bind_request.uri == "/v1/datasets/tags/binding"

        assert unbind_request.http_method.name == "POST"
        assert unbind_request.uri == "/v1/datasets/tags/unbinding"

        assert query_request.http_method.name == "POST"
        assert query_request.uri == "/v1/datasets/:dataset_id/tags"
