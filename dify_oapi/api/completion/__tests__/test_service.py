from dify_oapi.api.completion.service import CompletionService
from dify_oapi.api.completion.v1.resource.annotation import Annotation
from dify_oapi.api.completion.v1.resource.completion import Completion
from dify_oapi.api.completion.v1.version import V1


class TestCompletionService:
    def test_service_has_v1(self, config):
        service = CompletionService(config)
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_has_resources(self, config):
        v1 = CompletionService(config).v1
        assert isinstance(v1.completion, Completion)
        assert isinstance(v1.annotation, Annotation)
