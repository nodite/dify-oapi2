"""
Dify System-level Resource Integration Tests

Test functionality of various system-level resources
"""

from unittest.mock import Mock, patch

import pytest

from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


class TestFileResourceIntegration:
    """File Resource Integration Tests"""

    @pytest.fixture
    def client(self):
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_file_upload(self, mock_execute, client, request_option):
        """Test file upload"""
        from dify_oapi.api.dify.v1.model.upload_file_request import UploadFileRequest

        mock_response = Mock()
        mock_response.id = "file-123"
        mock_response.name = "test.txt"
        mock_response.size = 1024
        mock_response.type = "text/plain"
        mock_execute.return_value = mock_response

        request = UploadFileRequest.builder().build()
        response = client.dify.v1.file.upload(request, request_option)

        assert response.id == "file-123"
        assert response.name == "test.txt"
        assert response.size == 1024
        assert response.type == "text/plain"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_async_file_upload(self, mock_aexecute, client, request_option):
        """Test async file upload"""
        from dify_oapi.api.dify.v1.model.upload_file_request import UploadFileRequest

        mock_response = Mock()
        mock_response.id = "file-async-123"
        mock_aexecute.return_value = mock_response

        request = UploadFileRequest.builder().build()
        response = await client.dify.v1.file.aupload(request, request_option)

        assert response.id == "file-async-123"


class TestAudioResourceIntegration:
    """Audio Resource Integration Tests"""

    @pytest.fixture
    def client(self):
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_audio_to_text(self, mock_execute, client, request_option):
        """Test audio to text"""
        from dify_oapi.api.dify.v1.model.audio_to_text_request import AudioToTextRequest

        mock_response = Mock()
        mock_response.text = "Hello world"
        mock_execute.return_value = mock_response

        request = AudioToTextRequest.builder().build()
        response = client.dify.v1.audio.to_text(request, request_option)

        assert response.text == "Hello world"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_text_to_audio(self, mock_execute, client, request_option):
        """Test text to audio"""
        from dify_oapi.api.dify.v1.model.text_to_audio_request import TextToAudioRequest

        mock_response = Mock()
        mock_response.content = b"audio_data"
        mock_execute.return_value = mock_response

        request = TextToAudioRequest.builder().build()
        response = client.dify.v1.audio.from_text(request, request_option)

        assert response.content == b"audio_data"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_async_audio_to_text(self, mock_aexecute, client, request_option):
        """Test async audio to text"""
        from dify_oapi.api.dify.v1.model.audio_to_text_request import AudioToTextRequest

        mock_response = Mock()
        mock_response.text = "Async hello world"
        mock_aexecute.return_value = mock_response

        request = AudioToTextRequest.builder().build()
        response = await client.dify.v1.audio.ato_text(request, request_option)

        assert response.text == "Async hello world"


class TestInfoResourceIntegration:
    """Application Info Resource Integration Tests"""

    @pytest.fixture
    def client(self):
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_app_info(self, mock_execute, client, request_option):
        """Test get application info"""
        from dify_oapi.api.dify.v1.model.get_info_request import GetInfoRequest

        mock_response = Mock()
        mock_response.name = "Test App"
        mock_response.description = "Test Description"
        mock_response.mode = "chat"
        mock_execute.return_value = mock_response

        request = GetInfoRequest.builder().build()
        response = client.dify.v1.info.get(request, request_option)

        assert response.name == "Test App"
        assert response.description == "Test Description"
        assert response.mode == "chat"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_app_parameters(self, mock_execute, client, request_option):
        """Test get application parameters"""
        from dify_oapi.api.dify.v1.model.get_parameters_request import GetParametersRequest

        mock_response = Mock()
        mock_response.opening_statement = "Welcome"
        mock_response.suggested_questions = ["How are you?"]
        mock_execute.return_value = mock_response

        request = GetParametersRequest.builder().build()
        response = client.dify.v1.info.parameters(request, request_option)

        assert response.opening_statement == "Welcome"
        assert response.suggested_questions == ["How are you?"]

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_app_meta(self, mock_execute, client, request_option):
        """Test get application metadata"""
        from dify_oapi.api.dify.v1.model.get_meta_request import GetMetaRequest

        mock_response = Mock()
        mock_response.tool_icons = {"search": "icon_url"}
        mock_execute.return_value = mock_response

        request = GetMetaRequest.builder().build()
        response = client.dify.v1.info.meta(request, request_option)

        assert response.tool_icons == {"search": "icon_url"}

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_site_settings(self, mock_execute, client, request_option):
        """Test get site settings"""
        from dify_oapi.api.dify.v1.model.get_site_request import GetSiteRequest

        mock_response = Mock()
        mock_response.title = "Test Site"
        mock_response.description = "Test Site Description"
        mock_execute.return_value = mock_response

        request = GetSiteRequest.builder().build()
        response = client.dify.v1.info.site(request, request_option)

        assert response.title == "Test Site"
        assert response.description == "Test Site Description"


class TestFeedbackResourceIntegration:
    """Feedback Resource Integration Tests"""

    @pytest.fixture
    def client(self):
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_submit_feedback(self, mock_execute, client, request_option):
        """Test submit feedback"""
        from dify_oapi.api.dify.v1.model.submit_feedback_request import SubmitFeedbackRequest
        from dify_oapi.api.dify.v1.model.submit_feedback_request_body import SubmitFeedbackRequestBody

        mock_response = Mock()
        mock_response.result = "success"
        mock_execute.return_value = mock_response

        request_body = (
            SubmitFeedbackRequestBody.builder().rating("like").user("test-user").content("Great response!").build()
        )

        request = SubmitFeedbackRequest.builder().message_id("msg-123").request_body(request_body).build()

        response = client.dify.v1.feedback.submit(request, request_option)
        assert response.result == "success"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_feedbacks(self, mock_execute, client, request_option):
        """Test get feedback list"""
        from dify_oapi.api.dify.v1.model.get_feedbacks_request import GetFeedbacksRequest

        mock_response = Mock()
        mock_response.total = 10
        mock_response.page = 1
        mock_response.data = [
            Mock(id="fb-1", rating="like", content="Good"),
            Mock(id="fb-2", rating="dislike", content="Bad"),
        ]
        mock_execute.return_value = mock_response

        request = GetFeedbacksRequest.builder().page(1).limit(10).build()

        response = client.dify.v1.feedback.list(request, request_option)

        assert response.total == 10
        assert response.page == 1
        assert len(response.data) == 2
        assert response.data[0].id == "fb-1"
        assert response.data[1].rating == "dislike"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_async_submit_feedback(self, mock_aexecute, client, request_option):
        """Test async submit feedback"""
        from dify_oapi.api.dify.v1.model.submit_feedback_request import SubmitFeedbackRequest
        from dify_oapi.api.dify.v1.model.submit_feedback_request_body import SubmitFeedbackRequestBody

        mock_response = Mock()
        mock_response.result = "async_success"
        mock_aexecute.return_value = mock_response

        request_body = SubmitFeedbackRequestBody.builder().rating("like").user("async-user").build()

        request = SubmitFeedbackRequest.builder().message_id("msg-async").request_body(request_body).build()

        response = await client.dify.v1.feedback.asubmit(request, request_option)
        assert response.result == "async_success"


if __name__ == "__main__":
    pytest.main([__file__])
