# SCIMMappingRequest

SCIMMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | 
**expression** | **str** |  | 

## Example

```python
from authentik_openapi.models.scim_mapping_request import SCIMMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMMappingRequest from a JSON string
scim_mapping_request_instance = SCIMMappingRequest.from_json(json)
# print the JSON string representation of the object
print(SCIMMappingRequest.to_json())

# convert the object into a dict
scim_mapping_request_dict = scim_mapping_request_instance.to_dict()
# create an instance of SCIMMappingRequest from a dict
scim_mapping_request_from_dict = SCIMMappingRequest.from_dict(scim_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


