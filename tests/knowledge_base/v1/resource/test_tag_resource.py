import pytest
from unittest.mock import Mock, AsyncMock
from typing import Any
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption
from dify_oapi.api.knowledge_base.v1.resource.tag import Tag

# Import tag models
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
        mock_response = CreateTagResponse(
            id="test_tag_id",
            name="test_tag",
            type="knowledge",
            binding_count=0
        )
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = CreateTagRequest.builder().name("test_tag").build()
        response = tag_resource.create(request, request_option)

        assert response.id == "test_tag_id"
        assert response.name == "test_tag"
        assert response.type == "knowledge"
        assert response.binding_count == 0
        mock_execute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=CreateTagResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_acreate_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = CreateTagResponse(
            id="test_tag_id",
            name="test_tag",
            type="knowledge",
            binding_count=0
        )
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = CreateTagRequest.builder().name("test_tag").build()
        response = await tag_resource.acreate(request, request_option)

        assert response.id == "test_tag_id"
        assert response.name == "test_tag"
        assert response.type == "knowledge"
        assert response.binding_count == 0
        mock_aexecute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=CreateTagResponse, option=request_option
        )

    def test_list_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        tag1 = TagInfo.builder().id("tag1").name("Tag 1").type("knowledge").binding_count(2).build()
        tag2 = TagInfo.builder().id("tag2").name("Tag 2").type("knowledge").binding_count(1).build()
        mock_response = ListTagsResponse.builder().data([tag1, tag2]).build()
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListTagsRequest.builder().build()
        response = tag_resource.list(request, request_option)

        assert len(response.data) == 2
        assert response.data[0].id == "tag1"
        assert response.data[0].name == "Tag 1"
        mock_execute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=ListTagsResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_alist_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = ListTagsResponse.builder().data([]).build()
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = ListTagsRequest.builder().build()
        response = await tag_resource.alist(request, request_option)

        assert response.data == []
        mock_aexecute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=ListTagsResponse, option=request_option
        )

    def test_update_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = UpdateTagResponse(
            id="test_tag_id",
            name="updated_tag",
            type="knowledge",
            binding_count=0
        )
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            UpdateTagRequest.builder()
            .name("updated_tag")
            .tag_id("test_tag_id")
            .build()
        )
        response = tag_resource.update(request, request_option)

        assert response.id == "test_tag_id"
        assert response.name == "updated_tag"
        assert response.type == "knowledge"
        assert response.binding_count == 0
        mock_execute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=UpdateTagResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aupdate_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = UpdateTagResponse(
            id="test_tag_id",
            name="updated_tag",
            type="knowledge",
            binding_count=0
        )
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = (
            UpdateTagRequest.builder()
            .name("updated_tag")
            .tag_id("test_tag_id")
            .build()
        )
        response = await tag_resource.aupdate(request, request_option)

        assert response.id == "test_tag_id"
        assert response.name == "updated_tag"
        assert response.type == "knowledge"
        assert response.binding_count == 0
        mock_aexecute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=UpdateTagResponse, option=request_option
        )

    def test_delete_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = DeleteTagResponse(result="success")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = DeleteTagRequest.builder().tag_id("test_tag_id").build()
        response = tag_resource.delete(request, request_option)

        assert response.result == "success"
        mock_execute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=DeleteTagResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_adelete_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = DeleteTagResponse(result="success")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = DeleteTagRequest.builder().tag_id("test_tag_id").build()
        response = await tag_resource.adelete(request, request_option)

        assert response.result == "success"
        mock_aexecute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=DeleteTagResponse, option=request_option
        )

    def test_bind_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = BindTagsResponse(result="success")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            BindTagsRequest.builder()
            .tag_ids(["tag1", "tag2"])
            .target_id("dataset_id")
            .build()
        )
        response = tag_resource.bind_tags(request, request_option)

        assert response.result == "success"
        mock_execute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=BindTagsResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_abind_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = BindTagsResponse(result="success")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = (
            BindTagsRequest.builder()
            .tag_ids(["tag1", "tag2"])
            .target_id("dataset_id")
            .build()
        )
        response = await tag_resource.abind_tags(request, request_option)

        assert response.result == "success"
        mock_aexecute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=BindTagsResponse, option=request_option
        )

    def test_unbind_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        mock_response = UnbindTagResponse(result="success")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            UnbindTagRequest.builder()
            .tag_id("tag1")
            .target_id("dataset_id")
            .build()
        )
        response = tag_resource.unbind_tag(request, request_option)

        assert response.result == "success"
        mock_execute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=UnbindTagResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aunbind_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = UnbindTagResponse(result="success")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = (
            UnbindTagRequest.builder()
            .tag_id("tag1")
            .target_id("dataset_id")
            .build()
        )
        response = await tag_resource.aunbind_tag(request, request_option)

        assert response.result == "success"
        mock_aexecute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=UnbindTagResponse, option=request_option
        )

    def test_query_bound_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock Transport.execute
        tag1 = TagInfo.builder().id("tag1").name("Tag 1").build()
        tag2 = TagInfo.builder().id("tag2").name("Tag 2").build()
        mock_response = QueryBoundTagsResponse.builder().data([tag1, tag2]).total(2).build()
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = QueryBoundTagsRequest.builder().dataset_id("dataset_id").build()
        response = tag_resource.query_bound(request, request_option)

        assert len(response.data) == 2
        assert response.data[0].id == "tag1"
        assert response.data[0].name == "Tag 1"
        assert response.total == 2
        mock_execute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=QueryBoundTagsResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aquery_bound_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Mock ATransport.aexecute
        mock_response = QueryBoundTagsResponse.builder().data([]).total(0).build()
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = QueryBoundTagsRequest.builder().dataset_id("dataset_id").build()
        response = await tag_resource.aquery_bound(request, request_option)

        assert response.data == []
        assert response.total == 0
        mock_aexecute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=QueryBoundTagsResponse, option=request_option
        )

    def test_config_initialization(self, config: Config) -> None:
        tag = Tag(config)
        assert tag.config is config

    def test_optional_request_option(self, tag_resource: Tag, monkeypatch: Any) -> None:
        # Test that methods work without request_option parameter
        mock_response = CreateTagResponse(
            id="test_tag_id",
            name="test_tag",
            type="knowledge",
            binding_count=0
        )
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = CreateTagRequest.builder().name("test_tag").build()
        response = tag_resource.create(request)

        assert response.id == "test_tag_id"
        mock_execute.assert_called_once_with(
            tag_resource.config, request, unmarshal_as=CreateTagResponse, option=None
        )

    def test_request_url_patterns(self) -> None:
        # Test URL patterns for different endpoints
        create_request = CreateTagRequest.builder().build()
        assert create_request.uri == "/v1/datasets/tags"

        list_request = ListTagsRequest.builder().build()
        assert list_request.uri == "/v1/datasets/tags"

        update_request = UpdateTagRequest.builder().build()
        assert update_request.uri == "/v1/datasets/tags"

        delete_request = DeleteTagRequest.builder().build()
        assert delete_request.uri == "/v1/datasets/tags"

        bind_request = BindTagsRequest.builder().build()
        assert bind_request.uri == "/v1/datasets/tags/binding"

        unbind_request = UnbindTagRequest.builder().build()
        assert unbind_request.uri == "/v1/datasets/tags/unbinding"

        query_bound_request = QueryBoundTagsRequest.builder().dataset_id("dataset123").build()
        assert query_bound_request.uri == "/v1/datasets/:dataset_id/tags"
        assert query_bound_request.paths["dataset_id"] == "dataset123"

    def test_http_methods(self) -> None:
        # Test HTTP methods for different requests
        from dify_oapi.core.enum import HttpMethod

        create_request = CreateTagRequest.builder().build()
        assert create_request.http_method == HttpMethod.POST

        list_request = ListTagsRequest.builder().build()
        assert list_request.http_method == HttpMethod.GET

        update_request = UpdateTagRequest.builder().build()
        assert update_request.http_method == HttpMethod.PATCH

        delete_request = DeleteTagRequest.builder().build()
        assert delete_request.http_method == HttpMethod.DELETE

        bind_request = BindTagsRequest.builder().build()
        assert bind_request.http_method == HttpMethod.POST

        unbind_request = UnbindTagRequest.builder().build()
        assert unbind_request.http_method == HttpMethod.POST

        query_bound_request = QueryBoundTagsRequest.builder().build()
        assert query_bound_request.http_method == HttpMethod.POST

    def test_different_endpoint_patterns(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Test global tag operations (no dataset_id in path)
        mock_response = CreateTagResponse(
            id="test_tag_id",
            name="test_tag",
            type="knowledge",
            binding_count=0
        )
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Global tag creation
        create_request = CreateTagRequest.builder().name("test_tag").build()
        tag_resource.create(create_request, request_option)
        
        # Verify the request doesn't have dataset_id in paths
        assert not hasattr(create_request, 'paths') or 'dataset_id' not in getattr(create_request, 'paths', {})

        # Test dataset-specific operation (has dataset_id in path)
        query_response = QueryBoundTagsResponse(data=[], total=0)
        mock_execute.return_value = query_response
        
        query_request = QueryBoundTagsRequest.builder().dataset_id("dataset123").build()
        tag_resource.query_bound(query_request, request_option)
        
        # Verify the request has dataset_id in paths
        assert query_request.paths["dataset_id"] == "dataset123"

    def test_array_field_handling(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Test handling of tag_ids array in bind request
        mock_response = BindTagsResponse(result="success")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test with multiple tag IDs
        request = (
            BindTagsRequest.builder()
            .tag_ids(["tag1", "tag2", "tag3"])
            .target_id("dataset_id")
            .build()
        )
        response = tag_resource.bind_tags(request, request_option)

        assert response.result == "success"
        # Verify the request contains the array in request body
        assert request.request_body.tag_ids == ["tag1", "tag2", "tag3"]
        assert request.request_body.target_id == "dataset_id"

    def test_error_handling_scenarios(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Test that the resource properly passes through exceptions from transport
        mock_execute = Mock(side_effect=Exception("API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = CreateTagRequest.builder().name("test_tag").build()
        
        with pytest.raises(Exception, match="API Error"):
            tag_resource.create(request, request_option)

    @pytest.mark.asyncio
    async def test_async_error_handling_scenarios(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        # Test that the async resource properly passes through exceptions from transport
        mock_aexecute = AsyncMock(side_effect=Exception("Async API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = CreateTagRequest.builder().name("test_tag").build()
        
        with pytest.raises(Exception, match="Async API Error"):
            await tag_resource.acreate(request, request_option)