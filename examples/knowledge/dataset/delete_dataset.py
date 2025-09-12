import os

from dify_oapi.api.knowledge.v1.model.delete_dataset_request import DeleteDatasetRequest
from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


def delete_example_datasets():
    api_key = os.getenv("KNOWLEDGE_KEY")
    if not api_key:
        raise ValueError("KNOWLEDGE_KEY environment variable is required")

    client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
    req_option = RequestOption.builder().api_key(api_key).build()

    # List datasets to find example ones
    list_req = ListDatasetsRequest.builder().build()
    list_response = client.knowledge.v1.dataset.list(list_req, req_option)

    deleted_count = 0
    for dataset in list_response.data or []:
        if dataset.name and dataset.name.startswith("[Example]"):
            delete_req = DeleteDatasetRequest.builder().dataset_id(dataset.id).build()
            client.knowledge.v1.dataset.delete(delete_req, req_option)
            print(f"Deleted dataset: {dataset.name}")
            deleted_count += 1

    print(f"Deleted {deleted_count} example datasets")


if __name__ == "__main__":
    delete_example_datasets()
