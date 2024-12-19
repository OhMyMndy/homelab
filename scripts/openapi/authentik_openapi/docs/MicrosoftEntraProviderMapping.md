# MicrosoftEntraProviderMapping

MicrosoftEntraProviderMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | 
**expression** | **str** |  | 
**component** | **str** | Get object&#39;s component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 

## Example

```python
from authentik_openapi.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftEntraProviderMapping from a JSON string
microsoft_entra_provider_mapping_instance = MicrosoftEntraProviderMapping.from_json(json)
# print the JSON string representation of the object
print(MicrosoftEntraProviderMapping.to_json())

# convert the object into a dict
microsoft_entra_provider_mapping_dict = microsoft_entra_provider_mapping_instance.to_dict()
# create an instance of MicrosoftEntraProviderMapping from a dict
microsoft_entra_provider_mapping_from_dict = MicrosoftEntraProviderMapping.from_dict(microsoft_entra_provider_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


