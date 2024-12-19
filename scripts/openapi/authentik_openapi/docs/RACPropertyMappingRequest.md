# RACPropertyMappingRequest

RACPropertyMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | 
**expression** | **str** |  | [optional] 
**static_settings** | **Dict[str, object]** |  | 

## Example

```python
from authentik_openapi.models.rac_property_mapping_request import RACPropertyMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RACPropertyMappingRequest from a JSON string
rac_property_mapping_request_instance = RACPropertyMappingRequest.from_json(json)
# print the JSON string representation of the object
print(RACPropertyMappingRequest.to_json())

# convert the object into a dict
rac_property_mapping_request_dict = rac_property_mapping_request_instance.to_dict()
# create an instance of RACPropertyMappingRequest from a dict
rac_property_mapping_request_from_dict = RACPropertyMappingRequest.from_dict(rac_property_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


