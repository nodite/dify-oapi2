"""Tests for Annotation Management API models."""

from dify_oapi.api.chat.v1.model.annotation_info import AnnotationInfo
from dify_oapi.api.chat.v1.model.chat_types import AnnotationAction, JobStatus
from dify_oapi.api.chat.v1.model.configure_annotation_reply_request import (
    ConfigureAnnotationReplyRequest,
)
from dify_oapi.api.chat.v1.model.configure_annotation_reply_request_body import (
    ConfigureAnnotationReplyRequestBody,
)
from dify_oapi.api.chat.v1.model.configure_annotation_reply_response import (
    ConfigureAnnotationReplyResponse,
)
from dify_oapi.api.chat.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chat.v1.model.create_annotation_request_body import (
    CreateAnnotationRequestBody,
)
from dify_oapi.api.chat.v1.model.create_annotation_response import CreateAnnotationResponse
from dify_oapi.api.chat.v1.model.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.chat.v1.model.delete_annotation_response import DeleteAnnotationResponse
from dify_oapi.api.chat.v1.model.get_annotation_reply_status_request import (
    GetAnnotationReplyStatusRequest,
)
from dify_oapi.api.chat.v1.model.get_annotation_reply_status_response import (
    GetAnnotationReplyStatusResponse,
)
from dify_oapi.api.chat.v1.model.list_annotations_request import ListAnnotationsRequest
from dify_oapi.api.chat.v1.model.list_annotations_response import ListAnnotationsResponse
from dify_oapi.api.chat.v1.model.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.chat.v1.model.update_annotation_request_body import (
    UpdateAnnotationRequestBody,
)
from dify_oapi.api.chat.v1.model.update_annotation_response import UpdateAnnotationResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest
from dify_oapi.core.model.base_response import BaseResponse


class TestListAnnotationsModels:
    """Test list annotations models."""

    def test_list_annotations_request_builder(self):
        """Test ListAnnotationsRequest builder pattern."""
        request = ListAnnotationsRequest.builder().page(1).limit(20).build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/apps/annotations"
        assert ("page", "1") in request.queries
        assert ("limit", "20") in request.queries

    def test_list_annotations_request_optional_params(self):
        """Test ListAnnotationsRequest with optional parameters."""
        request = ListAnnotationsRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/apps/annotations"
        assert len(request.queries) == 0

    def test_list_annotations_response_inheritance(self):
        """Test ListAnnotationsResponse inherits from BaseResponse."""
        response = ListAnnotationsResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_list_annotations_response_fields(self):
        """Test ListAnnotationsResponse fields."""
        response = ListAnnotationsResponse()
        assert response.data == []
        assert response.has_more is False
        assert response.limit == 20
        assert response.total == 0
        assert response.page == 1


class TestCreateAnnotationModels:
    """Test create annotation models."""

    def test_create_annotation_request_body_builder(self):
        """Test CreateAnnotationRequestBody builder pattern."""
        request_body = (
            CreateAnnotationRequestBody.builder()
            .question("What is AI?")
            .answer("Artificial Intelligence is...")
            .build()
        )

        assert request_body.question == "What is AI?"
        assert request_body.answer == "Artificial Intelligence is..."

    def test_create_annotation_request_builder(self):
        """Test CreateAnnotationRequest builder pattern."""
        request_body = CreateAnnotationRequestBody.builder().question("Test").answer("Test answer").build()
        request = CreateAnnotationRequest.builder().request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/apps/annotations"
        assert request.request_body is not None
        assert request.request_body.question == "Test"

    def test_create_annotation_response_inheritance(self):
        """Test CreateAnnotationResponse inherits from BaseResponse and AnnotationInfo."""
        response = CreateAnnotationResponse()
        assert isinstance(response, BaseResponse)
        assert isinstance(response, AnnotationInfo)
        assert hasattr(response, "success")
        assert hasattr(response, "id")
        assert hasattr(response, "question")


class TestUpdateAnnotationModels:
    """Test update annotation models."""

    def test_update_annotation_request_body_builder(self):
        """Test UpdateAnnotationRequestBody builder pattern."""
        request_body = (
            UpdateAnnotationRequestBody.builder().question("Updated question").answer("Updated answer").build()
        )

        assert request_body.question == "Updated question"
        assert request_body.answer == "Updated answer"

    def test_update_annotation_request_builder(self):
        """Test UpdateAnnotationRequest builder pattern."""
        request_body = UpdateAnnotationRequestBody.builder().question("Test").answer("Test answer").build()
        request = UpdateAnnotationRequest.builder().annotation_id("annotation-123").request_body(request_body).build()

        assert request.http_method == HttpMethod.PUT
        assert request.uri == "/v1/apps/annotations/:annotation_id"
        assert request.paths["annotation_id"] == "annotation-123"
        assert request.request_body is not None

    def test_update_annotation_response_inheritance(self):
        """Test UpdateAnnotationResponse inherits from BaseResponse and AnnotationInfo."""
        response = UpdateAnnotationResponse()
        assert isinstance(response, BaseResponse)
        assert isinstance(response, AnnotationInfo)


class TestDeleteAnnotationModels:
    """Test delete annotation models."""

    def test_delete_annotation_request_builder(self):
        """Test DeleteAnnotationRequest builder pattern."""
        request = DeleteAnnotationRequest.builder().annotation_id("annotation-123").build()

        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/apps/annotations/:annotation_id"
        assert request.paths["annotation_id"] == "annotation-123"

    def test_delete_annotation_response_inheritance(self):
        """Test DeleteAnnotationResponse inherits from BaseResponse."""
        response = DeleteAnnotationResponse()
        assert isinstance(response, BaseResponse)


class TestConfigureAnnotationReplyModels:
    """Test configure annotation reply models."""

    def test_configure_annotation_reply_request_body_builder(self):
        """Test ConfigureAnnotationReplyRequestBody builder pattern."""
        request_body = (
            ConfigureAnnotationReplyRequestBody.builder()
            .embedding_provider_name("openai")
            .embedding_model_name("text-embedding-ada-002")
            .score_threshold(0.8)
            .build()
        )

        assert request_body.embedding_provider_name == "openai"
        assert request_body.embedding_model_name == "text-embedding-ada-002"
        assert request_body.score_threshold == 0.8

    def test_configure_annotation_reply_request_body_optional_fields(self):
        """Test ConfigureAnnotationReplyRequestBody with optional fields."""
        request_body = ConfigureAnnotationReplyRequestBody.builder().score_threshold(0.5).build()

        assert request_body.embedding_provider_name is None
        assert request_body.embedding_model_name is None
        assert request_body.score_threshold == 0.5

    def test_configure_annotation_reply_request_builder(self):
        """Test ConfigureAnnotationReplyRequest builder pattern."""
        request_body = ConfigureAnnotationReplyRequestBody.builder().score_threshold(0.8).build()
        request = ConfigureAnnotationReplyRequest.builder().action("enable").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/apps/annotation-reply/:action"
        assert request.paths["action"] == "enable"
        assert request.request_body is not None

    def test_configure_annotation_reply_response_inheritance(self):
        """Test ConfigureAnnotationReplyResponse inherits from BaseResponse."""
        response = ConfigureAnnotationReplyResponse()
        assert isinstance(response, BaseResponse)
        assert response.job_id is None
        assert response.job_status is None


class TestGetAnnotationReplyStatusModels:
    """Test get annotation reply status models."""

    def test_get_annotation_reply_status_request_builder(self):
        """Test GetAnnotationReplyStatusRequest builder pattern."""
        request = GetAnnotationReplyStatusRequest.builder().action("enable").job_id("job-123").build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/apps/annotation-reply/:action/status/:job_id"
        assert request.paths["action"] == "enable"
        assert request.paths["job_id"] == "job-123"

    def test_get_annotation_reply_status_response_inheritance(self):
        """Test GetAnnotationReplyStatusResponse inherits from BaseResponse."""
        response = GetAnnotationReplyStatusResponse()
        assert isinstance(response, BaseResponse)
        assert response.job_id is None
        assert response.job_status is None
        assert response.error_msg is None


class TestAnnotationTypesValidation:
    """Test annotation types validation."""

    def test_annotation_action_types(self):
        """Test AnnotationAction literal types."""
        # Test valid values
        assert "enable" in AnnotationAction.__args__
        assert "disable" in AnnotationAction.__args__

    def test_job_status_types(self):
        """Test JobStatus literal types."""
        # Test valid values
        assert "waiting" in JobStatus.__args__
        assert "running" in JobStatus.__args__
        assert "completed" in JobStatus.__args__
        assert "failed" in JobStatus.__args__

    def test_annotation_action_validation(self):
        """Test annotation action validation in requests."""
        request = ConfigureAnnotationReplyRequest.builder().action("enable").build()
        assert request.paths["action"] == "enable"

        request = ConfigureAnnotationReplyRequest.builder().action("disable").build()
        assert request.paths["action"] == "disable"


class TestAnnotationModelIntegration:
    """Test annotation model integration."""

    def test_all_request_models_inherit_base_request(self):
        """Test all annotation request models inherit from BaseRequest."""
        request_classes = [
            ListAnnotationsRequest,
            CreateAnnotationRequest,
            UpdateAnnotationRequest,
            DeleteAnnotationRequest,
            ConfigureAnnotationReplyRequest,
            GetAnnotationReplyStatusRequest,
        ]

        for request_class in request_classes:
            instance = request_class()
            assert isinstance(instance, BaseRequest)
            assert hasattr(instance, "http_method")
            assert hasattr(instance, "uri")

    def test_all_response_models_inherit_base_response(self):
        """Test all annotation response models inherit from BaseResponse."""
        response_classes = [
            ListAnnotationsResponse,
            CreateAnnotationResponse,
            UpdateAnnotationResponse,
            DeleteAnnotationResponse,
            ConfigureAnnotationReplyResponse,
            GetAnnotationReplyStatusResponse,
        ]

        for response_class in response_classes:
            instance = response_class()
            assert isinstance(instance, BaseResponse)
            assert hasattr(instance, "success")
            assert hasattr(instance, "code")
            assert hasattr(instance, "msg")

    def test_builder_patterns_implemented(self):
        """Test all models implement builder patterns correctly."""
        # Test request models
        assert hasattr(ListAnnotationsRequest, "builder")
        assert hasattr(CreateAnnotationRequest, "builder")
        assert hasattr(UpdateAnnotationRequest, "builder")
        assert hasattr(DeleteAnnotationRequest, "builder")
        assert hasattr(ConfigureAnnotationReplyRequest, "builder")
        assert hasattr(GetAnnotationReplyStatusRequest, "builder")

        # Test request body models
        assert hasattr(CreateAnnotationRequestBody, "builder")
        assert hasattr(UpdateAnnotationRequestBody, "builder")
        assert hasattr(ConfigureAnnotationReplyRequestBody, "builder")

        # Test builders are callable
        assert callable(ListAnnotationsRequest.builder)
        assert callable(CreateAnnotationRequestBody.builder)
