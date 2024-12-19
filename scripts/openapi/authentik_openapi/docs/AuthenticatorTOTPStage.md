# AuthenticatorTOTPStage

AuthenticatorTOTPStage Serializer

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
**digits** | [**DigitsEnum**](DigitsEnum.md) |  | 

## Example

```python
from authentik_openapi.models.authenticator_totp_stage import AuthenticatorTOTPStage

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorTOTPStage from a JSON string
authenticator_totp_stage_instance = AuthenticatorTOTPStage.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorTOTPStage.to_json())

# convert the object into a dict
authenticator_totp_stage_dict = authenticator_totp_stage_instance.to_dict()
# create an instance of AuthenticatorTOTPStage from a dict
authenticator_totp_stage_from_dict = AuthenticatorTOTPStage.from_dict(authenticator_totp_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


