import ssl

from dify_oapi.core.enum import LogLevel


class Config:
    def __init__(self):
        self.domain: str | None = None
        self.timeout: float | None = None  # Client timeout in seconds, default is no timeout
        self.log_level: LogLevel = LogLevel.WARNING  # Log level, default is WARNING
        self.max_retry_count: int = 3  # Maximum retry count after request failure. Default is 3

        # Connection pool settings
        self.max_keepalive_connections: int = 20  # Max keepalive connections per pool
        self.max_connections: int = 100  # Max total connections per pool
        self.keepalive_expiry: float = 30.0  # Keepalive connection expiry time in seconds

        # SSL settings
        self.verify_ssl: ssl.SSLContext | str | bool = True  # SSL certificate verification
