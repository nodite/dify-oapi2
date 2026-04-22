from dify_oapi.api.dify.service import DifyService
from dify_oapi.api.dify.v1.resource.audio import Audio
from dify_oapi.api.dify.v1.resource.feedback import Feedback
from dify_oapi.api.dify.v1.resource.file import File
from dify_oapi.api.dify.v1.resource.info import Info
from dify_oapi.api.dify.v1.version import V1


class TestDifyService:
    def test_service_has_v1(self, config):
        service = DifyService(config)
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_has_resources(self, config):
        v1 = DifyService(config).v1
        assert isinstance(v1.audio, Audio)
        assert isinstance(v1.feedback, Feedback)
        assert isinstance(v1.file, File)
        assert isinstance(v1.info, Info)
