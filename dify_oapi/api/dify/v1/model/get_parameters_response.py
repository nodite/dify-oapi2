from dify_oapi.core.model.base_response import BaseResponse


class GetParametersResponse(BaseResponse):
    """Response for get application parameters API."""

    opening_statement: str | None = None
    suggested_questions: list[str] | None = None
    speech_to_text: dict | None = None
    text_to_speech: dict | None = None
    retriever_resource: dict | None = None
    annotation_reply: dict | None = None
    more_like_this: dict | None = None
    user_input_form: list[dict] | None = None
    sensitive_word_avoidance: dict | None = None
    file_upload: dict | None = None
    system_parameters: dict | None = None
