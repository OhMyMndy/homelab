# OAuthSourceRequest

OAuth Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 
**provider_type** | [**ProviderTypeEnum**](ProviderTypeEnum.md) |  | 
**request_token_url** | **str** | URL used to request the initial token. This URL is only required for OAuth 1. | [optional] 
**authorization_url** | **str** | URL the user is redirect to to conest the flow. | [optional] 
**access_token_url** | **str** | URL used by authentik to retrieve tokens. | [optional] 
**profile_url** | **str** | URL used by authentik to get user information. | [optional] 
**consumer_key** | **str** |  | 
**consumer_secret** | **str** |  | 
**additional_scopes** | **str** |  | [optional] 
**oidc_well_known_url** | **str** |  | [optional] 
**oidc_jwks_url** | **str** |  | [optional] 
**oidc_jwks** | **object** |  | [optional] 

## Example

```python
from authentik_openapi.models.o_auth_source_request import OAuthSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthSourceRequest from a JSON string
o_auth_source_request_instance = OAuthSourceRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthSourceRequest.to_json())

# convert the object into a dict
o_auth_source_request_dict = o_auth_source_request_instance.to_dict()
# create an instance of OAuthSourceRequest from a dict
o_auth_source_request_from_dict = OAuthSourceRequest.from_dict(o_auth_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


