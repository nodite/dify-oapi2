import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chat.v1.model.create_annotation_request_body import CreateAnnotationRequestBody
from dify_oapi.api.chat.v1.model.delete_annotation_request import DeleteAnnotationRequest
from dify_oapi.api.chat.v1.model.list_annotations_request import ListAnnotationsRequest
from dify_oapi.api.chat.v1.model.update_annotation_request import UpdateAnnotationRequest
from dify_oapi.api.chat.v1.model.update_annotation_request_body import UpdateAnnotationRequestBody
from dify_oapi.api.chat.v1.resource.annotation import Annotation


class TestAnnotation:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Annotation(config)
        self.option = request_option

    @respx.mock
    def test_list(self):
        route = respx.get("https://api.dify.ai/v1/apps/annotations").mock(
            return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "limit": 20})
        )
        result = self.resource.list(
            ListAnnotationsRequest.builder().page(1).limit(20).build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_create(self):
        route = respx.post("https://api.dify.ai/v1/apps/annotations").mock(
            return_value=httpx.Response(200, json={"id": "ann-123", "question": "Q?", "answer": "A."})
        )
        body = CreateAnnotationRequestBody.builder().question("Q?").answer("A.").build()
        result = self.resource.create(
            CreateAnnotationRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "ann-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_update(self):
        route = respx.put(
            url__regex=r"https://api\.dify\.ai/v1/apps/annotations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={"id": "ann-123", "question": "Q?", "answer": "A2."}))
        body = UpdateAnnotationRequestBody.builder().question("Q?").answer("A2.").build()
        result = self.resource.update(
            UpdateAnnotationRequest.builder().annotation_id("ann-123").request_body(body).build(),
            self.option,
        )
        assert result.id == "ann-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_delete(self):
        route = respx.delete(
            url__regex=r"https://api\.dify\.ai/v1/apps/annotations/[^/]+"
        ).mock(return_value=httpx.Response(200, json={}))
        self.resource.delete(
            DeleteAnnotationRequest.builder().annotation_id("ann-123").build(), self.option
        )
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
