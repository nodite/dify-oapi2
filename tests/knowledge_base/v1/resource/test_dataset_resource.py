import pytest
from unittest.mock import Mock, AsyncMock
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption
from dify_oapi.api.knowledge_base.v1.resource.dataset import Dataset

# Import new dataset models
from dify_oapi.api.knowledge_base.v1.model.dataset.create_request import CreateDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.create_response import CreateDatasetResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.list_request import ListDatasetsRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.list_response import ListDatasetsResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.get_request import GetDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.get_response import GetDatasetResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.update_request import UpdateDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.update_response import UpdateDatasetResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.delete_request import DeleteDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.delete_response import DeleteDatasetResponse
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_request import RetrieveDatasetRequest
from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import RetrieveDatasetResponse

# Import legacy models for compatibility testing
from dify_oapi.api.knowledge_base.v1.model.hit_test_request import HitTestRequest
from dify_oapi.api.knowledge_base.v1.model.hit_test_response import HitTestResponse


class TestDatasetResource:
    @pytest.fixture
    def config(self):
        return Config()

    @pytest.fixture
    def dataset_resource(self, config):
        return Dataset(config)

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    def test_create_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        mock_response = CreateDatasetResponse(id="test_id", name="test_dataset")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = CreateDatasetRequest.builder().name("test_dataset").build()
        response = dataset_resource.create(request, request_option)

        assert response.id == "test_id"
        assert response.name == "test_dataset"
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=CreateDatasetResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_acreate_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = CreateDatasetResponse(id="test_id", name="test_dataset")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = CreateDatasetRequest.builder().name("test_dataset").build()
        response = await dataset_resource.acreate(request, request_option)

        assert response.id == "test_id"
        assert response.name == "test_dataset"
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=CreateDatasetResponse, option=request_option
        )

    def test_list_datasets(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        mock_response = ListDatasetsResponse.builder().data([]).total(0).build()
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListDatasetsRequest.builder().page(1).limit("20").build()
        response = dataset_resource.list(request, request_option)

        assert response.total == 0
        assert response.data == []
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=ListDatasetsResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_alist_datasets(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = ListDatasetsResponse.builder().data([]).total(0).build()
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = ListDatasetsRequest.builder().page(1).limit("20").build()
        response = await dataset_resource.alist(request, request_option)

        assert response.total == 0
        assert response.data == []
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=ListDatasetsResponse, option=request_option
        )

    def test_get_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        mock_response = GetDatasetResponse(id="test_id", name="test_dataset")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetDatasetRequest.builder().dataset_id("test_id").build()
        response = dataset_resource.get(request, request_option)

        assert response.id == "test_id"
        assert response.name == "test_dataset"
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=GetDatasetResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aget_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = GetDatasetResponse(id="test_id", name="test_dataset")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = GetDatasetRequest.builder().dataset_id("test_id").build()
        response = await dataset_resource.aget(request, request_option)

        assert response.id == "test_id"
        assert response.name == "test_dataset"
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=GetDatasetResponse, option=request_option
        )

    def test_update_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        mock_response = UpdateDatasetResponse(id="test_id", name="updated_dataset")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = UpdateDatasetRequest.builder().dataset_id("test_id").name("updated_dataset").build()
        response = dataset_resource.update(request, request_option)

        assert response.id == "test_id"
        assert response.name == "updated_dataset"
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=UpdateDatasetResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aupdate_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = UpdateDatasetResponse(id="test_id", name="updated_dataset")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = UpdateDatasetRequest.builder().dataset_id("test_id").name("updated_dataset").build()
        response = await dataset_resource.aupdate(request, request_option)

        assert response.id == "test_id"
        assert response.name == "updated_dataset"
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=UpdateDatasetResponse, option=request_option
        )

    def test_delete_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        mock_response = DeleteDatasetResponse()
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = DeleteDatasetRequest.builder().dataset_id("test_id").build()
        response = dataset_resource.delete(request, request_option)

        assert isinstance(response, DeleteDatasetResponse)
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=DeleteDatasetResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_adelete_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = DeleteDatasetResponse()
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = DeleteDatasetRequest.builder().dataset_id("test_id").build()
        response = await dataset_resource.adelete(request, request_option)

        assert isinstance(response, DeleteDatasetResponse)
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=DeleteDatasetResponse, option=request_option
        )

    def test_retrieve_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import QueryInfo
        query = QueryInfo(content="test query")
        mock_response = RetrieveDatasetResponse(query=query, records=[])
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = RetrieveDatasetRequest.builder().dataset_id("test_id").query("test query").build()
        response = dataset_resource.retrieve(request, request_option)

        assert response.query.content == "test query"
        assert response.records == []
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=RetrieveDatasetResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aretrieve_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        from dify_oapi.api.knowledge_base.v1.model.dataset.retrieve_response import QueryInfo
        query = QueryInfo(content="test query")
        mock_response = RetrieveDatasetResponse(query=query, records=[])
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = RetrieveDatasetRequest.builder().dataset_id("test_id").query("test query").build()
        response = await dataset_resource.aretrieve(request, request_option)

        assert response.query.content == "test query"
        assert response.records == []
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=RetrieveDatasetResponse, option=request_option
        )

    # Legacy compatibility tests
    def test_hit_test_legacy_compatibility(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        mock_response = HitTestResponse()
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = HitTestRequest()
        response = dataset_resource.hit_test(request, request_option)

        assert isinstance(response, HitTestResponse)
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=HitTestResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_ahit_test_legacy_compatibility(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = HitTestResponse()
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = HitTestRequest()
        response = await dataset_resource.ahit_test(request, request_option)

        assert isinstance(response, HitTestResponse)
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=HitTestResponse, option=request_option
        )

    def test_config_initialization(self, config):
        dataset = Dataset(config)
        assert dataset.config is config

    def test_optional_request_option(self, dataset_resource, monkeypatch):
        # Test that methods work without request_option parameter
        mock_response = CreateDatasetResponse(id="test_id", name="test_dataset")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = CreateDatasetRequest.builder().name("test_dataset").build()
        response = dataset_resource.create(request)

        assert response.id == "test_id"
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=CreateDatasetResponse, option=None
        )