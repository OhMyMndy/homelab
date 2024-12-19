# MicrosoftEntraProviderUser

MicrosoftEntraProviderUser Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**microsoft_id** | **str** |  | 
**user** | **int** |  | 
**user_obj** | [**GroupMember**](GroupMember.md) |  | [readonly] 
**provider** | **int** |  | 
**attributes** | **object** |  | [readonly] 

## Example

```python
from authentik_openapi.models.microsoft_entra_provider_user import MicrosoftEntraProviderUser

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftEntraProviderUser from a JSON string
microsoft_entra_provider_user_instance = MicrosoftEntraProviderUser.from_json(json)
# print the JSON string representation of the object
print(MicrosoftEntraProviderUser.to_json())

# convert the object into a dict
microsoft_entra_provider_user_dict = microsoft_entra_provider_user_instance.to_dict()
# create an instance of MicrosoftEntraProviderUser from a dict
microsoft_entra_provider_user_from_dict = MicrosoftEntraProviderUser.from_dict(microsoft_entra_provider_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


