# PaginatedRoleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Role]**](Role.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_role_list import PaginatedRoleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRoleList from a JSON string
paginated_role_list_instance = PaginatedRoleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRoleList.to_json())

# convert the object into a dict
paginated_role_list_dict = paginated_role_list_instance.to_dict()
# create an instance of PaginatedRoleList from a dict
paginated_role_list_from_dict = PaginatedRoleList.from_dict(paginated_role_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


