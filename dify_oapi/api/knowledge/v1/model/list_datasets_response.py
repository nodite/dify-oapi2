from dify_oapi.core.model.base_response import BaseResponse

from .dataset_info import DatasetInfo


class ListDatasetsResponse(BaseResponse):
    data: list[DatasetInfo] | None = None
    has_more: bool | None = None
    limit: int | None = None
    total: int | None = None
    page: int | None = None
