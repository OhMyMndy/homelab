# AuthenticatorWebAuthnStageRequest

AuthenticatorWebAuthnStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) |  | [optional] 
**authenticator_attachment** | [**AuthenticatorAttachmentEnum**](AuthenticatorAttachmentEnum.md) |  | [optional] 
**resident_key_requirement** | [**ResidentKeyRequirementEnum**](ResidentKeyRequirementEnum.md) |  | [optional] 
**device_type_restrictions** | **List[str]** |  | [optional] 

## Example

```python
from authentik_openapi.models.authenticator_web_authn_stage_request import AuthenticatorWebAuthnStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorWebAuthnStageRequest from a JSON string
authenticator_web_authn_stage_request_instance = AuthenticatorWebAuthnStageRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorWebAuthnStageRequest.to_json())

# convert the object into a dict
authenticator_web_authn_stage_request_dict = authenticator_web_authn_stage_request_instance.to_dict()
# create an instance of AuthenticatorWebAuthnStageRequest from a dict
authenticator_web_authn_stage_request_from_dict = AuthenticatorWebAuthnStageRequest.from_dict(authenticator_web_authn_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


