# RoleAssignedObjectPermission

Roles assigned object permission serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_pk** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 
**permissions** | [**List[RoleObjectPermission]**](RoleObjectPermission.md) |  | 

## Example

```python
from authentik_openapi.models.role_assigned_object_permission import RoleAssignedObjectPermission

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssignedObjectPermission from a JSON string
role_assigned_object_permission_instance = RoleAssignedObjectPermission.from_json(json)
# print the JSON string representation of the object
print(RoleAssignedObjectPermission.to_json())

# convert the object into a dict
role_assigned_object_permission_dict = role_assigned_object_permission_instance.to_dict()
# create an instance of RoleAssignedObjectPermission from a dict
role_assigned_object_permission_from_dict = RoleAssignedObjectPermission.from_dict(role_assigned_object_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


