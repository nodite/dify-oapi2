from dify_oapi.api.workflow.v1.model.info.get_info_request import GetInfoRequest
from dify_oapi.api.workflow.v1.model.info.get_info_response import GetInfoResponse
from dify_oapi.api.workflow.v1.model.info.get_parameters_request import GetParametersRequest
from dify_oapi.api.workflow.v1.model.info.get_parameters_response import GetParametersResponse
from dify_oapi.api.workflow.v1.model.info.get_site_request import GetSiteRequest
from dify_oapi.api.workflow.v1.model.info.get_site_response import GetSiteResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestGetInfoModels:
    def test_request_builder(self) -> None:
        """Test GetInfoRequest builder pattern."""
        request = GetInfoRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/info"

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
            description="Test Description",
            tags=["test", "app"],
            mode="workflow",
            author_name="Test Author",
        )
        assert response.name == "Test App"
        assert response.description == "Test Description"
        assert response.tags == ["test", "app"]
        assert response.mode == "workflow"
        assert response.author_name == "Test Author"


class TestGetParametersModels:
    def test_request_builder(self) -> None:
        """Test GetParametersRequest builder pattern."""
        request = GetParametersRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/parameters"

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
            user_input_form=[],
            file_upload=None,
            system_parameters=None,
        )
        assert response.user_input_form is not None
        assert len(response.user_input_form) == 0


class TestGetSiteModels:
    def test_request_builder(self) -> None:
        """Test GetSiteRequest builder pattern."""
        request = GetSiteRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/site"

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
            title="My Site",
            icon_type="emoji",
            icon="🚀",
            icon_background="#00FF00",
            description="My site description",
            show_workflow_steps=True,
        )
        assert response.title == "My Site"
        assert response.icon_type == "emoji"
        assert response.icon == "🚀"
        assert response.icon_background == "#00FF00"
        assert response.description == "My site description"
        assert response.show_workflow_steps is True
