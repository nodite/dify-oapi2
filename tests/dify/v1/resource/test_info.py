"""Info resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.dify.v1.resource.info import Info
from dify_oapi.core.model.request_option import RequestOption


class TestInfo:
    """Test Info resource."""

    @pytest.fixture
    def info(self, mock_config):
        """Create Info instance."""
        return Info(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_get(self, info, request_option):
        """Test get info."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(name="test-app")
            result = info.get(MagicMock(), request_option)
            assert hasattr(result, "name")

    def test_parameters(self, info, request_option):
        """Test get parameters."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(user_input_form=[])
            result = info.parameters(MagicMock(), request_option)
            assert result.user_input_form == []

    def test_meta(self, info, request_option):
        """Test get meta."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(tool_icons={})
            result = info.meta(MagicMock(), request_option)
            assert result.tool_icons == {}

    def test_site(self, info, request_option):
        """Test get site."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(title="test-site")
            result = info.site(MagicMock(), request_option)
            assert result.title == "test-site"
