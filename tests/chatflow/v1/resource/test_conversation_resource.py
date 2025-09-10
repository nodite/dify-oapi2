from unittest.mock import patch

import pytest

from dify_oapi.api.chatflow.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chatflow.v1.model.delete_conversation_response import DeleteConversationResponse
from dify_oapi.api.chatflow.v1.model.get_conversation_messages_request import GetConversationMessagesRequest
from dify_oapi.api.chatflow.v1.model.get_conversation_messages_response import GetConversationMessagesResponse
from dify_oapi.api.chatflow.v1.model.get_conversation_variables_request import GetConversationVariablesRequest
from dify_oapi.api.chatflow.v1.model.get_conversation_variables_response import GetConversationVariablesResponse
from dify_oapi.api.chatflow.v1.model.get_conversations_request import GetConversationsRequest
from dify_oapi.api.chatflow.v1.model.get_conversations_response import GetConversationsResponse
from dify_oapi.api.chatflow.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chatflow.v1.model.rename_conversation_response import RenameConversationResponse
from dify_oapi.api.chatflow.v1.resource.conversation import Conversation
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestConversationResource:
    def setup_method(self):
        self.config = Config()
        self.conversation = Conversation(self.config)
        self.request_option = RequestOption.builder().api_key("test-api-key").build()

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_messages_sync(self, mock_execute):
        # Arrange
        request = GetConversationMessagesRequest.builder().build()
        expected_response = GetConversationMessagesResponse()
        mock_execute.return_value = expected_response

        # Act
        result = self.conversation.messages(request, self.request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=GetConversationMessagesResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_messages_async(self, mock_aexecute):
        # Arrange
        request = GetConversationMessagesRequest.builder().build()
        expected_response = GetConversationMessagesResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await self.conversation.amessages(request, self.request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=GetConversationMessagesResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_list_sync(self, mock_execute):
        # Arrange
        request = GetConversationsRequest.builder().build()
        expected_response = GetConversationsResponse()
        mock_execute.return_value = expected_response

        # Act
        result = self.conversation.list(request, self.request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=GetConversationsResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_list_async(self, mock_aexecute):
        # Arrange
        request = GetConversationsRequest.builder().build()
        expected_response = GetConversationsResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await self.conversation.alist(request, self.request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=GetConversationsResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_delete_sync(self, mock_execute):
        # Arrange
        request = DeleteConversationRequest.builder().build()
        expected_response = DeleteConversationResponse()
        mock_execute.return_value = expected_response

        # Act
        result = self.conversation.delete(request, self.request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=DeleteConversationResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_delete_async(self, mock_aexecute):
        # Arrange
        request = DeleteConversationRequest.builder().build()
        expected_response = DeleteConversationResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await self.conversation.adelete(request, self.request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=DeleteConversationResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_rename_sync(self, mock_execute):
        # Arrange
        request = RenameConversationRequest.builder().build()
        expected_response = RenameConversationResponse()
        mock_execute.return_value = expected_response

        # Act
        result = self.conversation.rename(request, self.request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=RenameConversationResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_rename_async(self, mock_aexecute):
        # Arrange
        request = RenameConversationRequest.builder().build()
        expected_response = RenameConversationResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await self.conversation.arename(request, self.request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=RenameConversationResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_variables_sync(self, mock_execute):
        # Arrange
        request = GetConversationVariablesRequest.builder().build()
        expected_response = GetConversationVariablesResponse()
        mock_execute.return_value = expected_response

        # Act
        result = self.conversation.variables(request, self.request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=GetConversationVariablesResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_variables_async(self, mock_aexecute):
        # Arrange
        request = GetConversationVariablesRequest.builder().build()
        expected_response = GetConversationVariablesResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await self.conversation.avariables(request, self.request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=GetConversationVariablesResponse, option=self.request_option
        )

    def test_conversation_initialization(self):
        # Test that conversation resource initializes correctly
        assert self.conversation.config == self.config

    def test_conversation_methods_exist(self):
        # Test that all required methods exist
        assert hasattr(self.conversation, "messages")
        assert hasattr(self.conversation, "amessages")
        assert hasattr(self.conversation, "list")
        assert hasattr(self.conversation, "alist")
        assert hasattr(self.conversation, "delete")
        assert hasattr(self.conversation, "adelete")
        assert hasattr(self.conversation, "rename")
        assert hasattr(self.conversation, "arename")
        assert hasattr(self.conversation, "variables")
        assert hasattr(self.conversation, "avariables")

    def test_conversation_methods_callable(self):
        # Test that all methods are callable
        assert callable(self.conversation.messages)
        assert callable(self.conversation.amessages)
        assert callable(self.conversation.list)
        assert callable(self.conversation.alist)
        assert callable(self.conversation.delete)
        assert callable(self.conversation.adelete)
        assert callable(self.conversation.rename)
        assert callable(self.conversation.arename)
        assert callable(self.conversation.variables)
        assert callable(self.conversation.avariables)
