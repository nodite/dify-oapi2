from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestConfig:
    def test_config_defaults(self):
        c = Config()
        assert c.max_connections == 100
        assert c.max_keepalive_connections == 20
        assert c.max_retry_count == 3
        assert c.verify_ssl is True

    def test_config_domain_assignment(self, domain):
        c = Config()
        c.domain = domain
        assert c.domain == "https://api.dify.ai"


class TestRequestOption:
    def test_builder_sets_api_key(self, request_option):
        assert request_option.api_key == "test-key"

    def test_builder_chaining(self):
        option = RequestOption.builder().api_key("my-key").build()
        assert option.api_key == "my-key"
