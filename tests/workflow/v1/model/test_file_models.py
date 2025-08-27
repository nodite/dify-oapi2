from io import BytesIO

from dify_oapi.api.workflow.v1.model.file.preview_file_request import PreviewFileRequest
from dify_oapi.api.workflow.v1.model.file.preview_file_response import PreviewFileResponse
from dify_oapi.api.workflow.v1.model.file.upload_file_request import UploadFileRequest
from dify_oapi.api.workflow.v1.model.file.upload_file_request_body import UploadFileRequestBody
from dify_oapi.api.workflow.v1.model.file.upload_file_response import UploadFileResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestUploadFileModels:
    def test_request_builder(self) -> None:
        """Test UploadFileRequest builder pattern."""
        file_content = BytesIO(b"test file content")
        request_body = UploadFileRequestBody.builder().user("user-123").build()
        request = UploadFileRequest.builder().file(file_content, "test.txt").request_body(request_body).build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/files/upload"
        assert request.file is not None
        assert request.files is not None

    def test_request_validation(self) -> None:
        """Test UploadFileRequest validation."""
        file_content = BytesIO(b"test content")
        request = UploadFileRequest.builder().file(file_content).build()
        assert request.file is not None
        assert request.files is not None
        assert "file" in request.files

    def test_request_file_handling(self) -> None:
        """Test UploadFileRequest file handling."""
        file_content = BytesIO(b"test content")
        request = UploadFileRequest.builder().file(file_content, "document.pdf").build()
        assert request.files is not None
        assert request.files["file"][0] == "document.pdf"
        assert request.files["file"][1] == file_content

    def test_request_body_builder(self) -> None:
        """Test UploadFileRequestBody builder pattern."""
        request_body = UploadFileRequestBody.builder().user("user-456").build()
        assert request_body.user == "user-456"

    def test_request_body_validation(self) -> None:
        """Test UploadFileRequestBody validation."""
        request_body = UploadFileRequestBody(user="user-789")
        assert request_body.user == "user-789"

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
            name="uploaded.pdf",
            size=4096,
            extension="pdf",
            mime_type="application/pdf",
            created_by="user-789",
            created_at=1234567892,
        )
        assert response.id == "file-123"
        assert response.name == "uploaded.pdf"
        assert response.size == 4096
        assert response.extension == "pdf"
        assert response.mime_type == "application/pdf"


class TestPreviewFileModels:
    def test_request_builder(self) -> None:
        """Test PreviewFileRequest builder pattern."""
        request = PreviewFileRequest.builder().file_id("file-456").as_attachment(True).build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/files/:file_id/preview"
        assert request.file_id == "file-456"
        assert request.paths["file_id"] == "file-456"

    def test_request_validation(self) -> None:
        """Test PreviewFileRequest validation."""
        request = PreviewFileRequest.builder().file_id("file-789").build()
        assert request.file_id == "file-789"
        assert "file_id" in request.paths

    def test_request_query_parameters(self) -> None:
        """Test PreviewFileRequest query parameter handling."""
        request = PreviewFileRequest.builder().file_id("file-456").as_attachment(True).build()
        query_params = dict(request.queries)
        assert "as_attachment" in query_params
        assert query_params["as_attachment"] == "true"

    def test_response_inheritance(self) -> None:
        """Test PreviewFileResponse inherits from BaseResponse."""
        response = PreviewFileResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test PreviewFileResponse data access."""
        binary_content = b"binary file content"
        response = PreviewFileResponse(
            content_type="application/pdf",
            content_length=len(binary_content),
            content=binary_content,
        )
        assert response.content_type == "application/pdf"
        assert response.content_length == len(binary_content)
        assert response.content == binary_content
