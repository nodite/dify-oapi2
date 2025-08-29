"""Integration tests for Document API functionality."""

from __future__ import annotations

from unittest.mock import Mock, patch

import pytest

from dify_oapi.api.knowledge.v1.model.document.create_by_file_request import CreateByFileRequest
from dify_oapi.api.knowledge.v1.model.document.create_by_file_request_body import CreateByFileRequestBody
from dify_oapi.api.knowledge.v1.model.document.create_by_file_response import CreateByFileResponse
from dify_oapi.api.knowledge.v1.model.document.create_by_text_request import CreateByTextRequest
from dify_oapi.api.knowledge.v1.model.document.create_by_text_request_body import CreateByTextRequestBody
from dify_oapi.api.knowledge.v1.model.document.create_by_text_response import CreateByTextResponse
from dify_oapi.api.knowledge.v1.model.document.delete_request import DeleteRequest
from dify_oapi.api.knowledge.v1.model.document.delete_response import DeleteResponse
from dify_oapi.api.knowledge.v1.model.document.document_info import DocumentInfo
from dify_oapi.api.knowledge.v1.model.document.get_request import GetRequest
from dify_oapi.api.knowledge.v1.model.document.get_response import GetResponse
from dify_oapi.api.knowledge.v1.model.document.get_upload_file_request import GetUploadFileRequest
from dify_oapi.api.knowledge.v1.model.document.get_upload_file_response import GetUploadFileResponse
from dify_oapi.api.knowledge.v1.model.document.indexing_status_info import IndexingStatusInfo
from dify_oapi.api.knowledge.v1.model.document.indexing_status_request import IndexingStatusRequest
from dify_oapi.api.knowledge.v1.model.document.indexing_status_response import IndexingStatusResponse
from dify_oapi.api.knowledge.v1.model.document.list_request import ListRequest
from dify_oapi.api.knowledge.v1.model.document.list_response import ListResponse
from dify_oapi.api.knowledge.v1.model.document.process_rule import ProcessRule
from dify_oapi.api.knowledge.v1.model.document.update_by_file_request import UpdateByFileRequest
from dify_oapi.api.knowledge.v1.model.document.update_by_file_request_body import UpdateByFileRequestBody
from dify_oapi.api.knowledge.v1.model.document.update_by_file_response import UpdateByFileResponse
from dify_oapi.api.knowledge.v1.model.document.update_by_text_request import UpdateByTextRequest
from dify_oapi.api.knowledge.v1.model.document.update_by_text_request_body import UpdateByTextRequestBody
from dify_oapi.api.knowledge.v1.model.document.update_by_text_response import UpdateByTextResponse
from dify_oapi.api.knowledge.v1.model.document.update_status_request import UpdateStatusRequest
from dify_oapi.api.knowledge.v1.model.document.update_status_request_body import UpdateStatusRequestBody
from dify_oapi.api.knowledge.v1.model.document.update_status_response import UpdateStatusResponse
from dify_oapi.api.knowledge.v1.resource.document import Document
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestDocumentAPIIntegration:
    """Integration tests for Document API functionality."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.config = Config()
        self.document = Document(self.config)
        self.request_option = RequestOption.builder().api_key("test-api-key").build()
        self.dataset_id = "test-dataset-id"
        self.document_id = "test-document-id"
        self.batch_id = "test-batch-id"

    # ===== COMPLETE DOCUMENT LIFECYCLE TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_complete_document_lifecycle_sync(self, mock_execute: Mock) -> None:
        """Test complete document lifecycle with sync operations."""
        # Mock responses for each step
        create_response = CreateByTextResponse(
            document=DocumentInfo(id=self.document_id, name="[Example] Test Document"), batch=self.batch_id
        )
        get_response = GetResponse(id=self.document_id, name="[Example] Test Document")
        update_response = UpdateByTextResponse(
            document=DocumentInfo(id=self.document_id, name="[Example] Updated Document"), batch=self.batch_id
        )
        status_response = IndexingStatusResponse(
            data=[IndexingStatusInfo(id=self.document_id, indexing_status="completed")]
        )
        update_status_response = UpdateStatusResponse(result="success")
        delete_response = DeleteResponse()

        mock_execute.side_effect = [
            create_response,
            get_response,
            update_response,
            status_response,
            update_status_response,
            delete_response,
        ]

        # 1. Create document by text
        create_request = (
            CreateByTextRequest.builder()
            .dataset_id(self.dataset_id)
            .request_body(
                CreateByTextRequestBody.builder().name("[Example] Test Document").text("Test content").build()
            )
            .build()
        )
        result = self.document.create_by_text(create_request, self.request_option)
        assert result.document.id == self.document_id

        # 2. Get document details
        get_request = GetRequest.builder().dataset_id(self.dataset_id).document_id(self.document_id).build()
        result = self.document.get(get_request, self.request_option)
        assert result.id == self.document_id

        # 3. Update document content
        update_request = (
            UpdateByTextRequest.builder()
            .dataset_id(self.dataset_id)
            .document_id(self.document_id)
            .request_body(UpdateByTextRequestBody.builder().name("[Example] Updated Document").build())
            .build()
        )
        result = self.document.update_by_text(update_request, self.request_option)
        assert result.document.name == "[Example] Updated Document"

        # 4. Check indexing status
        status_request = IndexingStatusRequest.builder().dataset_id(self.dataset_id).batch(self.batch_id).build()
        result = self.document.indexing_status(status_request, self.request_option)
        assert result.data[0].indexing_status == "completed"

        # 5. Update document status
        update_status_request = (
            UpdateStatusRequest.builder()
            .dataset_id(self.dataset_id)
            .action("disable")
            .request_body(UpdateStatusRequestBody.builder().document_ids([self.document_id]).build())
            .build()
        )
        result = self.document.update_status(update_status_request, self.request_option)
        assert result.result == "success"

        # 6. Delete document
        delete_request = DeleteRequest.builder().dataset_id(self.dataset_id).document_id(self.document_id).build()
        self.document.delete(delete_request, self.request_option)

        assert mock_execute.call_count == 6

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_complete_document_lifecycle_async(self, mock_aexecute: Mock) -> None:
        """Test complete document lifecycle with async operations."""
        # Mock responses
        create_response = CreateByTextResponse(
            document=DocumentInfo(id=self.document_id, name="[Example] Test Document"), batch=self.batch_id
        )
        get_response = GetResponse(id=self.document_id, name="[Example] Test Document")
        delete_response = DeleteResponse()

        mock_aexecute.side_effect = [create_response, get_response, delete_response]

        # 1. Create document
        create_request = (
            CreateByTextRequest.builder()
            .dataset_id(self.dataset_id)
            .request_body(
                CreateByTextRequestBody.builder().name("[Example] Test Document").text("Test content").build()
            )
            .build()
        )
        result = await self.document.acreate_by_text(create_request, self.request_option)
        assert result.document.id == self.document_id

        # 2. Get document
        get_request = GetRequest.builder().dataset_id(self.dataset_id).document_id(self.document_id).build()
        result = await self.document.aget(get_request, self.request_option)
        assert result.id == self.document_id

        # 3. Delete document
        delete_request = DeleteRequest.builder().dataset_id(self.dataset_id).document_id(self.document_id).build()
        await self.document.adelete(delete_request, self.request_option)

        assert mock_aexecute.call_count == 3

    # ===== FILE OPERATIONS TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_file_operations_sync(self, mock_execute: Mock) -> None:
        """Test file operations with sync methods."""
        # Mock responses
        create_response = CreateByFileResponse(
            document=DocumentInfo(id=self.document_id, name="[Example] Test File"), batch=self.batch_id
        )
        update_response = UpdateByFileResponse(
            document=DocumentInfo(id=self.document_id, name="[Example] Updated File"), batch=self.batch_id
        )
        upload_file_response = GetUploadFileResponse(id="file-id", name="test.pdf", size=1024, extension="pdf")

        mock_execute.side_effect = [create_response, update_response, upload_file_response]

        # 1. Create document by file
        from dify_oapi.api.knowledge.v1.model.document.create_by_file_request_body_data import (
            CreateByFileRequestBodyData,
        )

        data = CreateByFileRequestBodyData.builder().file("test.pdf").build()
        create_request = (
            CreateByFileRequest.builder()
            .dataset_id(self.dataset_id)
            .request_body(CreateByFileRequestBody.builder().data(data).build())
            .build()
        )
        result = self.document.create_by_file(create_request, self.request_option)
        assert result.document.name == "[Example] Test File"

        # 2. Update document by file
        from dify_oapi.api.knowledge.v1.model.document.update_by_file_request_body_data import (
            UpdateByFileRequestBodyData,
        )

        update_data = UpdateByFileRequestBodyData.builder().name("[Example] Updated File").build()
        update_request = (
            UpdateByFileRequest.builder()
            .dataset_id(self.dataset_id)
            .document_id(self.document_id)
            .request_body(UpdateByFileRequestBody.builder().data(update_data).build())
            .build()
        )
        result = self.document.update_by_file(update_request, self.request_option)
        assert result.document.name == "[Example] Updated File"

        # 3. Get upload file information
        upload_file_request = (
            GetUploadFileRequest.builder().dataset_id(self.dataset_id).document_id(self.document_id).build()
        )
        result = self.document.get_upload_file(upload_file_request, self.request_option)
        assert result.extension == "pdf"

        assert mock_execute.call_count == 3

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_file_operations_async(self, mock_aexecute: Mock) -> None:
        """Test file operations with async methods."""
        # Mock responses
        create_response = CreateByFileResponse(
            document=DocumentInfo(id=self.document_id, name="[Example] Test File"), batch=self.batch_id
        )
        upload_file_response = GetUploadFileResponse(id="file-id", name="test.pdf", size=1024, extension="pdf")

        mock_aexecute.side_effect = [create_response, upload_file_response]

        # 1. Create document by file
        from dify_oapi.api.knowledge.v1.model.document.create_by_file_request_body_data import (
            CreateByFileRequestBodyData,
        )

        data = CreateByFileRequestBodyData.builder().file("test.pdf").build()
        create_request = (
            CreateByFileRequest.builder()
            .dataset_id(self.dataset_id)
            .request_body(CreateByFileRequestBody.builder().data(data).build())
            .build()
        )
        result = await self.document.acreate_by_file(create_request, self.request_option)
        assert result.document.name == "[Example] Test File"

        # 2. Get upload file information
        upload_file_request = (
            GetUploadFileRequest.builder().dataset_id(self.dataset_id).document_id(self.document_id).build()
        )
        result = await self.document.aget_upload_file(upload_file_request, self.request_option)
        assert result.extension == "pdf"

        assert mock_aexecute.call_count == 2

    # ===== BATCH OPERATIONS TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_batch_operations_sync(self, mock_execute: Mock) -> None:
        """Test batch operations with sync methods."""
        # Mock responses
        list_response = ListResponse(
            data=[
                DocumentInfo(id="doc1", name="[Example] Document 1"),
                DocumentInfo(id="doc2", name="[Example] Document 2"),
                DocumentInfo(id="doc3", name="[Example] Document 3"),
            ],
            has_more=False,
            limit=20,
            total=3,
            page=1,
        )
        update_status_response = UpdateStatusResponse(result="success")

        mock_execute.side_effect = [list_response, update_status_response]

        # 1. List documents with pagination
        list_request = ListRequest.builder().dataset_id(self.dataset_id).limit(20).page(1).build()
        result = self.document.list(list_request, self.request_option)
        assert len(result.data) == 3
        assert result.total == 3

        # 2. Batch status updates
        document_ids = [doc.id for doc in result.data]
        update_status_request = (
            UpdateStatusRequest.builder()
            .dataset_id(self.dataset_id)
            .action("archive")
            .request_body(UpdateStatusRequestBody.builder().document_ids(document_ids).build())
            .build()
        )
        result = self.document.update_status(update_status_request, self.request_option)
        assert result.result == "success"

        assert mock_execute.call_count == 2

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_batch_operations_async(self, mock_aexecute: Mock) -> None:
        """Test batch operations with async methods."""
        # Mock responses
        list_response = ListResponse(
            data=[
                DocumentInfo(id="doc1", name="[Example] Document 1"),
                DocumentInfo(id="doc2", name="[Example] Document 2"),
            ],
            has_more=False,
            limit=20,
            total=2,
            page=1,
        )
        update_status_response = UpdateStatusResponse(result="success")

        mock_aexecute.side_effect = [list_response, update_status_response]

        # 1. List documents
        list_request = ListRequest.builder().dataset_id(self.dataset_id).build()
        result = await self.document.alist(list_request, self.request_option)
        assert len(result.data) == 2

        # 2. Batch status updates
        document_ids = [doc.id for doc in result.data]
        update_status_request = (
            UpdateStatusRequest.builder()
            .dataset_id(self.dataset_id)
            .action("enable")
            .request_body(UpdateStatusRequestBody.builder().document_ids(document_ids).build())
            .build()
        )
        result = await self.document.aupdate_status(update_status_request, self.request_option)
        assert result.result == "success"

        assert mock_aexecute.call_count == 2

    # ===== ERROR SCENARIOS TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_invalid_dataset_id_error(self, mock_execute: Mock) -> None:
        """Test error handling for invalid dataset ID."""
        mock_execute.side_effect = Exception("Dataset not found")

        create_request = (
            CreateByTextRequest.builder()
            .dataset_id("invalid-id")
            .request_body(CreateByTextRequestBody.builder().name("[Example] Test").text("Test").build())
            .build()
        )

        with pytest.raises(Exception, match="Dataset not found"):
            self.document.create_by_text(create_request, self.request_option)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_missing_document_error(self, mock_execute: Mock) -> None:
        """Test error handling for missing document."""
        mock_execute.side_effect = Exception("Document not found")

        get_request = GetRequest.builder().dataset_id(self.dataset_id).document_id("missing-id").build()

        with pytest.raises(Exception, match="Document not found"):
            self.document.get(get_request, self.request_option)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_invalid_file_format_error(self, mock_execute: Mock) -> None:
        """Test error handling for invalid file format."""
        mock_execute.side_effect = Exception("Unsupported file format")

        from dify_oapi.api.knowledge.v1.model.document.create_by_file_request_body_data import (
            CreateByFileRequestBodyData,
        )

        data = CreateByFileRequestBodyData.builder().file("test.exe").build()
        create_request = (
            CreateByFileRequest.builder()
            .dataset_id(self.dataset_id)
            .request_body(CreateByFileRequestBody.builder().data(data).build())
            .build()
        )

        with pytest.raises(Exception, match="Unsupported file format"):
            self.document.create_by_file(create_request, self.request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_network_error_async(self, mock_aexecute: Mock) -> None:
        """Test error handling for network errors in async operations."""
        mock_aexecute.side_effect = Exception("Network timeout")

        list_request = ListRequest.builder().dataset_id(self.dataset_id).build()

        with pytest.raises(Exception, match="Network timeout"):
            await self.document.alist(list_request, self.request_option)

    # ===== REQUEST/RESPONSE MODEL HANDLING TESTS =====

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_request_response_model_handling(self, mock_execute: Mock) -> None:
        """Test proper request/response model handling."""
        # Mock response with all fields
        mock_response = CreateByTextResponse(
            document=DocumentInfo(
                id=self.document_id,
                name="[Example] Complete Document",
                data_source_type="upload_file",
                tokens=100,
                indexing_status="waiting",
                enabled=True,
                word_count=50,
                hit_count=0,
            ),
            batch=self.batch_id,
        )
        mock_execute.return_value = mock_response

        # Create request with process rule
        process_rule = ProcessRule.builder().mode("automatic").build()
        request_body = (
            CreateByTextRequestBody.builder()
            .name("[Example] Complete Document")
            .text("Complete test content")
            .process_rule(process_rule)
            .build()
        )
        request = CreateByTextRequest.builder().dataset_id(self.dataset_id).request_body(request_body).build()

        result = self.document.create_by_text(request, self.request_option)

        # Verify response model fields
        assert result.document.id == self.document_id
        assert result.document.name == "[Example] Complete Document"
        assert result.document.tokens == 100
        assert result.document.enabled is True
        assert result.batch == self.batch_id

        # Verify request was properly constructed
        mock_execute.assert_called_once()
        call_args = mock_execute.call_args
        assert call_args[0][1].dataset_id == self.dataset_id
        assert call_args[0][1].request_body.name == "[Example] Complete Document"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_pagination_handling(self, mock_execute: Mock) -> None:
        """Test pagination handling in list operations."""
        # Mock paginated response
        mock_response = ListResponse(
            data=[DocumentInfo(id=f"doc{i}", name=f"[Example] Document {i}") for i in range(1, 11)],
            has_more=True,
            limit=10,
            total=25,
            page=1,
        )
        mock_execute.return_value = mock_response

        # Test with pagination parameters
        request = ListRequest.builder().dataset_id(self.dataset_id).keyword("[Example]").page(1).limit(10).build()
        result = self.document.list(request, self.request_option)

        assert len(result.data) == 10
        assert result.has_more is True
        assert result.total == 25
        assert result.page == 1
        assert result.limit == 10

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_status_actions_handling(self, mock_execute: Mock) -> None:
        """Test different status actions handling."""
        mock_response = UpdateStatusResponse(result="success")
        mock_execute.return_value = mock_response

        actions = ["enable", "disable", "archive", "un_archive"]
        document_ids = ["doc1", "doc2", "doc3"]

        for action in actions:
            request = (
                UpdateStatusRequest.builder()
                .dataset_id(self.dataset_id)
                .action(action)
                .request_body(UpdateStatusRequestBody.builder().document_ids(document_ids).build())
                .build()
            )

            result = self.document.update_status(request, self.request_option)
            assert result.result == "success"

        assert mock_execute.call_count == len(actions)
