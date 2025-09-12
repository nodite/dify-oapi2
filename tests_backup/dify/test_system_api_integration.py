"""
Dify System-level API Integration Tests

Test unified dify system-level API functionality
"""

from unittest.mock import Mock, patch

import pytest

from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


class TestDifySystemAPIIntegration:
    """Dify System-level API Integration Tests"""

    @pytest.fixture
    def client(self):
        """Create test client"""
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        """Create test request option"""
        return RequestOption.builder().api_key("test-api-key").build()

    def test_dify_module_structure(self, client):
        """Test dify module structure"""
        # Verify dify module exists
        assert hasattr(client, "dify")
        assert hasattr(client.dify, "v1")

        # Verify system-level resources exist
        assert hasattr(client.dify.v1, "file")
        assert hasattr(client.dify.v1, "audio")
        assert hasattr(client.dify.v1, "info")
        assert hasattr(client.dify.v1, "feedback")

    def test_file_api_methods(self, client):
        """Test file API methods"""
        file_api = client.dify.v1.file

        # 验证方法存在
        assert hasattr(file_api, "upload")
        assert hasattr(file_api, "aupload")
        assert callable(file_api.upload)
        assert callable(file_api.aupload)

    def test_audio_api_methods(self, client):
        """Test audio API methods"""
        audio_api = client.dify.v1.audio

        # 验证方法存在
        assert hasattr(audio_api, "to_text")
        assert hasattr(audio_api, "ato_text")
        assert hasattr(audio_api, "from_text")
        assert hasattr(audio_api, "afrom_text")

        # 验证方法可调用
        assert callable(audio_api.to_text)
        assert callable(audio_api.ato_text)
        assert callable(audio_api.from_text)
        assert callable(audio_api.afrom_text)

    def test_info_api_methods(self, client):
        """Test application info API methods"""
        info_api = client.dify.v1.info

        # 验证方法存在
        assert hasattr(info_api, "get")
        assert hasattr(info_api, "aget")
        assert hasattr(info_api, "parameters")
        assert hasattr(info_api, "aparameters")
        assert hasattr(info_api, "meta")
        assert hasattr(info_api, "ameta")
        assert hasattr(info_api, "site")
        assert hasattr(info_api, "asite")

        # 验证方法可调用
        assert callable(info_api.get)
        assert callable(info_api.aget)
        assert callable(info_api.parameters)
        assert callable(info_api.aparameters)
        assert callable(info_api.meta)
        assert callable(info_api.ameta)
        assert callable(info_api.site)
        assert callable(info_api.asite)

    def test_feedback_api_methods(self, client):
        """Test feedback API methods"""
        feedback_api = client.dify.v1.feedback

        # 验证方法存在
        assert hasattr(feedback_api, "submit")
        assert hasattr(feedback_api, "asubmit")
        assert hasattr(feedback_api, "list")
        assert hasattr(feedback_api, "alist")

        # 验证方法可调用
        assert callable(feedback_api.submit)
        assert callable(feedback_api.asubmit)
        assert callable(feedback_api.list)
        assert callable(feedback_api.alist)

    def test_cross_module_compatibility(self, client):
        """Test cross-module compatibility"""
        # Verify all modules can access system-level APIs
        modules = ["chat", "completion", "chatflow", "workflow"]

        for module_name in modules:
            if hasattr(client, module_name):
                module = getattr(client, module_name)
                if hasattr(module, "v1"):
                    v1 = module.v1

                    # Verify system-level APIs are accessible
                    if hasattr(v1, "file"):
                        assert hasattr(v1.file, "upload")
                    if hasattr(v1, "audio"):
                        assert hasattr(v1.audio, "to_text") or hasattr(v1.audio, "text_to_audio")
                    if hasattr(v1, "feedback"):
                        assert hasattr(v1.feedback, "submit")

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_file_upload_integration(self, mock_execute, client, request_option):
        """Test file upload integration"""
        from dify_oapi.api.dify.v1.model.upload_file_request import UploadFileRequest

        # 模拟响应
        mock_response = Mock()
        mock_response.id = "file-123"
        mock_response.name = "test.txt"
        mock_execute.return_value = mock_response

        # 创建请求
        request = UploadFileRequest.builder().build()

        # 执行上传
        response = client.dify.v1.file.upload(request, request_option)

        # 验证结果
        assert response.id == "file-123"
        assert response.name == "test.txt"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_feedback_submit_integration(self, mock_execute, client, request_option):
        """Test feedback submit integration"""
        from dify_oapi.api.dify.v1.model.submit_feedback_request import SubmitFeedbackRequest
        from dify_oapi.api.dify.v1.model.submit_feedback_request_body import SubmitFeedbackRequestBody

        # 模拟响应
        mock_response = Mock()
        mock_response.result = "success"
        mock_execute.return_value = mock_response

        # 创建请求
        request_body = SubmitFeedbackRequestBody.builder().rating("like").user("test-user").build()
        request = SubmitFeedbackRequest.builder().message_id("msg-123").request_body(request_body).build()

        # 执行提交
        response = client.dify.v1.feedback.submit(request, request_option)

        # 验证结果
        assert response.result == "success"
        mock_execute.assert_called_once()

    def test_api_consistency(self, client):
        """Test API consistency"""
        # Verify all system-level APIs have both sync and async versions
        apis = [
            (client.dify.v1.file, ["upload", "aupload"]),
            (client.dify.v1.audio, ["to_text", "ato_text", "from_text", "afrom_text"]),
            (client.dify.v1.info, ["get", "aget", "parameters", "aparameters"]),
            (client.dify.v1.feedback, ["submit", "asubmit", "list", "alist"]),
        ]

        for api, methods in apis:
            for method in methods:
                assert hasattr(api, method), f"API {api} missing method {method}"
                assert callable(getattr(api, method)), f"Method {method} not callable"


class TestSystemAPIUnification:
    """System-level API Unification Tests"""

    @pytest.fixture
    def client(self):
        return Client.builder().domain("https://api.dify.ai").build()

    def test_unified_access_patterns(self, client):
        """Test unified access patterns"""
        # Direct access to dify system-level APIs
        assert hasattr(client.dify.v1, "file")
        assert hasattr(client.dify.v1, "audio")
        assert hasattr(client.dify.v1, "info")
        assert hasattr(client.dify.v1, "feedback")

    def test_module_delegation(self, client):
        """Test module delegation"""
        # Verify modules access system-level APIs through delegation
        if hasattr(client.chat.v1, "file"):
            # chat module's file should delegate to dify.file
            assert client.chat.v1.file.__class__.__name__ == "File"

        if hasattr(client.completion.v1, "audio"):
            # completion module's audio should delegate to dify.audio
            assert client.completion.v1.audio.__class__.__name__ == "Audio"

    def test_backward_compatibility(self, client):
        """Test backward compatibility"""
        # Verify original API calling methods are still valid
        modules_with_system_apis = [
            ("chat", ["file", "audio", "app", "feedback"]),
            ("completion", ["file", "audio", "info", "feedback"]),
            ("chatflow", ["file", "tts", "application", "feedback"]),
            ("workflow", ["file", "info", "feedback"]),
        ]

        for module_name, api_names in modules_with_system_apis:
            if hasattr(client, module_name):
                module = getattr(client, module_name)
                if hasattr(module, "v1"):
                    v1 = module.v1
                    for api_name in api_names:
                        if hasattr(v1, api_name):
                            api = getattr(v1, api_name)
                            # Verify API object exists and is usable
                            assert api is not None


if __name__ == "__main__":
    pytest.main([__file__])
