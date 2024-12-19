# MicrosoftEntraProviderGroup

MicrosoftEntraProviderGroup Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**microsoft_id** | **str** |  | 
**group** | **str** |  | 
**group_obj** | [**UserGroup**](UserGroup.md) |  | [readonly] 
**provider** | **int** |  | 
**attributes** | **object** |  | [readonly] 

## Example

```python
from authentik_openapi.models.microsoft_entra_provider_group import MicrosoftEntraProviderGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftEntraProviderGroup from a JSON string
microsoft_entra_provider_group_instance = MicrosoftEntraProviderGroup.from_json(json)
# print the JSON string representation of the object
print(MicrosoftEntraProviderGroup.to_json())

# convert the object into a dict
microsoft_entra_provider_group_dict = microsoft_entra_provider_group_instance.to_dict()
# create an instance of MicrosoftEntraProviderGroup from a dict
microsoft_entra_provider_group_from_dict = MicrosoftEntraProviderGroup.from_dict(microsoft_entra_provider_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


