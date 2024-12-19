# PaginatedDockerServiceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[DockerServiceConnection]**](DockerServiceConnection.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_docker_service_connection_list import PaginatedDockerServiceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDockerServiceConnectionList from a JSON string
paginated_docker_service_connection_list_instance = PaginatedDockerServiceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDockerServiceConnectionList.to_json())

# convert the object into a dict
paginated_docker_service_connection_list_dict = paginated_docker_service_connection_list_instance.to_dict()
# create an instance of PaginatedDockerServiceConnectionList from a dict
paginated_docker_service_connection_list_from_dict = PaginatedDockerServiceConnectionList.from_dict(paginated_docker_service_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


