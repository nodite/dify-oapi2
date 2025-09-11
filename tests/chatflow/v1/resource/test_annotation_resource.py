"""Tests for Annotation resource class."""

from unittest.mock import patch

import pytest

from dify_oapi.api.chatflow.v1.model.annotation_reply_settings_request import AnnotationReplySettingsRequest
from dify_oapi.api.chatflow.v1.model.annotation_reply_settings_request_body import AnnotationReplySettingsRequestBody
from dify_oapi.api.chatflow.v1.model.annotation_reply_settings_response import AnnotationReplySettingsResponse
from dify_oapi.api.chatflow.v1.model.annotation_reply_status_request import AnnotationReplyStatusRequest
from dify_oapi.api.chatflow.v1.model.annotation_reply_status_response import AnnotationReplyStatusResponse
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
from dify_oapi.api.chatflow.v1.resource.annotation import Annotation
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestAnnotationResource:
    """Test Annotation resource class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.config = Config()
        self.annotation = Annotation(self.config)
        self.request_option = RequestOption.builder().api_key("test-api-key").build()

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_list_annotations(self, mock_execute):
        """Test list annotations method."""
        # Setup
        mock_response = GetAnnotationsResponse()
        mock_execute.return_value = mock_response

        request = GetAnnotationsRequest.builder().page(1).limit(20).build()

        # Execute
        result = self.annotation.list(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=GetAnnotationsResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_alist_annotations(self, mock_aexecute):
        """Test async list annotations method."""
        # Setup
        mock_response = GetAnnotationsResponse()
        mock_aexecute.return_value = mock_response

        request = GetAnnotationsRequest.builder().page(1).limit(20).build()

        # Execute
        result = await self.annotation.alist(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=GetAnnotationsResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_create_annotation(self, mock_execute):
        """Test create annotation method."""
        # Setup
        mock_response = CreateAnnotationResponse()
        mock_execute.return_value = mock_response

        request_body = (
            CreateAnnotationRequestBody.builder()
            .question("What is AI?")
            .answer("AI is artificial intelligence")
            .build()
        )
        request = CreateAnnotationRequest.builder().request_body(request_body).build()

        # Execute
        result = self.annotation.create(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=CreateAnnotationResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_acreate_annotation(self, mock_aexecute):
        """Test async create annotation method."""
        # Setup
        mock_response = CreateAnnotationResponse()
        mock_aexecute.return_value = mock_response

        request_body = (
            CreateAnnotationRequestBody.builder()
            .question("What is AI?")
            .answer("AI is artificial intelligence")
            .build()
        )
        request = CreateAnnotationRequest.builder().request_body(request_body).build()

        # Execute
        result = await self.annotation.acreate(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=CreateAnnotationResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_update_annotation(self, mock_execute):
        """Test update annotation method."""
        # Setup
        mock_response = UpdateAnnotationResponse()
        mock_execute.return_value = mock_response

        request_body = (
            UpdateAnnotationRequestBody.builder().question("Updated question?").answer("Updated answer").build()
        )
        request = (
            UpdateAnnotationRequest.builder().annotation_id("test-annotation-id").request_body(request_body).build()
        )

        # Execute
        result = self.annotation.update(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=UpdateAnnotationResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_aupdate_annotation(self, mock_aexecute):
        """Test async update annotation method."""
        # Setup
        mock_response = UpdateAnnotationResponse()
        mock_aexecute.return_value = mock_response

        request_body = (
            UpdateAnnotationRequestBody.builder().question("Updated question?").answer("Updated answer").build()
        )
        request = (
            UpdateAnnotationRequest.builder().annotation_id("test-annotation-id").request_body(request_body).build()
        )

        # Execute
        result = await self.annotation.aupdate(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=UpdateAnnotationResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_delete_annotation(self, mock_execute):
        """Test delete annotation method."""
        # Setup
        mock_response = DeleteAnnotationResponse()
        mock_execute.return_value = mock_response

        request = DeleteAnnotationRequest.builder().annotation_id("test-annotation-id").build()

        # Execute
        result = self.annotation.delete(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=DeleteAnnotationResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_adelete_annotation(self, mock_aexecute):
        """Test async delete annotation method."""
        # Setup
        mock_response = DeleteAnnotationResponse()
        mock_aexecute.return_value = mock_response

        request = DeleteAnnotationRequest.builder().annotation_id("test-annotation-id").build()

        # Execute
        result = await self.annotation.adelete(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=DeleteAnnotationResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_reply_settings(self, mock_execute):
        """Test annotation reply settings method."""
        # Setup
        mock_response = AnnotationReplySettingsResponse()
        mock_execute.return_value = mock_response

        request_body = (
            AnnotationReplySettingsRequestBody.builder()
            .embedding_provider_name("openai")
            .embedding_model_name("text-embedding-ada-002")
            .score_threshold(0.8)
            .build()
        )
        request = AnnotationReplySettingsRequest.builder().action("enable").request_body(request_body).build()

        # Execute
        result = self.annotation.reply_settings(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=AnnotationReplySettingsResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_areply_settings(self, mock_aexecute):
        """Test async annotation reply settings method."""
        # Setup
        mock_response = AnnotationReplySettingsResponse()
        mock_aexecute.return_value = mock_response

        request_body = (
            AnnotationReplySettingsRequestBody.builder()
            .embedding_provider_name("openai")
            .embedding_model_name("text-embedding-ada-002")
            .score_threshold(0.8)
            .build()
        )
        request = AnnotationReplySettingsRequest.builder().action("enable").request_body(request_body).build()

        # Execute
        result = await self.annotation.areply_settings(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=AnnotationReplySettingsResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_reply_status(self, mock_execute):
        """Test annotation reply status method."""
        # Setup
        mock_response = AnnotationReplyStatusResponse()
        mock_execute.return_value = mock_response

        request = AnnotationReplyStatusRequest.builder().action("enable").job_id("test-job-id").build()

        # Execute
        result = self.annotation.reply_status(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=AnnotationReplyStatusResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_areply_status(self, mock_aexecute):
        """Test async annotation reply status method."""
        # Setup
        mock_response = AnnotationReplyStatusResponse()
        mock_aexecute.return_value = mock_response

        request = AnnotationReplyStatusRequest.builder().action("enable").job_id("test-job-id").build()

        # Execute
        result = await self.annotation.areply_status(request, self.request_option)

        # Verify
        assert result == mock_response
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=AnnotationReplyStatusResponse, option=self.request_option
        )

    def test_resource_initialization(self):
        """Test annotation resource initialization."""
        assert self.annotation.config == self.config
        assert isinstance(self.annotation, Annotation)
