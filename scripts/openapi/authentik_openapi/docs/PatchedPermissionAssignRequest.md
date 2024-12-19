# PatchedPermissionAssignRequest

Request to assign a new permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | [optional] 
**model** | [**ModelEnum**](ModelEnum.md) |  | [optional] 
**object_pk** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_permission_assign_request import PatchedPermissionAssignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPermissionAssignRequest from a JSON string
patched_permission_assign_request_instance = PatchedPermissionAssignRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPermissionAssignRequest.to_json())

# convert the object into a dict
patched_permission_assign_request_dict = patched_permission_assign_request_instance.to_dict()
# create an instance of PatchedPermissionAssignRequest from a dict
patched_permission_assign_request_from_dict = PatchedPermissionAssignRequest.from_dict(patched_permission_assign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


