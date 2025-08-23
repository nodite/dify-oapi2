"""Test cases for File resource."""

from __future__ import annotations

from io import BytesIO
from unittest.mock import AsyncMock, Mock

import pytest

from dify_oapi.api.completion.v1.model.file.upload_file_request import UploadFileRequest
from dify_oapi.api.completion.v1.model.file.upload_file_request_body import UploadFileRequestBody
from dify_oapi.api.completion.v1.model.file.upload_file_response import UploadFileResponse
from dify_oapi.api.completion.v1.resource.file import File
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestFileResource:
    """Test cases for File resource."""

    @pytest.fixture
    def config(self) -> Config:
        """Create test config."""
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self) -> RequestOption:
        """Create test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def file_resource(self, config: Config) -> File:
        """Create File resource instance."""
        return File(config)

    @pytest.fixture
    def upload_file_request(self) -> UploadFileRequest:
        """Create test upload file request."""
        request_body = UploadFileRequestBody.builder().user("test-user").build()

        test_file = BytesIO(b"test file content")

        return UploadFileRequest.builder().file(test_file, "test.txt").request_body(request_body).build()

    @pytest.fixture
    def upload_file_response(self) -> UploadFileResponse:
        """Create test upload file response."""
        response = UploadFileResponse(
            id="test-file-id",
            name="test.txt",
            size=17,
            extension="txt",
            mime_type="text/plain",
            created_by="test-user-id",
            created_at=1705395332,
            code=None,  # None means success
        )
        return response

    def test_upload_file_sync(
        self,
        file_resource: File,
        upload_file_request: UploadFileRequest,
        request_option: RequestOption,
        upload_file_response: UploadFileResponse,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Test sync upload file method."""
        # Mock Transport.execute
        mock_execute = Mock(return_value=upload_file_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Execute request
        result = file_resource.upload_file(upload_file_request, request_option)

        # Verify result
        assert result is not None
        assert result.id == "test-file-id"
        assert result.name == "test.txt"
        assert result.size == 17
        assert result.extension == "txt"
        assert result.mime_type == "text/plain"
        assert result.created_by == "test-user-id"
        assert result.created_at == 1705395332
        assert result.success is True

        # Verify Transport.execute was called correctly
        mock_execute.assert_called_once()
        call_args = mock_execute.call_args
        assert call_args[0][0] == file_resource.config
        assert call_args[0][1] == upload_file_request
        assert call_args[1]["unmarshal_as"] == UploadFileResponse
        assert call_args[1]["option"] == request_option

    @pytest.mark.asyncio
    async def test_upload_file_async(
        self,
        file_resource: File,
        upload_file_request: UploadFileRequest,
        request_option: RequestOption,
        upload_file_response: UploadFileResponse,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Test async upload file method."""
        # Mock ATransport.aexecute
        mock_aexecute = AsyncMock(return_value=upload_file_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        # Execute request
        result = await file_resource.aupload_file(upload_file_request, request_option)

        # Verify result
        assert result is not None
        assert result.id == "test-file-id"
        assert result.name == "test.txt"
        assert result.size == 17
        assert result.extension == "txt"
        assert result.mime_type == "text/plain"
        assert result.created_by == "test-user-id"
        assert result.created_at == 1705395332
        assert result.success is True

        # Verify ATransport.aexecute was called correctly
        mock_aexecute.assert_called_once()
        call_args = mock_aexecute.call_args
        assert call_args[0][0] == file_resource.config
        assert call_args[0][1] == upload_file_request
        assert call_args[1]["unmarshal_as"] == UploadFileResponse
        assert call_args[1]["option"] == request_option

    def test_upload_file_multipart_handling(
        self,
        file_resource: File,
        request_option: RequestOption,
        upload_file_response: UploadFileResponse,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Test multipart/form-data handling in upload file."""
        # Create request with multipart data
        request_body = UploadFileRequestBody.builder().user("test-user").build()

        test_file = BytesIO(b"multipart test content")

        request = UploadFileRequest.builder().file(test_file, "multipart.txt").request_body(request_body).build()

        # Mock Transport.execute
        mock_execute = Mock(return_value=upload_file_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Execute request
        result = file_resource.upload_file(request, request_option)

        # Verify result
        assert result is not None
        assert result.success is True

        # Verify request has proper multipart structure
        assert request.files is not None
        assert "file" in request.files
        assert request.files["file"][0] == "multipart.txt"
        assert request.files["file"][1] == test_file

        assert request.body is not None
        assert request.body["user"] == "test-user"

        # Verify Transport.execute was called
        mock_execute.assert_called_once()

    def test_upload_file_error_handling(
        self,
        file_resource: File,
        upload_file_request: UploadFileRequest,
        request_option: RequestOption,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Test error handling in upload file."""
        # Mock Transport.execute to raise exception
        mock_execute = Mock(side_effect=Exception("Upload failed"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Execute request and expect exception
        with pytest.raises(Exception, match="Upload failed"):
            file_resource.upload_file(upload_file_request, request_option)

        # Verify Transport.execute was called
        mock_execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_upload_file_async_error_handling(
        self,
        file_resource: File,
        upload_file_request: UploadFileRequest,
        request_option: RequestOption,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Test async error handling in upload file."""
        # Mock ATransport.aexecute to raise exception
        mock_aexecute = AsyncMock(side_effect=Exception("Async upload failed"))
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        # Execute request and expect exception
        with pytest.raises(Exception, match="Async upload failed"):
            await file_resource.aupload_file(upload_file_request, request_option)

        # Verify ATransport.aexecute was called
        mock_aexecute.assert_called_once()

    def test_upload_file_with_different_file_types(
        self,
        file_resource: File,
        request_option: RequestOption,
        upload_file_response: UploadFileResponse,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Test upload file with different file types."""
        # Mock Transport.execute
        mock_execute = Mock(return_value=upload_file_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test different file types
        file_types = [
            ("image.png", b"PNG image data"),
            ("document.pdf", b"PDF document data"),
            ("audio.mp3", b"MP3 audio data"),
        ]

        for filename, content in file_types:
            request_body = UploadFileRequestBody.builder().user("test-user").build()

            test_file = BytesIO(content)

            request = UploadFileRequest.builder().file(test_file, filename).request_body(request_body).build()

            # Execute request
            result = file_resource.upload_file(request, request_option)

            # Verify result
            assert result is not None
            assert result.success is True

            # Verify file was set correctly
            assert request.files is not None
            assert "file" in request.files
            assert request.files["file"][0] == filename
            assert request.files["file"][1] == test_file

        # Verify Transport.execute was called for each file type
        assert mock_execute.call_count == len(file_types)

    def test_upload_file_without_filename(
        self,
        file_resource: File,
        request_option: RequestOption,
        upload_file_response: UploadFileResponse,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Test upload file without explicit filename."""
        # Mock Transport.execute
        mock_execute = Mock(return_value=upload_file_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UploadFileRequestBody.builder().user("test-user").build()

        test_file = BytesIO(b"test content without filename")

        # Create request without explicit filename
        request = (
            UploadFileRequest.builder()
            .file(test_file)  # No filename provided
            .request_body(request_body)
            .build()
        )

        # Execute request
        result = file_resource.upload_file(request, request_option)

        # Verify result
        assert result is not None
        assert result.success is True

        # Verify default filename was used
        assert request.files is not None
        assert "file" in request.files
        assert request.files["file"][0] == "upload"  # Default filename
        assert request.files["file"][1] == test_file

        # Verify Transport.execute was called
        mock_execute.assert_called_once()
