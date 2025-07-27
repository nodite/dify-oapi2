from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest

from dify_oapi.api.knowledge_base.v1.model.dataset.create_request import CreateDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.create_response import CreateDatasetResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.dataset_info import DatasetInfo
from dify_oapi.api.knowledge_base.v1.model.dataset.delete_request import DeleteDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.delete_response import DeleteDatasetResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.get_request import GetDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.get_response import GetDatasetResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.list_request import ListDatasetsRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.list_response import ListDatasetsResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_request import RetrieveDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import QueryInfo, RetrieveDatasetResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.update_request import UpdateDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.update_response import UpdateDatasetResponse
from dify_oapi.api.knowledge_base.v1.resource.dataset import Dataset
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestDatasetAPIIntegration:
    @pytest.fixture
    def config(self) -> Config:
        return Config()

    @pytest.fixture
    def dataset_resource(self, config: Config) -> Dataset:
        return Dataset(config)

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_dataset_lifecycle_sync(
        self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test complete dataset lifecycle: create → get → update → retrieve → delete"""
        dataset_id = "test-dataset-id"

        # Mock create dataset
        create_response = CreateDatasetResponse(
            id=dataset_id, name="Test Dataset", description="Test description", provider="vendor", permission="only_me"
        )
        Mock(return_value=create_response)

        # Mock get dataset
        get_response = GetDatasetResponse(
            id=dataset_id,
            name="Test Dataset",
            description="Test description",
            provider="vendor",
            permission="only_me",
            app_count=0,
            document_count=0,
            word_count=0,
        )
        Mock(return_value=get_response)

        # Mock update dataset
        update_response = UpdateDatasetResponse(
            id=dataset_id, name="Updated Dataset", provider="vendor", permission="only_me"
        )
        Mock(return_value=update_response)

        # Mock retrieve dataset
        retrieve_response = RetrieveDatasetResponse(query=QueryInfo(content="test query"), records=[])
        Mock(return_value=retrieve_response)

        # Mock delete dataset
        delete_response = DeleteDatasetResponse()
        Mock(return_value=delete_response)

        # Set up mocks
        mock_execute = Mock()
        mock_execute.side_effect = [create_response, get_response, update_response, retrieve_response, delete_response]
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # 1. Create dataset
        create_request = CreateDatasetRequest.builder().name("Test Dataset").description("Test description").build()
        created = dataset_resource.create(create_request, request_option)
        assert created.id == dataset_id
        assert created.name == "Test Dataset"

        # 2. Get dataset details
        get_request = GetDatasetRequest.builder().dataset_id(dataset_id).build()
        retrieved = dataset_resource.get(get_request, request_option)
        assert retrieved.id == dataset_id
        assert retrieved.name == "Test Dataset"

        # 3. Update dataset
        update_request = UpdateDatasetRequest.builder().dataset_id(dataset_id).name("Updated Dataset").build()
        updated = dataset_resource.update(update_request, request_option)
        assert updated.id == dataset_id
        assert updated.name == "Updated Dataset"

        # 4. Retrieve from dataset
        retrieve_request = RetrieveDatasetRequest.builder().dataset_id(dataset_id).query("test query").build()
        search_result = dataset_resource.retrieve(retrieve_request, request_option)
        assert search_result.query.content == "test query"
        assert search_result.records == []

        # 5. Delete dataset
        delete_request = DeleteDatasetRequest.builder().dataset_id(dataset_id).build()
        dataset_resource.delete(delete_request, request_option)

        # Verify all calls were made
        assert mock_execute.call_count == 5

    @pytest.mark.asyncio
    async def test_dataset_lifecycle_async(
        self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test complete dataset lifecycle with async methods"""
        dataset_id = "test-dataset-id-async"

        # Mock responses
        create_response = CreateDatasetResponse(id=dataset_id, name="Async Dataset")
        get_response = GetDatasetResponse(id=dataset_id, name="Async Dataset")
        update_response = UpdateDatasetResponse(id=dataset_id, name="Updated Async Dataset")
        retrieve_response = RetrieveDatasetResponse(query=QueryInfo(content="async query"), records=[])
        delete_response = DeleteDatasetResponse()

        mock_aexecute = AsyncMock()
        mock_aexecute.side_effect = [create_response, get_response, update_response, retrieve_response, delete_response]
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        # Execute async lifecycle
        create_request = CreateDatasetRequest.builder().name("Async Dataset").build()
        created = await dataset_resource.acreate(create_request, request_option)
        assert created.id == dataset_id

        get_request = GetDatasetRequest.builder().dataset_id(dataset_id).build()
        retrieved = await dataset_resource.aget(get_request, request_option)
        assert retrieved.id == dataset_id

        update_request = UpdateDatasetRequest.builder().dataset_id(dataset_id).name("Updated Async Dataset").build()
        updated = await dataset_resource.aupdate(update_request, request_option)
        assert updated.name == "Updated Async Dataset"

        retrieve_request = RetrieveDatasetRequest.builder().dataset_id(dataset_id).query("async query").build()
        search_result = await dataset_resource.aretrieve(retrieve_request, request_option)
        assert search_result.query.content == "async query"

        delete_request = DeleteDatasetRequest.builder().dataset_id(dataset_id).build()
        await dataset_resource.adelete(delete_request, request_option)

        assert mock_aexecute.call_count == 5

    def test_dataset_list_with_pagination(
        self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test dataset listing with pagination and filtering"""
        mock_datasets = [DatasetInfo(id="dataset1", name="Dataset 1"), DatasetInfo(id="dataset2", name="Dataset 2")]

        list_response = (
            ListDatasetsResponse.builder().data(mock_datasets).total(2).page(1).limit("20").has_more(False).build()
        )
        mock_execute = Mock(return_value=list_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test with pagination
        list_request = ListDatasetsRequest.builder().page(1).limit("20").keyword("test").build()
        result = dataset_resource.list(list_request, request_option)

        assert len(result.data) == 2
        assert result.total == 2
        assert result.page == 1
        assert result.has_more is False

    def test_dataset_retrieve_with_advanced_config(
        self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test dataset retrieval with advanced retrieval configuration"""
        from dify_oapi.api.knowledge_base.v1.model.dataset.reranking_model import RerankingModel

        # Create advanced retrieval model
        reranking_model = (
            RerankingModel.builder()
            .reranking_provider_name("cohere")
            .reranking_model_name("rerank-english-v2.0")
            .build()
        )
        retrieval_model = (
            RetrievalModel.builder()
            .search_method("hybrid_search")
            .reranking_enable(True)
            .reranking_model(reranking_model)
            .top_k(10)
            .score_threshold_enabled(True)
            .score_threshold(0.7)
            .build()
        )

        retrieve_response = RetrieveDatasetResponse(query=QueryInfo(content="advanced query"), records=[])
        mock_execute = Mock(return_value=retrieve_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        retrieve_request = (
            RetrieveDatasetRequest.builder()
            .dataset_id("test-id")
            .query("advanced query")
            .retrieval_model(retrieval_model)
            .build()
        )
        result = dataset_resource.retrieve(retrieve_request, request_option)

        assert result.query.content == "advanced query"

    def test_error_scenarios(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test error handling scenarios"""

        # Mock error response
        mock_execute = Mock(side_effect=Exception("API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        create_request = CreateDatasetRequest.builder().name("Error Dataset").build()

        with pytest.raises(Exception) as exc_info:
            dataset_resource.create(create_request, request_option)

        assert str(exc_info.value) == "API Error"

    def test_edge_cases(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test edge cases and boundary conditions"""
        # Test with minimal required fields
        create_response = CreateDatasetResponse(id="minimal-id", name="Minimal Dataset")
        mock_execute = Mock(return_value=create_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create with only required fields
        minimal_request = CreateDatasetRequest.builder().name("Minimal Dataset").build()
        result = dataset_resource.create(minimal_request, request_option)

        assert result.id == "minimal-id"
        assert result.name == "Minimal Dataset"

        # Test empty list response
        empty_list_response = (
            ListDatasetsResponse.builder().data([]).total(0).page(1).limit("20").has_more(False).build()
        )
        mock_execute.return_value = empty_list_response

        list_request = ListDatasetsRequest.builder().page(1).limit("20").build()
        empty_result = dataset_resource.list(list_request, request_option)

        assert len(empty_result.data) == 0
        assert empty_result.total == 0
