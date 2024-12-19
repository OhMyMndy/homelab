# RoleObjectPermission

Role-bound object level permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**codename** | **str** |  | [readonly] 
**model** | **str** |  | [readonly] 
**app_label** | **str** |  | [readonly] 
**object_pk** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.role_object_permission import RoleObjectPermission

# TODO update the JSON string below
json = "{}"
# create an instance of RoleObjectPermission from a JSON string
role_object_permission_instance = RoleObjectPermission.from_json(json)
# print the JSON string representation of the object
print(RoleObjectPermission.to_json())

# convert the object into a dict
role_object_permission_dict = role_object_permission_instance.to_dict()
# create an instance of RoleObjectPermission from a dict
role_object_permission_from_dict = RoleObjectPermission.from_dict(role_object_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


