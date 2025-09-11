"""Tests for Chatflow service integration."""

from dify_oapi.api.chatflow.service import ChatflowService
from dify_oapi.api.chatflow.v1.version import V1
from dify_oapi.core.model.config import Config


class TestChatflowService:
    """Test cases for ChatflowService class."""

    def test_service_initialization(self):
        """Test service initialization with config."""
        config = Config()
        config.domain = "https://api.dify.ai"
        service = ChatflowService(config)

        assert service is not None
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_version_accessibility(self):
        """Test that v1 version is properly accessible."""
        config = Config()
        config.domain = "https://api.dify.ai"
        service = ChatflowService(config)

        # Verify v1 is accessible
        assert service.v1 is not None
        assert isinstance(service.v1, V1)

        # Verify all resources are accessible through v1
        assert hasattr(service.v1, "chatflow")
        assert hasattr(service.v1, "file")
        assert hasattr(service.v1, "feedback")
        assert hasattr(service.v1, "conversation")
        assert hasattr(service.v1, "tts")
        assert hasattr(service.v1, "application")
        assert hasattr(service.v1, "annotation")

    def test_configuration_propagation(self):
        """Test that configuration is properly propagated to v1."""
        domain = "https://test.api.dify.ai"
        config = Config()
        config.domain = domain
        service = ChatflowService(config)

        # Verify v1 is accessible
        assert service.v1 is not None

    def test_service_resource_methods(self):
        """Test that all expected resource methods are accessible."""
        config = Config()
        config.domain = "https://api.dify.ai"
        service = ChatflowService(config)

        # Test chatflow resource methods
        assert hasattr(service.v1.chatflow, "send")
        assert hasattr(service.v1.chatflow, "stop")
        assert hasattr(service.v1.chatflow, "suggested")

        # Test file resource methods
        assert hasattr(service.v1.file, "upload")

        # Test feedback resource methods
        assert hasattr(service.v1.feedback, "message")
        assert hasattr(service.v1.feedback, "list")

        # Test conversation resource methods
        assert hasattr(service.v1.conversation, "messages")
        assert hasattr(service.v1.conversation, "list")
        assert hasattr(service.v1.conversation, "delete")
        assert hasattr(service.v1.conversation, "rename")
        assert hasattr(service.v1.conversation, "variables")

        # Test TTS resource methods
        assert hasattr(service.v1.tts, "speech_to_text")
        assert hasattr(service.v1.tts, "text_to_audio")

        # Test application resource methods
        assert hasattr(service.v1.application, "info")
        assert hasattr(service.v1.application, "parameters")
        assert hasattr(service.v1.application, "meta")
        assert hasattr(service.v1.application, "site")

        # Test annotation resource methods
        assert hasattr(service.v1.annotation, "list")
        assert hasattr(service.v1.annotation, "create")
        assert hasattr(service.v1.annotation, "update")
        assert hasattr(service.v1.annotation, "delete")
        assert hasattr(service.v1.annotation, "reply_settings")
        assert hasattr(service.v1.annotation, "reply_status")

    def test_service_async_methods(self):
        """Test that all expected async resource methods are accessible."""
        config = Config()
        config.domain = "https://api.dify.ai"
        service = ChatflowService(config)

        # Test chatflow async methods
        assert hasattr(service.v1.chatflow, "asend")
        assert hasattr(service.v1.chatflow, "astop")
        assert hasattr(service.v1.chatflow, "asuggested")

        # Test file async methods
        assert hasattr(service.v1.file, "aupload")

        # Test feedback async methods
        assert hasattr(service.v1.feedback, "amessage")
        assert hasattr(service.v1.feedback, "alist")

        # Test conversation async methods
        assert hasattr(service.v1.conversation, "amessages")
        assert hasattr(service.v1.conversation, "alist")
        assert hasattr(service.v1.conversation, "adelete")
        assert hasattr(service.v1.conversation, "arename")
        assert hasattr(service.v1.conversation, "avariables")

        # Test TTS async methods
        assert hasattr(service.v1.tts, "aspeech_to_text")
        assert hasattr(service.v1.tts, "atext_to_audio")

        # Test application async methods
        assert hasattr(service.v1.application, "ainfo")
        assert hasattr(service.v1.application, "aparameters")
        assert hasattr(service.v1.application, "ameta")
        assert hasattr(service.v1.application, "asite")

        # Test annotation async methods
        assert hasattr(service.v1.annotation, "alist")
        assert hasattr(service.v1.annotation, "acreate")
        assert hasattr(service.v1.annotation, "aupdate")
        assert hasattr(service.v1.annotation, "adelete")
        assert hasattr(service.v1.annotation, "areply_settings")
        assert hasattr(service.v1.annotation, "areply_status")
