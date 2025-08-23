"""Integration tests for completion V1 version class."""

from __future__ import annotations

from dify_oapi.api.completion.v1.resource.annotation import Annotation
from dify_oapi.api.completion.v1.resource.audio import Audio
from dify_oapi.api.completion.v1.resource.completion import Completion
from dify_oapi.api.completion.v1.resource.feedback import Feedback
from dify_oapi.api.completion.v1.resource.file import File
from dify_oapi.api.completion.v1.resource.info import Info
from dify_oapi.api.completion.v1.version import V1
from dify_oapi.core.model.config import Config


class TestV1Integration:
    """Test V1 version integration."""

    def test_v1_initialization(self) -> None:
        """Test V1 class initialization with config."""
        config = Config()
        v1 = V1(config)

        assert v1 is not None
        assert isinstance(v1, V1)

    def test_all_resources_initialized(self) -> None:
        """Test all resources are properly initialized."""
        config = Config()
        v1 = V1(config)

        # Test all resources are initialized
        assert hasattr(v1, "completion")
        assert hasattr(v1, "file")
        assert hasattr(v1, "feedback")
        assert hasattr(v1, "audio")
        assert hasattr(v1, "info")
        assert hasattr(v1, "annotation")

    def test_resource_types(self) -> None:
        """Test all resources have correct types."""
        config = Config()
        v1 = V1(config)

        # Test resource types
        assert isinstance(v1.completion, Completion)
        assert isinstance(v1.file, File)
        assert isinstance(v1.feedback, Feedback)
        assert isinstance(v1.audio, Audio)
        assert isinstance(v1.info, Info)
        assert isinstance(v1.annotation, Annotation)

    def test_config_propagation(self) -> None:
        """Test config is correctly passed to all resources."""
        config = Config()
        config.domain = "https://test.example.com"
        v1 = V1(config)

        # Test config propagation
        assert v1.completion.config is config
        assert v1.file.config is config
        assert v1.feedback.config is config
        assert v1.audio.config is config
        assert v1.info.config is config
        assert v1.annotation.config is config

    def test_resource_accessibility(self) -> None:
        """Test all resources are accessible."""
        config = Config()
        v1 = V1(config)

        # Test resource accessibility
        assert v1.completion is not None
        assert v1.file is not None
        assert v1.feedback is not None
        assert v1.audio is not None
        assert v1.info is not None
        assert v1.annotation is not None

    def test_multiple_v1_instances(self) -> None:
        """Test multiple V1 instances work independently."""
        config1 = Config()
        config1.domain = "https://api1.example.com"

        config2 = Config()
        config2.domain = "https://api2.example.com"

        v1_instance1 = V1(config1)
        v1_instance2 = V1(config2)

        # Test instances are independent
        assert v1_instance1.completion.config is not v1_instance2.completion.config
        assert v1_instance1.completion.config.domain != v1_instance2.completion.config.domain

    def test_resource_method_availability(self) -> None:
        """Test key methods are available on all resources."""
        config = Config()
        v1 = V1(config)

        # Test completion resource methods
        assert hasattr(v1.completion, "send_message")
        assert hasattr(v1.completion, "asend_message")
        assert hasattr(v1.completion, "stop_response")
        assert hasattr(v1.completion, "astop_response")

        # Test file resource methods
        assert hasattr(v1.file, "upload_file")
        assert hasattr(v1.file, "aupload_file")

        # Test feedback resource methods
        assert hasattr(v1.feedback, "message_feedback")
        assert hasattr(v1.feedback, "amessage_feedback")
        assert hasattr(v1.feedback, "get_feedbacks")
        assert hasattr(v1.feedback, "aget_feedbacks")

        # Test audio resource methods
        assert hasattr(v1.audio, "text_to_audio")
        assert hasattr(v1.audio, "atext_to_audio")

        # Test info resource methods
        assert hasattr(v1.info, "get_info")
        assert hasattr(v1.info, "aget_info")
        assert hasattr(v1.info, "get_parameters")
        assert hasattr(v1.info, "aget_parameters")
        assert hasattr(v1.info, "get_site")
        assert hasattr(v1.info, "aget_site")

        # Test annotation resource methods
        assert hasattr(v1.annotation, "list_annotations")
        assert hasattr(v1.annotation, "alist_annotations")
        assert hasattr(v1.annotation, "create_annotation")
        assert hasattr(v1.annotation, "acreate_annotation")
        assert hasattr(v1.annotation, "update_annotation")
        assert hasattr(v1.annotation, "aupdate_annotation")
        assert hasattr(v1.annotation, "delete_annotation")
        assert hasattr(v1.annotation, "adelete_annotation")
        assert hasattr(v1.annotation, "annotation_reply_settings")
        assert hasattr(v1.annotation, "aannotation_reply_settings")
        assert hasattr(v1.annotation, "query_annotation_reply_status")
        assert hasattr(v1.annotation, "aquery_annotation_reply_status")

    def test_config_modification_isolation(self) -> None:
        """Test config modifications don't affect other instances."""
        config = Config()
        config.domain = "https://original.example.com"

        v1_instance1 = V1(config)

        # Modify config after initialization
        config.domain = "https://modified.example.com"

        v1_instance2 = V1(config)

        # Both instances should use the same config object but with current state
        assert v1_instance1.completion.config is config
        assert v1_instance2.completion.config is config
        assert v1_instance1.completion.config.domain == "https://modified.example.com"
        assert v1_instance2.completion.config.domain == "https://modified.example.com"
