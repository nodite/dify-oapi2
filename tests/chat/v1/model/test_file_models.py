from io import BytesIO

from dify_oapi.api.chat.v1.model.file_info import FileInfo
from dify_oapi.api.chat.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.chat.v1.model.upload_file_request_body import UploadFileRequestBody
from dify_oapi.api.chat.v1.model.upload_file_response import UploadFileResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestUploadFileModels:
    def test_upload_file_request_builder(self):
        """Test UploadFileRequest builder pattern"""
        file_data = BytesIO(b"test file content")
        request_body = UploadFileRequestBody.builder().user("user-123").build()
        request = UploadFileRequest.builder().file(file_data, "test.jpg").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/files/upload"
        assert "file" in request.files
        assert request.files["file"][0] == "test.jpg"
        assert request.body["user"] == "user-123"
        assert request.request_body.user == "user-123"

    def test_upload_file_request_file_without_name(self):
        """Test file upload without explicit filename"""
        file_data = BytesIO(b"test content")
        request_body = UploadFileRequestBody.builder().user("user-123").build()
        request = UploadFileRequest.builder().file(file_data).request_body(request_body).build()

        assert request.files["file"][0] == "upload"

    def test_upload_file_response_inheritance(self):
        """Test UploadFileResponse inherits from BaseResponse and FileInfo"""
        response = UploadFileResponse()
        assert isinstance(response, BaseResponse)
        assert isinstance(response, FileInfo)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_file_info_builder(self):
        """Test FileInfo builder pattern"""
        file_info = (
            FileInfo.builder()
            .id("file-123")
            .name("test.jpg")
            .size(1024)
            .extension("jpg")
            .mime_type("image/jpeg")
            .build()
        )

        assert file_info.id == "file-123"
        assert file_info.name == "test.jpg"
        assert file_info.size == 1024
        assert file_info.extension == "jpg"
        assert file_info.mime_type == "image/jpeg"

    def test_upload_file_request_multipart_handling(self):
        """Test multipart/form-data handling"""
        file_data = BytesIO(b"binary image data")
        request_body = UploadFileRequestBody.builder().user("test-user").build()
        request = UploadFileRequest.builder().file(file_data, "image.png").request_body(request_body).build()

        # Verify files field is set for multipart upload
        assert request.files is not None
        assert "file" in request.files
        assert request.files["file"][0] == "image.png"

        # Verify body contains user field
        assert request.body is not None
        assert request.body["user"] == "test-user"
        assert request.request_body.user == "test-user"

    def test_upload_file_request_body_builder(self):
        """Test UploadFileRequestBody builder pattern"""
        request_body = UploadFileRequestBody.builder().user("test-user").build()

        assert request_body.user == "test-user"
        assert isinstance(request_body, UploadFileRequestBody)
