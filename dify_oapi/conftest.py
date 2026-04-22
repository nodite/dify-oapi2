import pytest

from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


@pytest.fixture
def domain() -> str:
    return "https://api.dify.ai"


@pytest.fixture
def request_option() -> RequestOption:
    return RequestOption.builder().api_key("test-key").build()


@pytest.fixture
def config(domain: str) -> Config:
    c = Config()
    c.domain = domain
    return c
