import io

import httpx
import pytest
import respx

from dify_oapi.api.dify.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.dify.v1.resource.file import File


class TestFile:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = File(config)
        self.option = request_option

    @respx.mock
    def test_upload(self):
        route = respx.post("https://api.dify.ai/v1/files/upload").mock(
            return_value=httpx.Response(200, json={
                "id": "file-123",
                "name": "test.txt",
                "size": 12,
                "extension": "txt",
                "mime_type": "text/plain",
                "created_by": "user-1",
                "created_at": 1234567890,
            })
        )
        file_content = io.BytesIO(b"hello world!")
        request = UploadFileRequest.builder().file(file_content, "test.txt").build()
        result = self.resource.upload(request, self.option)
        assert result.id == "file-123"
        assert result.name == "test.txt"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
