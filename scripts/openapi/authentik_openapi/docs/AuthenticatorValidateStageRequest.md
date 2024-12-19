# AuthenticatorValidateStageRequest

AuthenticatorValidateStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**not_configured_action** | [**NotConfiguredActionEnum**](NotConfiguredActionEnum.md) |  | [optional] 
**device_classes** | [**List[DeviceClassesEnum]**](DeviceClassesEnum.md) | Device classes which can be used to authenticate | [optional] 
**configuration_stages** | **List[str]** | Stages used to configure Authenticator when user doesn&#39;t have any compatible devices. After this configuration Stage passes, the user is not prompted again. | [optional] 
**last_auth_threshold** | **str** | If any of the user&#39;s device has been used within this threshold, this stage will be skipped | [optional] 
**webauthn_user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) | Enforce user verification for WebAuthn devices. | [optional] 
**webauthn_allowed_device_types** | **List[str]** |  | [optional] 

## Example

```python
from authentik_openapi.models.authenticator_validate_stage_request import AuthenticatorValidateStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorValidateStageRequest from a JSON string
authenticator_validate_stage_request_instance = AuthenticatorValidateStageRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorValidateStageRequest.to_json())

# convert the object into a dict
authenticator_validate_stage_request_dict = authenticator_validate_stage_request_instance.to_dict()
# create an instance of AuthenticatorValidateStageRequest from a dict
authenticator_validate_stage_request_from_dict = AuthenticatorValidateStageRequest.from_dict(authenticator_validate_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


