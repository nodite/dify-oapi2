from __future__ import annotations

from pydantic import BaseModel


class EndUserInfo(BaseModel):
    id: str | None = None
    type: str | None = None
    is_anonymous: bool | None = None
    session_id: str | None = None

    @staticmethod
    def builder() -> EndUserInfoBuilder:
        return EndUserInfoBuilder()


class EndUserInfoBuilder:
    def __init__(self):
        self._end_user_info = EndUserInfo()

    def build(self) -> EndUserInfo:
        return self._end_user_info

    def id(self, id: str) -> EndUserInfoBuilder:
        self._end_user_info.id = id
        return self

    def type(self, type: str) -> EndUserInfoBuilder:
        self._end_user_info.type = type
        return self

    def is_anonymous(self, is_anonymous: bool) -> EndUserInfoBuilder:
        self._end_user_info.is_anonymous = is_anonymous
        return self

    def session_id(self, session_id: str) -> EndUserInfoBuilder:
        self._end_user_info.session_id = session_id
        return self
