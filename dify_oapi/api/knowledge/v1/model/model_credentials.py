"""Model credentials for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class ModelCredentials(BaseModel):
    """Model credentials with builder pattern."""

    api_key: Optional[str] = None
    api_base: Optional[str] = None

    @staticmethod
    def builder() -> "ModelCredentialsBuilder":
        return ModelCredentialsBuilder()


class ModelCredentialsBuilder:
    """Builder for ModelCredentials."""

    def __init__(self):
        self._model_credentials = ModelCredentials()

    def build(self) -> ModelCredentials:
        return self._model_credentials

    def api_key(self, api_key: str) -> "ModelCredentialsBuilder":
        self._model_credentials.api_key = api_key
        return self

    def api_base(self, api_base: str) -> "ModelCredentialsBuilder":
        self._model_credentials.api_base = api_base
        return self
