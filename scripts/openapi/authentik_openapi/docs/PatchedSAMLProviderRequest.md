# PatchedSAMLProviderRequest

SAMLProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**acs_url** | **str** |  | [optional] 
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

## Example

```python
from authentik_openapi.models.patched_saml_provider_request import PatchedSAMLProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSAMLProviderRequest from a JSON string
patched_saml_provider_request_instance = PatchedSAMLProviderRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSAMLProviderRequest.to_json())

# convert the object into a dict
patched_saml_provider_request_dict = patched_saml_provider_request_instance.to_dict()
# create an instance of PatchedSAMLProviderRequest from a dict
patched_saml_provider_request_from_dict = PatchedSAMLProviderRequest.from_dict(patched_saml_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


