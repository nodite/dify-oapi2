from io import BytesIO

from dify_oapi.api.chatflow.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.chatflow.v1.model.upload_file_response import UploadFileResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest
from dify_oapi.core.model.base_response import BaseResponse


class TestUploadFileModels:
    """Test class for Upload File API models."""

    def test_request_builder(self):
        """Test upload file request builder functionality."""
        # Create test file data
        test_file = BytesIO(b"test file content")
        test_user = "test_user_123"
        test_filename = "test_document.pdf"

        # Build request using builder pattern
        request = UploadFileRequest.builder().file(test_file, test_filename).user(test_user).build()

        # Verify request properties
        assert isinstance(request, BaseRequest)
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/files/upload"
        assert request.file == test_file
        assert request.user == test_user
        assert request.files == {"file": (test_filename, test_file)}
        assert request.body == {"user": test_user}

    def test_request_builder_default_filename(self):
        """Test upload file request builder with default filename."""
        test_file = BytesIO(b"test content")
        test_user = "user123"

        request = (
            UploadFileRequest.builder()
            .file(test_file)  # No filename provided
            .user(test_user)
            .build()
        )

        # Should use default filename
        assert request.files == {"file": ("upload", test_file)}

    def test_request_validation(self):
        """Test upload file request field validation."""
        request = UploadFileRequest()

        # Test initial state
        assert request.file is None
        assert request.user is None
        assert request.http_method is None
        assert request.uri is None

        # Test builder initialization
        builder = UploadFileRequest.builder()
        request = builder.build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/files/upload"

    def test_file_upload_handling(self):
        """Test file upload handling with different file types."""
        # Test with different file types
        test_cases = [
            (b"PDF content", "document.pdf"),
            (b"Image data", "image.jpg"),
            (b"Audio data", "audio.mp3"),
            (b"Video data", "video.mp4"),
        ]

        for content, filename in test_cases:
            test_file = BytesIO(content)
            request = UploadFileRequest.builder().file(test_file, filename).user("test_user").build()

            assert request.files == {"file": (filename, test_file)}
            assert request.file == test_file

    def test_response_inheritance(self):
        """Test upload file response inheritance from BaseResponse."""
        response = UploadFileResponse()

        # Verify inheritance
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

        # Test with data
        response_data = UploadFileResponse(
            id="file_123",
            name="test.pdf",
            size=1024,
            extension="pdf",
            mime_type="application/pdf",
            created_by="user_123",
            created_at=1234567890,
        )

        # Verify FileInfo fields are accessible
        assert response_data.id == "file_123"
        assert response_data.name == "test.pdf"
        assert response_data.size == 1024
        assert response_data.extension == "pdf"
        assert response_data.mime_type == "application/pdf"
        assert response_data.created_by == "user_123"
        assert response_data.created_at == 1234567890

    def test_response_data_access(self):
        """Test response data access patterns."""
        # Test successful response
        response = UploadFileResponse(
            id="file_456",
            name="upload.jpg",
            size=2048,
            extension="jpg",
            mime_type="image/jpeg",
            created_by="user_456",
            created_at=1234567891,
            success=True,
            code="200",
            msg="File uploaded successfully",
        )

        # Verify all fields accessible
        # Note: success is True when code is None, False when code is set
        assert response.success is False  # Because code is set to "200"
        assert response.code == "200"
        assert response.msg == "File uploaded successfully"
        assert response.id == "file_456"
        assert response.name == "upload.jpg"

    def test_multipart_form_data_structure(self):
        """Test multipart form-data structure for file uploads."""
        test_file = BytesIO(b"binary file data")
        filename = "test_file.docx"
        user = "upload_user"

        request = UploadFileRequest.builder().file(test_file, filename).user(user).build()

        # Verify multipart structure
        assert "file" in request.files
        assert request.files["file"] == (filename, test_file)
        assert request.body == {"user": user}

    def test_builder_method_chaining(self):
        """Test builder method chaining functionality."""
        test_file = BytesIO(b"chaining test")

        # Test method chaining
        request = UploadFileRequest.builder().user("chain_user").file(test_file, "chain.txt").build()

        assert request.user == "chain_user"
        assert request.file == test_file
        assert request.files == {"file": ("chain.txt", test_file)}

    def test_empty_file_handling(self):
        """Test handling of empty files."""
        empty_file = BytesIO(b"")

        request = UploadFileRequest.builder().file(empty_file, "empty.txt").user("test_user").build()

        assert request.file == empty_file
        assert request.files == {"file": ("empty.txt", empty_file)}

    def test_large_filename_handling(self):
        """Test handling of long filenames."""
        test_file = BytesIO(b"test content")
        long_filename = "a" * 255 + ".txt"  # Very long filename

        request = UploadFileRequest.builder().file(test_file, long_filename).user("test_user").build()

        assert request.files == {"file": (long_filename, test_file)}

    def test_special_characters_in_filename(self):
        """Test handling of special characters in filenames."""
        test_file = BytesIO(b"special chars test")
        special_filename = "测试文件-2024_v1.0 (final).pdf"

        request = UploadFileRequest.builder().file(test_file, special_filename).user("test_user").build()

        assert request.files == {"file": (special_filename, test_file)}
