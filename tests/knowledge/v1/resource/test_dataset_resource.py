from unittest.mock import AsyncMock, Mock

import pytest

# Import dataset models with flat structure
from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest as CreateRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody as CreateRequestBody
from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse as CreateResponse
from dify_oapi.api.knowledge.v1.model.delete_dataset_request import DeleteDatasetRequest as DeleteRequest
from dify_oapi.api.knowledge.v1.model.delete_dataset_response import DeleteDatasetResponse as DeleteResponse
from dify_oapi.api.knowledge.v1.model.get_dataset_request import GetDatasetRequest as GetRequest
from dify_oapi.api.knowledge.v1.model.get_dataset_response import GetDatasetResponse as GetResponse
from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest as ListRequest
from dify_oapi.api.knowledge.v1.model.list_datasets_response import ListDatasetsResponse as ListResponse
from dify_oapi.api.knowledge.v1.model.query_info import QueryInfo
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest as RetrieveRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request_body import (
    RetrieveFromDatasetRequestBody as RetrieveRequestBody,
)
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_response import (
    RetrieveFromDatasetResponse as RetrieveResponse,
)
from dify_oapi.api.knowledge.v1.model.update_dataset_request import UpdateDatasetRequest as UpdateRequest
from dify_oapi.api.knowledge.v1.model.update_dataset_request_body import UpdateDatasetRequestBody as UpdateRequestBody
from dify_oapi.api.knowledge.v1.model.update_dataset_response import UpdateDatasetResponse as UpdateResponse
from dify_oapi.api.knowledge.v1.resource.dataset import Dataset
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


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
        mock_response = CreateResponse(id="test_id", name="test_dataset")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateRequestBody.builder().name("test_dataset").build()
        request = CreateRequest.builder().request_body(request_body).build()
        response = dataset_resource.create(request, request_option)

        assert response.id == "test_id"
        assert response.name == "test_dataset"
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=CreateResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_acreate_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = CreateResponse(id="test_id", name="test_dataset")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request_body = CreateRequestBody.builder().name("test_dataset").build()
        request = CreateRequest.builder().request_body(request_body).build()
        response = await dataset_resource.acreate(request, request_option)

        assert response.id == "test_id"
        assert response.name == "test_dataset"
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=CreateResponse, option=request_option
        )

    def test_list_datasets(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        mock_response = ListResponse(data=[], total=0)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListRequest.builder().page(1).limit(20).build()
        response = dataset_resource.list(request, request_option)

        assert response.total == 0
        assert response.data == []
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=ListResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_alist_datasets(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = ListResponse(data=[], total=0)
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = ListRequest.builder().page(1).limit(20).build()
        response = await dataset_resource.alist(request, request_option)

        assert response.total == 0
        assert response.data == []
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=ListResponse, option=request_option
        )

    def test_get_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        mock_response = GetResponse(id="test_id", name="test_dataset")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetRequest.builder().dataset_id("test_id").build()
        response = dataset_resource.get(request, request_option)

        assert response.id == "test_id"
        assert response.name == "test_dataset"
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=GetResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aget_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = GetResponse(id="test_id", name="test_dataset")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = GetRequest.builder().dataset_id("test_id").build()
        response = await dataset_resource.aget(request, request_option)

        assert response.id == "test_id"
        assert response.name == "test_dataset"
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=GetResponse, option=request_option
        )

    def test_update_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        mock_response = UpdateResponse(id="test_id", name="updated_dataset")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UpdateRequestBody.builder().name("updated_dataset").build()
        request = UpdateRequest.builder().dataset_id("test_id").request_body(request_body).build()
        response = dataset_resource.update(request, request_option)

        assert response.id == "test_id"
        assert response.name == "updated_dataset"
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=UpdateResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aupdate_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = UpdateResponse(id="test_id", name="updated_dataset")
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request_body = UpdateRequestBody.builder().name("updated_dataset").build()
        request = UpdateRequest.builder().dataset_id("test_id").request_body(request_body).build()
        response = await dataset_resource.aupdate(request, request_option)

        assert response.id == "test_id"
        assert response.name == "updated_dataset"
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=UpdateResponse, option=request_option
        )

    def test_delete_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        mock_response = DeleteResponse()
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = DeleteRequest.builder().dataset_id("test_id").build()
        response = dataset_resource.delete(request, request_option)

        assert isinstance(response, DeleteResponse)
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=DeleteResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_adelete_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        mock_response = DeleteResponse()
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request = DeleteRequest.builder().dataset_id("test_id").build()
        response = await dataset_resource.adelete(request, request_option)

        assert isinstance(response, DeleteResponse)
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=DeleteResponse, option=request_option
        )

    def test_retrieve_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock Transport.execute
        query = QueryInfo(content="test query")
        mock_response = RetrieveResponse(query=query, records=[])
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = RetrieveRequestBody.builder().query("test query").build()
        request = RetrieveRequest.builder().dataset_id("test_id").request_body(request_body).build()
        response = dataset_resource.retrieve(request, request_option)

        assert response.query.content == "test query"
        assert response.records == []
        mock_execute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=RetrieveResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aretrieve_dataset(self, dataset_resource, request_option, monkeypatch):
        # Mock ATransport.aexecute
        query = QueryInfo(content="test query")
        mock_response = RetrieveResponse(query=query, records=[])
        mock_aexecute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        request_body = RetrieveRequestBody.builder().query("test query").build()
        request = RetrieveRequest.builder().dataset_id("test_id").request_body(request_body).build()
        response = await dataset_resource.aretrieve(request, request_option)

        assert response.query.content == "test query"
        assert response.records == []
        mock_aexecute.assert_called_once_with(
            dataset_resource.config, request, unmarshal_as=RetrieveResponse, option=request_option
        )

    def test_config_initialization(self, config):
        dataset = Dataset(config)
        assert dataset.config is config

    def test_optional_request_option(self, dataset_resource, monkeypatch):
        # Test that methods work without request_option parameter
        mock_response = CreateResponse(id="test_id", name="test_dataset")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateRequestBody.builder().name("test_dataset").build()
        request = CreateRequest.builder().request_body(request_body).build()
        response = dataset_resource.create(request)

        assert response.id == "test_id"
        mock_execute.assert_called_once_with(dataset_resource.config, request, unmarshal_as=CreateResponse, option=None)
