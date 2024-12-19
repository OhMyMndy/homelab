# PaginatedServiceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[ServiceConnection]**](ServiceConnection.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_service_connection_list import PaginatedServiceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedServiceConnectionList from a JSON string
paginated_service_connection_list_instance = PaginatedServiceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedServiceConnectionList.to_json())

# convert the object into a dict
paginated_service_connection_list_dict = paginated_service_connection_list_instance.to_dict()
# create an instance of PaginatedServiceConnectionList from a dict
paginated_service_connection_list_from_dict = PaginatedServiceConnectionList.from_dict(paginated_service_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


