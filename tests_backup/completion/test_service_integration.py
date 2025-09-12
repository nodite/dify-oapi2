"""Integration tests for Completion service class."""

from dify_oapi.api.completion.service import CompletionService
from dify_oapi.api.completion.v1.version import V1
from dify_oapi.core.model.config import Config


class TestCompletionServiceIntegration:
    """Test Completion service integration."""

    def test_completion_service_initialization(self) -> None:
        """Test Completion service initialization."""
        config = Config()
        completion = CompletionService(config)

        # Test V1 is properly initialized
        assert isinstance(completion.v1, V1)
        assert completion.v1 is not None

    def test_completion_service_v1_access(self) -> None:
        """Test Completion service V1 access."""
        config = Config()
        completion = CompletionService(config)

        # Test V1 can be accessed
        v1 = completion.v1
        assert isinstance(v1, V1)

        # Test all 6 resources are accessible through V1
        assert hasattr(v1, "completion")
        assert hasattr(v1, "file")
        assert hasattr(v1, "feedback")
        assert hasattr(v1, "audio")
        assert hasattr(v1, "info")
        assert hasattr(v1, "annotation")

    def test_completion_service_config_propagation(self) -> None:
        """Test config is properly propagated through service layers."""
        config = Config()
        completion = CompletionService(config)

        # Test config propagation through service -> V1 -> resources
        assert completion.v1.completion.config is config
        assert completion.v1.file.config is config
        assert completion.v1.feedback.config is config
        assert completion.v1.audio.config is config
        assert completion.v1.info.config is config
        assert completion.v1.annotation.config is config

    def test_completion_service_resource_methods(self) -> None:
        """Test all resources have expected methods through service."""
        config = Config()
        completion = CompletionService(config)

        # Test completion resource methods (2 APIs)
        completion_resource = completion.v1.completion
        assert hasattr(completion_resource, "send_message")
        assert hasattr(completion_resource, "stop_response")

        # Test file resource methods (1 API)
        file = completion.v1.file
        assert hasattr(file, "upload_file")

        # Test feedback resource methods (2 APIs)
        feedback = completion.v1.feedback
        assert hasattr(feedback, "message_feedback")
        assert hasattr(feedback, "get_feedbacks")

        # Test audio resource methods (1 API)
        audio = completion.v1.audio
        assert hasattr(audio, "text_to_audio")

        # Test info resource methods (3 APIs)
        info = completion.v1.info
        assert hasattr(info, "get_info")
        assert hasattr(info, "get_parameters")
        assert hasattr(info, "get_site")

        # Test annotation resource methods (6 APIs)
        annotation = completion.v1.annotation
        assert hasattr(annotation, "list_annotations")
        assert hasattr(annotation, "create_annotation")
        assert hasattr(annotation, "update_annotation")
        assert hasattr(annotation, "delete_annotation")
        assert hasattr(annotation, "annotation_reply_settings")
        assert hasattr(annotation, "query_annotation_reply_status")

    def test_completion_service_async_methods(self) -> None:
        """Test all resources have async method variants through service."""
        config = Config()
        completion = CompletionService(config)

        # Test completion async methods
        completion_resource = completion.v1.completion
        assert hasattr(completion_resource, "asend_message")
        assert hasattr(completion_resource, "astop_response")

        # Test file async methods
        file = completion.v1.file
        assert hasattr(file, "aupload_file")

        # Test feedback async methods
        feedback = completion.v1.feedback
        assert hasattr(feedback, "amessage_feedback")
        assert hasattr(feedback, "aget_feedbacks")

        # Test audio async methods
        audio = completion.v1.audio
        assert hasattr(audio, "atext_to_audio")

        # Test info async methods
        info = completion.v1.info
        assert hasattr(info, "aget_info")
        assert hasattr(info, "aget_parameters")
        assert hasattr(info, "aget_site")

        # Test annotation async methods
        annotation = completion.v1.annotation
        assert hasattr(annotation, "alist_annotations")
        assert hasattr(annotation, "acreate_annotation")
        assert hasattr(annotation, "aupdate_annotation")
        assert hasattr(annotation, "adelete_annotation")
        assert hasattr(annotation, "aannotation_reply_settings")
        assert hasattr(annotation, "aquery_annotation_reply_status")
