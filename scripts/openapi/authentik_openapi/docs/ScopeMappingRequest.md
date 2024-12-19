# ScopeMappingRequest

ScopeMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | 
**expression** | **str** |  | 
**scope_name** | **str** | Scope name requested by the client | 
**description** | **str** | Description shown to the user when consenting. If left empty, the user won&#39;t be informed. | [optional] 

## Example

```python
from authentik_openapi.models.scope_mapping_request import ScopeMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeMappingRequest from a JSON string
scope_mapping_request_instance = ScopeMappingRequest.from_json(json)
# print the JSON string representation of the object
print(ScopeMappingRequest.to_json())

# convert the object into a dict
scope_mapping_request_dict = scope_mapping_request_instance.to_dict()
# create an instance of ScopeMappingRequest from a dict
scope_mapping_request_from_dict = ScopeMappingRequest.from_dict(scope_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


