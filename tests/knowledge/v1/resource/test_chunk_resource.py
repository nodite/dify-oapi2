"""Tests for chunk resource."""

from unittest.mock import Mock

import pytest

from dify_oapi.api.knowledge.v1.model.create_child_chunk_request import CreateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.create_child_chunk_response import CreateChildChunkResponse
from dify_oapi.api.knowledge.v1.model.delete_child_chunk_request import DeleteChildChunkRequest
from dify_oapi.api.knowledge.v1.model.delete_child_chunk_response import DeleteChildChunkResponse
from dify_oapi.api.knowledge.v1.model.list_child_chunks_request import ListChildChunksRequest
from dify_oapi.api.knowledge.v1.model.list_child_chunks_response import ListChildChunksResponse
from dify_oapi.api.knowledge.v1.model.update_child_chunk_request import UpdateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.update_child_chunk_response import UpdateChildChunkResponse
from dify_oapi.api.knowledge.v1.resource.chunk import Chunk
from dify_oapi.core.http.transport.async_transport import ATransport
from dify_oapi.core.http.transport.sync_transport import Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestChunkResource:
    """Test Chunk resource."""

    @pytest.fixture
    def config(self) -> Config:
        """Create test config."""
        return Config(domain="https://api.dify.ai")

    @pytest.fixture
    def request_option(self) -> RequestOption:
        """Create test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def chunk_resource(self, config: Config) -> Chunk:
        """Create chunk resource."""
        return Chunk(config)

    def test_init(self, config: Config) -> None:
        """Test Chunk resource initialization."""
        chunk = Chunk(config)
        assert chunk.config == config

    def test_list(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch) -> None:
        """Test list method."""
        mock_response = ListChildChunksResponse(data=[])
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr(Transport, "execute", mock_execute)

        request = ListChildChunksRequest.builder().build()
        response = chunk_resource.list(request, request_option)

        assert response == mock_response
        mock_execute.assert_called_once_with(
            chunk_resource.config, request, unmarshal_as=ListChildChunksResponse, option=request_option
        )

    def test_create(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch) -> None:
        """Test create method."""
        mock_response = CreateChildChunkResponse(data=[])
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr(Transport, "execute", mock_execute)

        request = CreateChildChunkRequest.builder().build()
        response = chunk_resource.create(request, request_option)

        assert response == mock_response
        mock_execute.assert_called_once_with(
            chunk_resource.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option
        )

    def test_update(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch) -> None:
        """Test update method."""
        mock_response = UpdateChildChunkResponse()
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr(Transport, "execute", mock_execute)

        request = UpdateChildChunkRequest.builder().build()
        response = chunk_resource.update(request, request_option)

        assert response == mock_response
        mock_execute.assert_called_once_with(
            chunk_resource.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option
        )

    def test_delete(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch) -> None:
        """Test delete method."""
        mock_response = DeleteChildChunkResponse()
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr(Transport, "execute", mock_execute)

        request = DeleteChildChunkRequest.builder().build()
        response = chunk_resource.delete(request, request_option)

        assert response == mock_response
        mock_execute.assert_called_once_with(
            chunk_resource.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_alist(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch) -> None:
        """Test alist async method."""
        mock_response = ListChildChunksResponse(data=[])
        mock_aexecute = Mock(return_value=mock_response)
        monkeypatch.setattr(ATransport, "aexecute", mock_aexecute)

        request = ListChildChunksRequest.builder().build()
        response = await chunk_resource.alist(request, request_option)

        assert response == mock_response
        mock_aexecute.assert_called_once_with(
            chunk_resource.config, request, unmarshal_as=ListChildChunksResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_acreate(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch) -> None:
        """Test acreate async method."""
        mock_response = CreateChildChunkResponse(data=[])
        mock_aexecute = Mock(return_value=mock_response)
        monkeypatch.setattr(ATransport, "aexecute", mock_aexecute)

        request = CreateChildChunkRequest.builder().build()
        response = await chunk_resource.acreate(request, request_option)

        assert response == mock_response
        mock_aexecute.assert_called_once_with(
            chunk_resource.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_aupdate(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch) -> None:
        """Test aupdate async method."""
        mock_response = UpdateChildChunkResponse()
        mock_aexecute = Mock(return_value=mock_response)
        monkeypatch.setattr(ATransport, "aexecute", mock_aexecute)

        request = UpdateChildChunkRequest.builder().build()
        response = await chunk_resource.aupdate(request, request_option)

        assert response == mock_response
        mock_aexecute.assert_called_once_with(
            chunk_resource.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_adelete(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch) -> None:
        """Test adelete async method."""
        mock_response = DeleteChildChunkResponse()
        mock_aexecute = Mock(return_value=mock_response)
        monkeypatch.setattr(ATransport, "aexecute", mock_aexecute)

        request = DeleteChildChunkRequest.builder().build()
        response = await chunk_resource.adelete(request, request_option)

        assert response == mock_response
        mock_aexecute.assert_called_once_with(
            chunk_resource.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option
        )
