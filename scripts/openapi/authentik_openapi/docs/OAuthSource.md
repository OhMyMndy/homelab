# OAuthSource

OAuth Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [readonly] 
**user_path_template** | **str** |  | [optional] 
**icon** | **str** |  | [readonly] 
**provider_type** | [**ProviderTypeEnum**](ProviderTypeEnum.md) |  | 
**request_token_url** | **str** | URL used to request the initial token. This URL is only required for OAuth 1. | [optional] 
**authorization_url** | **str** | URL the user is redirect to to conest the flow. | [optional] 
**access_token_url** | **str** | URL used by authentik to retrieve tokens. | [optional] 
**profile_url** | **str** | URL used by authentik to get user information. | [optional] 
**consumer_key** | **str** |  | 
**callback_url** | **str** | Get OAuth Callback URL | [readonly] 
**additional_scopes** | **str** |  | [optional] 
**type** | [**SourceType**](SourceType.md) |  | [readonly] 
**oidc_well_known_url** | **str** |  | [optional] 
**oidc_jwks_url** | **str** |  | [optional] 
**oidc_jwks** | **object** |  | [optional] 

## Example

```python
from authentik_openapi.models.o_auth_source import OAuthSource

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthSource from a JSON string
o_auth_source_instance = OAuthSource.from_json(json)
# print the JSON string representation of the object
print(OAuthSource.to_json())

# convert the object into a dict
o_auth_source_dict = o_auth_source_instance.to_dict()
# create an instance of OAuthSource from a dict
o_auth_source_from_dict = OAuthSource.from_dict(o_auth_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


