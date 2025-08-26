"""Tests for file resource."""

from __future__ import annotations

from io import BytesIO
from unittest.mock import AsyncMock, Mock, patch

import pytest

from dify_oapi.api.workflow.v1.model.file.preview_file_request import (
    PreviewFileRequest,
)
from dify_oapi.api.workflow.v1.model.file.preview_file_response import (
    PreviewFileResponse,
)
from dify_oapi.api.workflow.v1.model.file.upload_file_request import (
    UploadFileRequest,
)
from dify_oapi.api.workflow.v1.model.file.upload_file_response import (
    UploadFileResponse,
)
from dify_oapi.api.workflow.v1.resource.file import File
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestFile:
    """Test cases for File resource."""

    @pytest.fixture
    def config(self) -> Config:
        """Create test config."""
        config = Config()
        config.domain = "https://api.test.com"
        return config

    @pytest.fixture
    def request_option(self) -> RequestOption:
        """Create test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def file_resource(self, config: Config) -> File:
        """Create file resource instance."""
        return File(config)

    @pytest.fixture
    def test_file(self) -> BytesIO:
        """Create test file."""
        return BytesIO(b"test file content")

    def test_file_initialization(self, config: Config) -> None:
        """Test file resource initialization."""
        file_resource = File(config)
        assert file_resource.config == config

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_file_sync(
        self,
        mock_execute: Mock,
        file_resource: File,
        request_option: RequestOption,
        test_file: BytesIO,
    ) -> None:
        """Test upload file sync."""
        # Arrange
        request = UploadFileRequest.builder().file(test_file, "test.txt").build()
        expected_response = UploadFileResponse()
        mock_execute.return_value = expected_response

        # Act
        result = file_resource.upload_file(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            file_resource.config,
            request,
            unmarshal_as=UploadFileResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aupload_file_async(
        self,
        mock_aexecute: AsyncMock,
        file_resource: File,
        request_option: RequestOption,
        test_file: BytesIO,
    ) -> None:
        """Test upload file async."""
        # Arrange
        request = UploadFileRequest.builder().file(test_file, "test.txt").build()
        expected_response = UploadFileResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await file_resource.aupload_file(request, request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            file_resource.config,
            request,
            unmarshal_as=UploadFileResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_preview_file_sync(
        self,
        mock_execute: Mock,
        file_resource: File,
        request_option: RequestOption,
    ) -> None:
        """Test preview file sync."""
        # Arrange
        request = PreviewFileRequest.builder().file_id("test-file-id").build()
        expected_response = PreviewFileResponse()
        mock_execute.return_value = expected_response

        # Act
        result = file_resource.preview_file(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            file_resource.config,
            request,
            unmarshal_as=PreviewFileResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_apreview_file_async(
        self,
        mock_aexecute: AsyncMock,
        file_resource: File,
        request_option: RequestOption,
    ) -> None:
        """Test preview file async."""
        # Arrange
        request = PreviewFileRequest.builder().file_id("test-file-id").build()
        expected_response = PreviewFileResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await file_resource.apreview_file(request, request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            file_resource.config,
            request,
            unmarshal_as=PreviewFileResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_file_with_multipart_data(
        self,
        mock_execute: Mock,
        file_resource: File,
        request_option: RequestOption,
        test_file: BytesIO,
    ) -> None:
        """Test upload file with multipart/form-data handling."""
        # Arrange
        from dify_oapi.api.workflow.v1.model.file.upload_file_request_body import (
            UploadFileRequestBody,
        )

        request_body = UploadFileRequestBody.builder().user("test-user").build()
        request = UploadFileRequest.builder().file(test_file, "test.txt").request_body(request_body).build()
        expected_response = UploadFileResponse()
        mock_execute.return_value = expected_response

        # Act
        result = file_resource.upload_file(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            file_resource.config,
            request,
            unmarshal_as=UploadFileResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_preview_file_with_query_params(
        self,
        mock_execute: Mock,
        file_resource: File,
        request_option: RequestOption,
    ) -> None:
        """Test preview file with query parameters."""
        # Arrange
        request = PreviewFileRequest.builder().file_id("test-file-id").as_attachment(True).build()
        expected_response = PreviewFileResponse()
        mock_execute.return_value = expected_response

        # Act
        result = file_resource.preview_file(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            file_resource.config,
            request,
            unmarshal_as=PreviewFileResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_file_error_handling(
        self,
        mock_execute: Mock,
        file_resource: File,
        request_option: RequestOption,
        test_file: BytesIO,
    ) -> None:
        """Test upload file error handling."""
        # Arrange
        request = UploadFileRequest.builder().file(test_file, "test.txt").build()
        mock_execute.side_effect = Exception("Upload Error")

        # Act & Assert
        with pytest.raises(Exception, match="Upload Error"):
            file_resource.upload_file(request, request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aupload_file_error_handling(
        self,
        mock_aexecute: AsyncMock,
        file_resource: File,
        request_option: RequestOption,
        test_file: BytesIO,
    ) -> None:
        """Test async upload file error handling."""
        # Arrange
        request = UploadFileRequest.builder().file(test_file, "test.txt").build()
        mock_aexecute.side_effect = Exception("Async Upload Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async Upload Error"):
            await file_resource.aupload_file(request, request_option)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_preview_file_error_handling(
        self,
        mock_execute: Mock,
        file_resource: File,
        request_option: RequestOption,
    ) -> None:
        """Test preview file error handling."""
        # Arrange
        request = PreviewFileRequest.builder().file_id("test-file-id").build()
        mock_execute.side_effect = Exception("Preview Error")

        # Act & Assert
        with pytest.raises(Exception, match="Preview Error"):
            file_resource.preview_file(request, request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_apreview_file_error_handling(
        self,
        mock_aexecute: AsyncMock,
        file_resource: File,
        request_option: RequestOption,
    ) -> None:
        """Test async preview file error handling."""
        # Arrange
        request = PreviewFileRequest.builder().file_id("test-file-id").build()
        mock_aexecute.side_effect = Exception("Async Preview Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async Preview Error"):
            await file_resource.apreview_file(request, request_option)

    def test_method_signatures(self, file_resource: File) -> None:
        """Test that all methods have correct signatures."""
        import inspect

        # Test sync methods
        assert hasattr(file_resource, "upload_file")
        assert hasattr(file_resource, "preview_file")

        # Test async methods
        assert hasattr(file_resource, "aupload_file")
        assert hasattr(file_resource, "apreview_file")

        # Verify method signatures
        sig = inspect.signature(file_resource.upload_file)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "request_option" in params

        sig = inspect.signature(file_resource.preview_file)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "request_option" in params

    def test_file_upload_request_structure(self, test_file: BytesIO) -> None:
        """Test file upload request structure."""
        # Test that file upload request can handle multipart data
        request = UploadFileRequest.builder().file(test_file, "test.txt").build()

        # Verify the request has the necessary attributes for multipart handling
        assert hasattr(request, "files")
        assert hasattr(request, "body")

    def test_binary_file_handling(self, test_file: BytesIO) -> None:
        """Test binary file handling."""
        # Test that BytesIO files are handled correctly
        request = UploadFileRequest.builder().file(test_file, "binary_file.bin").build()

        # Verify file content is preserved
        assert request.files is not None
        assert "file" in request.files

        # Test file name handling
        file_name, file_content = request.files["file"]
        assert file_name == "binary_file.bin"
        assert file_content == test_file

    def test_preview_file_response_handling(self) -> None:
        """Test preview file response handling."""
        # Test that preview response can handle binary content
        response = PreviewFileResponse()

        # Verify response has necessary fields for binary content
        assert hasattr(response, "content_type")
        assert hasattr(response, "content_length")
        assert hasattr(response, "content")
