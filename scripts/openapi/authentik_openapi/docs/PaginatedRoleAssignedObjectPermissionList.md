# PaginatedRoleAssignedObjectPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RoleAssignedObjectPermission]**](RoleAssignedObjectPermission.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_role_assigned_object_permission_list import PaginatedRoleAssignedObjectPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRoleAssignedObjectPermissionList from a JSON string
paginated_role_assigned_object_permission_list_instance = PaginatedRoleAssignedObjectPermissionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRoleAssignedObjectPermissionList.to_json())

# convert the object into a dict
paginated_role_assigned_object_permission_list_dict = paginated_role_assigned_object_permission_list_instance.to_dict()
# create an instance of PaginatedRoleAssignedObjectPermissionList from a dict
paginated_role_assigned_object_permission_list_from_dict = PaginatedRoleAssignedObjectPermissionList.from_dict(paginated_role_assigned_object_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


