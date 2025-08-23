#!/usr/bin/env python3

from io import BytesIO

import pytest

from dify_oapi.api.completion.v1.model.annotation.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.completion.v1.model.annotation.create_annotation_response import CreateAnnotationResponse
from dify_oapi.api.completion.v1.model.audio.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.completion.v1.model.audio.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.api.completion.v1.model.audio.text_to_audio_response import TextToAudioResponse
from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
from dify_oapi.api.completion.v1.model.completion.send_message_response import SendMessageResponse
from dify_oapi.api.completion.v1.model.feedback.message_feedback_request import MessageFeedbackRequest
from dify_oapi.api.completion.v1.model.feedback.message_feedback_request_body import MessageFeedbackRequestBody
from dify_oapi.api.completion.v1.model.feedback.message_feedback_response import MessageFeedbackResponse
from dify_oapi.api.completion.v1.model.file.upload_file_request import UploadFileRequest
from dify_oapi.api.completion.v1.model.file.upload_file_request_body import UploadFileRequestBody
from dify_oapi.api.completion.v1.model.file.upload_file_response import UploadFileResponse
from dify_oapi.api.completion.v1.model.info.get_info_request import GetInfoRequest
from dify_oapi.api.completion.v1.model.info.get_info_response import GetInfoResponse
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


class TestCompletionAPIIntegration:
    """Comprehensive integration tests for all completion APIs"""

    @pytest.fixture
    def client(self) -> Client:
        """Create test client"""
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self) -> RequestOption:
        """Create test request option"""
        return RequestOption.builder().api_key("test-api-key").build()

    def test_request_building(self) -> None:
        """Test that all request models can be built correctly"""
        # Test completion request building
        req_body = SendMessageRequestBody.builder().inputs({}).response_mode("blocking").user("user-123").build()
        req = SendMessageRequest.builder().request_body(req_body).build()

        assert isinstance(req, SendMessageRequest)
        assert req.request_body is not None
        assert req.request_body.response_mode == "blocking"
        assert req.request_body.user == "user-123"

        # Test file upload request building
        file_data = BytesIO(b"fake-image-data")
        file_body = UploadFileRequestBody.builder().user("user-123").build()
        file_req = UploadFileRequest.builder().file(file_data, "test.jpg").request_body(file_body).build()

        assert isinstance(file_req, UploadFileRequest)
        assert file_req.request_body is not None
        assert file_req.request_body.user == "user-123"

        # Test feedback request building
        feedback_body = (
            MessageFeedbackRequestBody.builder().rating("like").user("user-123").content("Great response!").build()
        )
        feedback_req = MessageFeedbackRequest.builder().message_id("msg-123").request_body(feedback_body).build()

        assert isinstance(feedback_req, MessageFeedbackRequest)
        assert feedback_req.message_id == "msg-123"
        assert feedback_req.request_body.rating == "like"

    def test_audio_request_building(self) -> None:
        """Test audio request building"""
        # Test text-to-audio request building
        audio_body = (
            TextToAudioRequestBody.builder()
            .text("[Example] Hello, this is a test audio message.")
            .user("user-123")
            .build()
        )
        audio_req = TextToAudioRequest.builder().request_body(audio_body).build()

        assert isinstance(audio_req, TextToAudioRequest)
        assert audio_req.request_body is not None
        assert audio_req.request_body.text == "[Example] Hello, this is a test audio message."
        assert audio_req.request_body.user == "user-123"

    def test_info_request_building(self) -> None:
        """Test info request building"""
        # Test get info request building
        info_req = GetInfoRequest.builder().build()
        assert isinstance(info_req, GetInfoRequest)

        # Test get parameters request building
        from dify_oapi.api.completion.v1.model.info.get_parameters_request import GetParametersRequest

        params_req = GetParametersRequest.builder().build()
        assert isinstance(params_req, GetParametersRequest)

        # Test get site request building
        from dify_oapi.api.completion.v1.model.info.get_site_request import GetSiteRequest

        site_req = GetSiteRequest.builder().build()
        assert isinstance(site_req, GetSiteRequest)

    def test_annotation_request_building(self) -> None:
        """Test annotation request building"""
        # Test create annotation request building
        create_body = (
            CreateAnnotationRequestBody.builder()
            .question("[Example] What is completion API?")
            .answer("[Example] API for text generation")
            .build()
        )
        create_req = CreateAnnotationRequest.builder().request_body(create_body).build()

        assert isinstance(create_req, CreateAnnotationRequest)
        assert create_req.request_body is not None
        assert create_req.request_body.question == "[Example] What is completion API?"
        assert create_req.request_body.answer == "[Example] API for text generation"

        # Test list annotations request building
        from dify_oapi.api.completion.v1.model.annotation.list_annotations_request import ListAnnotationsRequest

        list_req = ListAnnotationsRequest.builder().page("1").limit("10").build()
        assert isinstance(list_req, ListAnnotationsRequest)

        # Test update annotation request building
        from dify_oapi.api.completion.v1.model.annotation.update_annotation_request import UpdateAnnotationRequest
        from dify_oapi.api.completion.v1.model.annotation.update_annotation_request_body import (
            UpdateAnnotationRequestBody,
        )

        update_body = (
            UpdateAnnotationRequestBody.builder()
            .question("[Example] Updated question")
            .answer("[Example] Updated answer")
            .build()
        )
        update_req = UpdateAnnotationRequest.builder().annotation_id("annotation-123").request_body(update_body).build()

        assert isinstance(update_req, UpdateAnnotationRequest)
        assert update_req.annotation_id == "annotation-123"
        assert update_req.request_body.question == "[Example] Updated question"

        # Test delete annotation request building
        from dify_oapi.api.completion.v1.model.annotation.delete_annotation_request import DeleteAnnotationRequest

        delete_req = DeleteAnnotationRequest.builder().annotation_id("annotation-123").build()

        assert isinstance(delete_req, DeleteAnnotationRequest)
        assert delete_req.annotation_id == "annotation-123"

    def test_annotation_reply_settings_request_building(self) -> None:
        """Test annotation reply settings request building"""
        from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_request import (
            AnnotationReplySettingsRequest,
        )
        from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_request_body import (
            AnnotationReplySettingsRequestBody,
        )

        # Test annotation reply settings request building
        settings_body = (
            AnnotationReplySettingsRequestBody.builder()
            .embedding_provider_name("openai")
            .embedding_model_name("text-embedding-ada-002")
            .score_threshold(0.8)
            .build()
        )
        settings_req = AnnotationReplySettingsRequest.builder().action("enable").request_body(settings_body).build()

        assert isinstance(settings_req, AnnotationReplySettingsRequest)
        assert settings_req.action == "enable"
        assert settings_req.request_body is not None
        assert settings_req.request_body.embedding_provider_name == "openai"
        assert settings_req.request_body.score_threshold == 0.8

        # Test query annotation reply status request building
        from dify_oapi.api.completion.v1.model.annotation.query_annotation_reply_status_request import (
            QueryAnnotationReplyStatusRequest,
        )

        query_req = QueryAnnotationReplyStatusRequest.builder().action("enable").job_id("job-123").build()

        assert isinstance(query_req, QueryAnnotationReplyStatusRequest)
        assert query_req.action == "enable"
        assert query_req.job_id == "job-123"

    def test_stop_response_request_building(self) -> None:
        """Test stop response request building"""
        from dify_oapi.api.completion.v1.model.completion.stop_response_request import StopResponseRequest
        from dify_oapi.api.completion.v1.model.completion.stop_response_request_body import StopResponseRequestBody

        # Test stop response request building
        stop_body = StopResponseRequestBody.builder().user("user-123").build()
        stop_req = StopResponseRequest.builder().task_id("task-123").request_body(stop_body).build()

        assert isinstance(stop_req, StopResponseRequest)
        assert stop_req.task_id == "task-123"
        assert stop_req.request_body is not None
        assert stop_req.request_body.user == "user-123"

    def test_all_resources_accessible(self, client: Client) -> None:
        """Test that all completion resources are accessible"""
        # Verify all resources are properly initialized
        assert hasattr(client.completion.v1, "completion")
        assert hasattr(client.completion.v1, "file")
        assert hasattr(client.completion.v1, "feedback")
        assert hasattr(client.completion.v1, "audio")
        assert hasattr(client.completion.v1, "info")
        assert hasattr(client.completion.v1, "annotation")

        # Verify all resources have expected methods
        completion_methods = ["send_message", "asend_message", "stop_response", "astop_response"]
        for method in completion_methods:
            assert hasattr(client.completion.v1.completion, method)

        file_methods = ["upload_file", "aupload_file"]
        for method in file_methods:
            assert hasattr(client.completion.v1.file, method)

        feedback_methods = ["message_feedback", "amessage_feedback", "get_feedbacks", "aget_feedbacks"]
        for method in feedback_methods:
            assert hasattr(client.completion.v1.feedback, method)

        audio_methods = ["text_to_audio", "atext_to_audio"]
        for method in audio_methods:
            assert hasattr(client.completion.v1.audio, method)

        info_methods = ["get_info", "aget_info", "get_parameters", "aget_parameters", "get_site", "aget_site"]
        for method in info_methods:
            assert hasattr(client.completion.v1.info, method)

        annotation_methods = [
            "list_annotations",
            "alist_annotations",
            "create_annotation",
            "acreate_annotation",
            "update_annotation",
            "aupdate_annotation",
            "delete_annotation",
            "adelete_annotation",
            "annotation_reply_settings",
            "aannotation_reply_settings",
            "query_annotation_reply_status",
            "aquery_annotation_reply_status",
        ]
        for method in annotation_methods:
            assert hasattr(client.completion.v1.annotation, method)

    def test_feedback_request_building(self) -> None:
        """Test feedback request building"""
        # Test get feedbacks request building
        from dify_oapi.api.completion.v1.model.feedback.get_feedbacks_request import GetFeedbacksRequest

        feedbacks_req = GetFeedbacksRequest.builder().page("1").limit("20").build()

        assert isinstance(feedbacks_req, GetFeedbacksRequest)

        # Test message feedback request building
        feedback_body = (
            MessageFeedbackRequestBody.builder().rating("like").user("user-123").content("Great response!").build()
        )
        feedback_req = MessageFeedbackRequest.builder().message_id("msg-123").request_body(feedback_body).build()

        assert isinstance(feedback_req, MessageFeedbackRequest)
        assert feedback_req.message_id == "msg-123"
        assert feedback_req.request_body.rating == "like"
        assert feedback_req.request_body.user == "user-123"
        assert feedback_req.request_body.content == "Great response!"

    def test_response_inheritance(self) -> None:
        """Test that all response classes inherit from BaseResponse"""
        from dify_oapi.core.model.base_response import BaseResponse

        # Test response inheritance
        send_response = SendMessageResponse()
        assert isinstance(send_response, BaseResponse)
        assert hasattr(send_response, "success")
        assert hasattr(send_response, "code")
        assert hasattr(send_response, "msg")

        upload_response = UploadFileResponse()
        assert isinstance(upload_response, BaseResponse)

        feedback_response = MessageFeedbackResponse()
        assert isinstance(feedback_response, BaseResponse)

        audio_response = TextToAudioResponse()
        assert isinstance(audio_response, BaseResponse)

        info_response = GetInfoResponse()
        assert isinstance(info_response, BaseResponse)

        annotation_response = CreateAnnotationResponse()
        assert isinstance(annotation_response, BaseResponse)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
