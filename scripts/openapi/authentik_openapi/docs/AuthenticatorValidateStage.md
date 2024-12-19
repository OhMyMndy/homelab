# AuthenticatorValidateStage

AuthenticatorValidateStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [optional] 
**not_configured_action** | [**NotConfiguredActionEnum**](NotConfiguredActionEnum.md) |  | [optional] 
**device_classes** | [**List[DeviceClassesEnum]**](DeviceClassesEnum.md) | Device classes which can be used to authenticate | [optional] 
**configuration_stages** | **List[str]** | Stages used to configure Authenticator when user doesn&#39;t have any compatible devices. After this configuration Stage passes, the user is not prompted again. | [optional] 
**last_auth_threshold** | **str** | If any of the user&#39;s device has been used within this threshold, this stage will be skipped | [optional] 
**webauthn_user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) | Enforce user verification for WebAuthn devices. | [optional] 
**webauthn_allowed_device_types** | **List[str]** |  | [optional] 
**webauthn_allowed_device_types_obj** | [**List[WebAuthnDeviceType]**](WebAuthnDeviceType.md) |  | [readonly] 

## Example

```python
from authentik_openapi.models.authenticator_validate_stage import AuthenticatorValidateStage

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorValidateStage from a JSON string
authenticator_validate_stage_instance = AuthenticatorValidateStage.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorValidateStage.to_json())

# convert the object into a dict
authenticator_validate_stage_dict = authenticator_validate_stage_instance.to_dict()
# create an instance of AuthenticatorValidateStage from a dict
authenticator_validate_stage_from_dict = AuthenticatorValidateStage.from_dict(authenticator_validate_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


