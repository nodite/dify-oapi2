from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
from ..model.bind_tags_to_dataset_response import BindTagsToDatasetResponse
from ..model.create_tag_request import CreateTagRequest
from ..model.create_tag_response import CreateTagResponse
from ..model.delete_tag_request import DeleteTagRequest
from ..model.delete_tag_response import DeleteTagResponse
from ..model.get_dataset_tags_request import GetDatasetTagsRequest
from ..model.get_dataset_tags_response import GetDatasetTagsResponse
from ..model.list_tags_request import ListTagsRequest
from ..model.list_tags_response import ListTagsResponse
from ..model.unbind_tags_from_dataset_request import UnbindTagsFromDatasetRequest
from ..model.unbind_tags_from_dataset_response import UnbindTagsFromDatasetResponse
from ..model.update_tag_request import UpdateTagRequest
from ..model.update_tag_response import UpdateTagResponse


class Tag:
    def __init__(self, config: Config):
        self.config = config

    def list(self, request: ListTagsRequest, request_option: RequestOption) -> ListTagsResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListTagsResponse, option=request_option)

    async def alist(self, request: ListTagsRequest, request_option: RequestOption) -> ListTagsResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListTagsResponse, option=request_option)

    def create(self, request: CreateTagRequest, request_option: RequestOption) -> CreateTagResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateTagResponse, option=request_option)

    async def acreate(self, request: CreateTagRequest, request_option: RequestOption) -> CreateTagResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateTagResponse, option=request_option)

    def update(self, request: UpdateTagRequest, request_option: RequestOption) -> UpdateTagResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateTagResponse, option=request_option)

    async def aupdate(self, request: UpdateTagRequest, request_option: RequestOption) -> UpdateTagResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateTagResponse, option=request_option)

    def delete(self, request: DeleteTagRequest, request_option: RequestOption) -> DeleteTagResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteTagResponse, option=request_option)

    async def adelete(self, request: DeleteTagRequest, request_option: RequestOption) -> DeleteTagResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteTagResponse, option=request_option)

    def bind(self, request: BindTagsToDatasetRequest, request_option: RequestOption) -> BindTagsToDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=BindTagsToDatasetResponse, option=request_option)

    async def abind(
        self, request: BindTagsToDatasetRequest, request_option: RequestOption
    ) -> BindTagsToDatasetResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=BindTagsToDatasetResponse, option=request_option
        )

    def unbind(
        self, request: UnbindTagsFromDatasetRequest, request_option: RequestOption
    ) -> UnbindTagsFromDatasetResponse:
        return Transport.execute(
            self.config, request, unmarshal_as=UnbindTagsFromDatasetResponse, option=request_option
        )

    async def aunbind(
        self, request: UnbindTagsFromDatasetRequest, request_option: RequestOption
    ) -> UnbindTagsFromDatasetResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=UnbindTagsFromDatasetResponse, option=request_option
        )

    def get_dataset_tags(self, request: GetDatasetTagsRequest, request_option: RequestOption) -> GetDatasetTagsResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetDatasetTagsResponse, option=request_option)

    async def aget_dataset_tags(
        self, request: GetDatasetTagsRequest, request_option: RequestOption
    ) -> GetDatasetTagsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetDatasetTagsResponse, option=request_option
        )
