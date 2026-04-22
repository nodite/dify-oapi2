import httpx
import pytest
import respx

from dify_oapi.api.completion.v1.model.annotation.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.completion.v1.model.annotation.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.completion.v1.model.annotation.list_annotations_request import ListAnnotationsRequest
from dify_oapi.api.completion.v1.resource.annotation import Annotation


class TestAnnotation:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Annotation(config)
        self.option = request_option

    @respx.mock
    def test_list_annotations(self):
        route = respx.get("https://api.dify.ai/v1/apps/annotations").mock(
            return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "limit": 20})
        )
        result = self.resource.list_annotations(
            ListAnnotationsRequest.builder().page("1").limit("20").build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create_annotation(self):
        route = respx.post("https://api.dify.ai/v1/apps/annotations").mock(
            return_value=httpx.Response(200, json={"id": "ann-123", "question": "Q?", "answer": "A."})
        )
        body = CreateAnnotationRequestBody.builder().question("Q?").answer("A.").build()
        result = self.resource.create_annotation(
            CreateAnnotationRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "ann-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete_annotation(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/apps/annotations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={}))
        self.resource.delete_annotation(
            DeleteAnnotationRequest.builder().annotation_id("ann-123").build(), self.option
        )
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
