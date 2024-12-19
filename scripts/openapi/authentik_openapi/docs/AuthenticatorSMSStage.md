# AuthenticatorSMSStage

AuthenticatorSMSStage Serializer

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
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**provider** | [**ProviderEnum**](ProviderEnum.md) |  | 
**from_number** | **str** |  | 
**account_sid** | **str** |  | 
**auth** | **str** |  | 
**auth_password** | **str** |  | [optional] 
**auth_type** | [**AuthTypeEnum**](AuthTypeEnum.md) |  | [optional] 
**verify_only** | **bool** | When enabled, the Phone number is only used during enrollment to verify the users authenticity. Only a hash of the phone number is saved to ensure it is not reused in the future. | [optional] 
**mapping** | **str** | Optionally modify the payload being sent to custom providers. | [optional] 

## Example

```python
from authentik_openapi.models.authenticator_sms_stage import AuthenticatorSMSStage

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorSMSStage from a JSON string
authenticator_sms_stage_instance = AuthenticatorSMSStage.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorSMSStage.to_json())

# convert the object into a dict
authenticator_sms_stage_dict = authenticator_sms_stage_instance.to_dict()
# create an instance of AuthenticatorSMSStage from a dict
authenticator_sms_stage_from_dict = AuthenticatorSMSStage.from_dict(authenticator_sms_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


