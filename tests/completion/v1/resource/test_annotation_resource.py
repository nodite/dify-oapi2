from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

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
from dify_oapi.api.completion.v1.resource.annotation import Annotation
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestAnnotationResource:
    @pytest.fixture
    def config(self) -> Config:
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def annotation_resource(self, config: Config) -> Annotation:
        return Annotation(config)

    @pytest.fixture
    def list_annotations_request(self) -> ListAnnotationsRequest:
        return ListAnnotationsRequest.builder().page("1").limit("20").build()

    @pytest.fixture
    def create_annotation_request(self) -> CreateAnnotationRequest:
        request_body = (
            CreateAnnotationRequestBody.builder()
            .question("[Example] What is AI?")
            .answer("AI is artificial intelligence.")
            .build()
        )
        return CreateAnnotationRequest.builder().request_body(request_body).build()

    @pytest.fixture
    def update_annotation_request(self) -> UpdateAnnotationRequest:
        request_body = (
            UpdateAnnotationRequestBody.builder()
            .question("[Example] What is machine learning?")
            .answer("Machine learning is a subset of AI.")
            .build()
        )
        return UpdateAnnotationRequest.builder().annotation_id("test-annotation-id").request_body(request_body).build()

    @pytest.fixture
    def delete_annotation_request(self) -> DeleteAnnotationRequest:
        return DeleteAnnotationRequest.builder().annotation_id("test-annotation-id").build()

    @pytest.fixture
    def annotation_reply_settings_request(self) -> AnnotationReplySettingsRequest:
        request_body = (
            AnnotationReplySettingsRequestBody.builder()
            .embedding_provider_name("openai")
            .embedding_model_name("text-embedding-ada-002")
            .score_threshold(0.8)
            .build()
        )
        return AnnotationReplySettingsRequest.builder().action("enable").request_body(request_body).build()

    @pytest.fixture
    def query_annotation_reply_status_request(self) -> QueryAnnotationReplyStatusRequest:
        return QueryAnnotationReplyStatusRequest.builder().action("enable").job_id("test-job-id").build()

    def test_list_annotations_sync(
        self,
        annotation_resource: Annotation,
        list_annotations_request: ListAnnotationsRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = ListAnnotationsResponse(data=[], has_more=False, limit=20, total=0, page=1)

        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = annotation_resource.list_annotations(list_annotations_request, request_option)

            assert response == mock_response
            mock_execute.assert_called_once_with(
                annotation_resource.config,
                list_annotations_request,
                unmarshal_as=ListAnnotationsResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_list_annotations_async(
        self,
        annotation_resource: Annotation,
        list_annotations_request: ListAnnotationsRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = ListAnnotationsResponse(data=[], has_more=False, limit=20, total=0, page=1)

        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response
        ) as mock_aexecute:
            response = await annotation_resource.alist_annotations(list_annotations_request, request_option)

            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                annotation_resource.config,
                list_annotations_request,
                unmarshal_as=ListAnnotationsResponse,
                option=request_option,
            )

    def test_create_annotation_sync(
        self,
        annotation_resource: Annotation,
        create_annotation_request: CreateAnnotationRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = CreateAnnotationResponse(
            id="test-id", question="[Example] What is AI?", answer="AI is artificial intelligence.", hit_count=0
        )

        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = annotation_resource.create_annotation(create_annotation_request, request_option)

            assert response == mock_response
            mock_execute.assert_called_once_with(
                annotation_resource.config,
                create_annotation_request,
                unmarshal_as=CreateAnnotationResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_create_annotation_async(
        self,
        annotation_resource: Annotation,
        create_annotation_request: CreateAnnotationRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = CreateAnnotationResponse(
            id="test-id", question="[Example] What is AI?", answer="AI is artificial intelligence.", hit_count=0
        )

        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response
        ) as mock_aexecute:
            response = await annotation_resource.acreate_annotation(create_annotation_request, request_option)

            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                annotation_resource.config,
                create_annotation_request,
                unmarshal_as=CreateAnnotationResponse,
                option=request_option,
            )

    def test_update_annotation_sync(
        self,
        annotation_resource: Annotation,
        update_annotation_request: UpdateAnnotationRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = UpdateAnnotationResponse(
            id="test-annotation-id",
            question="[Example] What is machine learning?",
            answer="Machine learning is a subset of AI.",
            hit_count=0,
        )

        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = annotation_resource.update_annotation(update_annotation_request, request_option)

            assert response == mock_response
            mock_execute.assert_called_once_with(
                annotation_resource.config,
                update_annotation_request,
                unmarshal_as=UpdateAnnotationResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_update_annotation_async(
        self,
        annotation_resource: Annotation,
        update_annotation_request: UpdateAnnotationRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = UpdateAnnotationResponse(
            id="test-annotation-id",
            question="[Example] What is machine learning?",
            answer="Machine learning is a subset of AI.",
            hit_count=0,
        )

        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response
        ) as mock_aexecute:
            response = await annotation_resource.aupdate_annotation(update_annotation_request, request_option)

            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                annotation_resource.config,
                update_annotation_request,
                unmarshal_as=UpdateAnnotationResponse,
                option=request_option,
            )

    def test_delete_annotation_sync(
        self,
        annotation_resource: Annotation,
        delete_annotation_request: DeleteAnnotationRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = DeleteAnnotationResponse()

        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = annotation_resource.delete_annotation(delete_annotation_request, request_option)

            assert response == mock_response
            mock_execute.assert_called_once_with(
                annotation_resource.config,
                delete_annotation_request,
                unmarshal_as=DeleteAnnotationResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_delete_annotation_async(
        self,
        annotation_resource: Annotation,
        delete_annotation_request: DeleteAnnotationRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = DeleteAnnotationResponse()

        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response
        ) as mock_aexecute:
            response = await annotation_resource.adelete_annotation(delete_annotation_request, request_option)

            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                annotation_resource.config,
                delete_annotation_request,
                unmarshal_as=DeleteAnnotationResponse,
                option=request_option,
            )

    def test_annotation_reply_settings_sync(
        self,
        annotation_resource: Annotation,
        annotation_reply_settings_request: AnnotationReplySettingsRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = AnnotationReplySettingsResponse(job_id="test-job-id", job_status="waiting")

        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = annotation_resource.annotation_reply_settings(annotation_reply_settings_request, request_option)

            assert response == mock_response
            mock_execute.assert_called_once_with(
                annotation_resource.config,
                annotation_reply_settings_request,
                unmarshal_as=AnnotationReplySettingsResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_annotation_reply_settings_async(
        self,
        annotation_resource: Annotation,
        annotation_reply_settings_request: AnnotationReplySettingsRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = AnnotationReplySettingsResponse(job_id="test-job-id", job_status="waiting")

        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response
        ) as mock_aexecute:
            response = await annotation_resource.aannotation_reply_settings(
                annotation_reply_settings_request, request_option
            )

            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                annotation_resource.config,
                annotation_reply_settings_request,
                unmarshal_as=AnnotationReplySettingsResponse,
                option=request_option,
            )

    def test_query_annotation_reply_status_sync(
        self,
        annotation_resource: Annotation,
        query_annotation_reply_status_request: QueryAnnotationReplyStatusRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = QueryAnnotationReplyStatusResponse(job_id="test-job-id", job_status="completed", error_msg="")

        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = annotation_resource.query_annotation_reply_status(
                query_annotation_reply_status_request, request_option
            )

            assert response == mock_response
            mock_execute.assert_called_once_with(
                annotation_resource.config,
                query_annotation_reply_status_request,
                unmarshal_as=QueryAnnotationReplyStatusResponse,
                option=request_option,
            )

    @pytest.mark.asyncio
    async def test_query_annotation_reply_status_async(
        self,
        annotation_resource: Annotation,
        query_annotation_reply_status_request: QueryAnnotationReplyStatusRequest,
        request_option: RequestOption,
    ) -> None:
        mock_response = QueryAnnotationReplyStatusResponse(job_id="test-job-id", job_status="completed", error_msg="")

        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response
        ) as mock_aexecute:
            response = await annotation_resource.aquery_annotation_reply_status(
                query_annotation_reply_status_request, request_option
            )

            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                annotation_resource.config,
                query_annotation_reply_status_request,
                unmarshal_as=QueryAnnotationReplyStatusResponse,
                option=request_option,
            )

    def test_list_annotations_error_handling(
        self,
        annotation_resource: Annotation,
        list_annotations_request: ListAnnotationsRequest,
        request_option: RequestOption,
    ) -> None:
        with patch("dify_oapi.core.http.transport.Transport.execute", side_effect=Exception("API Error")):
            with pytest.raises(Exception, match="API Error"):
                annotation_resource.list_annotations(list_annotations_request, request_option)

    @pytest.mark.asyncio
    async def test_create_annotation_async_error_handling(
        self,
        annotation_resource: Annotation,
        create_annotation_request: CreateAnnotationRequest,
        request_option: RequestOption,
    ) -> None:
        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute",
            new_callable=AsyncMock,
            side_effect=Exception("API Error"),
        ):
            with pytest.raises(Exception, match="API Error"):
                await annotation_resource.acreate_annotation(create_annotation_request, request_option)

    def test_delete_annotation_error_handling(
        self,
        annotation_resource: Annotation,
        delete_annotation_request: DeleteAnnotationRequest,
        request_option: RequestOption,
    ) -> None:
        with patch("dify_oapi.core.http.transport.Transport.execute", side_effect=Exception("API Error")):
            with pytest.raises(Exception, match="API Error"):
                annotation_resource.delete_annotation(delete_annotation_request, request_option)

    @pytest.mark.asyncio
    async def test_annotation_reply_settings_async_error_handling(
        self,
        annotation_resource: Annotation,
        annotation_reply_settings_request: AnnotationReplySettingsRequest,
        request_option: RequestOption,
    ) -> None:
        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute",
            new_callable=AsyncMock,
            side_effect=Exception("API Error"),
        ):
            with pytest.raises(Exception, match="API Error"):
                await annotation_resource.aannotation_reply_settings(annotation_reply_settings_request, request_option)
