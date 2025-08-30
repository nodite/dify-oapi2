"""Integration tests for Dataset API functionality."""

from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest

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
from dify_oapi.api.knowledge.v1.model.query_info import QueryInfo
from dify_oapi.api.knowledge.v1.model.retrieval_model import RetrievalModel
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request_body import RetrieveFromDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_response import RetrieveFromDatasetResponse
from dify_oapi.api.knowledge.v1.model.update_dataset_request import UpdateDatasetRequest
from dify_oapi.api.knowledge.v1.model.update_dataset_request_body import UpdateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.update_dataset_response import UpdateDatasetResponse
from dify_oapi.api.knowledge.v1.resource.dataset import Dataset
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestDatasetIntegration:
    """Test all 6 Dataset Resource APIs."""

    @pytest.fixture
    def dataset_resource(self) -> Dataset:
        return Dataset(Config())

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_create_dataset(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test POST /v1/datasets"""
        response = CreateDatasetResponse(id="dataset-id", name="Test Dataset")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateDatasetRequestBody.builder().name("Test Dataset").build()
        request = CreateDatasetRequest.builder().request_body(request_body).build()
        result = dataset_resource.create(request, request_option)

        assert result.id == "dataset-id"
        assert result.name == "Test Dataset"

    def test_list_datasets(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets"""
        response = ListDatasetsResponse(data=[], has_more=False, limit=20, total=0, page=1)
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListDatasetsRequest.builder().page(1).limit(20).build()
        result = dataset_resource.list(request, request_option)

        assert result.total == 0
        assert result.page == 1

    def test_get_dataset(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets/{dataset_id}"""
        response = GetDatasetResponse(id="dataset-id", name="Test Dataset")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetDatasetRequest.builder().dataset_id("dataset-id").build()
        result = dataset_resource.get(request, request_option)

        assert result.id == "dataset-id"

    def test_update_dataset(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test PATCH /v1/datasets/{dataset_id}"""
        response = UpdateDatasetResponse(id="dataset-id", name="Updated Dataset")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UpdateDatasetRequestBody.builder().name("Updated Dataset").build()
        request = UpdateDatasetRequest.builder().dataset_id("dataset-id").request_body(request_body).build()
        result = dataset_resource.update(request, request_option)

        assert result.name == "Updated Dataset"

    def test_delete_dataset(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test DELETE /v1/datasets/{dataset_id}"""
        response = DeleteDatasetResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = DeleteDatasetRequest.builder().dataset_id("dataset-id").build()
        result = dataset_resource.delete(request, request_option)

        assert result.result == "success"

    def test_retrieve_from_dataset(
        self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test POST /v1/datasets/{dataset_id}/retrieve"""
        response = RetrieveFromDatasetResponse(query=QueryInfo(content="test query"), records=[])
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = RetrieveFromDatasetRequestBody.builder().query("test query").build()
        request = RetrieveFromDatasetRequest.builder().dataset_id("dataset-id").request_body(request_body).build()
        result = dataset_resource.retrieve(request, request_option)

        assert result.query.content == "test query"

    def test_dataset_lifecycle_sync(
        self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test complete dataset lifecycle: create → get → update → retrieve → delete"""
        dataset_id = "test-dataset-id"

        # Mock create dataset
        create_response = CreateDatasetResponse(
            id=dataset_id, name="Test Dataset", description="Test description", provider="vendor", permission="only_me"
        )

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

        # Mock update dataset
        update_response = UpdateDatasetResponse(
            id=dataset_id, name="Updated Dataset", provider="vendor", permission="only_me"
        )

        # Mock retrieve dataset
        query_info = QueryInfo(content="test query")
        retrieve_response = RetrieveFromDatasetResponse(query=query_info, records=[])

        # Mock delete dataset
        delete_response = DeleteDatasetResponse(result="success")

        # Set up mocks
        mock_execute = Mock()
        mock_execute.side_effect = [create_response, get_response, update_response, retrieve_response, delete_response]
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # 1. Create dataset
        create_body = CreateDatasetRequestBody.builder().name("Test Dataset").description("Test description").build()
        create_request = CreateDatasetRequest.builder().request_body(create_body).build()
        created = dataset_resource.create(create_request, request_option)
        assert created.id == dataset_id
        assert created.name == "Test Dataset"

        # 2. Get dataset details
        get_request = GetDatasetRequest.builder().dataset_id(dataset_id).build()
        retrieved = dataset_resource.get(get_request, request_option)
        assert retrieved.id == dataset_id
        assert retrieved.name == "Test Dataset"

        # 3. Update dataset
        update_body = UpdateDatasetRequestBody.builder().name("Updated Dataset").build()
        update_request = UpdateDatasetRequest.builder().dataset_id(dataset_id).request_body(update_body).build()
        updated = dataset_resource.update(update_request, request_option)
        assert updated.id == dataset_id
        assert updated.name == "Updated Dataset"

        # 4. Retrieve from dataset
        retrieve_body = RetrieveFromDatasetRequestBody.builder().query("test query").build()
        retrieve_request = (
            RetrieveFromDatasetRequest.builder().dataset_id(dataset_id).request_body(retrieve_body).build()
        )
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
        retrieve_response = RetrieveFromDatasetResponse(query=QueryInfo(content="async query"), records=[])
        delete_response = DeleteDatasetResponse(result="success")

        mock_aexecute = AsyncMock()
        mock_aexecute.side_effect = [create_response, get_response, update_response, retrieve_response, delete_response]
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        # Execute async lifecycle
        create_body = CreateDatasetRequestBody.builder().name("Async Dataset").build()
        create_request = CreateDatasetRequest.builder().request_body(create_body).build()
        created = await dataset_resource.acreate(create_request, request_option)
        assert created.id == dataset_id

        get_request = GetDatasetRequest.builder().dataset_id(dataset_id).build()
        retrieved = await dataset_resource.aget(get_request, request_option)
        assert retrieved.id == dataset_id

        update_body = UpdateDatasetRequestBody.builder().name("Updated Async Dataset").build()
        update_request = UpdateDatasetRequest.builder().dataset_id(dataset_id).request_body(update_body).build()
        updated = await dataset_resource.aupdate(update_request, request_option)
        assert updated.name == "Updated Async Dataset"

        retrieve_body = RetrieveFromDatasetRequestBody.builder().query("async query").build()
        retrieve_request = (
            RetrieveFromDatasetRequest.builder().dataset_id(dataset_id).request_body(retrieve_body).build()
        )
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

        list_response = ListDatasetsResponse(data=mock_datasets, total=2, page=1, limit="20", has_more=False)
        mock_execute = Mock(return_value=list_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test with pagination
        list_request = ListDatasetsRequest.builder().page(1).limit(20).build()
        result = dataset_resource.list(list_request, request_option)

        assert len(result.data) == 2
        assert result.total == 2
        assert result.page == 1
        assert result.has_more is False

    def test_dataset_retrieve_with_advanced_config(
        self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test dataset retrieval with advanced retrieval configuration"""
        from dify_oapi.api.knowledge.v1.model.reranking_model import RerankingModel

        # Create advanced retrieval model
        reranking_model = RerankingModel(reranking_provider_name="cohere", reranking_model_name="rerank-english-v2.0")
        retrieval_model = RetrievalModel(
            search_method="hybrid_search",
            reranking_enable=True,
            reranking_model=reranking_model,
            top_k=10,
            score_threshold_enabled=True,
            score_threshold=0.7,
        )

        retrieve_response = RetrieveFromDatasetResponse(query=QueryInfo(content="advanced query"), records=[])
        mock_execute = Mock(return_value=retrieve_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        retrieve_body = (
            RetrieveFromDatasetRequestBody.builder().query("advanced query").retrieval_model(retrieval_model).build()
        )
        retrieve_request = (
            RetrieveFromDatasetRequest.builder().dataset_id("test-id").request_body(retrieve_body).build()
        )
        result = dataset_resource.retrieve(retrieve_request, request_option)

        assert result.query.content == "advanced query"

    def test_error_scenarios(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test error handling scenarios"""

        # Mock error response
        mock_execute = Mock(side_effect=Exception("API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        create_body = CreateDatasetRequestBody.builder().name("Error Dataset").build()
        create_request = CreateDatasetRequest.builder().request_body(create_body).build()

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
        minimal_body = CreateDatasetRequestBody.builder().name("Minimal Dataset").build()
        minimal_request = CreateDatasetRequest.builder().request_body(minimal_body).build()
        result = dataset_resource.create(minimal_request, request_option)

        assert result.id == "minimal-id"
        assert result.name == "Minimal Dataset"

        # Test empty list response
        empty_list_response = ListDatasetsResponse(data=[], total=0, page=1, limit="20", has_more=False)
        mock_execute.return_value = empty_list_response

        list_request = ListDatasetsRequest.builder().page(1).limit(20).build()
        empty_result = dataset_resource.list(list_request, request_option)

        assert len(empty_result.data) == 0
        assert empty_result.total == 0
