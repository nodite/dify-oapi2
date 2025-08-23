from __future__ import annotations

from unittest.mock import AsyncMock, Mock, patch

import pytest

from dify_oapi.api.completion.v1.model.feedback.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.api.completion.v1.model.feedback.get_feedbacks_response import GetFeedbacksResponse
from dify_oapi.api.completion.v1.model.feedback.message_feedback_request import MessageFeedbackRequest
from dify_oapi.api.completion.v1.model.feedback.message_feedback_request_body import MessageFeedbackRequestBody
from dify_oapi.api.completion.v1.model.feedback.message_feedback_response import MessageFeedbackResponse
from dify_oapi.api.completion.v1.resource.feedback import Feedback
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestFeedbackResource:
    @pytest.fixture
    def config(self) -> Config:
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def feedback_resource(self, config: Config) -> Feedback:
        return Feedback(config)

    @pytest.fixture
    def message_feedback_request(self) -> MessageFeedbackRequest:
        request_body = (
            MessageFeedbackRequestBody.builder()
            .rating("like")
            .user("test-user")
            .content("Great response!")
            .build()
        )
        return (
            MessageFeedbackRequest.builder()
            .message_id("test-message-id")
            .request_body(request_body)
            .build()
        )

    @pytest.fixture
    def get_feedbacks_request(self) -> GetFeedbacksRequest:
        return (
            GetFeedbacksRequest.builder()
            .page("1")
            .limit("20")
            .build()
        )

    def test_message_feedback_sync(
        self, feedback_resource: Feedback, message_feedback_request: MessageFeedbackRequest, request_option: RequestOption
    ) -> None:
        mock_response = MessageFeedbackResponse(result="success")
        
        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = feedback_resource.message_feedback(message_feedback_request, request_option)
            
            assert response == mock_response
            mock_execute.assert_called_once_with(
                feedback_resource.config,
                message_feedback_request,
                unmarshal_as=MessageFeedbackResponse,
                option=request_option
            )

    @pytest.mark.asyncio
    async def test_message_feedback_async(
        self, feedback_resource: Feedback, message_feedback_request: MessageFeedbackRequest, request_option: RequestOption
    ) -> None:
        mock_response = MessageFeedbackResponse(result="success")
        
        with patch("dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response) as mock_aexecute:
            response = await feedback_resource.amessage_feedback(message_feedback_request, request_option)
            
            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                feedback_resource.config,
                message_feedback_request,
                unmarshal_as=MessageFeedbackResponse,
                option=request_option
            )

    def test_get_feedbacks_sync(
        self, feedback_resource: Feedback, get_feedbacks_request: GetFeedbacksRequest, request_option: RequestOption
    ) -> None:
        mock_response = GetFeedbacksResponse(data=[])
        
        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = feedback_resource.get_feedbacks(get_feedbacks_request, request_option)
            
            assert response == mock_response
            mock_execute.assert_called_once_with(
                feedback_resource.config,
                get_feedbacks_request,
                unmarshal_as=GetFeedbacksResponse,
                option=request_option
            )

    @pytest.mark.asyncio
    async def test_get_feedbacks_async(
        self, feedback_resource: Feedback, get_feedbacks_request: GetFeedbacksRequest, request_option: RequestOption
    ) -> None:
        mock_response = GetFeedbacksResponse(data=[])
        
        with patch("dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response) as mock_aexecute:
            response = await feedback_resource.aget_feedbacks(get_feedbacks_request, request_option)
            
            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                feedback_resource.config,
                get_feedbacks_request,
                unmarshal_as=GetFeedbacksResponse,
                option=request_option
            )

    def test_message_feedback_error_handling(
        self, feedback_resource: Feedback, message_feedback_request: MessageFeedbackRequest, request_option: RequestOption
    ) -> None:
        with patch("dify_oapi.core.http.transport.Transport.execute", side_effect=Exception("API Error")) as mock_execute:
            with pytest.raises(Exception, match="API Error"):
                feedback_resource.message_feedback(message_feedback_request, request_option)

    @pytest.mark.asyncio
    async def test_message_feedback_async_error_handling(
        self, feedback_resource: Feedback, message_feedback_request: MessageFeedbackRequest, request_option: RequestOption
    ) -> None:
        with patch("dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, side_effect=Exception("API Error")) as mock_aexecute:
            with pytest.raises(Exception, match="API Error"):
                await feedback_resource.amessage_feedback(message_feedback_request, request_option)

    def test_get_feedbacks_error_handling(
        self, feedback_resource: Feedback, get_feedbacks_request: GetFeedbacksRequest, request_option: RequestOption
    ) -> None:
        with patch("dify_oapi.core.http.transport.Transport.execute", side_effect=Exception("API Error")) as mock_execute:
            with pytest.raises(Exception, match="API Error"):
                feedback_resource.get_feedbacks(get_feedbacks_request, request_option)

    @pytest.mark.asyncio
    async def test_get_feedbacks_async_error_handling(
        self, feedback_resource: Feedback, get_feedbacks_request: GetFeedbacksRequest, request_option: RequestOption
    ) -> None:
        with patch("dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, side_effect=Exception("API Error")) as mock_aexecute:
            with pytest.raises(Exception, match="API Error"):
                await feedback_resource.aget_feedbacks(get_feedbacks_request, request_option)