# MicrosoftEntraProviderUserRequest

MicrosoftEntraProviderUser Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microsoft_id** | **str** |  | 
**user** | **int** |  | 
**provider** | **int** |  | 

## Example

```python
from authentik_openapi.models.microsoft_entra_provider_user_request import MicrosoftEntraProviderUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftEntraProviderUserRequest from a JSON string
microsoft_entra_provider_user_request_instance = MicrosoftEntraProviderUserRequest.from_json(json)
# print the JSON string representation of the object
print(MicrosoftEntraProviderUserRequest.to_json())

# convert the object into a dict
microsoft_entra_provider_user_request_dict = microsoft_entra_provider_user_request_instance.to_dict()
# create an instance of MicrosoftEntraProviderUserRequest from a dict
microsoft_entra_provider_user_request_from_dict = MicrosoftEntraProviderUserRequest.from_dict(microsoft_entra_provider_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


