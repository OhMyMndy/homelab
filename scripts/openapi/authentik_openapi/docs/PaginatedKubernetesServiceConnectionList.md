# PaginatedKubernetesServiceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[KubernetesServiceConnection]**](KubernetesServiceConnection.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_kubernetes_service_connection_list import PaginatedKubernetesServiceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedKubernetesServiceConnectionList from a JSON string
paginated_kubernetes_service_connection_list_instance = PaginatedKubernetesServiceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedKubernetesServiceConnectionList.to_json())

# convert the object into a dict
paginated_kubernetes_service_connection_list_dict = paginated_kubernetes_service_connection_list_instance.to_dict()
# create an instance of PaginatedKubernetesServiceConnectionList from a dict
paginated_kubernetes_service_connection_list_from_dict = PaginatedKubernetesServiceConnectionList.from_dict(paginated_kubernetes_service_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


