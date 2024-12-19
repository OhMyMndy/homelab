# MicrosoftEntraProviderMappingRequest

MicrosoftEntraProviderMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | 
**expression** | **str** |  | 

## Example

```python
from authentik_openapi.models.microsoft_entra_provider_mapping_request import MicrosoftEntraProviderMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftEntraProviderMappingRequest from a JSON string
microsoft_entra_provider_mapping_request_instance = MicrosoftEntraProviderMappingRequest.from_json(json)
# print the JSON string representation of the object
print(MicrosoftEntraProviderMappingRequest.to_json())

# convert the object into a dict
microsoft_entra_provider_mapping_request_dict = microsoft_entra_provider_mapping_request_instance.to_dict()
# create an instance of MicrosoftEntraProviderMappingRequest from a dict
microsoft_entra_provider_mapping_request_from_dict = MicrosoftEntraProviderMappingRequest.from_dict(microsoft_entra_provider_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


