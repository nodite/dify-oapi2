from io import BytesIO
from unittest.mock import patch

import pytest

from dify_oapi.api.chat.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.chat.v1.model.upload_file_request_body import UploadFileRequestBody
from dify_oapi.api.chat.v1.model.upload_file_response import UploadFileResponse
from dify_oapi.api.chat.v1.resource.file import File
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestFileResource:
    @pytest.fixture
    def file_resource(self):
        config = Config()
        return File(config)

    @pytest.fixture
    def upload_request(self):
        file_data = BytesIO(b"test file content")
        request_body = UploadFileRequestBody.builder().user("test-user").build()
        return UploadFileRequest.builder().file(file_data, "test.jpg").request_body(request_body).build()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-key").build()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_file(self, mock_execute, file_resource, upload_request, request_option):
        """Test file upload method"""
        mock_response = UploadFileResponse()
        mock_response.id = "file-123"
        mock_response.name = "test.jpg"
        mock_response.size = 1024
        mock_execute.return_value = mock_response

        result = file_resource.upload(upload_request, request_option)

        assert isinstance(result, UploadFileResponse)
        assert result.id == "file-123"
        assert result.name == "test.jpg"
        assert result.size == 1024
        mock_execute.assert_called_once_with(
            file_resource.config, upload_request, unmarshal_as=UploadFileResponse, option=request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    async def test_async_upload_file(self, mock_aexecute, file_resource, upload_request, request_option):
        """Test async file upload method"""
        mock_response = UploadFileResponse()
        mock_response.id = "file-456"
        mock_response.name = "async_test.png"
        mock_response.size = 2048
        mock_aexecute.return_value = mock_response

        result = await file_resource.aupload(upload_request, request_option)

        assert isinstance(result, UploadFileResponse)
        assert result.id == "file-456"
        assert result.name == "async_test.png"
        assert result.size == 2048
        mock_aexecute.assert_called_once_with(
            file_resource.config, upload_request, unmarshal_as=UploadFileResponse, option=request_option
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_file_without_option(self, mock_execute, file_resource, upload_request):
        """Test file upload without request option"""
        mock_response = UploadFileResponse()
        mock_execute.return_value = mock_response

        result = file_resource.upload(upload_request)

        assert isinstance(result, UploadFileResponse)
        mock_execute.assert_called_once_with(
            file_resource.config, upload_request, unmarshal_as=UploadFileResponse, option=None
        )

    def test_file_resource_initialization(self):
        """Test File resource initialization"""
        config = Config()
        file_resource = File(config)

        assert file_resource.config == config
        assert hasattr(file_resource, "upload")
        assert hasattr(file_resource, "aupload")

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_file_type_validation(self, mock_execute, file_resource):
        """Test file type validation through request"""
        # Test with different file types
        image_data = BytesIO(b"fake image data")
        request_body = UploadFileRequestBody.builder().user("test-user").build()
        request = UploadFileRequest.builder().file(image_data, "image.png").request_body(request_body).build()

        mock_response = UploadFileResponse()
        mock_response.mime_type = "image/png"
        mock_execute.return_value = mock_response

        result = file_resource.upload(request)

        assert result.mime_type == "image/png"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_upload_file_size_handling(self, mock_execute, file_resource):
        """Test file size handling"""
        large_file_data = BytesIO(b"x" * 1024 * 1024)  # 1MB file
        request_body = UploadFileRequestBody.builder().user("test-user").build()
        request = UploadFileRequest.builder().file(large_file_data, "large_file.jpg").request_body(request_body).build()

        mock_response = UploadFileResponse()
        mock_response.size = 1024 * 1024
        mock_execute.return_value = mock_response

        result = file_resource.upload(request)

        assert result.size == 1024 * 1024
        mock_execute.assert_called_once()
