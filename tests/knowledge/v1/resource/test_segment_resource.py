"""Tests for Segment resource class."""

from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest

from dify_oapi.api.knowledge.v1.model.segment.create_child_chunk_request import CreateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.segment.create_child_chunk_response import CreateChildChunkResponse
from dify_oapi.api.knowledge.v1.model.segment.create_request import CreateRequest
from dify_oapi.api.knowledge.v1.model.segment.create_response import CreateResponse
from dify_oapi.api.knowledge.v1.model.segment.delete_child_chunk_request import DeleteChildChunkRequest
from dify_oapi.api.knowledge.v1.model.segment.delete_child_chunk_response import DeleteChildChunkResponse
from dify_oapi.api.knowledge.v1.model.segment.delete_request import DeleteRequest
from dify_oapi.api.knowledge.v1.model.segment.delete_response import DeleteResponse
from dify_oapi.api.knowledge.v1.model.segment.get_request import GetRequest
from dify_oapi.api.knowledge.v1.model.segment.get_response import GetResponse
from dify_oapi.api.knowledge.v1.model.segment.list_child_chunks_request import ListChildChunksRequest
from dify_oapi.api.knowledge.v1.model.segment.list_child_chunks_response import ListChildChunksResponse
from dify_oapi.api.knowledge.v1.model.segment.list_request import ListRequest
from dify_oapi.api.knowledge.v1.model.segment.list_response import ListResponse
from dify_oapi.api.knowledge.v1.model.segment.update_child_chunk_request import UpdateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.segment.update_child_chunk_response import UpdateChildChunkResponse
from dify_oapi.api.knowledge.v1.model.segment.update_request import UpdateRequest
from dify_oapi.api.knowledge.v1.model.segment.update_response import UpdateResponse
from dify_oapi.api.knowledge.v1.resource.segment import Segment
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestSegmentResource:
    """Test cases for Segment resource."""

    @pytest.fixture
    def config(self) -> Config:
        """Create test config."""
        config = Config()
        config.domain = "https://api.test.com"
        return config

    @pytest.fixture
    def segment(self, config: Config) -> Segment:
        """Create segment resource instance."""
        return Segment(config)

    @pytest.fixture
    def request_option(self) -> RequestOption:
        """Create test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    # ===== CORE SEGMENT OPERATIONS TESTS =====

    def test_create_sync(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test sync create method."""
        # Mock Transport.execute
        mock_response = CreateResponse(success=True, data=[], doc_form="text_model")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create request
        request = CreateRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()

        # Execute
        response = segment.create(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=CreateResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_create_async(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test async acreate method."""
        # Mock ATransport.aexecute
        mock_response = CreateResponse(success=True, data=[], doc_form="text_model")
        mock_execute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_execute)

        # Create request
        request = CreateRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()

        # Execute
        response = await segment.acreate(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=CreateResponse, option=request_option
        )

    def test_list_sync(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test sync list method."""
        # Mock Transport.execute
        mock_response = ListResponse(success=True, data=[], has_more=False, limit=20, total=0, page=1)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create request
        request = ListRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()

        # Execute
        response = segment.list(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(segment.config, request, unmarshal_as=ListResponse, option=request_option)

    @pytest.mark.asyncio
    async def test_list_async(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test async alist method."""
        # Mock ATransport.aexecute
        mock_response = ListResponse(success=True, data=[], has_more=False, limit=20, total=0, page=1)
        mock_execute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_execute)

        # Create request
        request = ListRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()

        # Execute
        response = await segment.alist(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(segment.config, request, unmarshal_as=ListResponse, option=request_option)

    def test_get_sync(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test sync get method."""
        # Mock Transport.execute
        mock_response = GetResponse(success=True, data=None, doc_form="text_model")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create request
        request = (
            GetRequest.builder().dataset_id("test-dataset").document_id("test-doc").segment_id("test-segment").build()
        )

        # Execute
        response = segment.get(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(segment.config, request, unmarshal_as=GetResponse, option=request_option)

    @pytest.mark.asyncio
    async def test_get_async(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test async aget method."""
        # Mock ATransport.aexecute
        mock_response = GetResponse(success=True, data=None, doc_form="text_model")
        mock_execute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_execute)

        # Create request
        request = (
            GetRequest.builder().dataset_id("test-dataset").document_id("test-doc").segment_id("test-segment").build()
        )

        # Execute
        response = await segment.aget(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(segment.config, request, unmarshal_as=GetResponse, option=request_option)

    def test_update_sync(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test sync update method."""
        # Mock Transport.execute
        mock_response = UpdateResponse(success=True, data=None, doc_form="text_model")
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create request
        request = (
            UpdateRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .build()
        )

        # Execute
        response = segment.update(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=UpdateResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_update_async(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test async aupdate method."""
        # Mock ATransport.aexecute
        mock_response = UpdateResponse(success=True, data=None, doc_form="text_model")
        mock_execute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_execute)

        # Create request
        request = (
            UpdateRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .build()
        )

        # Execute
        response = await segment.aupdate(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=UpdateResponse, option=request_option
        )

    def test_delete_sync(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test sync delete method."""
        # Mock Transport.execute
        mock_response = DeleteResponse(success=True)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create request
        request = (
            DeleteRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .build()
        )

        # Execute
        response = segment.delete(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=DeleteResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_delete_async(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test async adelete method."""
        # Mock ATransport.aexecute
        mock_response = DeleteResponse(success=True)
        mock_execute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_execute)

        # Create request
        request = (
            DeleteRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .build()
        )

        # Execute
        response = await segment.adelete(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=DeleteResponse, option=request_option
        )

    # ===== CHILD CHUNK OPERATIONS TESTS =====

    def test_create_child_chunk_sync(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test sync create_child_chunk method."""
        # Mock Transport.execute
        mock_response = CreateChildChunkResponse(success=True, data=None)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create request
        request = (
            CreateChildChunkRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .build()
        )

        # Execute
        response = segment.create_child_chunk(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_create_child_chunk_async(
        self, segment: Segment, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test async acreate_child_chunk method."""
        # Mock ATransport.aexecute
        mock_response = CreateChildChunkResponse(success=True, data=None)
        mock_execute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_execute)

        # Create request
        request = (
            CreateChildChunkRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .build()
        )

        # Execute
        response = await segment.acreate_child_chunk(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option
        )

    def test_list_child_chunks_sync(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test sync list_child_chunks method."""
        # Mock Transport.execute
        mock_response = ListChildChunksResponse(success=True, data=[], total=0, total_pages=1, page=1, limit=20)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create request
        request = (
            ListChildChunksRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .build()
        )

        # Execute
        response = segment.list_child_chunks(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=ListChildChunksResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_list_child_chunks_async(
        self, segment: Segment, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test async alist_child_chunks method."""
        # Mock ATransport.aexecute
        mock_response = ListChildChunksResponse(success=True, data=[], total=0, total_pages=1, page=1, limit=20)
        mock_execute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_execute)

        # Create request
        request = (
            ListChildChunksRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .build()
        )

        # Execute
        response = await segment.alist_child_chunks(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=ListChildChunksResponse, option=request_option
        )

    def test_update_child_chunk_sync(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test sync update_child_chunk method."""
        # Mock Transport.execute
        mock_response = UpdateChildChunkResponse(success=True, data=None)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create request
        request = (
            UpdateChildChunkRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .child_chunk_id("test-chunk")
            .build()
        )

        # Execute
        response = segment.update_child_chunk(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_update_child_chunk_async(
        self, segment: Segment, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test async aupdate_child_chunk method."""
        # Mock ATransport.aexecute
        mock_response = UpdateChildChunkResponse(success=True, data=None)
        mock_execute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_execute)

        # Create request
        request = (
            UpdateChildChunkRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .child_chunk_id("test-chunk")
            .build()
        )

        # Execute
        response = await segment.aupdate_child_chunk(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option
        )

    def test_delete_child_chunk_sync(self, segment: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test sync delete_child_chunk method."""
        # Mock Transport.execute
        mock_response = DeleteChildChunkResponse(success=True)
        mock_execute = Mock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create request
        request = (
            DeleteChildChunkRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .child_chunk_id("test-chunk")
            .build()
        )

        # Execute
        response = segment.delete_child_chunk(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option
        )

    @pytest.mark.asyncio
    async def test_delete_child_chunk_async(
        self, segment: Segment, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test async adelete_child_chunk method."""
        # Mock ATransport.aexecute
        mock_response = DeleteChildChunkResponse(success=True)
        mock_execute = AsyncMock(return_value=mock_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_execute)

        # Create request
        request = (
            DeleteChildChunkRequest.builder()
            .dataset_id("test-dataset")
            .document_id("test-doc")
            .segment_id("test-segment")
            .child_chunk_id("test-chunk")
            .build()
        )

        # Execute
        response = await segment.adelete_child_chunk(request, request_option)

        # Verify
        assert response == mock_response
        mock_execute.assert_called_once_with(
            segment.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option
        )

    # ===== HTTP METHOD AND URL VERIFICATION TESTS =====

    def test_request_http_methods(self) -> None:
        """Test that requests have correct HTTP methods configured."""
        # Core segment operations
        create_request = CreateRequest.builder().build()
        assert create_request.http_method == HttpMethod.POST

        list_request = ListRequest.builder().build()
        assert list_request.http_method == HttpMethod.GET

        get_request = GetRequest.builder().build()
        assert get_request.http_method == HttpMethod.GET

        update_request = UpdateRequest.builder().build()
        assert update_request.http_method == HttpMethod.POST

        delete_request = DeleteRequest.builder().build()
        assert delete_request.http_method == HttpMethod.DELETE

        # Child chunk operations
        create_child_chunk_request = CreateChildChunkRequest.builder().build()
        assert create_child_chunk_request.http_method == HttpMethod.POST

        list_child_chunks_request = ListChildChunksRequest.builder().build()
        assert list_child_chunks_request.http_method == HttpMethod.GET

        update_child_chunk_request = UpdateChildChunkRequest.builder().build()
        assert update_child_chunk_request.http_method == HttpMethod.PATCH

        delete_child_chunk_request = DeleteChildChunkRequest.builder().build()
        assert delete_child_chunk_request.http_method == HttpMethod.DELETE

    def test_request_uris(self) -> None:
        """Test that requests have correct URIs configured."""
        # Core segment operations
        create_request = CreateRequest.builder().build()
        assert create_request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments"

        list_request = ListRequest.builder().build()
        assert list_request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments"

        get_request = GetRequest.builder().build()
        assert get_request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"

        update_request = UpdateRequest.builder().build()
        assert update_request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"

        delete_request = DeleteRequest.builder().build()
        assert delete_request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"

        # Child chunk operations
        create_child_chunk_request = CreateChildChunkRequest.builder().build()
        assert (
            create_child_chunk_request.uri
            == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks"
        )

        list_child_chunks_request = ListChildChunksRequest.builder().build()
        assert (
            list_child_chunks_request.uri
            == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks"
        )

        update_child_chunk_request = UpdateChildChunkRequest.builder().build()
        assert (
            update_child_chunk_request.uri
            == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id"
        )

        delete_child_chunk_request = DeleteChildChunkRequest.builder().build()
        assert (
            delete_child_chunk_request.uri
            == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id"
        )
