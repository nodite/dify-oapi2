import httpx
import pytest
import respx

from dify_oapi.api.dify.v1.model.get_info_request import GetInfoRequest
from dify_oapi.api.dify.v1.model.get_meta_request import GetMetaRequest
from dify_oapi.api.dify.v1.model.get_parameters_request import GetParametersRequest
from dify_oapi.api.dify.v1.model.get_site_request import GetSiteRequest
from dify_oapi.api.dify.v1.resource.info import Info


class TestInfo:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Info(config)
        self.option = request_option

    @respx.mock
    def test_get(self):
        route = respx.get("https://api.dify.ai/v1/info").mock(
            return_value=httpx.Response(200, json={"name": "My App", "description": "A test app"})
        )
        result = self.resource.get(
            GetInfoRequest.builder().user("u1").build(), self.option
        )
        assert result.name == "My App"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_parameters(self):
        route = respx.get("https://api.dify.ai/v1/parameters").mock(
            return_value=httpx.Response(200, json={"user_input_form": []})
        )
        result = self.resource.parameters(
            GetParametersRequest.builder().user("u1").build(), self.option
        )
        assert result.user_input_form == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_meta(self):
        route = respx.get("https://api.dify.ai/v1/meta").mock(
            return_value=httpx.Response(200, json={"tool_icons": {"dalle2": "icon-url"}})
        )
        result = self.resource.meta(GetMetaRequest.builder().build(), self.option)
        assert result.tool_icons is not None
        assert result.tool_icons.dalle2 == "icon-url"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_site(self):
        route = respx.get("https://api.dify.ai/v1/site").mock(
            return_value=httpx.Response(200, json={"title": "Test App"})
        )
        result = self.resource.site(GetSiteRequest.builder().build(), self.option)
        assert result.title == "Test App"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
