"""Test configuration and fixtures."""

from unittest.mock import MagicMock

import pytest

from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


@pytest.fixture
def mock_config():
    """Create mock config."""
    return MagicMock(spec=Config)


@pytest.fixture
def request_option():
    """Create request option."""
    return RequestOption.builder().api_key("test-key").build()


@pytest.fixture
def mock_response():
    """Create mock response."""
    return MagicMock()
