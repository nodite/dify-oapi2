import pytest

from dify_oapi.api.chat.v1.resource.annotation import Annotation
from dify_oapi.api.chat.v1.resource.app import App
from dify_oapi.api.chat.v1.resource.audio import Audio
from dify_oapi.api.chat.v1.resource.chat import Chat
from dify_oapi.api.chat.v1.resource.conversation import Conversation
from dify_oapi.api.chat.v1.resource.feedback import Feedback
from dify_oapi.api.chat.v1.resource.file import File
from dify_oapi.api.chat.v1.resource.message import Message
from dify_oapi.api.chat.v1.version import V1
from dify_oapi.core.model.config import Config


class TestV1Integration:
    @pytest.fixture
    def config(self):
        return Config()

    @pytest.fixture
    def v1_instance(self, config):
        return V1(config)

    def test_v1_initialization(self, v1_instance):
        """Test V1 class initialization"""
        assert v1_instance is not None
        assert hasattr(v1_instance, "chat")
        assert hasattr(v1_instance, "file")
        assert hasattr(v1_instance, "feedback")
        assert hasattr(v1_instance, "conversation")
        assert hasattr(v1_instance, "audio")
        assert hasattr(v1_instance, "app")
        assert hasattr(v1_instance, "annotation")
        assert hasattr(v1_instance, "message")  # Deprecated but maintained

    def test_all_resources_accessible(self, v1_instance):
        """Test all resources are accessible"""
        # Test new resources
        assert isinstance(v1_instance.chat, Chat)
        assert isinstance(v1_instance.file, File)
        assert isinstance(v1_instance.feedback, Feedback)
        assert isinstance(v1_instance.conversation, Conversation)
        assert isinstance(v1_instance.audio, Audio)
        assert isinstance(v1_instance.app, App)
        assert isinstance(v1_instance.annotation, Annotation)

        # Test deprecated resource
        assert isinstance(v1_instance.message, Message)

    def test_resource_method_accessibility(self, v1_instance):
        """Test resource method accessibility"""
        # Chat resource methods
        assert hasattr(v1_instance.chat, "chat")
        assert hasattr(v1_instance.chat, "stop")
        assert hasattr(v1_instance.chat, "suggested")
        assert hasattr(v1_instance.chat, "achat")
        assert hasattr(v1_instance.chat, "astop")
        assert hasattr(v1_instance.chat, "asuggested")

        # File resource methods
        assert hasattr(v1_instance.file, "upload")
        assert hasattr(v1_instance.file, "aupload")

        # Feedback resource methods
        assert hasattr(v1_instance.feedback, "submit")
        assert hasattr(v1_instance.feedback, "list")
        assert hasattr(v1_instance.feedback, "asubmit")
        assert hasattr(v1_instance.feedback, "alist")

        # Conversation resource methods
        assert hasattr(v1_instance.conversation, "list")
        assert hasattr(v1_instance.conversation, "delete")
        assert hasattr(v1_instance.conversation, "rename")
        assert hasattr(v1_instance.conversation, "history")
        assert hasattr(v1_instance.conversation, "variables")
        assert hasattr(v1_instance.conversation, "alist")
        assert hasattr(v1_instance.conversation, "adelete")
        assert hasattr(v1_instance.conversation, "arename")
        assert hasattr(v1_instance.conversation, "ahistory")
        assert hasattr(v1_instance.conversation, "avariables")

        # Audio resource methods
        assert hasattr(v1_instance.audio, "to_text")
        assert hasattr(v1_instance.audio, "to_audio")
        assert hasattr(v1_instance.audio, "ato_text")
        assert hasattr(v1_instance.audio, "ato_audio")

        # App resource methods
        assert hasattr(v1_instance.app, "info")
        assert hasattr(v1_instance.app, "parameters")
        assert hasattr(v1_instance.app, "meta")
        assert hasattr(v1_instance.app, "site")
        assert hasattr(v1_instance.app, "ainfo")
        assert hasattr(v1_instance.app, "aparameters")
        assert hasattr(v1_instance.app, "ameta")
        assert hasattr(v1_instance.app, "asite")

        # Annotation resource methods
        assert hasattr(v1_instance.annotation, "list")
        assert hasattr(v1_instance.annotation, "create")
        assert hasattr(v1_instance.annotation, "update")
        assert hasattr(v1_instance.annotation, "delete")
        assert hasattr(v1_instance.annotation, "configure")
        assert hasattr(v1_instance.annotation, "status")
        assert hasattr(v1_instance.annotation, "alist")
        assert hasattr(v1_instance.annotation, "acreate")
        assert hasattr(v1_instance.annotation, "aupdate")
        assert hasattr(v1_instance.annotation, "adelete")
        assert hasattr(v1_instance.annotation, "aconfigure")
        assert hasattr(v1_instance.annotation, "astatus")

    def test_configuration_propagation(self, config, v1_instance):
        """Test configuration propagation to all resources"""
        assert v1_instance.chat.config is config
        assert v1_instance.file.config is config
        assert v1_instance.feedback.config is config
        assert v1_instance.conversation.config is config
        assert v1_instance.audio.config is config
        assert v1_instance.app.config is config
        assert v1_instance.annotation.config is config
        assert v1_instance.message.config is config

    def test_backward_compatibility(self, v1_instance):
        """Test backward compatibility with deprecated message resource"""
        # Message resource should still be accessible
        assert hasattr(v1_instance, "message")
        assert isinstance(v1_instance.message, Message)

        # Message resource methods should still work
        assert hasattr(v1_instance.message, "suggested")
        assert hasattr(v1_instance.message, "history")
        assert hasattr(v1_instance.message, "asuggested")
        assert hasattr(v1_instance.message, "ahistory")

    def test_resource_independence(self, v1_instance):
        """Test that resources are independent instances"""
        resources = [
            v1_instance.chat,
            v1_instance.file,
            v1_instance.feedback,
            v1_instance.conversation,
            v1_instance.audio,
            v1_instance.app,
            v1_instance.annotation,
            v1_instance.message,
        ]

        # Ensure all resources are different instances
        for i, resource1 in enumerate(resources):
            for j, resource2 in enumerate(resources):
                if i != j:
                    assert resource1 is not resource2

    def test_all_seven_resources_present(self, v1_instance):
        """Test that all 7 main resources plus deprecated message resource are present"""
        main_resources = ["chat", "file", "feedback", "conversation", "audio", "app", "annotation"]
        deprecated_resources = ["message"]

        for resource_name in main_resources:
            assert hasattr(v1_instance, resource_name)
            resource = getattr(v1_instance, resource_name)
            assert resource is not None

        for resource_name in deprecated_resources:
            assert hasattr(v1_instance, resource_name)
            resource = getattr(v1_instance, resource_name)
            assert resource is not None
