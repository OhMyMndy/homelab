# PatchedRoleRequest

Role serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_role_request import PatchedRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRoleRequest from a JSON string
patched_role_request_instance = PatchedRoleRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedRoleRequest.to_json())

# convert the object into a dict
patched_role_request_dict = patched_role_request_instance.to_dict()
# create an instance of PatchedRoleRequest from a dict
patched_role_request_from_dict = PatchedRoleRequest.from_dict(patched_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


