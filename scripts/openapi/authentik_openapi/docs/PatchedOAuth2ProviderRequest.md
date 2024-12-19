# PatchedOAuth2ProviderRequest

OAuth2Provider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**client_type** | [**ClientTypeEnum**](ClientTypeEnum.md) | Confidential clients are capable of maintaining the confidentiality of their credentials. Public clients are incapable | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**access_code_validity** | **str** | Access codes not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**access_token_validity** | **str** | Tokens not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**refresh_token_validity** | **str** | Tokens not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**include_claims_in_id_token** | **bool** | Include User claims from scopes in the id_token, for applications that don&#39;t access the userinfo endpoint. | [optional] 
**signing_key** | **str** | Key used to sign the tokens. Only required when JWT Algorithm is set to RS256. | [optional] 
**redirect_uris** | **str** | Enter each URI on a new line. | [optional] 
**sub_mode** | [**SubModeEnum**](SubModeEnum.md) | Configure what data should be used as unique User Identifier. For most cases, the default should be fine. | [optional] 
**issuer_mode** | [**IssuerModeEnum**](IssuerModeEnum.md) | Configure how the issuer field of the ID Token should be filled. | [optional] 
**jwks_sources** | **List[str]** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_o_auth2_provider_request import PatchedOAuth2ProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedOAuth2ProviderRequest from a JSON string
patched_o_auth2_provider_request_instance = PatchedOAuth2ProviderRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedOAuth2ProviderRequest.to_json())

# convert the object into a dict
patched_o_auth2_provider_request_dict = patched_o_auth2_provider_request_instance.to_dict()
# create an instance of PatchedOAuth2ProviderRequest from a dict
patched_o_auth2_provider_request_from_dict = PatchedOAuth2ProviderRequest.from_dict(patched_o_auth2_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


