# SAMLProvider

SAMLProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | 
**property_mappings** | **List[str]** |  | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**assigned_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_application_name** | **str** | Application&#39;s display Name. | [readonly] 
**assigned_backchannel_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_backchannel_application_name** | **str** | Application&#39;s display Name. | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**acs_url** | **str** |  | 
**audience** | **str** | Value of the audience restriction field of the assertion. When left empty, no audience restriction will be added. | [optional] 
**issuer** | **str** | Also known as EntityID | [optional] 
**assertion_valid_not_before** | **str** | Assertion valid not before current time + this value (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3). | [optional] 
**assertion_valid_not_on_or_after** | **str** | Assertion not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**session_valid_not_on_or_after** | **str** | Session not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**name_id_mapping** | **str** | Configure how the NameID value will be created. When left empty, the NameIDPolicy of the incoming request will be considered | [optional] 
**digest_algorithm** | [**DigestAlgorithmEnum**](DigestAlgorithmEnum.md) |  | [optional] 
**signature_algorithm** | [**SignatureAlgorithmEnum**](SignatureAlgorithmEnum.md) |  | [optional] 
**signing_kp** | **str** | Keypair used to sign outgoing Responses going to the Service Provider. | [optional] 
**verification_kp** | **str** | When selected, incoming assertion&#39;s Signatures will be validated against this certificate. To allow unsigned Requests, leave on default. | [optional] 
**sp_binding** | [**SpBindingEnum**](SpBindingEnum.md) | This determines how authentik sends the response back to the Service Provider. | [optional] 
**default_relay_state** | **str** | Default relay_state value for IDP-initiated logins | [optional] 
**url_download_metadata** | **str** | Get metadata download URL | [readonly] 
**url_sso_post** | **str** | Get SSO Post URL | [readonly] 
**url_sso_redirect** | **str** | Get SSO Redirect URL | [readonly] 
**url_sso_init** | **str** | Get SSO IDP-Initiated URL | [readonly] 
**url_slo_post** | **str** | Get SLO POST URL | [readonly] 
**url_slo_redirect** | **str** | Get SLO redirect URL | [readonly] 

## Example

```python
from authentik_openapi.models.saml_provider import SAMLProvider

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLProvider from a JSON string
saml_provider_instance = SAMLProvider.from_json(json)
# print the JSON string representation of the object
print(SAMLProvider.to_json())

# convert the object into a dict
saml_provider_dict = saml_provider_instance.to_dict()
# create an instance of SAMLProvider from a dict
saml_provider_from_dict = SAMLProvider.from_dict(saml_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


