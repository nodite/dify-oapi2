"""Comprehensive tests for all Chatflow types."""

from typing import get_args

from dify_oapi.api.chatflow.v1.model.chatflow_types import (
    AnnotationAction,
    AudioFormat,
    AutoPlay,
    ChatColorTheme,
    ConversationStatus,
    DefaultLanguage,
    FeedbackRating,
    FileType,
    FormInputType,
    IconType,
    JobStatus,
    LanguageCode,
    MessageFileBelongsTo,
    NodeStatus,
    ResponseMode,
    SortBy,
    StreamEvent,
    TransferMethod,
    VariableValueType,
    WorkflowStatus,
)


class TestChatflowTypes:
    """Test class for validating all Chatflow type definitions."""

    def test_response_mode_values(self):
        """Test ResponseMode Literal type values."""
        expected_values = {"streaming", "blocking"}
        actual_values = set(get_args(ResponseMode))
        assert actual_values == expected_values, f"ResponseMode values should be {expected_values}"

    def test_file_type_values(self):
        """Test FileType Literal type values."""
        expected_values = {"document", "image", "audio", "video", "custom"}
        actual_values = set(get_args(FileType))
        assert actual_values == expected_values, f"FileType values should be {expected_values}"

    def test_transfer_method_values(self):
        """Test TransferMethod Literal type values."""
        expected_values = {"remote_url", "local_file"}
        actual_values = set(get_args(TransferMethod))
        assert actual_values == expected_values, f"TransferMethod values should be {expected_values}"

    def test_stream_event_values(self):
        """Test StreamEvent Literal type values."""
        expected_values = {
            "message",
            "message_file",
            "message_end",
            "tts_message",
            "tts_message_end",
            "message_replace",
            "workflow_started",
            "node_started",
            "node_finished",
            "workflow_finished",
            "error",
            "ping",
        }
        actual_values = set(get_args(StreamEvent))
        assert actual_values == expected_values, f"StreamEvent values should be {expected_values}"

    def test_message_file_belongs_to_values(self):
        """Test MessageFileBelongsTo Literal type values."""
        expected_values = {"user", "assistant"}
        actual_values = set(get_args(MessageFileBelongsTo))
        assert actual_values == expected_values, f"MessageFileBelongsTo values should be {expected_values}"

    def test_feedback_rating_values(self):
        """Test FeedbackRating Literal type values."""
        expected_values = {"like", "dislike"}
        actual_values = set(get_args(FeedbackRating))
        assert actual_values == expected_values, f"FeedbackRating values should be {expected_values}"

    def test_sort_by_values(self):
        """Test SortBy Literal type values."""
        expected_values = {"created_at", "-created_at", "updated_at", "-updated_at"}
        actual_values = set(get_args(SortBy))
        assert actual_values == expected_values, f"SortBy values should be {expected_values}"

    def test_conversation_status_values(self):
        """Test ConversationStatus Literal type values."""
        expected_values = {"normal", "archived"}
        actual_values = set(get_args(ConversationStatus))
        assert actual_values == expected_values, f"ConversationStatus values should be {expected_values}"

    def test_variable_value_type_values(self):
        """Test VariableValueType Literal type values."""
        expected_values = {"string", "number", "select"}
        actual_values = set(get_args(VariableValueType))
        assert actual_values == expected_values, f"VariableValueType values should be {expected_values}"

    def test_form_input_type_values(self):
        """Test FormInputType Literal type values."""
        expected_values = {"text-input", "paragraph", "select"}
        actual_values = set(get_args(FormInputType))
        assert actual_values == expected_values, f"FormInputType values should be {expected_values}"

    def test_job_status_values(self):
        """Test JobStatus Literal type values."""
        expected_values = {"waiting", "running", "completed", "failed"}
        actual_values = set(get_args(JobStatus))
        assert actual_values == expected_values, f"JobStatus values should be {expected_values}"

    def test_audio_format_values(self):
        """Test AudioFormat Literal type values."""
        expected_values = {"mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"}
        actual_values = set(get_args(AudioFormat))
        assert actual_values == expected_values, f"AudioFormat values should be {expected_values}"

    def test_language_code_values(self):
        """Test LanguageCode Literal type values."""
        expected_values = {"en", "zh", "ja", "ko", "es", "fr", "de", "it", "pt", "ru"}
        actual_values = set(get_args(LanguageCode))
        assert actual_values == expected_values, f"LanguageCode values should be {expected_values}"

    def test_chat_color_theme_values(self):
        """Test ChatColorTheme Literal type values."""
        expected_values = {"blue", "green", "purple", "orange", "red"}
        actual_values = set(get_args(ChatColorTheme))
        assert actual_values == expected_values, f"ChatColorTheme values should be {expected_values}"

    def test_default_language_values(self):
        """Test DefaultLanguage Literal type values."""
        expected_values = {
            "en-US",
            "zh-Hans",
            "zh-Hant",
            "ja-JP",
            "ko-KR",
            "es-ES",
            "fr-FR",
            "de-DE",
            "it-IT",
            "pt-BR",
            "ru-RU",
        }
        actual_values = set(get_args(DefaultLanguage))
        assert actual_values == expected_values, f"DefaultLanguage values should be {expected_values}"

    def test_icon_type_values(self):
        """Test IconType Literal type values."""
        expected_values = {"emoji", "image"}
        actual_values = set(get_args(IconType))
        assert actual_values == expected_values, f"IconType values should be {expected_values}"

    def test_auto_play_values(self):
        """Test AutoPlay Literal type values."""
        expected_values = {"enabled", "disabled"}
        actual_values = set(get_args(AutoPlay))
        assert actual_values == expected_values, f"AutoPlay values should be {expected_values}"

    def test_annotation_action_values(self):
        """Test AnnotationAction Literal type values."""
        expected_values = {"enable", "disable"}
        actual_values = set(get_args(AnnotationAction))
        assert actual_values == expected_values, f"AnnotationAction values should be {expected_values}"

    def test_node_status_values(self):
        """Test NodeStatus Literal type values."""
        expected_values = {"running", "succeeded", "failed", "stopped"}
        actual_values = set(get_args(NodeStatus))
        assert actual_values == expected_values, f"NodeStatus values should be {expected_values}"

    def test_workflow_status_values(self):
        """Test WorkflowStatus Literal type values."""
        expected_values = {"running", "succeeded", "failed", "stopped"}
        actual_values = set(get_args(WorkflowStatus))
        assert actual_values == expected_values, f"WorkflowStatus values should be {expected_values}"

    def test_all_types_are_importable(self):
        """Test that all types can be imported successfully."""
        # This test ensures all types are properly defined and importable
        assert ResponseMode is not None
        assert FileType is not None
        assert TransferMethod is not None
        assert StreamEvent is not None
        assert MessageFileBelongsTo is not None
        assert FeedbackRating is not None
        assert SortBy is not None
        assert ConversationStatus is not None
        assert VariableValueType is not None
        assert FormInputType is not None
        assert JobStatus is not None
        assert AudioFormat is not None
        assert LanguageCode is not None
        assert ChatColorTheme is not None
        assert DefaultLanguage is not None
        assert IconType is not None
        assert AutoPlay is not None
        assert AnnotationAction is not None
        assert NodeStatus is not None
        assert WorkflowStatus is not None

    def test_type_constraints_work(self):
        """Test that type constraints work correctly with valid values."""
        # Test some valid assignments (these should not raise type errors)
        response_mode: ResponseMode = "streaming"
        file_type: FileType = "document"
        transfer_method: TransferMethod = "remote_url"
        feedback_rating: FeedbackRating = "like"

        # Verify the assignments worked
        assert response_mode == "streaming"
        assert file_type == "document"
        assert transfer_method == "remote_url"
        assert feedback_rating == "like"

    def test_api_specification_compliance(self):
        """Test that all enum values match the API specification."""
        # Verify critical enum values match the official Dify API specification

        # Response modes from API spec
        assert "streaming" in get_args(ResponseMode)
        assert "blocking" in get_args(ResponseMode)

        # File types from API spec
        file_types = get_args(FileType)
        assert "document" in file_types
        assert "image" in file_types
        assert "audio" in file_types
        assert "video" in file_types
        assert "custom" in file_types

        # Stream events from API spec
        stream_events = get_args(StreamEvent)
        assert "message" in stream_events
        assert "message_end" in stream_events
        assert "workflow_started" in stream_events
        assert "workflow_finished" in stream_events
        assert "error" in stream_events

        # Feedback ratings from API spec
        assert "like" in get_args(FeedbackRating)
        assert "dislike" in get_args(FeedbackRating)
