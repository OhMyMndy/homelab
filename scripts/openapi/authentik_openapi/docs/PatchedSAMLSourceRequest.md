# PatchedSAMLSourceRequest

SAMLSource Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | [optional] 
**slug** | **str** | Internal source name, used in URLs. | [optional] 
**enabled** | **bool** |  | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 
**pre_authentication_flow** | **str** | Flow used before authentication. | [optional] 
**issuer** | **str** | Also known as Entity ID. Defaults the Metadata URL. | [optional] 
**sso_url** | **str** | URL that the initial Login request is sent to. | [optional] 
**slo_url** | **str** | Optional URL if your IDP supports Single-Logout. | [optional] 
**allow_idp_initiated** | **bool** | Allows authentication flows initiated by the IdP. This can be a security risk, as no validation of the request ID is done. | [optional] 
**name_id_policy** | [**NameIdPolicyEnum**](NameIdPolicyEnum.md) | NameID Policy sent to the IdP. Can be unset, in which case no Policy is sent. | [optional] 
**binding_type** | [**BindingTypeEnum**](BindingTypeEnum.md) |  | [optional] 
**verification_kp** | **str** | When selected, incoming assertion&#39;s Signatures will be validated against this certificate. To allow unsigned Requests, leave on default. | [optional] 
**signing_kp** | **str** | Keypair used to sign outgoing Responses going to the Identity Provider. | [optional] 
**digest_algorithm** | [**DigestAlgorithmEnum**](DigestAlgorithmEnum.md) |  | [optional] 
**signature_algorithm** | [**SignatureAlgorithmEnum**](SignatureAlgorithmEnum.md) |  | [optional] 
**temporary_user_delete_after** | **str** | Time offset when temporary users should be deleted. This only applies if your IDP uses the NameID Format &#39;transient&#39;, and the user doesn&#39;t log out manually. (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 

## Example

```python
from authentik_openapi.models.patched_saml_source_request import PatchedSAMLSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSAMLSourceRequest from a JSON string
patched_saml_source_request_instance = PatchedSAMLSourceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSAMLSourceRequest.to_json())

# convert the object into a dict
patched_saml_source_request_dict = patched_saml_source_request_instance.to_dict()
# create an instance of PatchedSAMLSourceRequest from a dict
patched_saml_source_request_from_dict = PatchedSAMLSourceRequest.from_dict(patched_saml_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


