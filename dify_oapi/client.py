from __future__ import annotations

import ssl

from .api.chat.service import ChatService
from .api.chatflow.service import ChatflowService
from .api.completion.service import CompletionService
from .api.dify.service import DifyService
from .api.knowledge.service import KnowledgeService
from .api.workflow.service import WorkflowService
from .core.enum import LogLevel
from .core.http.transport import Transport
from .core.http.transport.connection_pool import connection_pool
from .core.log import logger
from .core.model.base_request import BaseRequest
from .core.model.config import Config


class Client:
    def __init__(self):
        self._config: Config | None = None
        self._chat: ChatService | None = None
        self._chatflow: ChatflowService | None = None
        self._completion: CompletionService | None = None
        self._dify: DifyService | None = None
        self._workflow: WorkflowService | None = None
        self._knowledge: KnowledgeService | None = None

    @property
    def chat(self) -> ChatService:
        if self._chat is None:
            raise RuntimeError("Chat service has not been initialized")
        return self._chat

    @property
    def chatflow(self) -> ChatflowService:
        if self._chatflow is None:
            raise RuntimeError("Chatflow service has not been initialized")
        return self._chatflow

    @property
    def completion(self) -> CompletionService:
        if self._completion is None:
            raise RuntimeError("Completion service has not been initialized")
        return self._completion

    @property
    def dify(self) -> DifyService:
        if self._dify is None:
            raise RuntimeError("Dify service has not been initialized")
        return self._dify

    @property
    def workflow(self) -> WorkflowService:
        if self._workflow is None:
            raise RuntimeError("Workflow service has not been initialized")
        return self._workflow

    @property
    def knowledge(self) -> KnowledgeService:
        if self._knowledge is None:
            raise RuntimeError("Knowledge base service has not been initialized")
        return self._knowledge

    def request(self, request: BaseRequest):
        if self._config is None:
            raise RuntimeError("Config is not set")
        resp = Transport.execute(self._config, request)
        return resp

    def close(self):
        """Close all HTTP connections and clean up resources."""
        connection_pool.close_all()

    async def aclose(self):
        """Async version of close for proper cleanup of async connections."""
        await connection_pool.aclose_all()

    @staticmethod
    def builder() -> ClientBuilder:
        return ClientBuilder()


class ClientBuilder:
    def __init__(self) -> None:
        self._config = Config()

    def domain(self, domain: str) -> ClientBuilder:
        self._config.domain = domain
        return self

    def log_level(self, level: LogLevel) -> ClientBuilder:
        self._config.log_level = level
        return self

    def max_retry_count(self, count: int) -> ClientBuilder:
        self._config.max_retry_count = count
        return self

    def max_keepalive_connections(self, count: int) -> ClientBuilder:
        """Set maximum keepalive connections per connection pool."""
        self._config.max_keepalive_connections = count
        return self

    def max_connections(self, count: int) -> ClientBuilder:
        """Set maximum total connections per connection pool."""
        self._config.max_connections = count
        return self

    def keepalive_expiry(self, seconds: float) -> ClientBuilder:
        """Set keepalive connection expiry time in seconds."""
        self._config.keepalive_expiry = seconds
        return self

    def timeout(self, seconds: float) -> ClientBuilder:
        """Set client timeout in seconds."""
        self._config.timeout = seconds
        return self

    def verify_ssl(self, verify: ssl.SSLContext | str | bool) -> ClientBuilder:
        """Set SSL certificate verification."""
        self._config.verify_ssl = verify
        return self

    def build(self) -> Client:
        client: Client = Client()
        client._config = self._config

        # Initialize logger
        self._init_logger()

        # Initialize services
        client._chat = ChatService(self._config)
        client._chatflow = ChatflowService(self._config)
        client._completion = CompletionService(self._config)
        client._dify = DifyService(self._config)
        client._workflow = WorkflowService(self._config)
        client._knowledge = KnowledgeService(self._config)
        return client

    def _init_logger(self):
        logger.setLevel(int(self._config.log_level.value))
