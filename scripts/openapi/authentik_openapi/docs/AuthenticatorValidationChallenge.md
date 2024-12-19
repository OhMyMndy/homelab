# AuthenticatorValidationChallenge

Authenticator challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-validate']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**device_challenges** | [**List[DeviceChallenge]**](DeviceChallenge.md) |  | 
**configuration_stages** | [**List[SelectableStage]**](SelectableStage.md) |  | 

## Example

```python
from authentik_openapi.models.authenticator_validation_challenge import AuthenticatorValidationChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorValidationChallenge from a JSON string
authenticator_validation_challenge_instance = AuthenticatorValidationChallenge.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorValidationChallenge.to_json())

# convert the object into a dict
authenticator_validation_challenge_dict = authenticator_validation_challenge_instance.to_dict()
# create an instance of AuthenticatorValidationChallenge from a dict
authenticator_validation_challenge_from_dict = AuthenticatorValidationChallenge.from_dict(authenticator_validation_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


