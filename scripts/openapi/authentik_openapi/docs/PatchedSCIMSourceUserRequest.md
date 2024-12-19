# PatchedSCIMSourceUserRequest

SCIMSourceUser Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user** | **int** |  | [optional] 
**source** | **str** |  | [optional] 
**attributes** | **object** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_scim_source_user_request import PatchedSCIMSourceUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSCIMSourceUserRequest from a JSON string
patched_scim_source_user_request_instance = PatchedSCIMSourceUserRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSCIMSourceUserRequest.to_json())

# convert the object into a dict
patched_scim_source_user_request_dict = patched_scim_source_user_request_instance.to_dict()
# create an instance of PatchedSCIMSourceUserRequest from a dict
patched_scim_source_user_request_from_dict = PatchedSCIMSourceUserRequest.from_dict(patched_scim_source_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


