import pytest
from unittest.mock import Mock, AsyncMock
from typing import Any

from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption
from dify_oapi.api.knowledge_base.v1.resource.dataset import Dataset
from dify_oapi.api.knowledge_base.v1.resource.metadata import Metadata
from dify_oapi.api.knowledge_base.v1.resource.tag import Tag

# Dataset imports
from dify_oapi.api.knowledge_base.v1.model.dataset.create_request import (
    CreateDatasetRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.create_response import (
    CreateDatasetResponse,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_request import (
    RetrieveDatasetRequest,
)
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import (
    RetrieveDatasetResponse,
    QueryInfo,
)

# Metadata imports
from dify_oapi.api.knowledge_base.v1.model.metadata.create_request import (
    CreateMetadataRequest,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.create_response import (
    CreateMetadataResponse,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.list_request import (
    ListMetadataRequest,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.list_response import (
    ListMetadataResponse,
)
from dify_oapi.api.knowledge_base.v1.model.metadata.metadata_info import MetadataInfo

# Tag imports
from dify_oapi.api.knowledge_base.v1.model.tag.create_request import CreateTagRequest
from dify_oapi.api.knowledge_base.v1.model.tag.create_response import CreateTagResponse
from dify_oapi.api.knowledge_base.v1.model.tag.bind_request import BindTagsRequest
from dify_oapi.api.knowledge_base.v1.model.tag.bind_response import BindTagsResponse
from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_request import (
    QueryBoundTagsRequest,
)
from dify_oapi.api.knowledge_base.v1.model.tag.query_bound_response import (
    QueryBoundTagsResponse,
)
from dify_oapi.api.knowledge_base.v1.model.tag.tag_info import TagInfo


class TestComprehensiveIntegration:
    @pytest.fixture
    def config(self) -> Config:
        return Config()

    @pytest.fixture
    def dataset_resource(self, config: Config) -> Dataset:
        return Dataset(config)

    @pytest.fixture
    def metadata_resource(self, config: Config) -> Metadata:
        return Metadata(config)

    @pytest.fixture
    def tag_resource(self, config: Config) -> Tag:
        return Tag(config)

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_complete_knowledge_base_setup_workflow(
        self,
        dataset_resource: Dataset,
        metadata_resource: Metadata,
        tag_resource: Tag,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test complete workflow: create dataset → add metadata → create tags → bind tags → retrieve"""
        dataset_id = "comprehensive-dataset-id"
        tag_id = "comprehensive-tag-id"
        metadata_id = "comprehensive-metadata-id"

        # Mock responses for the complete workflow
        responses = [
            # 1. Create dataset
            CreateDatasetResponse(
                id=dataset_id,
                name="Comprehensive Dataset",
                description="Full workflow test",
            ),
            # 2. Create metadata
            CreateMetadataResponse(
                id=metadata_id, type="string", name="Document Category"
            ),
            # 3. List metadata to verify creation
            ListMetadataResponse(
                doc_metadata=[
                    MetadataInfo(
                        id=metadata_id,
                        name="Document Category",
                        type="string",
                        use_count=0,
                    )
                ],
                built_in_field_enabled=True,
            ),
            # 4. Create tag
            CreateTagResponse(
                id=tag_id,
                name="Technical Documentation",
                type="knowledge",
                binding_count=0,
            ),
            # 5. Bind tag to dataset
            BindTagsResponse(result="success"),
            # 6. Query bound tags to verify binding
            QueryBoundTagsResponse(
                data=[TagInfo(id=tag_id, name="Technical Documentation")], total=1
            ),
            # 7. Retrieve from dataset with metadata filtering
            RetrieveDatasetResponse(
                query=QueryInfo(content="comprehensive test query"), records=[]
            ),
        ]

        mock_execute = Mock()
        mock_execute.side_effect = responses
        monkeypatch.setattr(
            "dify_oapi.core.http.transport.Transport.execute", mock_execute
        )

        # 1. Create dataset
        create_dataset_request = (
            CreateDatasetRequest.builder()
            .name("Comprehensive Dataset")
            .description("Full workflow test")
            .build()
        )
        created_dataset = dataset_resource.create(
            create_dataset_request, request_option
        )
        assert created_dataset.id == dataset_id
        assert created_dataset.name == "Comprehensive Dataset"

        # 2. Add metadata to dataset
        create_metadata_request = (
            CreateMetadataRequest.builder()
            .dataset_id(dataset_id)
            .type("string")
            .name("Document Category")
            .build()
        )
        created_metadata = metadata_resource.create(
            create_metadata_request, request_option
        )
        assert created_metadata.id == metadata_id
        assert created_metadata.name == "Document Category"

        # 3. Verify metadata was created
        list_metadata_request = (
            ListMetadataRequest.builder().dataset_id(dataset_id).build()
        )
        metadata_list = metadata_resource.list(list_metadata_request, request_option)
        assert len(metadata_list.doc_metadata) == 1
        assert metadata_list.doc_metadata[0].id == metadata_id

        # 4. Create knowledge type tag
        create_tag_request = (
            CreateTagRequest.builder().name("Technical Documentation").build()
        )
        created_tag = tag_resource.create(create_tag_request, request_option)
        assert created_tag.id == tag_id
        assert created_tag.name == "Technical Documentation"

        # 5. Bind tag to dataset
        bind_tag_request = (
            BindTagsRequest.builder().tag_ids([tag_id]).target_id(dataset_id).build()
        )
        bind_result = tag_resource.bind_tags(bind_tag_request, request_option)
        assert bind_result.result == "success"

        # 6. Verify tag binding
        query_bound_request = (
            QueryBoundTagsRequest.builder().dataset_id(dataset_id).build()
        )
        bound_tags = tag_resource.query_bound(query_bound_request, request_option)
        assert len(bound_tags.data) == 1
        assert bound_tags.data[0].id == tag_id

        # 7. Perform retrieval with the configured dataset
        retrieve_request = (
            RetrieveDatasetRequest.builder()
            .dataset_id(dataset_id)
            .query("comprehensive test query")
            .build()
        )
        retrieve_result = dataset_resource.retrieve(retrieve_request, request_option)
        assert retrieve_result.query.content == "comprehensive test query"

        # Verify all operations were executed
        assert mock_execute.call_count == 7

    @pytest.mark.asyncio
    async def test_complete_workflow_async(
        self,
        dataset_resource: Dataset,
        metadata_resource: Metadata,
        tag_resource: Tag,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test complete workflow with async methods"""
        dataset_id = "async-comprehensive-dataset"
        tag_id = "async-comprehensive-tag"
        metadata_id = "async-comprehensive-metadata"

        # Mock async responses
        responses = [
            CreateDatasetResponse(id=dataset_id, name="Async Comprehensive Dataset"),
            CreateMetadataResponse(
                id=metadata_id, type="number", name="Priority Level"
            ),
            CreateTagResponse(
                id=tag_id, name="High Priority", type="knowledge", binding_count=0
            ),
            BindTagsResponse(result="success"),
            RetrieveDatasetResponse(query=QueryInfo(content="async query"), records=[]),
        ]

        mock_aexecute = AsyncMock()
        mock_aexecute.side_effect = responses
        monkeypatch.setattr(
            "dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute
        )

        # Execute async workflow
        create_dataset_request = (
            CreateDatasetRequest.builder().name("Async Comprehensive Dataset").build()
        )
        created_dataset = await dataset_resource.acreate(
            create_dataset_request, request_option
        )
        assert created_dataset.id == dataset_id

        create_metadata_request = (
            CreateMetadataRequest.builder()
            .dataset_id(dataset_id)
            .type("number")
            .name("Priority Level")
            .build()
        )
        created_metadata = await metadata_resource.acreate(
            create_metadata_request, request_option
        )
        assert created_metadata.id == metadata_id

        create_tag_request = CreateTagRequest.builder().name("High Priority").build()
        created_tag = await tag_resource.acreate(create_tag_request, request_option)
        assert created_tag.id == tag_id

        bind_tag_request = (
            BindTagsRequest.builder().tag_ids([tag_id]).target_id(dataset_id).build()
        )
        bind_result = await tag_resource.abind_tags(bind_tag_request, request_option)
        assert bind_result.result == "success"

        retrieve_request = (
            RetrieveDatasetRequest.builder()
            .dataset_id(dataset_id)
            .query("async query")
            .build()
        )
        retrieve_result = await dataset_resource.aretrieve(
            retrieve_request, request_option
        )
        assert retrieve_result.query.content == "async query"

        assert mock_aexecute.call_count == 5

    def test_cross_resource_dependencies(
        self,
        dataset_resource: Dataset,
        metadata_resource: Metadata,
        tag_resource: Tag,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test dependencies and interactions between different resources"""
        dataset_id = "dependency-dataset"

        # Test that metadata operations require existing dataset
        create_metadata_request = (
            CreateMetadataRequest.builder()
            .dataset_id(dataset_id)
            .type("string")
            .name("Test Field")
            .build()
        )

        # Mock metadata creation response
        metadata_response = CreateMetadataResponse(
            id="meta-id", type="string", name="Test Field"
        )
        mock_execute = Mock(return_value=metadata_response)
        monkeypatch.setattr(
            "dify_oapi.core.http.transport.Transport.execute", mock_execute
        )

        # This should work (assuming dataset exists)
        result = metadata_resource.create(create_metadata_request, request_option)
        assert result.name == "Test Field"

        # Test that tag binding requires existing dataset and tag
        bind_request = (
            BindTagsRequest.builder()
            .tag_ids(["existing-tag"])
            .target_id(dataset_id)
            .build()
        )
        bind_response = BindTagsResponse(result="success")
        mock_execute.return_value = bind_response

        bind_result = tag_resource.bind_tags(bind_request, request_option)
        assert bind_result.result == "success"

    def test_multiple_datasets_with_shared_resources(
        self,
        dataset_resource: Dataset,
        metadata_resource: Metadata,
        tag_resource: Tag,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test scenarios with multiple datasets sharing tags and metadata patterns"""
        dataset1_id = "shared-dataset-1"
        dataset2_id = "shared-dataset-2"
        shared_tag_id = "shared-tag"

        # Mock responses for multiple dataset scenario
        responses = [
            # Create first dataset
            CreateDatasetResponse(id=dataset1_id, name="Shared Dataset 1"),
            # Create second dataset
            CreateDatasetResponse(id=dataset2_id, name="Shared Dataset 2"),
            # Create shared tag
            CreateTagResponse(
                id=shared_tag_id,
                name="Shared Category",
                type="knowledge",
                binding_count=0,
            ),
            # Bind tag to first dataset
            BindTagsResponse(result="success"),
            # Bind tag to second dataset
            BindTagsResponse(result="success"),
            # Query tags for first dataset
            QueryBoundTagsResponse(
                data=[TagInfo(id=shared_tag_id, name="Shared Category")], total=1
            ),
            # Query tags for second dataset
            QueryBoundTagsResponse(
                data=[TagInfo(id=shared_tag_id, name="Shared Category")], total=1
            ),
        ]

        mock_execute = Mock()
        mock_execute.side_effect = responses
        monkeypatch.setattr(
            "dify_oapi.core.http.transport.Transport.execute", mock_execute
        )

        # Create two datasets
        create_request1 = (
            CreateDatasetRequest.builder().name("Shared Dataset 1").build()
        )
        dataset1 = dataset_resource.create(create_request1, request_option)
        assert dataset1.id == dataset1_id

        create_request2 = (
            CreateDatasetRequest.builder().name("Shared Dataset 2").build()
        )
        dataset2 = dataset_resource.create(create_request2, request_option)
        assert dataset2.id == dataset2_id

        # Create shared tag
        create_tag_request = CreateTagRequest.builder().name("Shared Category").build()
        shared_tag = tag_resource.create(create_tag_request, request_option)
        assert shared_tag.id == shared_tag_id

        # Bind tag to both datasets
        bind_request1 = (
            BindTagsRequest.builder()
            .tag_ids([shared_tag_id])
            .target_id(dataset1_id)
            .build()
        )
        bind_result1 = tag_resource.bind_tags(bind_request1, request_option)
        assert bind_result1.result == "success"

        bind_request2 = (
            BindTagsRequest.builder()
            .tag_ids([shared_tag_id])
            .target_id(dataset2_id)
            .build()
        )
        bind_result2 = tag_resource.bind_tags(bind_request2, request_option)
        assert bind_result2.result == "success"

        # Verify both datasets have the shared tag
        query_request1 = QueryBoundTagsRequest.builder().dataset_id(dataset1_id).build()
        tags1 = tag_resource.query_bound(query_request1, request_option)
        assert len(tags1.data) == 1
        assert tags1.data[0].id == shared_tag_id

        query_request2 = QueryBoundTagsRequest.builder().dataset_id(dataset2_id).build()
        tags2 = tag_resource.query_bound(query_request2, request_option)
        assert len(tags2.data) == 1
        assert tags2.data[0].id == shared_tag_id

        assert mock_execute.call_count == 7

    def test_advanced_retrieval_with_metadata_filtering(
        self,
        dataset_resource: Dataset,
        metadata_resource: Metadata,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test advanced retrieval scenarios with metadata filtering"""
        dataset_id = "filtered-dataset"

        # Mock retrieval with metadata filtering
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import (
            RetrievalModel,
        )
        from dify_oapi.api.knowledge_base.v1.model.dataset.metadata_filtering_conditions import (
            MetadataFilteringConditions,
        )
        from dify_oapi.api.knowledge_base.v1.model.dataset.filter_condition import (
            FilterCondition,
        )

        # Create metadata filtering conditions
        filter_condition = (
            FilterCondition.builder()
            .name("category")
            .comparison_operator("is")
            .value("technical")
            .build()
        )
        filtering_conditions = (
            MetadataFilteringConditions.builder()
            .logical_operator("and")
            .conditions([filter_condition])
            .build()
        )

        # Create retrieval model with filtering
        retrieval_model = (
            RetrievalModel.builder()
            .search_method("semantic_search")
            .top_k(5)
            .metadata_filtering_conditions(filtering_conditions)
            .build()
        )

        # Mock filtered retrieval response
        retrieve_response = RetrieveDatasetResponse(
            query=QueryInfo(content="filtered query"), records=[]
        )
        mock_execute = Mock(return_value=retrieve_response)
        monkeypatch.setattr(
            "dify_oapi.core.http.transport.Transport.execute", mock_execute
        )

        # Perform filtered retrieval
        retrieve_request = (
            RetrieveDatasetRequest.builder()
            .dataset_id(dataset_id)
            .query("filtered query")
            .retrieval_model(retrieval_model)
            .build()
        )
        result = dataset_resource.retrieve(retrieve_request, request_option)

        assert result.query.content == "filtered query"

    def test_error_propagation_across_resources(
        self,
        dataset_resource: Dataset,
        metadata_resource: Metadata,
        tag_resource: Tag,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test error handling and propagation across different resources"""
        # Mock error in dataset creation
        mock_execute = Mock(side_effect=Exception("Dataset creation failed"))
        monkeypatch.setattr(
            "dify_oapi.core.http.transport.Transport.execute", mock_execute
        )

        create_dataset_request = (
            CreateDatasetRequest.builder().name("Error Dataset").build()
        )

        with pytest.raises(Exception) as exc_info:
            dataset_resource.create(create_dataset_request, request_option)
        assert str(exc_info.value) == "Dataset creation failed"

        # Mock error in metadata creation
        mock_execute.side_effect = Exception("Metadata creation failed")
        create_metadata_request = (
            CreateMetadataRequest.builder()
            .dataset_id("error-dataset")
            .type("string")
            .name("Error Field")
            .build()
        )

        with pytest.raises(Exception) as exc_info:
            metadata_resource.create(create_metadata_request, request_option)
        assert str(exc_info.value) == "Metadata creation failed"

        # Mock error in tag creation
        mock_execute.side_effect = Exception("Tag creation failed")
        create_tag_request = CreateTagRequest.builder().name("Error Tag").build()

        with pytest.raises(Exception) as exc_info:
            tag_resource.create(create_tag_request, request_option)
        assert str(exc_info.value) == "Tag creation failed"

    def test_resource_cleanup_workflow(
        self,
        dataset_resource: Dataset,
        metadata_resource: Metadata,
        tag_resource: Tag,
        request_option: RequestOption,
        monkeypatch: Any,
    ) -> None:
        """Test proper cleanup workflow: unbind tags → delete metadata → delete dataset → delete tags"""
        dataset_id = "cleanup-dataset"
        tag_id = "cleanup-tag"
        metadata_id = "cleanup-metadata"

        # Mock cleanup responses
        from dify_oapi.api.knowledge_base.v1.model.tag.unbind_request import (
            UnbindTagRequest,
        )
        from dify_oapi.api.knowledge_base.v1.model.tag.unbind_response import (
            UnbindTagResponse,
        )
        from dify_oapi.api.knowledge_base.v1.model.metadata.delete_request import (
            DeleteMetadataRequest,
        )
        from dify_oapi.api.knowledge_base.v1.model.metadata.delete_response import (
            DeleteMetadataResponse,
        )
        from dify_oapi.api.knowledge_base.v1.model.dataset.delete_request import (
            DeleteDatasetRequest,
        )
        from dify_oapi.api.knowledge_base.v1.model.dataset.delete_response import (
            DeleteDatasetResponse,
        )
        from dify_oapi.api.knowledge_base.v1.model.tag.delete_request import (
            DeleteTagRequest,
        )
        from dify_oapi.api.knowledge_base.v1.model.tag.delete_response import (
            DeleteTagResponse,
        )

        cleanup_responses = [
            UnbindTagResponse(result="success"),  # Unbind tag
            DeleteMetadataResponse(),  # Delete metadata
            DeleteDatasetResponse(),  # Delete dataset
            DeleteTagResponse(result="success"),  # Delete tag
        ]

        mock_execute = Mock()
        mock_execute.side_effect = cleanup_responses
        monkeypatch.setattr(
            "dify_oapi.core.http.transport.Transport.execute", mock_execute
        )

        # 1. Unbind tag from dataset
        unbind_request = (
            UnbindTagRequest.builder().tag_id(tag_id).target_id(dataset_id).build()
        )
        unbind_result = tag_resource.unbind_tag(unbind_request, request_option)
        assert unbind_result.result == "success"

        # 2. Delete metadata
        delete_metadata_request = (
            DeleteMetadataRequest.builder()
            .dataset_id(dataset_id)
            .metadata_id(metadata_id)
            .build()
        )
        metadata_resource.delete(delete_metadata_request, request_option)

        # 3. Delete dataset
        delete_dataset_request = (
            DeleteDatasetRequest.builder().dataset_id(dataset_id).build()
        )
        dataset_resource.delete(delete_dataset_request, request_option)

        # 4. Delete tag
        delete_tag_request = DeleteTagRequest.builder().tag_id(tag_id).build()
        delete_result = tag_resource.delete(delete_tag_request, request_option)
        assert delete_result.result == "success"

        # Verify all cleanup operations were executed
        assert mock_execute.call_count == 4
