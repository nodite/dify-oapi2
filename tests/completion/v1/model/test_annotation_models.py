from __future__ import annotations

from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_request import (
    AnnotationReplySettingsRequest,
)
from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_request_body import (
    AnnotationReplySettingsRequestBody,
)
from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_response import (
    AnnotationReplySettingsResponse,
)
from dify_oapi.api.completion.v1.model.annotation.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.completion.v1.model.annotation.create_annotation_response import CreateAnnotationResponse
from dify_oapi.api.completion.v1.model.annotation.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.delete_annotation_response import DeleteAnnotationResponse
from dify_oapi.api.completion.v1.model.annotation.list_annotations_request import ListAnnotationsRequest
from dify_oapi.api.completion.v1.model.annotation.list_annotations_response import ListAnnotationsResponse
from dify_oapi.api.completion.v1.model.annotation.query_annotation_reply_status_request import (
    QueryAnnotationReplyStatusRequest,
)
from dify_oapi.api.completion.v1.model.annotation.query_annotation_reply_status_response import (
    QueryAnnotationReplyStatusResponse,
)
from dify_oapi.api.completion.v1.model.annotation.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.api.completion.v1.model.annotation.update_annotation_response import UpdateAnnotationResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestListAnnotationsModels:
    """Test ListAnnotations API models."""

    def test_request_builder(self) -> None:
        """Test ListAnnotationsRequest builder pattern."""
        request = ListAnnotationsRequest.builder().page("1").limit("20").build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/apps/annotations"
        assert ("page", "1") in request.queries
        assert ("limit", "20") in request.queries

    def test_request_validation(self) -> None:
        """Test ListAnnotationsRequest validation."""
        request = ListAnnotationsRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert len(request.queries) == 0

    def test_response_inheritance(self) -> None:
        """Test ListAnnotationsResponse inherits from BaseResponse."""
        response = ListAnnotationsResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")


class TestCreateAnnotationModels:
    """Test CreateAnnotation API models."""

    def test_request_builder(self) -> None:
        """Test CreateAnnotationRequest builder pattern."""
        request_body = CreateAnnotationRequestBody.builder().question("What is AI?").answer("AI is...").build()

        request = CreateAnnotationRequest.builder().request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/apps/annotations"
        assert request.request_body == request_body

    def test_request_body_builder(self) -> None:
        """Test CreateAnnotationRequestBody builder pattern."""
        request_body = (
            CreateAnnotationRequestBody.builder()
            .question("What is machine learning?")
            .answer("Machine learning is a subset of AI")
            .build()
        )

        assert request_body.question == "What is machine learning?"
        assert request_body.answer == "Machine learning is a subset of AI"

    def test_response_inheritance(self) -> None:
        """Test CreateAnnotationResponse inherits from BaseResponse."""
        response = CreateAnnotationResponse()

        assert isinstance(response, BaseResponse)


class TestUpdateAnnotationModels:
    """Test UpdateAnnotation API models."""

    def test_request_builder(self) -> None:
        """Test UpdateAnnotationRequest builder pattern."""
        request_body = UpdateAnnotationRequestBody.builder().question("Updated question").build()

        request = UpdateAnnotationRequest.builder().annotation_id("ann-123").request_body(request_body).build()

        assert request.http_method == HttpMethod.PUT
        assert request.uri == "/v1/apps/annotations/:annotation_id"
        assert request.annotation_id == "ann-123"
        assert request.paths["annotation_id"] == "ann-123"

    def test_request_body_builder(self) -> None:
        """Test UpdateAnnotationRequestBody builder pattern."""
        request_body = UpdateAnnotationRequestBody.builder().answer("Updated answer").build()

        assert request_body.answer == "Updated answer"

    def test_response_inheritance(self) -> None:
        """Test UpdateAnnotationResponse inherits from BaseResponse."""
        response = UpdateAnnotationResponse()

        assert isinstance(response, BaseResponse)


class TestDeleteAnnotationModels:
    """Test DeleteAnnotation API models."""

    def test_request_builder(self) -> None:
        """Test DeleteAnnotationRequest builder pattern."""
        request = DeleteAnnotationRequest.builder().annotation_id("ann-456").build()

        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/apps/annotations/:annotation_id"
        assert request.annotation_id == "ann-456"
        assert request.paths["annotation_id"] == "ann-456"

    def test_response_inheritance(self) -> None:
        """Test DeleteAnnotationResponse inherits from BaseResponse."""
        response = DeleteAnnotationResponse()

        assert isinstance(response, BaseResponse)


class TestAnnotationReplySettingsModels:
    """Test AnnotationReplySettings API models."""

    def test_request_builder(self) -> None:
        """Test AnnotationReplySettingsRequest builder pattern."""
        request_body = AnnotationReplySettingsRequestBody.builder().build()

        request = AnnotationReplySettingsRequest.builder().action("enable").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/apps/annotation-reply/:action"
        assert request.request_body == request_body
        assert request.action == "enable"

    def test_request_body_builder(self) -> None:
        """Test AnnotationReplySettingsRequestBody builder pattern."""
        request_body = AnnotationReplySettingsRequestBody.builder().build()

        assert request_body is not None

    def test_response_inheritance(self) -> None:
        """Test AnnotationReplySettingsResponse inherits from BaseResponse."""
        response = AnnotationReplySettingsResponse()

        assert isinstance(response, BaseResponse)


class TestQueryAnnotationReplyStatusModels:
    """Test QueryAnnotationReplyStatus API models."""

    def test_request_builder(self) -> None:
        """Test QueryAnnotationReplyStatusRequest builder pattern."""
        request = QueryAnnotationReplyStatusRequest.builder().action("enable").job_id("job-123").build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/apps/annotation-reply/:action/status/:job_id"
        assert request.action == "enable"
        assert request.job_id == "job-123"

    def test_response_inheritance(self) -> None:
        """Test QueryAnnotationReplyStatusResponse inherits from BaseResponse."""
        response = QueryAnnotationReplyStatusResponse()

        assert isinstance(response, BaseResponse)
