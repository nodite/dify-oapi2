"""Tests for Conversation Management API models."""

from dify_oapi.api.chat.v1.model.conversation_info import ConversationInfo
from dify_oapi.api.chat.v1.model.conversation_variable import ConversationVariable
from dify_oapi.api.chat.v1.model.delete_conversation_request import DeleteConversationRequest
from dify_oapi.api.chat.v1.model.delete_conversation_request_body import DeleteConversationRequestBody
from dify_oapi.api.chat.v1.model.delete_conversation_response import DeleteConversationResponse
from dify_oapi.api.chat.v1.model.get_conversation_list_request import GetConversationsRequest
from dify_oapi.api.chat.v1.model.get_conversation_list_response import GetConversationsResponse
from dify_oapi.api.chat.v1.model.get_conversation_variables_request import GetConversationVariablesRequest
from dify_oapi.api.chat.v1.model.get_conversation_variables_response import GetConversationVariablesResponse
from dify_oapi.api.chat.v1.model.message_history_request import GetMessageHistoryRequest
from dify_oapi.api.chat.v1.model.message_history_response import GetMessageHistoryResponse
from dify_oapi.api.chat.v1.model.message_info import MessageInfo
from dify_oapi.api.chat.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chat.v1.model.rename_conversation_request_body import RenameConversationRequestBody
from dify_oapi.api.chat.v1.model.rename_conversation_response import RenameConversationResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest
from dify_oapi.core.model.base_response import BaseResponse


class TestGetMessageHistoryModels:
    """Test Get Message History API models."""

    def test_get_message_history_request_builder(self):
        """Test GetMessageHistoryRequest builder pattern."""
        request = (
            GetMessageHistoryRequest.builder()
            .conversation_id("conv-123")
            .user("user-123")
            .first_id("msg-123")
            .limit(20)
            .build()
        )

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/messages"
        assert request.conversation_id == "conv-123"
        assert request.user == "user-123"
        assert request.first_id == "msg-123"
        assert request.limit == 20

        # Check query parameters
        query_dict = dict(request.queries)
        assert "conversation_id" in query_dict
        assert "user" in query_dict
        assert "first_id" in query_dict
        assert "limit" in query_dict
        assert query_dict["conversation_id"] == "conv-123"
        assert query_dict["user"] == "user-123"
        assert query_dict["first_id"] == "msg-123"
        assert query_dict["limit"] == "20"

    def test_get_message_history_request_inheritance(self):
        """Test GetMessageHistoryRequest inherits from BaseRequest."""
        request = GetMessageHistoryRequest()
        assert isinstance(request, BaseRequest)
        assert hasattr(request, "http_method")
        assert hasattr(request, "uri")
        assert hasattr(request, "paths")
        assert hasattr(request, "queries")

    def test_get_message_history_response_inheritance(self):
        """Test GetMessageHistoryResponse inherits from BaseResponse."""
        response = GetMessageHistoryResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_get_message_history_response_fields(self):
        """Test GetMessageHistoryResponse field types."""
        response = GetMessageHistoryResponse()
        response.limit = 20
        response.has_more = True
        response.data = [MessageInfo()]

        assert response.limit == 20
        assert response.has_more is True
        assert isinstance(response.data, list)
        assert len(response.data) == 1
        assert isinstance(response.data[0], MessageInfo)


class TestGetConversationsModels:
    """Test Get Conversations API models."""

    def test_get_conversations_request_builder(self):
        """Test GetConversationsRequest builder pattern."""
        request = (
            GetConversationsRequest.builder()
            .user("user-123")
            .last_id("conv-123")
            .limit(20)
            .sort_by("created_at")
            .build()
        )

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/conversations"
        assert request.user == "user-123"
        assert request.last_id == "conv-123"
        assert request.limit == 20
        assert request.sort_by == "created_at"

        # Check query parameters
        query_dict = dict(request.queries)
        assert "user" in query_dict
        assert "last_id" in query_dict
        assert "limit" in query_dict
        assert "sort_by" in query_dict
        assert query_dict["user"] == "user-123"
        assert query_dict["last_id"] == "conv-123"
        assert query_dict["limit"] == "20"
        assert query_dict["sort_by"] == "created_at"

    def test_get_conversations_request_sort_by_validation(self):
        """Test GetConversationsRequest sort_by field validation."""
        # Test valid sort_by values
        valid_sort_values = ["created_at", "-created_at", "updated_at", "-updated_at"]

        for sort_value in valid_sort_values:
            request = GetConversationsRequest.builder().sort_by(sort_value).build()
            assert request.sort_by == sort_value

    def test_get_conversations_request_inheritance(self):
        """Test GetConversationsRequest inherits from BaseRequest."""
        request = GetConversationsRequest()
        assert isinstance(request, BaseRequest)
        assert hasattr(request, "http_method")
        assert hasattr(request, "uri")
        assert hasattr(request, "paths")
        assert hasattr(request, "queries")

    def test_get_conversations_response_inheritance(self):
        """Test GetConversationsResponse inherits from BaseResponse."""
        response = GetConversationsResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_get_conversations_response_fields(self):
        """Test GetConversationsResponse field types."""
        response = GetConversationsResponse()
        response.limit = 20
        response.has_more = False
        response.data = [ConversationInfo()]

        assert response.limit == 20
        assert response.has_more is False
        assert isinstance(response.data, list)
        assert len(response.data) == 1
        assert isinstance(response.data[0], ConversationInfo)


class TestDeleteConversationModels:
    """Test Delete Conversation API models."""

    def test_delete_conversation_request_builder(self):
        """Test DeleteConversationRequest builder pattern."""
        request_body = DeleteConversationRequestBody.builder().user("user-123").build()
        request = DeleteConversationRequest.builder().conversation_id("conv-123").request_body(request_body).build()

        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/conversations/:conversation_id"
        assert request.conversation_id == "conv-123"
        assert request.request_body is not None
        assert request.request_body.user == "user-123"

        # Check path parameters
        assert "conversation_id" in request.paths
        assert request.paths["conversation_id"] == "conv-123"

        # Check request body
        assert request.body is not None
        assert isinstance(request.body, dict)

    def test_delete_conversation_request_body_builder(self):
        """Test DeleteConversationRequestBody builder pattern."""
        request_body = DeleteConversationRequestBody.builder().user("user-123").build()

        assert request_body.user == "user-123"

    def test_delete_conversation_request_inheritance(self):
        """Test DeleteConversationRequest inherits from BaseRequest."""
        request = DeleteConversationRequest()
        assert isinstance(request, BaseRequest)
        assert hasattr(request, "http_method")
        assert hasattr(request, "uri")
        assert hasattr(request, "paths")
        assert hasattr(request, "queries")

    def test_delete_conversation_response_inheritance(self):
        """Test DeleteConversationResponse inherits from BaseResponse."""
        response = DeleteConversationResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_delete_conversation_response_fields(self):
        """Test DeleteConversationResponse field types."""
        response = DeleteConversationResponse()
        response.result = "success"

        assert response.result == "success"


class TestRenameConversationModels:
    """Test Rename Conversation API models."""

    def test_rename_conversation_request_builder(self):
        """Test RenameConversationRequest builder pattern."""
        request_body = (
            RenameConversationRequestBody.builder().name("New Chat Name").auto_generate(False).user("user-123").build()
        )
        request = RenameConversationRequest.builder().conversation_id("conv-123").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/conversations/:conversation_id/name"
        assert request.conversation_id == "conv-123"
        assert request.request_body is not None
        assert request.request_body.name == "New Chat Name"
        assert request.request_body.auto_generate is False
        assert request.request_body.user == "user-123"

        # Check path parameters
        assert "conversation_id" in request.paths
        assert request.paths["conversation_id"] == "conv-123"

        # Check request body
        assert request.body is not None
        assert isinstance(request.body, dict)

    def test_rename_conversation_request_body_builder(self):
        """Test RenameConversationRequestBody builder pattern."""
        request_body = (
            RenameConversationRequestBody.builder().name("Test Chat").auto_generate(True).user("user-123").build()
        )

        assert request_body.name == "Test Chat"
        assert request_body.auto_generate is True
        assert request_body.user == "user-123"

    def test_rename_conversation_request_body_auto_generate_only(self):
        """Test RenameConversationRequestBody with auto_generate only."""
        request_body = RenameConversationRequestBody.builder().auto_generate(True).user("user-123").build()

        assert request_body.name is None
        assert request_body.auto_generate is True
        assert request_body.user == "user-123"

    def test_rename_conversation_request_inheritance(self):
        """Test RenameConversationRequest inherits from BaseRequest."""
        request = RenameConversationRequest()
        assert isinstance(request, BaseRequest)
        assert hasattr(request, "http_method")
        assert hasattr(request, "uri")
        assert hasattr(request, "paths")
        assert hasattr(request, "queries")

    def test_rename_conversation_response_inheritance(self):
        """Test RenameConversationResponse inherits from BaseResponse."""
        response = RenameConversationResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_rename_conversation_response_fields(self):
        """Test RenameConversationResponse field types."""
        response = RenameConversationResponse()
        response.id = "conv-123"
        response.result = "success"
        response.inputs = {"key": "value"}
        response.status = "normal"
        response.introduction = "Test conversation"
        response.created_at = 1679586595
        response.updated_at = 1679586600

        assert response.id == "conv-123"
        assert response.result == "success"
        assert response.inputs == {"key": "value"}
        assert response.status == "normal"
        assert response.introduction == "Test conversation"
        assert response.created_at == 1679586595
        assert response.updated_at == 1679586600


class TestGetConversationVariablesModels:
    """Test Get Conversation Variables API models."""

    def test_get_conversation_variables_request_builder(self):
        """Test GetConversationVariablesRequest builder pattern."""
        request = (
            GetConversationVariablesRequest.builder()
            .conversation_id("conv-123")
            .user("user-123")
            .last_id("var-123")
            .limit(20)
            .variable_name("test_var")
            .build()
        )

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/conversations/:conversation_id/variables"
        assert request.conversation_id == "conv-123"
        assert request.user == "user-123"
        assert request.last_id == "var-123"
        assert request.limit == 20
        assert request.variable_name == "test_var"

        # Check path parameters
        assert "conversation_id" in request.paths
        assert request.paths["conversation_id"] == "conv-123"

        # Check query parameters
        query_dict = dict(request.queries)
        assert "user" in query_dict
        assert "last_id" in query_dict
        assert "limit" in query_dict
        assert "variable_name" in query_dict
        assert query_dict["user"] == "user-123"
        assert query_dict["last_id"] == "var-123"
        assert query_dict["limit"] == "20"
        assert query_dict["variable_name"] == "test_var"

    def test_get_conversation_variables_request_minimal(self):
        """Test GetConversationVariablesRequest with minimal parameters."""
        request = GetConversationVariablesRequest.builder().conversation_id("conv-123").user("user-123").build()

        assert request.conversation_id == "conv-123"
        assert request.user == "user-123"
        assert request.last_id is None
        assert request.limit is None
        assert request.variable_name is None

    def test_get_conversation_variables_request_inheritance(self):
        """Test GetConversationVariablesRequest inherits from BaseRequest."""
        request = GetConversationVariablesRequest()
        assert isinstance(request, BaseRequest)
        assert hasattr(request, "http_method")
        assert hasattr(request, "uri")
        assert hasattr(request, "paths")
        assert hasattr(request, "queries")

    def test_get_conversation_variables_response_inheritance(self):
        """Test GetConversationVariablesResponse inherits from BaseResponse."""
        response = GetConversationVariablesResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_get_conversation_variables_response_fields(self):
        """Test GetConversationVariablesResponse field types."""
        response = GetConversationVariablesResponse()
        response.limit = 20
        response.has_more = True
        response.data = [ConversationVariable()]

        assert response.limit == 20
        assert response.has_more is True
        assert isinstance(response.data, list)
        assert len(response.data) == 1
        assert isinstance(response.data[0], ConversationVariable)


class TestConversationModelsIntegration:
    """Test integration between conversation models."""

    def test_all_request_models_have_builders(self):
        """Test all request models implement builder patterns."""
        request_models = [
            GetMessageHistoryRequest,
            GetConversationsRequest,
            DeleteConversationRequest,
            RenameConversationRequest,
            GetConversationVariablesRequest,
        ]

        for model_class in request_models:
            assert hasattr(model_class, "builder"), f"{model_class.__name__} should have builder method"
            assert callable(model_class.builder), f"{model_class.__name__}.builder should be callable"

            builder = model_class.builder()
            assert hasattr(builder, "build"), f"{model_class.__name__} builder should have build method"
            assert callable(builder.build), f"{model_class.__name__} builder.build should be callable"

    def test_all_request_body_models_have_builders(self):
        """Test all request body models implement builder patterns."""
        request_body_models = [
            DeleteConversationRequestBody,
            RenameConversationRequestBody,
        ]

        for model_class in request_body_models:
            assert hasattr(model_class, "builder"), f"{model_class.__name__} should have builder method"
            assert callable(model_class.builder), f"{model_class.__name__}.builder should be callable"

            builder = model_class.builder()
            assert hasattr(builder, "build"), f"{model_class.__name__} builder should have build method"
            assert callable(builder.build), f"{model_class.__name__} builder.build should be callable"

    def test_all_response_models_inherit_base_response(self):
        """Test all response models inherit from BaseResponse."""
        response_models = [
            GetMessageHistoryResponse,
            GetConversationsResponse,
            DeleteConversationResponse,
            RenameConversationResponse,
            GetConversationVariablesResponse,
        ]

        for response_class in response_models:
            assert issubclass(response_class, BaseResponse), (
                f"{response_class.__name__} should inherit from BaseResponse"
            )

            instance = response_class()
            assert hasattr(instance, "success"), f"{response_class.__name__} should have success attribute"
            assert hasattr(instance, "code"), f"{response_class.__name__} should have code attribute"
            assert hasattr(instance, "msg"), f"{response_class.__name__} should have msg attribute"
            assert hasattr(instance, "raw"), f"{response_class.__name__} should have raw attribute"

    def test_all_request_models_inherit_base_request(self):
        """Test all request models inherit from BaseRequest."""
        request_models = [
            GetMessageHistoryRequest,
            GetConversationsRequest,
            DeleteConversationRequest,
            RenameConversationRequest,
            GetConversationVariablesRequest,
        ]

        for request_class in request_models:
            assert issubclass(request_class, BaseRequest), f"{request_class.__name__} should inherit from BaseRequest"

            instance = request_class()
            assert hasattr(instance, "http_method"), f"{request_class.__name__} should have http_method attribute"
            assert hasattr(instance, "uri"), f"{request_class.__name__} should have uri attribute"
            assert hasattr(instance, "paths"), f"{request_class.__name__} should have paths attribute"
            assert hasattr(instance, "queries"), f"{request_class.__name__} should have queries attribute"

    def test_http_methods_and_uris_correct(self):
        """Test HTTP methods and URIs are correctly configured."""
        # Test GET requests
        get_message_history = GetMessageHistoryRequest.builder().build()
        assert get_message_history.http_method == HttpMethod.GET
        assert get_message_history.uri == "/v1/messages"

        get_conversations = GetConversationsRequest.builder().build()
        assert get_conversations.http_method == HttpMethod.GET
        assert get_conversations.uri == "/v1/conversations"

        get_variables = GetConversationVariablesRequest.builder().build()
        assert get_variables.http_method == HttpMethod.GET
        assert get_variables.uri == "/v1/conversations/:conversation_id/variables"

        # Test DELETE request
        delete_conversation = DeleteConversationRequest.builder().build()
        assert delete_conversation.http_method == HttpMethod.DELETE
        assert delete_conversation.uri == "/v1/conversations/:conversation_id"

        # Test POST request
        rename_conversation = RenameConversationRequest.builder().build()
        assert rename_conversation.http_method == HttpMethod.POST
        assert rename_conversation.uri == "/v1/conversations/:conversation_id/name"
