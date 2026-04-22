import httpx
import pytest
import respx

from dify_oapi.api.dify.v1.model.get_info_request import GetInfoRequest
from dify_oapi.api.dify.v1.resource.info import Info


class TestErrorHandling:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Info(config)
        self.option = request_option

    @respx.mock
    def test_404_response_returns_failed_result(self):
        # Dify API returns a JSON body with "code" field on errors, which drives success=False
        respx.get("https://api.dify.ai/v1/info").mock(
            return_value=httpx.Response(
                404,
                json={"code": "not_found", "message": "Not found"},
                headers={"content-type": "application/json"},
            )
        )
        result = self.resource.get(GetInfoRequest.builder().user("u1").build(), self.option)
        assert result.success is False

    @respx.mock
    def test_500_response_returns_failed_result(self):
        # Dify API returns a JSON body with "code" field on errors, which drives success=False
        respx.get("https://api.dify.ai/v1/info").mock(
            return_value=httpx.Response(
                500,
                json={"code": "internal_error", "message": "Internal Server Error"},
                headers={"content-type": "application/json"},
            )
        )
        result = self.resource.get(GetInfoRequest.builder().user("u1").build(), self.option)
        assert result.success is False

    @respx.mock
    def test_connection_error_raises(self):
        respx.get("https://api.dify.ai/v1/info").mock(
            side_effect=httpx.ConnectError("Connection refused")
        )
        with pytest.raises(Exception):
            self.resource.get(GetInfoRequest.builder().user("u1").build(), self.option)
