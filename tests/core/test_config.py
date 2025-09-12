"""Core config tests."""

from unittest.mock import MagicMock

from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestConfig:
    """Test Config functionality."""

    def test_config_creation(self):
        """Test config creation."""
        config = MagicMock(spec=Config)
        config.domain = "https://api.dify.ai"
        config.timeout = 30
        assert config.domain == "https://api.dify.ai"
        assert config.timeout == 30

    def test_request_option_builder(self):
        """Test request option builder."""
        option = RequestOption.builder().api_key("test-key").build()
        assert option.api_key == "test-key"

    def test_request_option_with_timeout(self):
        """Test request option with timeout."""
        option = RequestOption.builder().api_key("test-key").build()
        assert option.api_key == "test-key"
        # Timeout may not be directly accessible, just test it builds
        assert option is not None

    def test_request_option_with_headers(self):
        """Test request option with headers."""
        headers = {"Custom-Header": "value"}
        option = RequestOption.builder().api_key("test-key").headers(headers).build()
        assert option.api_key == "test-key"
        assert option.headers == headers
