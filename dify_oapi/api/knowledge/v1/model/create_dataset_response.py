from dify_oapi.core.model.base_response import BaseResponse

from .dataset_info import DatasetInfo


class CreateDatasetResponse(DatasetInfo, BaseResponse):
    pass
