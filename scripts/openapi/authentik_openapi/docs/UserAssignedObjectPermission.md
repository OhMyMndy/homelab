# UserAssignedObjectPermission

Users assigned object permission serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**name** | **str** | User&#39;s display name. | 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**last_login** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**uid** | **str** |  | [readonly] 
**permissions** | [**List[UserObjectPermission]**](UserObjectPermission.md) |  | 
**is_superuser** | **bool** |  | 

## Example

```python
from authentik_openapi.models.user_assigned_object_permission import UserAssignedObjectPermission

# TODO update the JSON string below
json = "{}"
# create an instance of UserAssignedObjectPermission from a JSON string
user_assigned_object_permission_instance = UserAssignedObjectPermission.from_json(json)
# print the JSON string representation of the object
print(UserAssignedObjectPermission.to_json())

# convert the object into a dict
user_assigned_object_permission_dict = user_assigned_object_permission_instance.to_dict()
# create an instance of UserAssignedObjectPermission from a dict
user_assigned_object_permission_from_dict = UserAssignedObjectPermission.from_dict(user_assigned_object_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


