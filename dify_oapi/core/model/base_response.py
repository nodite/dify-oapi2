from pydantic import BaseModel, Field

from .raw_response import RawResponse


class BaseResponse(BaseModel):
    raw: RawResponse | None = None
    code: str | None = Field(default=None, exclude=True)
    msg_: str | None = Field(default=None, validation_alias="msg", exclude=True)
    message_: str | None = Field(default=None, validation_alias="message", exclude=True)

    @property
    def msg(self) -> str | None:
        if self.msg_ is not None:
            return self.msg_

        if self.message_ is not None:
            return self.message_

        if self.raw is not None and self.raw.content is not None:
            return self.raw.content.decode("utf-8")

        return None

    @property
    def success(self) -> bool:
        return self.code is None
