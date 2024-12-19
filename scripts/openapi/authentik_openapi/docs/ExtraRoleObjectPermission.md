# ExtraRoleObjectPermission

User permission with additional object-related data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**codename** | **str** |  | [readonly] 
**model** | **str** |  | [readonly] 
**app_label** | **str** |  | [readonly] 
**object_pk** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 
**app_label_verbose** | **str** | Get app label from permission&#39;s model | [readonly] 
**model_verbose** | **str** | Get model label from permission&#39;s model | [readonly] 
**object_description** | **str** | Get model description from attached model. This operation takes at least one additional query, and the description is only shown if the user/role has the view_ permission on the object | [readonly] 

## Example

```python
from authentik_openapi.models.extra_role_object_permission import ExtraRoleObjectPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraRoleObjectPermission from a JSON string
extra_role_object_permission_instance = ExtraRoleObjectPermission.from_json(json)
# print the JSON string representation of the object
print(ExtraRoleObjectPermission.to_json())

# convert the object into a dict
extra_role_object_permission_dict = extra_role_object_permission_instance.to_dict()
# create an instance of ExtraRoleObjectPermission from a dict
extra_role_object_permission_from_dict = ExtraRoleObjectPermission.from_dict(extra_role_object_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


