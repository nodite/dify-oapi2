"""Tests for Annotation API models."""

from dify_oapi.api.chatflow.v1.model.annotation_info import AnnotationInfo
from dify_oapi.api.chatflow.v1.model.annotation_reply_settings_request import AnnotationReplySettingsRequest
from dify_oapi.api.chatflow.v1.model.annotation_reply_settings_request_body import AnnotationReplySettingsRequestBody
from dify_oapi.api.chatflow.v1.model.annotation_reply_settings_response import AnnotationReplySettingsResponse
from dify_oapi.api.chatflow.v1.model.annotation_reply_status_request import AnnotationReplyStatusRequest
from dify_oapi.api.chatflow.v1.model.annotation_reply_status_response import AnnotationReplyStatusResponse
from dify_oapi.api.chatflow.v1.model.chatflow_types import AnnotationAction, JobStatus
from dify_oapi.api.chatflow.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chatflow.v1.model.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.chatflow.v1.model.create_annotation_response import CreateAnnotationResponse
from dify_oapi.api.chatflow.v1.model.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.chatflow.v1.model.delete_annotation_response import DeleteAnnotationResponse
from dify_oapi.api.chatflow.v1.model.get_annotations_request import GetAnnotationsRequest
from dify_oapi.api.chatflow.v1.model.get_annotations_response import GetAnnotationsResponse
from dify_oapi.api.chatflow.v1.model.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.chatflow.v1.model.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.api.chatflow.v1.model.update_annotation_response import UpdateAnnotationResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestGetAnnotationsModels:
    """Test GetAnnotations API models."""

    def test_request_builder(self):
        """Test GetAnnotationsRequest builder pattern."""
        request = GetAnnotationsRequest.builder().page(1).limit(20).build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/apps/annotations"
        assert "page" in request.query
        assert request.query["page"] == 1
        assert "limit" in request.query
        assert request.query["limit"] == 20

    def test_request_validation(self):
        """Test GetAnnotationsRequest validation."""
        request = GetAnnotationsRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/apps/annotations"
        # Page and limit are optional

    def test_response_inheritance(self):
        """Test GetAnnotationsResponse inherits from BaseResponse."""
        response = GetAnnotationsResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self):
        """Test GetAnnotationsResponse data access."""
        annotation = AnnotationInfo.builder().id("test-id").question("Test?").answer("Test answer").build()
        response = GetAnnotationsResponse()
        response.data = [annotation]
        response.has_more = False
        response.limit = 20
        response.total = 1
        response.page = 1

        assert len(response.data) == 1
        assert response.data[0].id == "test-id"
        assert response.has_more is False
        assert response.limit == 20
        assert response.total == 1
        assert response.page == 1


class TestCreateAnnotationModels:
    """Test CreateAnnotation API models."""

    def test_request_builder(self):
        """Test CreateAnnotationRequest builder pattern."""
        request_body = (
            CreateAnnotationRequestBody.builder()
            .question("What is AI?")
            .answer("AI is artificial intelligence")
            .build()
        )

        request = CreateAnnotationRequest.builder().request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/apps/annotations"
        assert request.request_body is not None
        assert request.body is not None

    def test_request_body_builder(self):
        """Test CreateAnnotationRequestBody builder pattern."""
        request_body = (
            CreateAnnotationRequestBody.builder()
            .question("What is AI?")
            .answer("AI is artificial intelligence")
            .build()
        )

        assert request_body.question == "What is AI?"
        assert request_body.answer == "AI is artificial intelligence"

    def test_request_body_validation(self):
        """Test CreateAnnotationRequestBody validation."""
        request_body = CreateAnnotationRequestBody()

        # Both fields are optional in the model but required by API
        assert request_body.question is None
        assert request_body.answer is None

    def test_response_inheritance(self):
        """Test CreateAnnotationResponse inherits from BaseResponse."""
        response = CreateAnnotationResponse()

        assert isinstance(response, BaseResponse)
        assert isinstance(response, AnnotationInfo)
        assert hasattr(response, "success")
        assert hasattr(response, "id")
        assert hasattr(response, "question")
        assert hasattr(response, "answer")


class TestUpdateAnnotationModels:
    """Test UpdateAnnotation API models."""

    def test_request_builder(self):
        """Test UpdateAnnotationRequest builder pattern."""
        request_body = (
            UpdateAnnotationRequestBody.builder().question("Updated question?").answer("Updated answer").build()
        )

        request = (
            UpdateAnnotationRequest.builder().annotation_id("test-annotation-id").request_body(request_body).build()
        )

        assert request.http_method == HttpMethod.PUT
        assert request.uri == "/v1/apps/annotations/:annotation_id"
        assert request.annotation_id == "test-annotation-id"
        assert request.paths["annotation_id"] == "test-annotation-id"
        assert request.request_body is not None
        assert request.body is not None

    def test_request_body_builder(self):
        """Test UpdateAnnotationRequestBody builder pattern."""
        request_body = (
            UpdateAnnotationRequestBody.builder().question("Updated question?").answer("Updated answer").build()
        )

        assert request_body.question == "Updated question?"
        assert request_body.answer == "Updated answer"

    def test_response_inheritance(self):
        """Test UpdateAnnotationResponse inherits from BaseResponse."""
        response = UpdateAnnotationResponse()

        assert isinstance(response, BaseResponse)
        assert isinstance(response, AnnotationInfo)
        assert hasattr(response, "success")
        assert hasattr(response, "id")
        assert hasattr(response, "question")
        assert hasattr(response, "answer")


class TestDeleteAnnotationModels:
    """Test DeleteAnnotation API models."""

    def test_request_builder(self):
        """Test DeleteAnnotationRequest builder pattern."""
        request = DeleteAnnotationRequest.builder().annotation_id("test-annotation-id").build()

        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/apps/annotations/:annotation_id"
        assert request.annotation_id == "test-annotation-id"
        assert request.paths["annotation_id"] == "test-annotation-id"

    def test_response_inheritance(self):
        """Test DeleteAnnotationResponse inherits from BaseResponse."""
        response = DeleteAnnotationResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")


class TestAnnotationReplySettingsModels:
    """Test AnnotationReplySettings API models."""

    def test_request_builder(self):
        """Test AnnotationReplySettingsRequest builder pattern."""
        request_body = (
            AnnotationReplySettingsRequestBody.builder()
            .embedding_provider_name("openai")
            .embedding_model_name("text-embedding-ada-002")
            .score_threshold(0.8)
            .build()
        )

        request = AnnotationReplySettingsRequest.builder().action("enable").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/apps/annotation-reply/:action"
        assert request.action == "enable"
        assert request.paths["action"] == "enable"
        assert request.request_body is not None
        assert request.body is not None

    def test_request_body_builder(self):
        """Test AnnotationReplySettingsRequestBody builder pattern."""
        request_body = (
            AnnotationReplySettingsRequestBody.builder()
            .embedding_provider_name("openai")
            .embedding_model_name("text-embedding-ada-002")
            .score_threshold(0.8)
            .build()
        )

        assert request_body.embedding_provider_name == "openai"
        assert request_body.embedding_model_name == "text-embedding-ada-002"
        assert request_body.score_threshold == 0.8

    def test_action_validation(self):
        """Test AnnotationAction type validation."""
        # Test valid actions
        valid_actions: list[AnnotationAction] = ["enable", "disable"]
        for action in valid_actions:
            request = AnnotationReplySettingsRequest.builder().action(action).build()
            assert request.action == action

    def test_response_inheritance(self):
        """Test AnnotationReplySettingsResponse inherits from BaseResponse."""
        response = AnnotationReplySettingsResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "job_id")
        assert hasattr(response, "job_status")

    def test_job_status_validation(self):
        """Test JobStatus type validation."""
        response = AnnotationReplySettingsResponse()

        # Test valid job statuses
        valid_statuses: list[JobStatus] = ["waiting", "running", "completed", "failed"]
        for status in valid_statuses:
            response.job_status = status
            assert response.job_status == status


class TestAnnotationReplyStatusModels:
    """Test AnnotationReplyStatus API models."""

    def test_request_builder(self):
        """Test AnnotationReplyStatusRequest builder pattern."""
        request = AnnotationReplyStatusRequest.builder().action("enable").job_id("test-job-id").build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/apps/annotation-reply/:action/status/:job_id"
        assert request.action == "enable"
        assert request.job_id == "test-job-id"
        assert request.paths["action"] == "enable"
        assert request.paths["job_id"] == "test-job-id"

    def test_path_parameters(self):
        """Test path parameter handling."""
        request = AnnotationReplyStatusRequest.builder().action("disable").job_id("another-job-id").build()

        assert request.paths["action"] == "disable"
        assert request.paths["job_id"] == "another-job-id"

    def test_response_inheritance(self):
        """Test AnnotationReplyStatusResponse inherits from BaseResponse."""
        response = AnnotationReplyStatusResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "job_id")
        assert hasattr(response, "job_status")
        assert hasattr(response, "error_msg")

    def test_response_data_access(self):
        """Test AnnotationReplyStatusResponse data access."""
        response = AnnotationReplyStatusResponse()
        response.job_id = "test-job-id"
        response.job_status = "completed"
        response.error_msg = None

        assert response.job_id == "test-job-id"
        assert response.job_status == "completed"
        assert response.error_msg is None

    def test_error_response_data(self):
        """Test AnnotationReplyStatusResponse with error."""
        response = AnnotationReplyStatusResponse()
        response.job_id = "failed-job-id"
        response.job_status = "failed"
        response.error_msg = "Processing failed"

        assert response.job_id == "failed-job-id"
        assert response.job_status == "failed"
        assert response.error_msg == "Processing failed"
