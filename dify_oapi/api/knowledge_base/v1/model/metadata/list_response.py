from __future__ import annotations

from typing import List, Optional

from dify_oapi.core.model.base_response import BaseResponse

from dify_oapi.api.knowledge_base.v1.model.metadata.metadata_info import MetadataInfo


class ListResponse(BaseResponse):
    doc_metadata: Optional[List[MetadataInfo]] = None
    built_in_field_enabled: Optional[bool] = None
