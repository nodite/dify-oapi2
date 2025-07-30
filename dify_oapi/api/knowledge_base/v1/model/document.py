from __future__ import annotations

from pydantic import BaseModel


class Document(BaseModel):
    id: str | None = None
    position: int | None = None
    data_source_type: str | None = None
    data_source_info: DocumentDataSourceInfo | None = None
    data_source_detail_dict: DocumentDataSourceDetailDict | None = None
    dataset_process_rule_id: str | None = None
    name: str | None = None
    created_from: str | None = None
    created_by: str | None = None
    created_at: int | None = None
    tokens: int | None = None
    indexing_status: str | None = None
    error: str | None = None
    enabled: bool | None = None
    disabled_at: int | None = None
    disabled_by: str | None = None
    archived: bool | None = None
    display_status: str | None = None
    word_count: int | None = None
    hit_count: int | None = None
    doc_form: str | None = None

    @staticmethod
    def builder() -> DocumentBuilder:
        return DocumentBuilder()


class DocumentBuilder:
    def __init__(self):
        self._document = Document()

    def build(self) -> Document:
        return self._document

    def id(self, id: str) -> DocumentBuilder:
        self._document.id = id
        return self

    def position(self, position: int) -> DocumentBuilder:
        self._document.position = position
        return self

    def data_source_type(self, data_source_type: str) -> DocumentBuilder:
        self._document.data_source_type = data_source_type
        return self

    def data_source_info(self, data_source_info: DocumentDataSourceInfo) -> DocumentBuilder:
        self._document.data_source_info = data_source_info
        return self

    def data_source_detail_dict(self, data_source_detail_dict: DocumentDataSourceDetailDict) -> DocumentBuilder:
        self._document.data_source_detail_dict = data_source_detail_dict
        return self

    def dataset_process_rule_id(self, dataset_process_rule_id: str) -> DocumentBuilder:
        self._document.dataset_process_rule_id = dataset_process_rule_id
        return self

    def name(self, name: str) -> DocumentBuilder:
        self._document.name = name
        return self

    def created_from(self, created_from: str) -> DocumentBuilder:
        self._document.created_from = created_from
        return self

    def created_by(self, created_by: str) -> DocumentBuilder:
        self._document.created_by = created_by
        return self

    def created_at(self, created_at: int) -> DocumentBuilder:
        self._document.created_at = created_at
        return self

    def tokens(self, tokens: int) -> DocumentBuilder:
        self._document.tokens = tokens
        return self

    def indexing_status(self, indexing_status: str) -> DocumentBuilder:
        self._document.indexing_status = indexing_status
        return self

    def error(self, error: str) -> DocumentBuilder:
        self._document.error = error
        return self

    def enabled(self, enabled: bool) -> DocumentBuilder:
        self._document.enabled = enabled
        return self

    def disabled_at(self, disabled_at: int) -> DocumentBuilder:
        self._document.disabled_at = disabled_at
        return self

    def disabled_by(self, disabled_by: str) -> DocumentBuilder:
        self._document.disabled_by = disabled_by
        return self

    def archived(self, archived: bool) -> DocumentBuilder:
        self._document.archived = archived
        return self

    def display_status(self, display_status: str) -> DocumentBuilder:
        self._document.display_status = display_status
        return self

    def word_count(self, word_count: int) -> DocumentBuilder:
        self._document.word_count = word_count
        return self

    def hit_count(self, hit_count: int) -> DocumentBuilder:
        self._document.hit_count = hit_count
        return self

    def doc_form(self, doc_form: str) -> DocumentBuilder:
        self._document.doc_form = doc_form
        return self


class DocumentDataSourceInfo(BaseModel):
    upload_file_id: str | None = None

    @staticmethod
    def builder() -> DocumentDataSourceInfoBuilder:
        return DocumentDataSourceInfoBuilder()


class DocumentDataSourceInfoBuilder:
    def __init__(self):
        self._document_data_source_info = DocumentDataSourceInfo()

    def build(self) -> DocumentDataSourceInfo:
        return self._document_data_source_info

    def upload_file_id(self, upload_file_id: str) -> DocumentDataSourceInfoBuilder:
        self._document_data_source_info.upload_file_id = upload_file_id
        return self


class DocumentDataSourceDetailDict(BaseModel):
    upload_file: DocumentDataSourceDetailDictUploadFile | None = None

    @staticmethod
    def builder() -> DocumentDataSourceDetailDictBuilder:
        return DocumentDataSourceDetailDictBuilder()


class DocumentDataSourceDetailDictBuilder:
    def __init__(self):
        self._document_data_source_detail_dict = DocumentDataSourceDetailDict()

    def build(self) -> DocumentDataSourceDetailDict:
        return self._document_data_source_detail_dict

    def upload_file(self, upload_file: DocumentDataSourceDetailDictUploadFile) -> DocumentDataSourceDetailDictBuilder:
        self._document_data_source_detail_dict.upload_file = upload_file
        return self


class DocumentDataSourceDetailDictUploadFile(BaseModel):
    id: str | None = None
    name: str | None = None
    size: int | None = None
    extension: str | None = None
    mime_type: str | None = None
    created_by: str | None = None
    created_at: float | None = None

    @staticmethod
    def builder() -> DocumentDataSourceDetailDictUploadFileBuilder:
        return DocumentDataSourceDetailDictUploadFileBuilder()


class DocumentDataSourceDetailDictUploadFileBuilder:
    def __init__(self):
        self._document_data_source_detail_dict_upload_file = DocumentDataSourceDetailDictUploadFile()

    def build(self) -> DocumentDataSourceDetailDictUploadFile:
        return self._document_data_source_detail_dict_upload_file

    def id(self, id: str) -> DocumentDataSourceDetailDictUploadFileBuilder:
        self._document_data_source_detail_dict_upload_file.id = id
        return self

    def name(self, name: str) -> DocumentDataSourceDetailDictUploadFileBuilder:
        self._document_data_source_detail_dict_upload_file.name = name
        return self

    def size(self, size: int) -> DocumentDataSourceDetailDictUploadFileBuilder:
        self._document_data_source_detail_dict_upload_file.size = size
        return self

    def extension(self, extension: str) -> DocumentDataSourceDetailDictUploadFileBuilder:
        self._document_data_source_detail_dict_upload_file.extension = extension
        return self

    def mime_type(self, mime_type: str) -> DocumentDataSourceDetailDictUploadFileBuilder:
        self._document_data_source_detail_dict_upload_file.mime_type = mime_type
        return self

    def created_by(self, created_by: str) -> DocumentDataSourceDetailDictUploadFileBuilder:
        self._document_data_source_detail_dict_upload_file.created_by = created_by
        return self

    def created_at(self, created_at: float) -> DocumentDataSourceDetailDictUploadFileBuilder:
        self._document_data_source_detail_dict_upload_file.created_at = created_at
        return self
