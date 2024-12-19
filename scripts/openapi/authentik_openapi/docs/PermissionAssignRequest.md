# PermissionAssignRequest

Request to assign a new permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | 
**model** | [**ModelEnum**](ModelEnum.md) |  | [optional] 
**object_pk** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.permission_assign_request import PermissionAssignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionAssignRequest from a JSON string
permission_assign_request_instance = PermissionAssignRequest.from_json(json)
# print the JSON string representation of the object
print(PermissionAssignRequest.to_json())

# convert the object into a dict
permission_assign_request_dict = permission_assign_request_instance.to_dict()
# create an instance of PermissionAssignRequest from a dict
permission_assign_request_from_dict = PermissionAssignRequest.from_dict(permission_assign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


