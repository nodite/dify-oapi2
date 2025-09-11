from dify_oapi.core.model.config import Config

from .v1.version import V1


class ChatflowService:
    """Chatflow API service providing access to all chatflow-related operations.

    This service provides access to 17 chatflow APIs across 6 resource categories:
    - Chatflow: 3 APIs (send, stop, suggested)
    - File: 1 API (upload)
    - Feedback: 2 APIs (message, list)
    - Conversation: 5 APIs (messages, list, delete, rename, variables)
    - TTS: 2 APIs (speech_to_text, text_to_audio)
    - Application: 4 APIs (info, parameters, meta, site)
    - Annotation: 6 APIs (list, create, update, delete, reply_settings, reply_status)
    """

    def __init__(self, config: Config):
        """Initialize the Chatflow service with configuration.

        Args:
            config: The configuration object containing API settings
        """
        self.v1 = V1(config)
