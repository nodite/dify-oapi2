"""Tests for Chatflow V1 version integration."""

from dify_oapi.api.chatflow.v1.resource.annotation import Annotation
from dify_oapi.api.chatflow.v1.resource.application import Application
from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow
from dify_oapi.api.chatflow.v1.resource.conversation import Conversation
from dify_oapi.api.chatflow.v1.resource.feedback import Feedback
from dify_oapi.api.chatflow.v1.resource.file import File
from dify_oapi.api.chatflow.v1.resource.tts import TTS
from dify_oapi.api.chatflow.v1.version import V1
from dify_oapi.core.model.config import Config


class TestV1VersionIntegration:
    """Test V1 version integration class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.config = Config()
        self.v1 = V1(self.config)

    def test_v1_initialization(self):
        """Test V1 class initialization."""
        assert self.v1 is not None
        assert isinstance(self.v1, V1)

    def test_chatflow_resource_accessible(self):
        """Test chatflow resource is properly accessible."""
        assert hasattr(self.v1, "chatflow")
        assert isinstance(self.v1.chatflow, Chatflow)
        assert self.v1.chatflow.config == self.config

    def test_file_resource_accessible(self):
        """Test file resource is properly accessible."""
        assert hasattr(self.v1, "file")
        assert isinstance(self.v1.file, File)
        assert self.v1.file.config == self.config

    def test_feedback_resource_accessible(self):
        """Test feedback resource is properly accessible."""
        assert hasattr(self.v1, "feedback")
        assert isinstance(self.v1.feedback, Feedback)
        assert self.v1.feedback.config == self.config

    def test_conversation_resource_accessible(self):
        """Test conversation resource is properly accessible."""
        assert hasattr(self.v1, "conversation")
        assert isinstance(self.v1.conversation, Conversation)
        assert self.v1.conversation.config == self.config

    def test_tts_resource_accessible(self):
        """Test TTS resource is properly accessible."""
        assert hasattr(self.v1, "tts")
        assert isinstance(self.v1.tts, TTS)
        assert self.v1.tts.config == self.config

    def test_application_resource_accessible(self):
        """Test application resource is properly accessible."""
        assert hasattr(self.v1, "application")
        assert isinstance(self.v1.application, Application)
        assert self.v1.application.config == self.config

    def test_annotation_resource_accessible(self):
        """Test annotation resource is properly accessible."""
        assert hasattr(self.v1, "annotation")
        assert isinstance(self.v1.annotation, Annotation)
        assert self.v1.annotation.config == self.config

    def test_all_resources_initialized(self):
        """Test all 6 resources are properly initialized."""
        resources = ["chatflow", "file", "feedback", "conversation", "tts", "application", "annotation"]

        for resource_name in resources:
            assert hasattr(self.v1, resource_name)
            resource = getattr(self.v1, resource_name)
            assert resource is not None
            assert hasattr(resource, "config")
            assert resource.config == self.config

    def test_configuration_propagation(self):
        """Test configuration is properly propagated to all resources."""
        # Test that all resources receive the same config instance
        assert self.v1.chatflow.config is self.config
        assert self.v1.file.config is self.config
        assert self.v1.feedback.config is self.config
        assert self.v1.conversation.config is self.config
        assert self.v1.tts.config is self.config
        assert self.v1.application.config is self.config
        assert self.v1.annotation.config is self.config

    def test_resource_method_accessibility(self):
        """Test that resource methods are accessible through V1."""
        # Test chatflow methods
        assert hasattr(self.v1.chatflow, "send")
        assert hasattr(self.v1.chatflow, "stop")
        assert hasattr(self.v1.chatflow, "suggested")
        assert hasattr(self.v1.chatflow, "asend")
        assert hasattr(self.v1.chatflow, "astop")
        assert hasattr(self.v1.chatflow, "asuggested")

        # Test file methods
        assert hasattr(self.v1.file, "upload")
        assert hasattr(self.v1.file, "aupload")

        # Test feedback methods
        assert hasattr(self.v1.feedback, "message")
        assert hasattr(self.v1.feedback, "list")
        assert hasattr(self.v1.feedback, "amessage")
        assert hasattr(self.v1.feedback, "alist")

        # Test conversation methods
        assert hasattr(self.v1.conversation, "messages")
        assert hasattr(self.v1.conversation, "list")
        assert hasattr(self.v1.conversation, "delete")
        assert hasattr(self.v1.conversation, "rename")
        assert hasattr(self.v1.conversation, "variables")
        assert hasattr(self.v1.conversation, "amessages")
        assert hasattr(self.v1.conversation, "alist")
        assert hasattr(self.v1.conversation, "adelete")
        assert hasattr(self.v1.conversation, "arename")
        assert hasattr(self.v1.conversation, "avariables")

        # Test TTS methods
        assert hasattr(self.v1.tts, "speech_to_text")
        assert hasattr(self.v1.tts, "text_to_audio")
        assert hasattr(self.v1.tts, "aspeech_to_text")
        assert hasattr(self.v1.tts, "atext_to_audio")

        # Test application methods
        assert hasattr(self.v1.application, "info")
        assert hasattr(self.v1.application, "parameters")
        assert hasattr(self.v1.application, "meta")
        assert hasattr(self.v1.application, "site")
        assert hasattr(self.v1.application, "ainfo")
        assert hasattr(self.v1.application, "aparameters")
        assert hasattr(self.v1.application, "ameta")
        assert hasattr(self.v1.application, "asite")

        # Test annotation methods
        assert hasattr(self.v1.annotation, "list")
        assert hasattr(self.v1.annotation, "create")
        assert hasattr(self.v1.annotation, "update")
        assert hasattr(self.v1.annotation, "delete")
        assert hasattr(self.v1.annotation, "reply_settings")
        assert hasattr(self.v1.annotation, "reply_status")
        assert hasattr(self.v1.annotation, "alist")
        assert hasattr(self.v1.annotation, "acreate")
        assert hasattr(self.v1.annotation, "aupdate")
        assert hasattr(self.v1.annotation, "adelete")
        assert hasattr(self.v1.annotation, "areply_settings")
        assert hasattr(self.v1.annotation, "areply_status")

    def test_resource_independence(self):
        """Test that resources are independent instances."""
        # Each resource should be a separate instance
        assert self.v1.chatflow is not self.v1.file
        assert self.v1.file is not self.v1.feedback
        assert self.v1.feedback is not self.v1.conversation
        assert self.v1.conversation is not self.v1.tts
        assert self.v1.tts is not self.v1.application
        assert self.v1.application is not self.v1.annotation

    def test_multiple_v1_instances(self):
        """Test that multiple V1 instances work independently."""
        config1 = Config()
        config2 = Config()

        v1_instance1 = V1(config1)
        v1_instance2 = V1(config2)

        # Instances should be different
        assert v1_instance1 is not v1_instance2

        # Resources should have different configs
        assert v1_instance1.chatflow.config is config1
        assert v1_instance2.chatflow.config is config2
        assert v1_instance1.chatflow.config is not v1_instance2.chatflow.config
