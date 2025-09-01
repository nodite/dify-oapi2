"""Tests for Chat API type definitions."""

from typing import get_args

from dify_oapi.api.chat.v1.model.chat_types import (
    AnnotationAction,
    AudioFormat,
    AutoPlay,
    ConversationStatus,
    FileType,
    FormInputType,
    HttpStatusCode,
    IconType,
    ImageFormat,
    JobStatus,
    MessageBelongsTo,
    Rating,
    ResponseMode,
    SortBy,
    StreamingEventType,
    TransferMethod,
    VariableValueType,
)


class TestChatTypes:
    """Test all Chat API type definitions."""

    def test_response_mode_values(self):
        """Test ResponseMode Literal type values."""
        expected_values = ("streaming", "blocking")
        assert get_args(ResponseMode) == expected_values

    def test_file_type_values(self):
        """Test FileType Literal type values."""
        expected_values = ("image",)
        assert get_args(FileType) == expected_values

    def test_transfer_method_values(self):
        """Test TransferMethod Literal type values."""
        expected_values = ("remote_url", "local_file")
        assert get_args(TransferMethod) == expected_values

    def test_rating_values(self):
        """Test Rating Literal type values."""
        expected_values = ("like", "dislike")
        assert get_args(Rating) == expected_values

    def test_sort_by_values(self):
        """Test SortBy Literal type values."""
        expected_values = ("created_at", "-created_at", "updated_at", "-updated_at")
        assert get_args(SortBy) == expected_values

    def test_icon_type_values(self):
        """Test IconType Literal type values."""
        expected_values = ("emoji", "image")
        assert get_args(IconType) == expected_values

    def test_auto_play_values(self):
        """Test AutoPlay Literal type values."""
        expected_values = ("enabled", "disabled")
        assert get_args(AutoPlay) == expected_values

    def test_annotation_action_values(self):
        """Test AnnotationAction Literal type values."""
        expected_values = ("enable", "disable")
        assert get_args(AnnotationAction) == expected_values

    def test_job_status_values(self):
        """Test JobStatus Literal type values."""
        expected_values = ("waiting", "running", "completed", "failed")
        assert get_args(JobStatus) == expected_values

    def test_message_belongs_to_values(self):
        """Test MessageBelongsTo Literal type values."""
        expected_values = ("user", "assistant")
        assert get_args(MessageBelongsTo) == expected_values

    def test_conversation_status_values(self):
        """Test ConversationStatus Literal type values."""
        expected_values = ("normal", "archived")
        assert get_args(ConversationStatus) == expected_values

    def test_variable_value_type_values(self):
        """Test VariableValueType Literal type values."""
        expected_values = ("string", "number", "select")
        assert get_args(VariableValueType) == expected_values

    def test_form_input_type_values(self):
        """Test FormInputType Literal type values."""
        expected_values = ("text-input", "paragraph", "select")
        assert get_args(FormInputType) == expected_values

    def test_streaming_event_type_values(self):
        """Test StreamingEventType Literal type values."""
        expected_values = (
            "message",
            "agent_message",
            "tts_message",
            "tts_message_end",
            "agent_thought",
            "message_file",
            "message_end",
            "message_replace",
            "error",
            "ping",
        )
        assert get_args(StreamingEventType) == expected_values

    def test_audio_format_values(self):
        """Test AudioFormat Literal type values."""
        expected_values = ("mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm")
        assert get_args(AudioFormat) == expected_values

    def test_image_format_values(self):
        """Test ImageFormat Literal type values."""
        expected_values = ("png", "jpg", "jpeg", "webp", "gif")
        assert get_args(ImageFormat) == expected_values

    def test_http_status_code_values(self):
        """Test HttpStatusCode Literal type values."""
        expected_values = (200, 204, 400, 401, 403, 404, 413, 415, 429, 500, 503)
        assert get_args(HttpStatusCode) == expected_values

    def test_all_types_importable(self):
        """Test all type definitions can be imported correctly."""
        # This test passes if all imports in the module work
        assert ResponseMode is not None
        assert FileType is not None
        assert TransferMethod is not None
        assert Rating is not None
        assert SortBy is not None
        assert IconType is not None
        assert AutoPlay is not None
        assert AnnotationAction is not None
        assert JobStatus is not None
        assert MessageBelongsTo is not None
        assert ConversationStatus is not None
        assert VariableValueType is not None
        assert FormInputType is not None
        assert StreamingEventType is not None
        assert AudioFormat is not None
        assert ImageFormat is not None
        assert HttpStatusCode is not None
