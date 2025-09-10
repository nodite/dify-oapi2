"""HTTP connection pool management for efficient TCP connection reuse."""

import threading
from typing import Optional

import httpx


class ConnectionPoolManager:
    """Manages HTTP connection pools to reduce TCP connection overhead."""

    _instance: Optional["ConnectionPoolManager"] = None
    _lock = threading.Lock()

    def __new__(cls) -> "ConnectionPoolManager":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._sync_clients: dict[str, httpx.Client] = {}
            self._async_clients: dict[str, httpx.AsyncClient] = {}
            self._client_lock = threading.Lock()
            self._initialized = True

    def get_sync_client(
        self,
        domain: str,
        timeout: Optional[float] = None,
        max_keepalive: int = 20,
        max_connections: int = 100,
        keepalive_expiry: float = 30.0,
        verify_ssl: bool = True,
    ) -> httpx.Client:
        """Get or create a sync HTTP client for the given domain."""
        client_key = f"{domain}:{timeout}:{max_keepalive}:{max_connections}:{keepalive_expiry}:{verify_ssl}"

        with self._client_lock:
            if client_key not in self._sync_clients:
                # Configure connection limits to prevent excessive connections
                limits = httpx.Limits(
                    max_keepalive_connections=max_keepalive,
                    max_connections=max_connections,
                    keepalive_expiry=keepalive_expiry,
                )

                self._sync_clients[client_key] = httpx.Client(
                    timeout=timeout,
                    limits=limits,
                    verify=verify_ssl,
                    # Note: HTTP/2 disabled to avoid h2 dependency requirement
                )

            return self._sync_clients[client_key]

    def get_async_client(
        self,
        domain: str,
        timeout: Optional[float] = None,
        max_keepalive: int = 20,
        max_connections: int = 100,
        keepalive_expiry: float = 30.0,
        verify_ssl: bool = True,
    ) -> httpx.AsyncClient:
        """Get or create an async HTTP client for the given domain."""
        client_key = f"{domain}:{timeout}:{max_keepalive}:{max_connections}:{keepalive_expiry}:{verify_ssl}"

        with self._client_lock:
            if client_key not in self._async_clients:
                # Configure connection limits to prevent excessive connections
                limits = httpx.Limits(
                    max_keepalive_connections=max_keepalive,
                    max_connections=max_connections,
                    keepalive_expiry=keepalive_expiry,
                )

                self._async_clients[client_key] = httpx.AsyncClient(
                    timeout=timeout,
                    limits=limits,
                    verify=verify_ssl,
                    # Note: HTTP/2 disabled to avoid h2 dependency requirement
                )

            return self._async_clients[client_key]

    def close_all(self):
        """Close all HTTP clients and clean up connections."""
        with self._client_lock:
            # Close sync clients
            for client in self._sync_clients.values():
                try:
                    client.close()
                except Exception:
                    pass
            self._sync_clients.clear()

            # Close async clients
            for _client in self._async_clients.values():
                try:
                    # Note: This should be called from an async context in practice
                    # For cleanup purposes, we'll just clear the dict
                    pass
                except Exception:
                    pass
            self._async_clients.clear()

    async def aclose_all(self):
        """Async version of close_all for proper async client cleanup."""
        with self._client_lock:
            # Close sync clients
            for sync_client in self._sync_clients.values():
                try:
                    sync_client.close()
                except Exception:
                    pass
            self._sync_clients.clear()

            # Close async clients properly
            for async_client in self._async_clients.values():
                try:
                    await async_client.aclose()
                except Exception:
                    pass
            self._async_clients.clear()


# Global connection pool manager instance
connection_pool = ConnectionPoolManager()
