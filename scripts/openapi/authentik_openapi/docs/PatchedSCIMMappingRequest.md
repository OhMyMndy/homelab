# PatchedSCIMMappingRequest

SCIMMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_scim_mapping_request import PatchedSCIMMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSCIMMappingRequest from a JSON string
patched_scim_mapping_request_instance = PatchedSCIMMappingRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSCIMMappingRequest.to_json())

# convert the object into a dict
patched_scim_mapping_request_dict = patched_scim_mapping_request_instance.to_dict()
# create an instance of PatchedSCIMMappingRequest from a dict
patched_scim_mapping_request_from_dict = PatchedSCIMMappingRequest.from_dict(patched_scim_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


