# AuthenticatorTOTPStageRequest

AuthenticatorTOTPStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**digits** | [**DigitsEnum**](DigitsEnum.md) |  | 

## Example

```python
from authentik_openapi.models.authenticator_totp_stage_request import AuthenticatorTOTPStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorTOTPStageRequest from a JSON string
authenticator_totp_stage_request_instance = AuthenticatorTOTPStageRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorTOTPStageRequest.to_json())

# convert the object into a dict
authenticator_totp_stage_request_dict = authenticator_totp_stage_request_instance.to_dict()
# create an instance of AuthenticatorTOTPStageRequest from a dict
authenticator_totp_stage_request_from_dict = AuthenticatorTOTPStageRequest.from_dict(authenticator_totp_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


