# SAMLSource

SAMLSource Serializer

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
**pre_authentication_flow** | **str** | Flow used before authentication. | 
**issuer** | **str** | Also known as Entity ID. Defaults the Metadata URL. | [optional] 
**sso_url** | **str** | URL that the initial Login request is sent to. | 
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
from authentik_openapi.models.saml_source import SAMLSource

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLSource from a JSON string
saml_source_instance = SAMLSource.from_json(json)
# print the JSON string representation of the object
print(SAMLSource.to_json())

# convert the object into a dict
saml_source_dict = saml_source_instance.to_dict()
# create an instance of SAMLSource from a dict
saml_source_from_dict = SAMLSource.from_dict(saml_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


