from dify_oapi.core.enum import LogLevel


class Config:
    def __init__(self):
        self.domain: str | None = None
        self.timeout: float | None = None  # Client timeout in seconds, default is no timeout
        self.log_level: LogLevel = LogLevel.WARNING  # Log level, default is WARNING
        self.max_retry_count: int = 3  # Maximum retry count after request failure. Default is 3
