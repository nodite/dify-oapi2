from unittest.mock import patch

import pytest

from dify_oapi.api.chat.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chat.v1.model.delete_conversation_response import DeleteConversationResponse
from dify_oapi.api.chat.v1.model.get_conversation_list_request import GetConversationsRequest
from dify_oapi.api.chat.v1.model.get_conversation_list_response import GetConversationsResponse
from dify_oapi.api.chat.v1.model.get_conversation_variables_request import GetConversationVariablesRequest
from dify_oapi.api.chat.v1.model.get_conversation_variables_response import GetConversationVariablesResponse
from dify_oapi.api.chat.v1.model.message_history_request import GetMessageHistoryRequest
from dify_oapi.api.chat.v1.model.message_history_response import GetMessageHistoryResponse
from dify_oapi.api.chat.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chat.v1.model.rename_conversation_response import RenameConversationResponse
from dify_oapi.api.chat.v1.resource.conversation import Conversation
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestConversationResource:
    """Test Conversation resource class."""

    @pytest.fixture
    def conversation_resource(self):
        """Create Conversation resource instance."""
        config = Config()
        return Conversation(config)

    @pytest.fixture
    def request_option(self):
        """Create RequestOption instance."""
        return RequestOption.builder().api_key("test-api-key").build()

    def test_list_conversations(self, conversation_resource, request_option):
        """Test list conversations method."""
        request = GetConversationsRequest.builder().user("user-123").build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_response = GetConversationsResponse()
            mock_execute.return_value = mock_response

            result = conversation_resource.list(request, request_option)

            assert result == mock_response
            mock_execute.assert_called_once_with(
                conversation_resource.config,
                request,
                unmarshal_as=GetConversationsResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_alist_conversations(self, conversation_resource, request_option):
        """Test async list conversations method."""
        request = GetConversationsRequest.builder().user("user-123").build()

        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_aexecute:
            mock_response = GetConversationsResponse()
            mock_aexecute.return_value = mock_response

            result = await conversation_resource.alist(request, request_option)

            assert result == mock_response
            mock_aexecute.assert_called_once_with(
                conversation_resource.config,
                request,
                unmarshal_as=GetConversationsResponse,
                option=request_option,
            )

    def test_get_message_history(self, conversation_resource, request_option):
        """Test get message history method."""
        request = GetMessageHistoryRequest.builder().conversation_id("conv-123").user("user-123").build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_response = GetMessageHistoryResponse()
            mock_execute.return_value = mock_response

            result = conversation_resource.history(request, request_option)

            assert result == mock_response
            mock_execute.assert_called_once_with(
                conversation_resource.config,
                request,
                unmarshal_as=GetMessageHistoryResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_ahistory(self, conversation_resource, request_option):
        """Test async get message history method."""
        request = GetMessageHistoryRequest.builder().conversation_id("conv-123").user("user-123").build()

        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_aexecute:
            mock_response = GetMessageHistoryResponse()
            mock_aexecute.return_value = mock_response

            result = await conversation_resource.ahistory(request, request_option)

            assert result == mock_response
            mock_aexecute.assert_called_once_with(
                conversation_resource.config,
                request,
                unmarshal_as=GetMessageHistoryResponse,
                option=request_option,
            )

    def test_get_conversation_variables(self, conversation_resource, request_option):
        """Test get conversation variables method."""
        request = GetConversationVariablesRequest.builder().conversation_id("conv-123").user("user-123").build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_response = GetConversationVariablesResponse()
            mock_execute.return_value = mock_response

            result = conversation_resource.variables(request, request_option)

            assert result == mock_response
            mock_execute.assert_called_once_with(
                conversation_resource.config,
                request,
                unmarshal_as=GetConversationVariablesResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_avariables(self, conversation_resource, request_option):
        """Test async get conversation variables method."""
        request = GetConversationVariablesRequest.builder().conversation_id("conv-123").user("user-123").build()

        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_aexecute:
            mock_response = GetConversationVariablesResponse()
            mock_aexecute.return_value = mock_response

            result = await conversation_resource.avariables(request, request_option)

            assert result == mock_response
            mock_aexecute.assert_called_once_with(
                conversation_resource.config,
                request,
                unmarshal_as=GetConversationVariablesResponse,
                option=request_option,
            )

    def test_delete_conversation(self, conversation_resource, request_option):
        """Test delete conversation method."""
        request = DeleteConversationRequest.builder().conversation_id("conv-123").build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_response = DeleteConversationResponse()
            mock_execute.return_value = mock_response

            result = conversation_resource.delete(request, request_option)

            assert result == mock_response
            mock_execute.assert_called_once_with(
                conversation_resource.config,
                request,
                unmarshal_as=DeleteConversationResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_adelete_conversation(self, conversation_resource, request_option):
        """Test async delete conversation method."""
        request = DeleteConversationRequest.builder().conversation_id("conv-123").build()

        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_aexecute:
            mock_response = DeleteConversationResponse()
            mock_aexecute.return_value = mock_response

            result = await conversation_resource.adelete(request, request_option)

            assert result == mock_response
            mock_aexecute.assert_called_once_with(
                conversation_resource.config,
                request,
                unmarshal_as=DeleteConversationResponse,
                option=request_option,
            )

    def test_rename_conversation(self, conversation_resource, request_option):
        """Test rename conversation method."""
        request = RenameConversationRequest.builder().conversation_id("conv-123").build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_response = RenameConversationResponse()
            mock_execute.return_value = mock_response

            result = conversation_resource.rename(request, request_option)

            assert result == mock_response
            mock_execute.assert_called_once_with(
                conversation_resource.config,
                request,
                unmarshal_as=RenameConversationResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_arename_conversation(self, conversation_resource, request_option):
        """Test async rename conversation method."""
        request = RenameConversationRequest.builder().conversation_id("conv-123").build()

        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_aexecute:
            mock_response = RenameConversationResponse()
            mock_aexecute.return_value = mock_response

            result = await conversation_resource.arename(request, request_option)

            assert result == mock_response
            mock_aexecute.assert_called_once_with(
                conversation_resource.config,
                request,
                unmarshal_as=RenameConversationResponse,
                option=request_option,
            )

    def test_conversation_resource_initialization(self, conversation_resource):
        """Test conversation resource initialization."""
        assert isinstance(conversation_resource.config, Config)
        assert hasattr(conversation_resource, "list")
        assert hasattr(conversation_resource, "alist")
        assert hasattr(conversation_resource, "history")
        assert hasattr(conversation_resource, "ahistory")
        assert hasattr(conversation_resource, "variables")
        assert hasattr(conversation_resource, "avariables")
        assert hasattr(conversation_resource, "delete")
        assert hasattr(conversation_resource, "adelete")
        assert hasattr(conversation_resource, "rename")
        assert hasattr(conversation_resource, "arename")

    def test_all_methods_with_none_option(self, conversation_resource):
        """Test all methods work with None option."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = GetConversationsResponse()

            # Test list with None option
            request = GetConversationsRequest.builder().user("user-123").build()
            conversation_resource.list(request, None)

            mock_execute.assert_called_with(
                conversation_resource.config,
                request,
                unmarshal_as=GetConversationsResponse,
                option=None,
            )

    def test_pagination_and_filtering(self, conversation_resource, request_option):
        """Test pagination and filtering functionality."""
        # Test conversations list with pagination
        request = (
            GetConversationsRequest.builder()
            .user("user-123")
            .last_id("conv-456")
            .limit(10)
            .sort_by("-updated_at")
            .build()
        )

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_response = GetConversationsResponse()
            mock_execute.return_value = mock_response

            result = conversation_resource.list(request, request_option)

            assert result == mock_response
            mock_execute.assert_called_once()

    def test_conversation_variables_filtering(self, conversation_resource, request_option):
        """Test conversation variables with filtering."""
        request = (
            GetConversationVariablesRequest.builder()
            .conversation_id("conv-123")
            .user("user-123")
            .last_id("var-456")
            .limit(20)
            .variable_name("test_var")
            .build()
        )

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_response = GetConversationVariablesResponse()
            mock_execute.return_value = mock_response

            result = conversation_resource.variables(request, request_option)

            assert result == mock_response
            mock_execute.assert_called_once()

    def test_message_history_pagination(self, conversation_resource, request_option):
        """Test message history with pagination."""
        request = (
            GetMessageHistoryRequest.builder()
            .conversation_id("conv-123")
            .user("user-123")
            .first_id("msg-456")
            .limit(50)
            .build()
        )

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_response = GetMessageHistoryResponse()
            mock_execute.return_value = mock_response

            result = conversation_resource.history(request, request_option)

            assert result == mock_response
            mock_execute.assert_called_once()
