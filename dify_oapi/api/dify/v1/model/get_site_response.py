from dify_oapi.core.model.base_response import BaseResponse


class GetSiteResponse(BaseResponse):
    """Response for get site settings API."""

    title: str | None = None
    icon: str | None = None
    icon_background: str | None = None
    description: str | None = None
    default_language: str | None = None
    customize_domain: str | None = None
    customize_token_strategy: str | None = None
    prompt_public: bool | None = None
    copyright: str | None = None
    privacy_policy: str | None = None
    custom_disclaimer: str | None = None
