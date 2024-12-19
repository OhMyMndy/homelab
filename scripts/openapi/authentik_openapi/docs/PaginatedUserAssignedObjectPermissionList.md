# PaginatedUserAssignedObjectPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserAssignedObjectPermission]**](UserAssignedObjectPermission.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_user_assigned_object_permission_list import PaginatedUserAssignedObjectPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserAssignedObjectPermissionList from a JSON string
paginated_user_assigned_object_permission_list_instance = PaginatedUserAssignedObjectPermissionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserAssignedObjectPermissionList.to_json())

# convert the object into a dict
paginated_user_assigned_object_permission_list_dict = paginated_user_assigned_object_permission_list_instance.to_dict()
# create an instance of PaginatedUserAssignedObjectPermissionList from a dict
paginated_user_assigned_object_permission_list_from_dict = PaginatedUserAssignedObjectPermissionList.from_dict(paginated_user_assigned_object_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


