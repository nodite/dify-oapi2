from io import BytesIO
from unittest.mock import patch

import pytest

from dify_oapi.api.chatflow.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.chatflow.v1.model.upload_file_response import UploadFileResponse
from dify_oapi.api.chatflow.v1.resource.file import File
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestFileResource:
    """Test class for File resource."""

    @pytest.fixture
    def config(self):
        """Create test config."""
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self):
        """Create test request option."""
        return RequestOption.builder().api_key("test_api_key").build()

    @pytest.fixture
    def file_resource(self, config):
        """Create File resource instance."""
        return File(config)

    @pytest.fixture
    def upload_request(self):
        """Create test upload request."""
        test_file = BytesIO(b"test file content")
        return UploadFileRequest.builder().file(test_file, "test.pdf").user("test_user").build()

    @pytest.fixture
    def mock_response(self):
        """Create mock upload response."""
        return UploadFileResponse(
            id="file_123",
            name="test.pdf",
            size=1024,
            extension="pdf",
            mime_type="application/pdf",
            created_by="user_123",
            created_at=1234567890,
            success=True,
            code="200",
            msg="File uploaded successfully",
        )

    def test_file_resource_initialization(self, config):
        """Test File resource initialization."""
        file_resource = File(config)
        assert file_resource.config == config

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_sync(self, mock_execute, file_resource, upload_request, request_option, mock_response):
        """Test sync file upload."""
        # Setup mock
        mock_execute.return_value = mock_response

        # Execute upload
        response = file_resource.upload(upload_request, request_option)

        # Verify mock was called correctly
        mock_execute.assert_called_once_with(
            file_resource.config, upload_request, unmarshal_as=UploadFileResponse, option=request_option
        )

        # Verify response
        assert response == mock_response
        assert response.success is False  # success is False when code is set
        assert response.id == "file_123"
        assert response.name == "test.pdf"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_upload_async(self, mock_aexecute, file_resource, upload_request, request_option, mock_response):
        """Test async file upload."""
        # Setup mock
        mock_aexecute.return_value = mock_response

        # Execute async upload
        response = await file_resource.aupload(upload_request, request_option)

        # Verify mock was called correctly
        mock_aexecute.assert_called_once_with(
            file_resource.config, upload_request, unmarshal_as=UploadFileResponse, option=request_option
        )

        # Verify response
        assert response == mock_response
        assert response.success is False  # success is False when code is set
        assert response.id == "file_123"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_different_file_types(self, mock_execute, file_resource, request_option):
        """Test uploading different file types."""
        file_types = [
            (b"PDF content", "document.pdf", "application/pdf"),
            (b"Image data", "image.jpg", "image/jpeg"),
            (b"Audio data", "audio.mp3", "audio/mpeg"),
            (b"Video data", "video.mp4", "video/mp4"),
        ]

        for content, filename, mime_type in file_types:
            # Create mock response for this file type
            mock_response = UploadFileResponse(
                id=f"file_{filename}",
                name=filename,
                size=len(content),
                extension=filename.split(".")[-1],
                mime_type=mime_type,
                created_by="test_user",
                created_at=1234567890,
                success=True,
            )
            mock_execute.return_value = mock_response

            # Create request
            test_file = BytesIO(content)
            request = UploadFileRequest.builder().file(test_file, filename).user("test_user").build()

            # Execute upload
            response = file_resource.upload(request, request_option)

            # Verify response
            assert response.name == filename
            assert response.mime_type == mime_type
            assert response.size == len(content)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_error_handling(self, mock_execute, file_resource, upload_request, request_option):
        """Test file upload error handling."""
        # Create error response
        error_response = UploadFileResponse(success=False, code="413", msg="File too large")
        mock_execute.return_value = error_response

        # Execute upload
        response = file_resource.upload(upload_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "413"
        assert response.msg == "File too large"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_large_file(self, mock_execute, file_resource, request_option):
        """Test uploading large files."""
        # Create large file (1MB)
        large_content = b"x" * (1024 * 1024)
        large_file = BytesIO(large_content)

        request = UploadFileRequest.builder().file(large_file, "large_file.bin").user("test_user").build()

        mock_response = UploadFileResponse(
            id="large_file_123",
            name="large_file.bin",
            size=len(large_content),
            extension="bin",
            mime_type="application/octet-stream",
            created_by="test_user",
            created_at=1234567890,
            success=True,
        )
        mock_execute.return_value = mock_response

        # Execute upload
        response = file_resource.upload(request, request_option)

        # Verify large file handling
        assert response.size == len(large_content)
        assert response.name == "large_file.bin"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_empty_file(self, mock_execute, file_resource, request_option):
        """Test uploading empty files."""
        empty_file = BytesIO(b"")

        request = UploadFileRequest.builder().file(empty_file, "empty.txt").user("test_user").build()

        mock_response = UploadFileResponse(
            id="empty_file_123",
            name="empty.txt",
            size=0,
            extension="txt",
            mime_type="text/plain",
            created_by="test_user",
            created_at=1234567890,
            success=True,
        )
        mock_execute.return_value = mock_response

        # Execute upload
        response = file_resource.upload(request, request_option)

        # Verify empty file handling
        assert response.size == 0
        assert response.name == "empty.txt"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_special_filename(self, mock_execute, file_resource, request_option):
        """Test uploading files with special characters in filename."""
        test_file = BytesIO(b"special content")
        special_filename = "测试文件-2024_v1.0 (final).pdf"

        request = UploadFileRequest.builder().file(test_file, special_filename).user("test_user").build()

        mock_response = UploadFileResponse(
            id="special_file_123",
            name=special_filename,
            size=len(b"special content"),
            extension="pdf",
            mime_type="application/pdf",
            created_by="test_user",
            created_at=1234567890,
            success=True,
        )
        mock_execute.return_value = mock_response

        # Execute upload
        response = file_resource.upload(request, request_option)

        # Verify special filename handling
        assert response.name == special_filename

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_upload_async_error_handling(self, mock_aexecute, file_resource, upload_request, request_option):
        """Test async file upload error handling."""
        # Create error response
        error_response = UploadFileResponse(success=False, code="415", msg="Unsupported file type")
        mock_aexecute.return_value = error_response

        # Execute async upload
        response = await file_resource.aupload(upload_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "415"
        assert response.msg == "Unsupported file type"

    def test_upload_method_signatures(self, file_resource):
        """Test upload method signatures."""
        # Verify sync method exists
        assert hasattr(file_resource, "upload")
        assert callable(file_resource.upload)

        # Verify async method exists
        assert hasattr(file_resource, "aupload")
        assert callable(file_resource.aupload)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_request_validation(self, mock_execute, file_resource, request_option):
        """Test upload request validation."""
        # Test with minimal valid request
        test_file = BytesIO(b"minimal")
        request = (
            UploadFileRequest.builder()
            .file(test_file)  # No filename
            .user("test_user")
            .build()
        )

        mock_response = UploadFileResponse(success=True)
        mock_execute.return_value = mock_response

        # Should work with default filename
        response = file_resource.upload(request, request_option)
        assert response.success is True

        # Verify the request was properly formed
        mock_execute.assert_called_once()
        call_args = mock_execute.call_args
        assert call_args[0][1] == request  # Second argument should be the request
