# PaginatedPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Permission]**](Permission.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_permission_list import PaginatedPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPermissionList from a JSON string
paginated_permission_list_instance = PaginatedPermissionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPermissionList.to_json())

# convert the object into a dict
paginated_permission_list_dict = paginated_permission_list_instance.to_dict()
# create an instance of PaginatedPermissionList from a dict
paginated_permission_list_from_dict = PaginatedPermissionList.from_dict(paginated_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


