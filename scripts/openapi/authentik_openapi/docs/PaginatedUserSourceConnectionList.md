# PaginatedUserSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserSourceConnection]**](UserSourceConnection.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_user_source_connection_list import PaginatedUserSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserSourceConnectionList from a JSON string
paginated_user_source_connection_list_instance = PaginatedUserSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserSourceConnectionList.to_json())

# convert the object into a dict
paginated_user_source_connection_list_dict = paginated_user_source_connection_list_instance.to_dict()
# create an instance of PaginatedUserSourceConnectionList from a dict
paginated_user_source_connection_list_from_dict = PaginatedUserSourceConnectionList.from_dict(paginated_user_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


