# PatchedAuthenticatorWebAuthnStageRequest

AuthenticatorWebAuthnStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) |  | [optional] 
**authenticator_attachment** | [**AuthenticatorAttachmentEnum**](AuthenticatorAttachmentEnum.md) |  | [optional] 
**resident_key_requirement** | [**ResidentKeyRequirementEnum**](ResidentKeyRequirementEnum.md) |  | [optional] 
**device_type_restrictions** | **List[str]** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_authenticator_web_authn_stage_request import PatchedAuthenticatorWebAuthnStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAuthenticatorWebAuthnStageRequest from a JSON string
patched_authenticator_web_authn_stage_request_instance = PatchedAuthenticatorWebAuthnStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAuthenticatorWebAuthnStageRequest.to_json())

# convert the object into a dict
patched_authenticator_web_authn_stage_request_dict = patched_authenticator_web_authn_stage_request_instance.to_dict()
# create an instance of PatchedAuthenticatorWebAuthnStageRequest from a dict
patched_authenticator_web_authn_stage_request_from_dict = PatchedAuthenticatorWebAuthnStageRequest.from_dict(patched_authenticator_web_authn_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


