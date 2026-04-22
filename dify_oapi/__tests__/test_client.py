from dify_oapi.api.chat.service import ChatService
from dify_oapi.api.chatflow.service import ChatflowService
from dify_oapi.api.completion.service import CompletionService
from dify_oapi.api.dify.service import DifyService
from dify_oapi.api.knowledge.service import KnowledgeService
from dify_oapi.api.workflow.service import WorkflowService
from dify_oapi.client import Client


class TestClient:
    def test_builder_creates_client(self):
        client = Client.builder().domain("https://api.dify.ai").build()
        assert client is not None

    def test_client_has_all_services(self):
        client = Client.builder().domain("https://api.dify.ai").build()
        assert isinstance(client.chat, ChatService)
        assert isinstance(client.chatflow, ChatflowService)
        assert isinstance(client.completion, CompletionService)
        assert isinstance(client.dify, DifyService)
        assert isinstance(client.knowledge, KnowledgeService)
        assert isinstance(client.workflow, WorkflowService)

    def test_builder_domain_required(self):
        # A client built without domain should still build but may fail on request
        client = Client.builder().build()
        assert client is not None
