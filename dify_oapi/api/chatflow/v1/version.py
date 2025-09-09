from dify_oapi.core.model.config import Config

from .resource.annotation import Annotation
from .resource.application import Application
from .resource.chatflow import Chatflow
from .resource.conversation import Conversation
from .resource.feedback import Feedback
from .resource.file import File
from .resource.tts import TTS


class V1:
    """Chatflow API v1 version class integrating all 6 resources.

    This class provides access to all chatflow resources:
    - chatflow: Core chatflow operations (3 APIs)
    - file: File management operations (1 API)
    - feedback: Feedback operations (2 APIs)
    - conversation: Conversation management operations (5 APIs)
    - tts: Text-to-Speech operations (2 APIs)
    - application: Application configuration operations (4 APIs)
    - annotation: Annotation management operations (6 APIs)
    """

    def __init__(self, config: Config):
        """Initialize the V1 version with all resources.

        Args:
            config: The configuration object containing API settings
        """
        self.annotation = Annotation(config)
        self.application = Application(config)
        self.chatflow = Chatflow(config)
        self.conversation = Conversation(config)
        self.feedback = Feedback(config)
        self.file = File(config)
        self.tts = TTS(config)
