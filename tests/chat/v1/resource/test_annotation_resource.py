from unittest.mock import AsyncMock, Mock

import pytest

from dify_oapi.api.chat.v1.model.configure_annotation_reply_request import ConfigureAnnotationReplyRequest
from dify_oapi.api.chat.v1.model.configure_annotation_reply_request_body import ConfigureAnnotationReplyRequestBody
from dify_oapi.api.chat.v1.model.configure_annotation_reply_response import ConfigureAnnotationReplyResponse
from dify_oapi.api.chat.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chat.v1.model.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.chat.v1.model.create_annotation_response import CreateAnnotationResponse
from dify_oapi.api.chat.v1.model.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.chat.v1.model.delete_annotation_response import DeleteAnnotationResponse
from dify_oapi.api.chat.v1.model.get_annotation_reply_status_request import GetAnnotationReplyStatusRequest
from dify_oapi.api.chat.v1.model.get_annotation_reply_status_response import GetAnnotationReplyStatusResponse
from dify_oapi.api.chat.v1.model.list_annotations_request import ListAnnotationsRequest
from dify_oapi.api.chat.v1.model.list_annotations_response import ListAnnotationsResponse
from dify_oapi.api.chat.v1.model.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.chat.v1.model.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.api.chat.v1.model.update_annotation_response import UpdateAnnotationResponse
from dify_oapi.api.chat.v1.resource.annotation import Annotation
from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestAnnotationResource:
    @pytest.fixture
    def annotation_resource(self):
        config = Config()
        return Annotation(config)

    @pytest.fixture
    def mock_transport(self, monkeypatch):
        mock = Mock()
        monkeypatch.setattr(Transport, "execute", mock)
        return mock

    @pytest.fixture
    def mock_atransport(self, monkeypatch):
        mock = AsyncMock()
        monkeypatch.setattr(ATransport, "aexecute", mock)
        return mock

    def test_list_annotations(self, annotation_resource, mock_transport):
        """Test list annotations"""
        request = ListAnnotationsRequest.builder().page(1).limit(20).build()
        option = RequestOption.builder().build()

        mock_transport.return_value = ListAnnotationsResponse(data=[], has_more=False, limit=20, total=0, page=1)
        result = annotation_resource.list(request, option)

        assert isinstance(result, ListAnnotationsResponse)
        mock_transport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=ListAnnotationsResponse, option=option
        )

    def test_create_annotation(self, annotation_resource, mock_transport):
        """Test create annotation"""
        request_body = CreateAnnotationRequestBody.builder().question("What is AI?").answer("AI is...").build()
        request = CreateAnnotationRequest.builder().request_body(request_body).build()
        option = RequestOption.builder().build()

        mock_transport.return_value = CreateAnnotationResponse(
            id="annotation-123", question="What is AI?", answer="AI is...", hit_count=0, created_at=1234567890
        )
        result = annotation_resource.create(request, option)

        assert isinstance(result, CreateAnnotationResponse)
        mock_transport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=CreateAnnotationResponse, option=option
        )

    def test_update_annotation(self, annotation_resource, mock_transport):
        """Test update annotation"""
        request_body = (
            UpdateAnnotationRequestBody.builder().question("Updated question").answer("Updated answer").build()
        )
        request = UpdateAnnotationRequest.builder().annotation_id("annotation-123").request_body(request_body).build()
        option = RequestOption.builder().build()

        mock_transport.return_value = UpdateAnnotationResponse(
            id="annotation-123",
            question="Updated question",
            answer="Updated answer",
            hit_count=0,
            created_at=1234567890,
        )
        result = annotation_resource.update(request, option)

        assert isinstance(result, UpdateAnnotationResponse)
        mock_transport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=UpdateAnnotationResponse, option=option
        )

    def test_delete_annotation(self, annotation_resource, mock_transport):
        """Test delete annotation"""
        request = DeleteAnnotationRequest.builder().annotation_id("annotation-123").build()
        option = RequestOption.builder().build()

        mock_transport.return_value = DeleteAnnotationResponse()
        result = annotation_resource.delete(request, option)

        assert isinstance(result, DeleteAnnotationResponse)
        mock_transport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=DeleteAnnotationResponse, option=option
        )

    def test_configure_annotation_reply(self, annotation_resource, mock_transport):
        """Test configure annotation reply settings"""
        request_body = ConfigureAnnotationReplyRequestBody.builder().score_threshold(0.8).build()
        request = ConfigureAnnotationReplyRequest.builder().action("enable").request_body(request_body).build()
        option = RequestOption.builder().build()

        mock_transport.return_value = ConfigureAnnotationReplyResponse(job_id="job-123", job_status="running")
        result = annotation_resource.configure(request, option)

        assert isinstance(result, ConfigureAnnotationReplyResponse)
        mock_transport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=ConfigureAnnotationReplyResponse, option=option
        )

    def test_get_annotation_reply_status(self, annotation_resource, mock_transport):
        """Test get annotation reply settings status"""
        request = GetAnnotationReplyStatusRequest.builder().action("enable").job_id("job-123").build()
        option = RequestOption.builder().build()

        mock_transport.return_value = GetAnnotationReplyStatusResponse(
            job_id="job-123", job_status="completed", error_msg=None
        )
        result = annotation_resource.status(request, option)

        assert isinstance(result, GetAnnotationReplyStatusResponse)
        mock_transport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=GetAnnotationReplyStatusResponse, option=option
        )

    @pytest.mark.asyncio
    async def test_async_list_annotations(self, annotation_resource, mock_atransport):
        """Test async list annotations"""
        request = ListAnnotationsRequest.builder().page(1).limit(20).build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = ListAnnotationsResponse(data=[], has_more=False, limit=20, total=0, page=1)
        result = await annotation_resource.alist(request, option)

        assert isinstance(result, ListAnnotationsResponse)
        mock_atransport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=ListAnnotationsResponse, option=option
        )

    @pytest.mark.asyncio
    async def test_async_create_annotation(self, annotation_resource, mock_atransport):
        """Test async create annotation"""
        request_body = CreateAnnotationRequestBody.builder().question("What is AI?").answer("AI is...").build()
        request = CreateAnnotationRequest.builder().request_body(request_body).build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = CreateAnnotationResponse(
            id="annotation-123", question="What is AI?", answer="AI is...", hit_count=0, created_at=1234567890
        )
        result = await annotation_resource.acreate(request, option)

        assert isinstance(result, CreateAnnotationResponse)
        mock_atransport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=CreateAnnotationResponse, option=option
        )

    @pytest.mark.asyncio
    async def test_async_update_annotation(self, annotation_resource, mock_atransport):
        """Test async update annotation"""
        request_body = (
            UpdateAnnotationRequestBody.builder().question("Updated question").answer("Updated answer").build()
        )
        request = UpdateAnnotationRequest.builder().annotation_id("annotation-123").request_body(request_body).build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = UpdateAnnotationResponse(
            id="annotation-123",
            question="Updated question",
            answer="Updated answer",
            hit_count=0,
            created_at=1234567890,
        )
        result = await annotation_resource.aupdate(request, option)

        assert isinstance(result, UpdateAnnotationResponse)
        mock_atransport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=UpdateAnnotationResponse, option=option
        )

    @pytest.mark.asyncio
    async def test_async_delete_annotation(self, annotation_resource, mock_atransport):
        """Test async delete annotation"""
        request = DeleteAnnotationRequest.builder().annotation_id("annotation-123").build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = DeleteAnnotationResponse()
        result = await annotation_resource.adelete(request, option)

        assert isinstance(result, DeleteAnnotationResponse)
        mock_atransport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=DeleteAnnotationResponse, option=option
        )

    @pytest.mark.asyncio
    async def test_async_configure_annotation_reply(self, annotation_resource, mock_atransport):
        """Test async configure annotation reply settings"""
        request_body = ConfigureAnnotationReplyRequestBody.builder().score_threshold(0.8).build()
        request = ConfigureAnnotationReplyRequest.builder().action("enable").request_body(request_body).build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = ConfigureAnnotationReplyResponse(job_id="job-123", job_status="running")
        result = await annotation_resource.aconfigure(request, option)

        assert isinstance(result, ConfigureAnnotationReplyResponse)
        mock_atransport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=ConfigureAnnotationReplyResponse, option=option
        )

    @pytest.mark.asyncio
    async def test_async_get_annotation_reply_status(self, annotation_resource, mock_atransport):
        """Test async get annotation reply settings status"""
        request = GetAnnotationReplyStatusRequest.builder().action("enable").job_id("job-123").build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = GetAnnotationReplyStatusResponse(
            job_id="job-123", job_status="completed", error_msg=None
        )
        result = await annotation_resource.astatus(request, option)

        assert isinstance(result, GetAnnotationReplyStatusResponse)
        mock_atransport.assert_called_once_with(
            annotation_resource.config, request, unmarshal_as=GetAnnotationReplyStatusResponse, option=option
        )
