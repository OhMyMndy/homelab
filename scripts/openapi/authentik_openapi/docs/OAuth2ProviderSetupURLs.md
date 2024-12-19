# OAuth2ProviderSetupURLs

OAuth2 Provider Metadata serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** |  | [readonly] 
**authorize** | **str** |  | [readonly] 
**token** | **str** |  | [readonly] 
**user_info** | **str** |  | [readonly] 
**provider_info** | **str** |  | [readonly] 
**logout** | **str** |  | [readonly] 
**jwks** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.o_auth2_provider_setup_urls import OAuth2ProviderSetupURLs

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ProviderSetupURLs from a JSON string
o_auth2_provider_setup_urls_instance = OAuth2ProviderSetupURLs.from_json(json)
# print the JSON string representation of the object
print(OAuth2ProviderSetupURLs.to_json())

# convert the object into a dict
o_auth2_provider_setup_urls_dict = o_auth2_provider_setup_urls_instance.to_dict()
# create an instance of OAuth2ProviderSetupURLs from a dict
o_auth2_provider_setup_urls_from_dict = OAuth2ProviderSetupURLs.from_dict(o_auth2_provider_setup_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


