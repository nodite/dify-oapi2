from __future__ import annotations

from dify_oapi.api.completion.v1.model.info.get_info_request import GetInfoRequest
from dify_oapi.api.completion.v1.model.info.get_info_response import GetInfoResponse
from dify_oapi.api.completion.v1.model.info.get_parameters_request import GetParametersRequest
from dify_oapi.api.completion.v1.model.info.get_parameters_response import GetParametersResponse
from dify_oapi.api.completion.v1.model.info.get_site_request import GetSiteRequest
from dify_oapi.api.completion.v1.model.info.get_site_response import GetSiteResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestGetInfoModels:
    """Test GetInfo API models."""

    def test_request_builder(self) -> None:
        """Test GetInfoRequest builder pattern."""
        request = GetInfoRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/info"
        assert len(request.queries) == 0

    def test_request_validation(self) -> None:
        """Test GetInfoRequest validation."""
        request = GetInfoRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/info"

    def test_response_inheritance(self) -> None:
        """Test GetInfoResponse inherits from BaseResponse."""
        response = GetInfoResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetInfoResponse data access."""
        response = GetInfoResponse(
            name="Test App",
            description="A test application",
            tags=["ai", "completion"],
            mode="completion",
            author_name="Test Author",
        )

        assert response.name == "Test App"
        assert response.description == "A test application"
        assert response.tags == ["ai", "completion"]
        assert response.mode == "completion"
        assert response.author_name == "Test Author"


class TestGetParametersModels:
    """Test GetParameters API models."""

    def test_request_builder(self) -> None:
        """Test GetParametersRequest builder pattern."""
        request = GetParametersRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/parameters"
        assert len(request.queries) == 0

    def test_request_validation(self) -> None:
        """Test GetParametersRequest validation."""
        request = GetParametersRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/parameters"

    def test_response_inheritance(self) -> None:
        """Test GetParametersResponse inherits from BaseResponse."""
        response = GetParametersResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetParametersResponse data access."""
        response = GetParametersResponse(
            opening_statement="Welcome",
            suggested_questions=["What can you do?"],
        )

        assert response.opening_statement == "Welcome"
        assert response.suggested_questions == ["What can you do?"]


class TestGetSiteModels:
    """Test GetSite API models."""

    def test_request_builder(self) -> None:
        """Test GetSiteRequest builder pattern."""
        request = GetSiteRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/site"
        assert len(request.queries) == 0

    def test_request_validation(self) -> None:
        """Test GetSiteRequest validation."""
        request = GetSiteRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/site"

    def test_response_inheritance(self) -> None:
        """Test GetSiteResponse inherits from BaseResponse."""
        response = GetSiteResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetSiteResponse data access."""
        response = GetSiteResponse(
            title="Test WebApp",
            chat_color_theme="#007bff",
            icon_type="emoji",
            icon="🤖",
            description="A test web application",
            default_language="en",
        )

        assert response.title == "Test WebApp"
        assert response.chat_color_theme == "#007bff"
        assert response.icon_type == "emoji"
        assert response.icon == "🤖"
        assert response.description == "A test web application"
        assert response.default_language == "en"
