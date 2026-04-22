from dify_oapi.api.chat.service import ChatService
from dify_oapi.api.chat.v1.resource.annotation import Annotation
from dify_oapi.api.chat.v1.resource.chat import Chat
from dify_oapi.api.chat.v1.resource.conversation import Conversation
from dify_oapi.api.chat.v1.resource.message import Message
from dify_oapi.api.chat.v1.version import V1


class TestChatService:
    def test_service_has_v1(self, config):
        service = ChatService(config)
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_has_resources(self, config):
        v1 = ChatService(config).v1
        assert isinstance(v1.chat, Chat)
        assert isinstance(v1.conversation, Conversation)
        assert isinstance(v1.annotation, Annotation)
        assert isinstance(v1.message, Message)
