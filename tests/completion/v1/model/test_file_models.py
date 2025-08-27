from __future__ import annotations

from io import BytesIO

from dify_oapi.api.completion.v1.model.file.upload_file_request import UploadFileRequest
from dify_oapi.api.completion.v1.model.file.upload_file_request_body import UploadFileRequestBody
from dify_oapi.api.completion.v1.model.file.upload_file_response import UploadFileResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestUploadFileModels:
    """Test UploadFile API models."""

    def test_request_builder(self) -> None:
        """Test UploadFileRequest builder pattern."""
        file_data = BytesIO(b"test file content")
        request_body = UploadFileRequestBody.builder().user("test-user").build()

        request = UploadFileRequest.builder().file(file_data, "test.jpg").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/files/upload"
        assert request.file == file_data
        assert request.request_body == request_body
        assert request.files is not None
        assert "file" in request.files
        assert request.files["file"][0] == "test.jpg"
        assert request.files["file"][1] == file_data

    def test_request_validation(self) -> None:
        """Test UploadFileRequest validation."""
        request = UploadFileRequest.builder().build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/files/upload"

    def test_request_file_handling(self) -> None:
        """Test UploadFileRequest file handling."""
        file_data = BytesIO(b"test content")

        # Test with filename
        request = UploadFileRequest.builder().file(file_data, "test.txt").build()
        assert request.file == file_data
        assert request.files is not None
        assert "file" in request.files
        assert request.files["file"][0] == "test.txt"
        assert request.files["file"][1] == file_data

        # Test with default filename
        request_default = UploadFileRequest.builder().file(file_data).build()
        assert request_default.files is not None
        assert request_default.files["file"][0] == "upload"

    def test_request_body_builder(self) -> None:
        """Test UploadFileRequestBody builder pattern."""
        request_body = UploadFileRequestBody.builder().user("user-123").build()

        assert request_body.user == "user-123"

    def test_request_body_validation(self) -> None:
        """Test UploadFileRequestBody validation."""
        request_body = UploadFileRequestBody.builder().build()

        assert request_body.user is None

    def test_response_inheritance(self) -> None:
        """Test UploadFileResponse inherits from BaseResponse."""
        response = UploadFileResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UploadFileResponse data access."""
        response = UploadFileResponse(
            id="file-123",
            name="test.jpg",
            size=1024,
            extension="jpg",
            mime_type="image/jpeg",
            created_by="user-123",
            created_at=1705395332,
        )

        assert response.id == "file-123"
        assert response.name == "test.jpg"
        assert response.size == 1024
        assert response.extension == "jpg"
        assert response.mime_type == "image/jpeg"
        assert response.created_by == "user-123"
        assert response.created_at == 1705395332
