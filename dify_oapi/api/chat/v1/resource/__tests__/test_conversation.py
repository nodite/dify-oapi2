import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chat.v1.model.delete_conversation_request_body import DeleteConversationRequestBody
from dify_oapi.api.chat.v1.model.get_conversation_list_request import GetConversationsListRequest
from dify_oapi.api.chat.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chat.v1.model.rename_conversation_request_body import RenameConversationRequestBody
from dify_oapi.api.chat.v1.resource.conversation import Conversation


class TestConversation:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Conversation(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get("https://api.dify.ai/v1/conversations").mock(
            return_value=httpx.Response(200, json={"data": [], "has_more": False, "limit": 20})
        )
        result = self.resource.list(
            GetConversationsListRequest.builder().user("u1").limit(20).build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/conversations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = DeleteConversationRequestBody.builder().user("u1").build()
        result = self.resource.delete(
            DeleteConversationRequest.builder().conversation_id("conv-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_rename(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/conversations/[^/]+/name"
        ).mock(return_value=httpx.Response(200, json={"id": "conv-123", "result": "success"}))
        body = RenameConversationRequestBody.builder().name("New Name").build()
        result = self.resource.rename(
            RenameConversationRequest.builder().conversation_id("conv-123").request_body(body).build(),
            self.option,
        )
        assert result.id == "conv-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
