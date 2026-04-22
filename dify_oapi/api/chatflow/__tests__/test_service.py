from dify_oapi.api.chatflow.service import ChatflowService
from dify_oapi.api.chatflow.v1.resource.annotation import Annotation
from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow
from dify_oapi.api.chatflow.v1.resource.conversation import Conversation
from dify_oapi.api.chatflow.v1.version import V1


class TestChatflowService:
    def test_service_has_v1(self, config):
        service = ChatflowService(config)
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_has_resources(self, config):
        v1 = ChatflowService(config).v1
        assert isinstance(v1.chatflow, Chatflow)
        assert isinstance(v1.conversation, Conversation)
        assert isinstance(v1.annotation, Annotation)
