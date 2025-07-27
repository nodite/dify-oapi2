from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest

from dify_oapi.api.knowledge_base.v1.model.tag.bind_request import BindTagsRequest
from dify_oapi.api.knowledge_base.v1.model.tag.bind_response import BindTagsResponse
from dify_oapi.api.knowledge_base.v1.model.tag.create_request import CreateTagRequest
from dify_oapi.api.knowledge_base.v1.model.tag.create_response import CreateTagResponse
from dify_oapi.api.knowledge_base.v1.model.tag.delete_request import DeleteTagRequest
from dify_oapi.api.knowledge_base.v1.model.tag.delete_response import DeleteTagResponse
from dify_oapi.api.knowledge_base.v1.model.tag.list_request import ListTagsRequest
from dify_oapi.api.knowledge_base.v1.model.tag.list_response import ListTagsResponse
from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_request import (
    QueryBoundTagsRequest,
)
from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_response import (
    QueryBoundTagsResponse,
)
from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo
from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request import UnbindTagRequest
from dify_oapi.api.knowledge_base.v1.model.tag.unbind_response import UnbindTagResponse
from dify_oapi.api.knowledge_base.v1.model.tag.update_request import UpdateTagRequest
from dify_oapi.api.knowledge_base.v1.model.tag.update_response import UpdateTagResponse
from dify_oapi.api.knowledge_base.v1.resource.tag import Tag
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestTagAPIIntegration:
    @pytest.fixture
    def config(self) -> Config:
        return Config()

    @pytest.fixture
    def tag_resource(self, config: Config) -> Tag:
        return Tag(config)

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_tag_management_and_binding_workflow_sync(
        self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test complete tag management and binding workflow: create → list → bind → query → unbind → update → delete"""
        tag_id = "test-tag-id"
        dataset_id = "test-dataset-id"

        # Mock create tag
        create_response = CreateTagResponse(id=tag_id, name="Test Tag", type="knowledge", binding_count=0)

        # Mock list tags
        tag_list = [TagInfo(id=tag_id, name="Test Tag", type="knowledge", binding_count=0)]
        list_response = ListTagsResponse(data=tag_list)

        # Mock bind tags
        bind_response = BindTagsResponse(result="success")

        # Mock query bound tags
        bound_tags = [TagInfo(id=tag_id, name="Test Tag")]
        query_response = QueryBoundTagsResponse(data=bound_tags, total=1)

        # Mock unbind tag
        unbind_response = UnbindTagResponse(result="success")

        # Mock update tag
        update_response = UpdateTagResponse(id=tag_id, name="Updated Tag", type="knowledge", binding_count=0)

        # Mock delete tag
        delete_response = DeleteTagResponse(result="success")

        # Set up mocks
        mock_execute = Mock()
        mock_execute.side_effect = [
            create_response,
            list_response,
            bind_response,
            query_response,
            unbind_response,
            update_response,
            delete_response,
        ]
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # 1. Create tag
        create_request = CreateTagRequest.builder().name("Test Tag").build()
        created = tag_resource.create(create_request, request_option)
        assert created.id == tag_id
        assert created.name == "Test Tag"
        assert created.type == "knowledge"
        assert created.binding_count == 0

        # 2. List tags
        list_request = ListTagsRequest.builder().build()
        tag_list_result = tag_resource.list(list_request, request_option)
        assert len(tag_list_result.data) == 1
        assert tag_list_result.data[0].id == tag_id

        # 3. Bind tag to dataset
        bind_request = BindTagsRequest.builder().tag_ids([tag_id]).target_id(dataset_id).build()
        bind_result = tag_resource.bind_tags(bind_request, request_option)
        assert bind_result.result == "success"

        # 4. Query bound tags
        query_request = QueryBoundTagsRequest.builder().dataset_id(dataset_id).build()
        query_result = tag_resource.query_bound(query_request, request_option)
        assert len(query_result.data) == 1
        assert query_result.data[0].id == tag_id
        assert query_result.total == 1

        # 5. Unbind tag
        unbind_request = UnbindTagRequest.builder().tag_id(tag_id).target_id(dataset_id).build()
        unbind_result = tag_resource.unbind_tag(unbind_request, request_option)
        assert unbind_result.result == "success"

        # 6. Update tag
        update_request = UpdateTagRequest.builder().name("Updated Tag").tag_id(tag_id).build()
        updated = tag_resource.update(update_request, request_option)
        assert updated.id == tag_id
        assert updated.name == "Updated Tag"

        # 7. Delete tag
        delete_request = DeleteTagRequest.builder().tag_id(tag_id).build()
        delete_result = tag_resource.delete(delete_request, request_option)
        assert delete_result.result == "success"

        # Verify all calls were made
        assert mock_execute.call_count == 7

    @pytest.mark.asyncio
    async def test_tag_management_workflow_async(
        self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test tag management workflow with async methods"""
        tag_id = "async-tag-id"
        dataset_id = "async-dataset-id"

        # Mock responses
        create_response = CreateTagResponse(id=tag_id, name="Async Tag", type="knowledge", binding_count=0)
        list_response = ListTagsResponse(data=[TagInfo(id=tag_id, name="Async Tag", type="knowledge", binding_count=0)])
        bind_response = BindTagsResponse(result="success")
        query_response = QueryBoundTagsResponse(data=[TagInfo(id=tag_id, name="Async Tag")], total=1)
        unbind_response = UnbindTagResponse(result="success")
        update_response = UpdateTagResponse(id=tag_id, name="Updated Async Tag", type="knowledge", binding_count=0)
        delete_response = DeleteTagResponse(result="success")

        mock_aexecute = AsyncMock()
        mock_aexecute.side_effect = [
            create_response,
            list_response,
            bind_response,
            query_response,
            unbind_response,
            update_response,
            delete_response,
        ]
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        # Execute async workflow
        create_request = CreateTagRequest.builder().name("Async Tag").build()
        created = await tag_resource.acreate(create_request, request_option)
        assert created.id == tag_id

        list_request = ListTagsRequest.builder().build()
        listed = await tag_resource.alist(list_request, request_option)
        assert len(listed.data) == 1

        bind_request = BindTagsRequest.builder().tag_ids([tag_id]).target_id(dataset_id).build()
        bind_result = await tag_resource.abind_tags(bind_request, request_option)
        assert bind_result.result == "success"

        query_request = QueryBoundTagsRequest.builder().dataset_id(dataset_id).build()
        query_result = await tag_resource.aquery_bound(query_request, request_option)
        assert len(query_result.data) == 1

        unbind_request = UnbindTagRequest.builder().tag_id(tag_id).target_id(dataset_id).build()
        unbind_result = await tag_resource.aunbind_tag(unbind_request, request_option)
        assert unbind_result.result == "success"

        update_request = UpdateTagRequest.builder().name("Updated Async Tag").tag_id(tag_id).build()
        updated = await tag_resource.aupdate(update_request, request_option)
        assert updated.name == "Updated Async Tag"

        delete_request = DeleteTagRequest.builder().tag_id(tag_id).build()
        delete_result = await tag_resource.adelete(delete_request, request_option)
        assert delete_result.result == "success"

        assert mock_aexecute.call_count == 7

    def test_multiple_tag_binding(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test binding multiple tags to a single dataset"""
        dataset_id = "multi-tag-dataset"
        tag_ids = ["tag1", "tag2", "tag3"]

        # Mock bind multiple tags
        bind_response = BindTagsResponse(result="success")
        mock_execute = Mock(return_value=bind_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        bind_request = BindTagsRequest.builder().tag_ids(tag_ids).target_id(dataset_id).build()
        result = tag_resource.bind_tags(bind_request, request_option)
        assert result.result == "success"

        # Mock query bound tags with multiple results
        bound_tags = [
            TagInfo(id="tag1", name="Tag 1"),
            TagInfo(id="tag2", name="Tag 2"),
            TagInfo(id="tag3", name="Tag 3"),
        ]
        query_response = QueryBoundTagsResponse(data=bound_tags, total=3)
        mock_execute.return_value = query_response

        query_request = QueryBoundTagsRequest.builder().dataset_id(dataset_id).build()
        query_result = tag_resource.query_bound(query_request, request_option)
        assert len(query_result.data) == 3
        assert query_result.total == 3

    def test_tag_binding_count_tracking(
        self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test tag binding count tracking"""
        tag_id = "binding-count-tag"

        # Mock tag with different binding counts
        initial_tag = TagInfo(id=tag_id, name="Binding Count Tag", type="knowledge", binding_count=0)
        after_bind_tag = TagInfo(id=tag_id, name="Binding Count Tag", type="knowledge", binding_count=1)

        # Mock list with initial count
        list_response = ListTagsResponse(data=[initial_tag])
        mock_execute = Mock(return_value=list_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        list_request = ListTagsRequest.builder().build()
        result = tag_resource.list(list_request, request_option)
        assert result.data[0].binding_count == 0

        # Mock list after binding
        list_response_after = ListTagsResponse(data=[after_bind_tag])
        mock_execute.return_value = list_response_after

        result_after = tag_resource.list(list_request, request_option)
        assert result_after.data[0].binding_count == 1

    def test_global_vs_dataset_specific_operations(
        self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test distinction between global tag operations and dataset-specific operations"""
        tag_id = "global-tag"
        dataset_id = "specific-dataset"

        # Global operations (create, list, update, delete)
        create_response = CreateTagResponse(id=tag_id, name="Global Tag", type="knowledge", binding_count=0)
        list_response = ListTagsResponse(
            data=[TagInfo(id=tag_id, name="Global Tag", type="knowledge", binding_count=0)]
        )
        update_response = UpdateTagResponse(id=tag_id, name="Updated Global Tag", type="knowledge", binding_count=0)
        delete_response = DeleteTagResponse(result="success")

        # Dataset-specific operations (query_bound)
        query_response = QueryBoundTagsResponse(data=[TagInfo(id=tag_id, name="Global Tag")], total=1)

        mock_execute = Mock()
        mock_execute.side_effect = [
            create_response,
            list_response,
            update_response,
            query_response,
            delete_response,
        ]
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test global operations
        create_request = CreateTagRequest.builder().name("Global Tag").build()
        created = tag_resource.create(create_request, request_option)
        assert created.name == "Global Tag"

        list_request = ListTagsRequest.builder().build()
        listed = tag_resource.list(list_request, request_option)
        assert len(listed.data) == 1

        update_request = UpdateTagRequest.builder().name("Updated Global Tag").tag_id(tag_id).build()
        updated = tag_resource.update(update_request, request_option)
        assert updated.name == "Updated Global Tag"

        # Test dataset-specific operation
        query_request = QueryBoundTagsRequest.builder().dataset_id(dataset_id).build()
        query_result = tag_resource.query_bound(query_request, request_option)
        assert len(query_result.data) == 1

        delete_request = DeleteTagRequest.builder().tag_id(tag_id).build()
        delete_result = tag_resource.delete(delete_request, request_option)
        assert delete_result.result == "success"

    def test_error_scenarios(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test error handling scenarios"""
        # Mock error response
        mock_execute = Mock(side_effect=Exception("Tag API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        create_request = CreateTagRequest.builder().name("Error Tag").build()

        with pytest.raises(Exception) as exc_info:
            tag_resource.create(create_request, request_option)

        assert str(exc_info.value) == "Tag API Error"

    def test_edge_cases(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test edge cases and boundary conditions"""
        # Test empty tag list
        empty_list_response = ListTagsResponse(data=[])
        mock_execute = Mock(return_value=empty_list_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        list_request = ListTagsRequest.builder().build()
        result = tag_resource.list(list_request, request_option)
        assert len(result.data) == 0

        # Test empty bound tags query
        empty_query_response = QueryBoundTagsResponse(data=[], total=0)
        mock_execute.return_value = empty_query_response

        query_request = QueryBoundTagsRequest.builder().dataset_id("empty-dataset").build()
        query_result = tag_resource.query_bound(query_request, request_option)
        assert len(query_result.data) == 0
        assert query_result.total == 0

        # Test tag with maximum length name (50 characters)
        long_name = "A" * 50
        create_response = CreateTagResponse(id="long-name-tag", name=long_name, type="knowledge", binding_count=0)
        mock_execute.return_value = create_response

        create_request = CreateTagRequest.builder().name(long_name).build()
        result = tag_resource.create(create_request, request_option)
        assert result.name == long_name
        assert len(result.name) == 50

    def test_tag_name_validation_scenarios(
        self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test various tag name validation scenarios"""
        # Test different valid tag names
        valid_names = [
            "Simple Tag",
            "Tag-with-hyphens",
            "Tag_with_underscores",
            "Tag123",
            "中文标签",  # Chinese characters
            "Tag with spaces",
        ]

        for name in valid_names:
            create_response = CreateTagResponse(id=f"tag-{hash(name)}", name=name, type="knowledge", binding_count=0)
            mock_execute = Mock(return_value=create_response)
            monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

            create_request = CreateTagRequest.builder().name(name).build()
            result = tag_resource.create(create_request, request_option)
            assert result.name == name
