from unittest.mock import patch

import pytest

from dify_oapi.api.chat.v1.model.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.api.chat.v1.model.get_feedbacks_response import GetFeedbacksResponse
from dify_oapi.api.chat.v1.model.submit_feedback_request import SubmitFeedbackRequest
from dify_oapi.api.chat.v1.model.submit_feedback_response import SubmitFeedbackResponse
from dify_oapi.api.chat.v1.resource.feedback import Feedback
from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestFeedbackResource:
    @pytest.fixture
    def feedback_resource(self):
        config = Config()
        return Feedback(config)

    @pytest.fixture
    def mock_transport(self):
        with patch.object(Transport, "execute") as mock:
            yield mock

    @pytest.fixture
    def mock_atransport(self):
        with patch.object(ATransport, "aexecute") as mock:
            yield mock

    def test_submit_feedback(self, feedback_resource, mock_transport):
        """Test submit feedback method"""
        request = SubmitFeedbackRequest.builder().build()
        option = RequestOption.builder().build()

        mock_transport.return_value = SubmitFeedbackResponse()
        result = feedback_resource.submit(request, option)

        assert isinstance(result, SubmitFeedbackResponse)
        mock_transport.assert_called_once_with(
            feedback_resource.config, request, unmarshal_as=SubmitFeedbackResponse, option=option
        )

    async def test_async_submit_feedback(self, feedback_resource, mock_atransport):
        """Test async submit feedback method"""
        request = SubmitFeedbackRequest.builder().build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = SubmitFeedbackResponse()
        result = await feedback_resource.asubmit(request, option)

        assert isinstance(result, SubmitFeedbackResponse)
        mock_atransport.assert_called_once_with(
            feedback_resource.config, request, unmarshal_as=SubmitFeedbackResponse, option=option
        )

    def test_list_feedbacks(self, feedback_resource, mock_transport):
        """Test list feedbacks method"""
        request = GetFeedbacksRequest.builder().build()
        option = RequestOption.builder().build()

        mock_transport.return_value = GetFeedbacksResponse()
        result = feedback_resource.list(request, option)

        assert isinstance(result, GetFeedbacksResponse)
        mock_transport.assert_called_once_with(
            feedback_resource.config, request, unmarshal_as=GetFeedbacksResponse, option=option
        )

    async def test_async_list_feedbacks(self, feedback_resource, mock_atransport):
        """Test async list feedbacks method"""
        request = GetFeedbacksRequest.builder().build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = GetFeedbacksResponse()
        result = await feedback_resource.alist(request, option)

        assert isinstance(result, GetFeedbacksResponse)
        mock_atransport.assert_called_once_with(
            feedback_resource.config, request, unmarshal_as=GetFeedbacksResponse, option=option
        )

    def test_submit_feedback_without_option(self, feedback_resource, mock_transport):
        """Test submit feedback without request option"""
        request = SubmitFeedbackRequest.builder().build()

        mock_transport.return_value = SubmitFeedbackResponse()
        result = feedback_resource.submit(request)

        assert isinstance(result, SubmitFeedbackResponse)
        mock_transport.assert_called_once_with(
            feedback_resource.config, request, unmarshal_as=SubmitFeedbackResponse, option=None
        )

    def test_list_feedbacks_without_option(self, feedback_resource, mock_transport):
        """Test list feedbacks without request option"""
        request = GetFeedbacksRequest.builder().build()

        mock_transport.return_value = GetFeedbacksResponse()
        result = feedback_resource.list(request)

        assert isinstance(result, GetFeedbacksResponse)
        mock_transport.assert_called_once_with(
            feedback_resource.config, request, unmarshal_as=GetFeedbacksResponse, option=None
        )
