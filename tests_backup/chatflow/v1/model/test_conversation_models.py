from dify_oapi.api.chatflow.v1.model.chatflow_types import SortBy, VariableValueType
from dify_oapi.api.chatflow.v1.model.conversation_variable import ConversationVariable
from dify_oapi.api.chatflow.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chatflow.v1.model.delete_conversation_request_body import DeleteConversationRequestBody
from dify_oapi.api.chatflow.v1.model.delete_conversation_response import DeleteConversationResponse
from dify_oapi.api.chatflow.v1.model.get_conversation_messages_request import GetConversationMessagesRequest
from dify_oapi.api.chatflow.v1.model.get_conversation_messages_response import GetConversationMessagesResponse
from dify_oapi.api.chatflow.v1.model.get_conversation_variables_request import GetConversationVariablesRequest
from dify_oapi.api.chatflow.v1.model.get_conversation_variables_response import GetConversationVariablesResponse
from dify_oapi.api.chatflow.v1.model.get_conversations_request import GetConversationsRequest
from dify_oapi.api.chatflow.v1.model.get_conversations_response import GetConversationsResponse
from dify_oapi.api.chatflow.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chatflow.v1.model.rename_conversation_request_body import RenameConversationRequestBody
from dify_oapi.api.chatflow.v1.model.rename_conversation_response import RenameConversationResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestGetConversationMessagesModels:
    """Test class for Get Conversation Messages API models."""

    def test_request_builder(self):
        """Test request builder functionality."""
        request = (
            GetConversationMessagesRequest.builder()
            .conversation_id("conv_123")
            .user("user_123")
            .first_id("msg_123")
            .limit(20)
            .build()
        )

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/messages"
        assert ("conversation_id", "conv_123") in request.queries
        assert ("user", "user_123") in request.queries
        assert ("first_id", "msg_123") in request.queries
        assert ("limit", "20") in request.queries

    def test_request_validation(self):
        """Test request validation."""
        request = GetConversationMessagesRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/messages"

    def test_response_inheritance(self):
        """Test response inherits from BaseResponse."""
        response = GetConversationMessagesResponse()
        assert isinstance(response, BaseResponse)

    def test_response_builder(self):
        """Test response builder functionality."""
        response = GetConversationMessagesResponse.builder().limit(20).has_more(True).data([]).build()

        assert response.limit == 20
        assert response.has_more is True
        assert response.data == []


class TestGetConversationsModels:
    """Test class for Get Conversations API models."""

    def test_request_builder(self):
        """Test request builder functionality."""
        request = (
            GetConversationsRequest.builder()
            .user("user_123")
            .last_id("conv_123")
            .limit(20)
            .sort_by("-updated_at")
            .build()
        )

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/conversations"
        assert ("user", "user_123") in request.queries
        assert ("last_id", "conv_123") in request.queries
        assert ("limit", "20") in request.queries
        assert ("sort_by", "-updated_at") in request.queries

    def test_sort_by_validation(self):
        """Test sort_by parameter validation."""
        valid_sort_options: list[SortBy] = ["created_at", "-created_at", "updated_at", "-updated_at"]

        for sort_option in valid_sort_options:
            request = GetConversationsRequest.builder().user("user_123").sort_by(sort_option).build()
            assert ("sort_by", sort_option) in request.queries

    def test_response_inheritance(self):
        """Test response inherits from BaseResponse."""
        response = GetConversationsResponse()
        assert isinstance(response, BaseResponse)

    def test_response_builder(self):
        """Test response builder functionality."""
        response = GetConversationsResponse.builder().limit(20).has_more(False).data([]).build()

        assert response.limit == 20
        assert response.has_more is False
        assert response.data == []


class TestDeleteConversationModels:
    """Test class for Delete Conversation API models."""

    def test_request_body_builder(self):
        """Test request body builder functionality."""
        request_body = DeleteConversationRequestBody.builder().user("user_123").build()

        assert request_body.user == "user_123"

    def test_request_builder(self):
        """Test request builder functionality."""
        request_body = DeleteConversationRequestBody.builder().user("user_123").build()
        request = DeleteConversationRequest.builder().conversation_id("conv_123").request_body(request_body).build()

        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/conversations/:conversation_id"
        assert request.conversation_id == "conv_123"
        assert "conversation_id" in request.paths
        assert request.paths["conversation_id"] == "conv_123"
        assert request.request_body == request_body
        assert request.body is not None

    def test_response_inheritance(self):
        """Test response inherits from BaseResponse."""
        response = DeleteConversationResponse()
        assert isinstance(response, BaseResponse)


class TestRenameConversationModels:
    """Test class for Rename Conversation API models."""

    def test_request_body_builder(self):
        """Test request body builder functionality."""
        request_body = (
            RenameConversationRequestBody.builder()
            .name("New Conversation Name")
            .auto_generate(False)
            .user("user_123")
            .build()
        )

        assert request_body.name == "New Conversation Name"
        assert request_body.auto_generate is False
        assert request_body.user == "user_123"

    def test_request_body_auto_generate(self):
        """Test request body with auto_generate option."""
        request_body = RenameConversationRequestBody.builder().auto_generate(True).user("user_123").build()

        assert request_body.name is None
        assert request_body.auto_generate is True
        assert request_body.user == "user_123"

    def test_request_builder(self):
        """Test request builder functionality."""
        request_body = RenameConversationRequestBody.builder().name("New Name").user("user_123").build()
        request = RenameConversationRequest.builder().conversation_id("conv_123").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/conversations/:conversation_id/name"
        assert request.conversation_id == "conv_123"
        assert "conversation_id" in request.paths
        assert request.paths["conversation_id"] == "conv_123"
        assert request.request_body == request_body
        assert request.body is not None

    def test_response_inheritance(self):
        """Test response inherits from BaseResponse."""
        response = RenameConversationResponse()
        assert isinstance(response, BaseResponse)

    def test_response_builder(self):
        """Test response builder functionality."""
        response = (
            RenameConversationResponse.builder()
            .id("conv_123")
            .name("Updated Name")
            .status("normal")
            .created_at(1640995200)
            .updated_at(1640995300)
            .build()
        )

        assert response.id == "conv_123"
        assert response.name == "Updated Name"
        assert response.status == "normal"
        assert response.created_at == 1640995200
        assert response.updated_at == 1640995300


class TestGetConversationVariablesModels:
    """Test class for Get Conversation Variables API models."""

    def test_request_builder(self):
        """Test request builder functionality."""
        request = (
            GetConversationVariablesRequest.builder()
            .conversation_id("conv_123")
            .user("user_123")
            .last_id("var_123")
            .limit(20)
            .variable_name("user_name")
            .build()
        )

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/conversations/:conversation_id/variables"
        assert request.conversation_id == "conv_123"
        assert "conversation_id" in request.paths
        assert request.paths["conversation_id"] == "conv_123"
        assert ("user", "user_123") in request.queries
        assert ("last_id", "var_123") in request.queries
        assert ("limit", "20") in request.queries
        assert ("variable_name", "user_name") in request.queries

    def test_response_inheritance(self):
        """Test response inherits from BaseResponse."""
        response = GetConversationVariablesResponse()
        assert isinstance(response, BaseResponse)

    def test_response_builder(self):
        """Test response builder functionality."""
        variables = [
            ConversationVariable.builder().id("var_1").name("user_name").value_type("string").value("Alice").build()
        ]

        response = GetConversationVariablesResponse.builder().limit(20).has_more(False).data(variables).build()

        assert response.limit == 20
        assert response.has_more is False
        assert response.data == variables
        assert len(response.data) == 1
        assert response.data[0].name == "user_name"


class TestConversationVariable:
    """Test class for ConversationVariable model."""

    def test_builder_pattern(self):
        """Test builder pattern functionality."""
        variable = (
            ConversationVariable.builder()
            .id("var_123")
            .name("user_preference")
            .value_type("select")
            .value("dark_mode")
            .description("User interface theme preference")
            .created_at(1640995200)
            .updated_at(1640995300)
            .build()
        )

        assert variable.id == "var_123"
        assert variable.name == "user_preference"
        assert variable.value_type == "select"
        assert variable.value == "dark_mode"
        assert variable.description == "User interface theme preference"
        assert variable.created_at == 1640995200
        assert variable.updated_at == 1640995300

    def test_field_validation(self):
        """Test field validation."""
        variable = ConversationVariable()
        assert variable.id is None
        assert variable.name is None
        assert variable.value_type is None
        assert variable.value is None
        assert variable.description is None
        assert variable.created_at is None
        assert variable.updated_at is None

    def test_value_type_validation(self):
        """Test value_type field validation."""
        valid_types: list[VariableValueType] = ["string", "number", "select"]

        for value_type in valid_types:
            variable = ConversationVariable.builder().value_type(value_type).build()
            assert variable.value_type == value_type
