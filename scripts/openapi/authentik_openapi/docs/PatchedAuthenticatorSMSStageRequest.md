# PatchedAuthenticatorSMSStageRequest

AuthenticatorSMSStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**provider** | [**ProviderEnum**](ProviderEnum.md) |  | [optional] 
**from_number** | **str** |  | [optional] 
**account_sid** | **str** |  | [optional] 
**auth** | **str** |  | [optional] 
**auth_password** | **str** |  | [optional] 
**auth_type** | [**AuthTypeEnum**](AuthTypeEnum.md) |  | [optional] 
**verify_only** | **bool** | When enabled, the Phone number is only used during enrollment to verify the users authenticity. Only a hash of the phone number is saved to ensure it is not reused in the future. | [optional] 
**mapping** | **str** | Optionally modify the payload being sent to custom providers. | [optional] 

## Example

```python
from authentik_openapi.models.patched_authenticator_sms_stage_request import PatchedAuthenticatorSMSStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAuthenticatorSMSStageRequest from a JSON string
patched_authenticator_sms_stage_request_instance = PatchedAuthenticatorSMSStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAuthenticatorSMSStageRequest.to_json())

# convert the object into a dict
patched_authenticator_sms_stage_request_dict = patched_authenticator_sms_stage_request_instance.to_dict()
# create an instance of PatchedAuthenticatorSMSStageRequest from a dict
patched_authenticator_sms_stage_request_from_dict = PatchedAuthenticatorSMSStageRequest.from_dict(patched_authenticator_sms_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


