from unittest.mock import AsyncMock, Mock, patch

import pytest

from dify_oapi.api.knowledge.v1.model.document.create_by_file_request import CreateByFileRequest
from dify_oapi.api.knowledge.v1.model.document.create_by_file_response import CreateByFileResponse
from dify_oapi.api.knowledge.v1.model.document.create_by_text_request import CreateByTextRequest
from dify_oapi.api.knowledge.v1.model.document.create_by_text_response import CreateByTextResponse
from dify_oapi.api.knowledge.v1.model.document.delete_request import DeleteRequest
from dify_oapi.api.knowledge.v1.model.document.delete_response import DeleteResponse
from dify_oapi.api.knowledge.v1.model.document.get_request import GetRequest
from dify_oapi.api.knowledge.v1.model.document.get_response import GetResponse
from dify_oapi.api.knowledge.v1.model.document.get_upload_file_request import GetUploadFileRequest
from dify_oapi.api.knowledge.v1.model.document.get_upload_file_response import GetUploadFileResponse
from dify_oapi.api.knowledge.v1.model.document.indexing_status_request import IndexingStatusRequest
from dify_oapi.api.knowledge.v1.model.document.indexing_status_response import IndexingStatusResponse
from dify_oapi.api.knowledge.v1.model.document.list_request import ListRequest
from dify_oapi.api.knowledge.v1.model.document.list_response import ListResponse
from dify_oapi.api.knowledge.v1.model.document.update_by_file_request import UpdateByFileRequest
from dify_oapi.api.knowledge.v1.model.document.update_by_file_response import UpdateByFileResponse
from dify_oapi.api.knowledge.v1.model.document.update_by_text_request import UpdateByTextRequest
from dify_oapi.api.knowledge.v1.model.document.update_by_text_response import UpdateByTextResponse
from dify_oapi.api.knowledge.v1.model.document.update_status_request import UpdateStatusRequest
from dify_oapi.api.knowledge.v1.model.document.update_status_response import UpdateStatusResponse
from dify_oapi.api.knowledge.v1.resource.document import Document
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestDocumentResource:
    @pytest.fixture
    def config(self) -> Config:
        return Config()

    @pytest.fixture
    def document_resource(self, config: Config) -> Document:
        return Document(config)

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    # ===== CREATE BY TEXT TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_create_by_text_sync(
        self, mock_execute: Mock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = CreateByTextRequest.builder().dataset_id("test-dataset").build()
        expected_response = CreateByTextResponse()
        mock_execute.return_value = expected_response

        result = document_resource.create_by_text(request, request_option)

        mock_execute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=CreateByTextResponse, option=request_option
        )
        assert result == expected_response

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_create_by_text_async(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = CreateByTextRequest.builder().dataset_id("test-dataset").build()
        expected_response = CreateByTextResponse()
        mock_aexecute.return_value = expected_response

        result = await document_resource.acreate_by_text(request, request_option)

        mock_aexecute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=CreateByTextResponse, option=request_option
        )
        assert result == expected_response

    # ===== CREATE BY FILE TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_create_by_file_sync(
        self, mock_execute: Mock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = CreateByFileRequest.builder().dataset_id("test-dataset").build()
        expected_response = CreateByFileResponse()
        mock_execute.return_value = expected_response

        result = document_resource.create_by_file(request, request_option)

        mock_execute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=CreateByFileResponse, option=request_option
        )
        assert result == expected_response

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_create_by_file_async(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = CreateByFileRequest.builder().dataset_id("test-dataset").build()
        expected_response = CreateByFileResponse()
        mock_aexecute.return_value = expected_response

        result = await document_resource.acreate_by_file(request, request_option)

        mock_aexecute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=CreateByFileResponse, option=request_option
        )
        assert result == expected_response

    # ===== UPDATE BY TEXT TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_update_by_text_sync(
        self, mock_execute: Mock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = UpdateByTextRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()
        expected_response = UpdateByTextResponse()
        mock_execute.return_value = expected_response

        result = document_resource.update_by_text(request, request_option)

        mock_execute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=UpdateByTextResponse, option=request_option
        )
        assert result == expected_response

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_update_by_text_async(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = UpdateByTextRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()
        expected_response = UpdateByTextResponse()
        mock_aexecute.return_value = expected_response

        result = await document_resource.aupdate_by_text(request, request_option)

        mock_aexecute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=UpdateByTextResponse, option=request_option
        )
        assert result == expected_response

    # ===== UPDATE BY FILE TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_update_by_file_sync(
        self, mock_execute: Mock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = UpdateByFileRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()
        expected_response = UpdateByFileResponse()
        mock_execute.return_value = expected_response

        result = document_resource.update_by_file(request, request_option)

        mock_execute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=UpdateByFileResponse, option=request_option
        )
        assert result == expected_response

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_update_by_file_async(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = UpdateByFileRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()
        expected_response = UpdateByFileResponse()
        mock_aexecute.return_value = expected_response

        result = await document_resource.aupdate_by_file(request, request_option)

        mock_aexecute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=UpdateByFileResponse, option=request_option
        )
        assert result == expected_response

    # ===== LIST TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_list_sync(self, mock_execute: Mock, document_resource: Document, request_option: RequestOption) -> None:
        request = ListRequest.builder().dataset_id("test-dataset").build()
        expected_response = ListResponse()
        mock_execute.return_value = expected_response

        result = document_resource.list(request, request_option)

        mock_execute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=ListResponse, option=request_option
        )
        assert result == expected_response

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_list_async(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = ListRequest.builder().dataset_id("test-dataset").build()
        expected_response = ListResponse()
        mock_aexecute.return_value = expected_response

        result = await document_resource.alist(request, request_option)

        mock_aexecute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=ListResponse, option=request_option
        )
        assert result == expected_response

    # ===== DELETE TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_delete_sync(self, mock_execute: Mock, document_resource: Document, request_option: RequestOption) -> None:
        request = DeleteRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()
        expected_response = DeleteResponse()
        mock_execute.return_value = expected_response

        result = document_resource.delete(request, request_option)

        mock_execute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=DeleteResponse, option=request_option
        )
        assert result == expected_response

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_delete_async(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = DeleteRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()
        expected_response = DeleteResponse()
        mock_aexecute.return_value = expected_response

        result = await document_resource.adelete(request, request_option)

        mock_aexecute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=DeleteResponse, option=request_option
        )
        assert result == expected_response

    # ===== INDEXING STATUS TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_indexing_status_sync(
        self, mock_execute: Mock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = IndexingStatusRequest.builder().dataset_id("test-dataset").batch("test-batch").build()
        expected_response = IndexingStatusResponse()
        mock_execute.return_value = expected_response

        result = document_resource.indexing_status(request, request_option)

        mock_execute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=IndexingStatusResponse, option=request_option
        )
        assert result == expected_response

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_indexing_status_async(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = IndexingStatusRequest.builder().dataset_id("test-dataset").batch("test-batch").build()
        expected_response = IndexingStatusResponse()
        mock_aexecute.return_value = expected_response

        result = await document_resource.aindexing_status(request, request_option)

        mock_aexecute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=IndexingStatusResponse, option=request_option
        )
        assert result == expected_response

    # ===== GET TESTS (NEW) =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_sync(self, mock_execute: Mock, document_resource: Document, request_option: RequestOption) -> None:
        request = GetRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()
        expected_response = GetResponse()
        mock_execute.return_value = expected_response

        result = document_resource.get(request, request_option)

        mock_execute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=GetResponse, option=request_option
        )
        assert result == expected_response

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_get_async(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = GetRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()
        expected_response = GetResponse()
        mock_aexecute.return_value = expected_response

        result = await document_resource.aget(request, request_option)

        mock_aexecute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=GetResponse, option=request_option
        )
        assert result == expected_response

    # ===== UPDATE STATUS TESTS (NEW) =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_update_status_sync(
        self, mock_execute: Mock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = UpdateStatusRequest.builder().dataset_id("test-dataset").action("enable").build()
        expected_response = UpdateStatusResponse()
        mock_execute.return_value = expected_response

        result = document_resource.update_status(request, request_option)

        mock_execute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=UpdateStatusResponse, option=request_option
        )
        assert result == expected_response

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_update_status_async(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = UpdateStatusRequest.builder().dataset_id("test-dataset").action("enable").build()
        expected_response = UpdateStatusResponse()
        mock_aexecute.return_value = expected_response

        result = await document_resource.aupdate_status(request, request_option)

        mock_aexecute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=UpdateStatusResponse, option=request_option
        )
        assert result == expected_response

    # ===== GET UPLOAD FILE TESTS (NEW) =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_upload_file_sync(
        self, mock_execute: Mock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = GetUploadFileRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()
        expected_response = GetUploadFileResponse()
        mock_execute.return_value = expected_response

        result = document_resource.get_upload_file(request, request_option)

        mock_execute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=GetUploadFileResponse, option=request_option
        )
        assert result == expected_response

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_get_upload_file_async(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = GetUploadFileRequest.builder().dataset_id("test-dataset").document_id("test-doc").build()
        expected_response = GetUploadFileResponse()
        mock_aexecute.return_value = expected_response

        result = await document_resource.aget_upload_file(request, request_option)

        mock_aexecute.assert_called_once_with(
            document_resource.config, request, unmarshal_as=GetUploadFileResponse, option=request_option
        )
        assert result == expected_response

    # ===== ERROR HANDLING TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_create_by_text_error_handling(
        self, mock_execute: Mock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = CreateByTextRequest.builder().dataset_id("test-dataset").build()
        mock_execute.side_effect = Exception("API Error")

        with pytest.raises(Exception, match="API Error"):
            document_resource.create_by_text(request, request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_create_by_text_async_error_handling(
        self, mock_aexecute: AsyncMock, document_resource: Document, request_option: RequestOption
    ) -> None:
        request = CreateByTextRequest.builder().dataset_id("test-dataset").build()
        mock_aexecute.side_effect = Exception("Async API Error")

        with pytest.raises(Exception, match="Async API Error"):
            await document_resource.acreate_by_text(request, request_option)

    def test_document_resource_initialization(self, config: Config) -> None:
        document_resource = Document(config)
        assert document_resource.config == config
