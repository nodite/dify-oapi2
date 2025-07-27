from __future__ import annotations

from dify_oapi.api.knowledge_base.v1.model.metadata.metadata_info import MetadataInfo
from dify_oapi.core.model.base_response import BaseResponse


class ListResponse(BaseResponse):
    doc_metadata: list[MetadataInfo] | None = None
    built_in_field_enabled: bool | None = None
