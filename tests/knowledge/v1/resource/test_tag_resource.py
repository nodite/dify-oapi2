from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest

from dify_oapi.api.knowledge.v1.model.tag.bind_request import BindRequest
from dify_oapi.api.knowledge.v1.model.tag.bind_request_body import BindRequestBody
from dify_oapi.api.knowledge.v1.model.tag.bind_response import BindResponse

# Import tag models with correct names
from dify_oapi.api.knowledge.v1.model.tag.create_request import CreateRequest
from dify_oapi.api.knowledge.v1.model.tag.create_request_body import CreateRequestBody
from dify_oapi.api.knowledge.v1.model.tag.create_response import CreateResponse
from dify_oapi.api.knowledge.v1.model.tag.delete_request import DeleteRequest
from dify_oapi.api.knowledge.v1.model.tag.delete_request_body import DeleteRequestBody
from dify_oapi.api.knowledge.v1.model.tag.delete_response import DeleteResponse
from dify_oapi.api.knowledge.v1.model.tag.list_request import ListRequest
from dify_oapi.api.knowledge.v1.model.tag.list_response import ListResponse
from dify_oapi.api.knowledge.v1.model.tag.query_bound_request import QueryBoundRequest
from dify_oapi.api.knowledge.v1.model.tag.query_bound_response import QueryBoundResponse
from dify_oapi.api.knowledge.v1.model.tag.tag_info import TagInfo
from dify_oapi.api.knowledge.v1.model.tag.unbind_request import UnbindRequest
from dify_oapi.api.knowledge.v1.model.tag.unbind_request_body import UnbindRequestBody
from dify_oapi.api.knowledge.v1.model.tag.unbind_response import UnbindResponse
from dify_oapi.api.knowledge.v1.model.tag.update_request import UpdateRequest
from dify_oapi.api.knowledge.v1.model.tag.update_request_body import UpdateRequestBody
from dify_oapi.api.knowledge.v1.model.tag.update_response import UpdateResponse
from dify_oapi.api.knowledge.v1.resource.tag import Tag
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestTagResource:
    @pytest.fixture
    def config(self) -> Config:
        return Config()

    @pytest.fixture
    def tag_resource(self, config: Config) -> Tag:
        return Tag(config)

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_create_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = CreateResponse(id="test_tag_id", name="test_tag", type="knowledge", binding_count=0)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateRequestBody.builder().name("test_tag").build()
        request = CreateRequest.builder().request_body(request_body).build()
        response = tag_resource.create(request, request_option)

        assert response.id == "test_tag_id"
        assert response.name == "test_tag"
        assert response.type == "knowledge"
        assert response.binding_count == 0
        mock_execute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=CreateResponse,
            option=request_option,
        )

    @pytest.mark.asyncio
    async def test_acreate_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = CreateResponse(id="test_tag_id", name="test_tag", type="knowledge", binding_count=0)
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request_body = CreateRequestBody.builder().name("test_tag").build()
        request = CreateRequest.builder().request_body(request_body).build()
        response = await tag_resource.acreate(request, request_option)

        assert response.id == "test_tag_id"
        assert response.name == "test_tag"
        assert response.type == "knowledge"
        assert response.binding_count == 0
        mock_aexecute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=CreateResponse,
            option=request_option,
        )

    def test_list_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        tag1 = TagInfo(id="tag1", name="Tag 1", type="knowledge", binding_count=2)
        tag2 = TagInfo(id="tag2", name="Tag 2", type="knowledge", binding_count=1)
        mock_response = ListResponse(data=[tag1, tag2])
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListRequest.builder().build()
        response = tag_resource.list(request, request_option)

        assert len(response.data) == 2
        assert response.data[0].id == "tag1"
        assert response.data[0].name == "Tag 1"
        mock_execute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=ListResponse,
            option=request_option,
        )

    @pytest.mark.asyncio
    async def test_alist_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = ListResponse(data=[])
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = ListRequest.builder().build()
        response = await tag_resource.alist(request, request_option)

        assert response.data == []
        mock_aexecute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=ListResponse,
            option=request_option,
        )

    def test_update_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = UpdateResponse(id="test_tag_id", name="updated_tag", type="knowledge", binding_count=0)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UpdateRequestBody.builder().name("updated_tag").tag_id("test_tag_id").build()
        request = UpdateRequest.builder().request_body(request_body).build()
        response = tag_resource.update(request, request_option)

        assert response.id == "test_tag_id"
        assert response.name == "updated_tag"
        assert response.type == "knowledge"
        assert response.binding_count == 0
        mock_execute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=UpdateResponse,
            option=request_option,
        )

    @pytest.mark.asyncio
    async def test_aupdate_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = UpdateResponse(id="test_tag_id", name="updated_tag", type="knowledge", binding_count=0)
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request_body = UpdateRequestBody.builder().name("updated_tag").tag_id("test_tag_id").build()
        request = UpdateRequest.builder().request_body(request_body).build()
        response = await tag_resource.aupdate(request, request_option)

        assert response.id == "test_tag_id"
        assert response.name == "updated_tag"
        assert response.type == "knowledge"
        assert response.binding_count == 0
        mock_aexecute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=UpdateResponse,
            option=request_option,
        )

    def test_delete_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = DeleteResponse(result="success")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = DeleteRequestBody.builder().tag_id("test_tag_id").build()
        request = DeleteRequest.builder().request_body(request_body).build()
        response = tag_resource.delete(request, request_option)

        assert response.result == "success"
        mock_execute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=DeleteResponse,
            option=request_option,
        )

    @pytest.mark.asyncio
    async def test_adelete_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = DeleteResponse(result="success")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request_body = DeleteRequestBody.builder().tag_id("test_tag_id").build()
        request = DeleteRequest.builder().request_body(request_body).build()
        response = await tag_resource.adelete(request, request_option)

        assert response.result == "success"
        mock_aexecute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=DeleteResponse,
            option=request_option,
        )

    def test_bind_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = BindResponse(result="success")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = BindRequestBody.builder().tag_ids(["tag1", "tag2"]).target_id("dataset_id").build()
        request = BindRequest.builder().request_body(request_body).build()
        response = tag_resource.bind_tags(request, request_option)

        assert response.result == "success"
        mock_execute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=BindResponse,
            option=request_option,
        )

    @pytest.mark.asyncio
    async def test_abind_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = BindResponse(result="success")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request_body = BindRequestBody.builder().tag_ids(["tag1", "tag2"]).target_id("dataset_id").build()
        request = BindRequest.builder().request_body(request_body).build()
        response = await tag_resource.abind_tags(request, request_option)

        assert response.result == "success"
        mock_aexecute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=BindResponse,
            option=request_option,
        )

    def test_unbind_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = UnbindResponse(result="success")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UnbindRequestBody.builder().tag_id("tag1").target_id("dataset_id").build()
        request = UnbindRequest.builder().request_body(request_body).build()
        response = tag_resource.unbind_tag(request, request_option)

        assert response.result == "success"
        mock_execute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=UnbindResponse,
            option=request_option,
        )

    @pytest.mark.asyncio
    async def test_aunbind_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = UnbindResponse(result="success")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request_body = UnbindRequestBody.builder().tag_id("tag1").target_id("dataset_id").build()
        request = UnbindRequest.builder().request_body(request_body).build()
        response = await tag_resource.aunbind_tag(request, request_option)

        assert response.result == "success"
        mock_aexecute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=UnbindResponse,
            option=request_option,
        )

    def test_query_bound_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        tag1 = TagInfo(id="tag1", name="Tag 1")
        tag2 = TagInfo(id="tag2", name="Tag 2")
        mock_response = QueryBoundResponse(data=[tag1, tag2], total=2)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = QueryBoundRequest.builder().dataset_id("dataset_id").build()
        response = tag_resource.query_bound(request, request_option)

        assert len(response.data) == 2
        assert response.data[0].id == "tag1"
        assert response.data[0].name == "Tag 1"
        assert response.total == 2
        mock_execute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=QueryBoundResponse,
            option=request_option,
        )

    @pytest.mark.asyncio
    async def test_aquery_bound_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = QueryBoundResponse(data=[], total=0)
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = QueryBoundRequest.builder().dataset_id("dataset_id").build()
        response = await tag_resource.aquery_bound(request, request_option)

        assert response.data == []
        assert response.total == 0
        mock_aexecute.assert_called_once_with(
            tag_resource.config,
            request,
            unmarshal_as=QueryBoundResponse,
            option=request_option,
        )

    def test_config_initialization(self, config: Config) -> None:
        tag = Tag(config)
        assert tag.config is config

    def test_optional_request_option(self, tag_resource: Tag, monkeypatch: Any) -> None:
        # Test that methods work without request_option parameter
        mock_response = CreateResponse(id="test_tag_id", name="test_tag", type="knowledge", binding_count=0)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateRequestBody.builder().name("test_tag").build()
        request = CreateRequest.builder().request_body(request_body).build()
        response = tag_resource.create(request)

        assert response.id == "test_tag_id"
        mock_execute.assert_called_once_with(tag_resource.config, request, unmarshal_as=CreateResponse, option=None)

    def test_request_url_patterns(self) -> None:
        # Test URL patterns for different endpoints
        create_request = CreateRequest.builder().build()
        assert create_request.uri == "/v1/datasets/tags"

        list_request = ListRequest.builder().build()
        assert list_request.uri == "/v1/datasets/tags"

        update_request = UpdateRequest.builder().build()
        assert update_request.uri == "/v1/datasets/tags"

        delete_request = DeleteRequest.builder().build()
        assert delete_request.uri == "/v1/datasets/tags"

        bind_request = BindRequest.builder().build()
        assert bind_request.uri == "/v1/datasets/tags/binding"

        unbind_request = UnbindRequest.builder().build()
        assert unbind_request.uri == "/v1/datasets/tags/unbinding"

        query_bound_request = QueryBoundRequest.builder().dataset_id("dataset123").build()
        assert query_bound_request.uri == "/v1/datasets/:dataset_id/tags"
        assert query_bound_request.paths["dataset_id"] == "dataset123"

    def test_http_methods(self) -> None:
        # Test HTTP methods for different requests
        from dify_oapi.core.enum import HttpMethod

        create_request = CreateRequest.builder().build()
        assert create_request.http_method == HttpMethod.POST

        list_request = ListRequest.builder().build()
        assert list_request.http_method == HttpMethod.GET

        update_request = UpdateRequest.builder().build()
        assert update_request.http_method == HttpMethod.PATCH

        delete_request = DeleteRequest.builder().build()
        assert delete_request.http_method == HttpMethod.DELETE

        bind_request = BindRequest.builder().build()
        assert bind_request.http_method == HttpMethod.POST

        unbind_request = UnbindRequest.builder().build()
        assert unbind_request.http_method == HttpMethod.POST

        query_bound_request = QueryBoundRequest.builder().build()
        assert query_bound_request.http_method == HttpMethod.GET

    def test_array_field_handling(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Test handling of tag_ids array in bind request
        mock_response = BindResponse(result="success")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test with multiple tag IDs
        request_body = BindRequestBody.builder().tag_ids(["tag1", "tag2", "tag3"]).target_id("dataset_id").build()
        request = BindRequest.builder().request_body(request_body).build()
        response = tag_resource.bind_tags(request, request_option)

        assert response.result == "success"
        # Verify the request contains the array in request body
        assert request.request_body.tag_ids == ["tag1", "tag2", "tag3"]
        assert request.request_body.target_id == "dataset_id"

    def test_error_handling_scenarios(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Test that the resource properly passes through exceptions from transport
        mock_execute = Mock(side_effect=Exception("API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateRequestBody.builder().name("test_tag").build()
        request = CreateRequest.builder().request_body(request_body).build()

        with pytest.raises(Exception, match="API Error"):
            tag_resource.create(request, request_option)

    @pytest.mark.asyncio
    async def test_async_error_handling_scenarios(
        self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        # Test that the async resource properly passes through exceptions from transport
        mock_aexecute = AsyncMock(side_effect=Exception("Async API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request_body = CreateRequestBody.builder().name("test_tag").build()
        request = CreateRequest.builder().request_body(request_body).build()

        with pytest.raises(Exception, match="Async API Error"):
            await tag_resource.acreate(request, request_option)
