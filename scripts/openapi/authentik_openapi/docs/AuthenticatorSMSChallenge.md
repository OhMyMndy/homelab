# AuthenticatorSMSChallenge

SMS Setup challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-sms']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**phone_number_required** | **bool** |  | [optional] [default to True]

## Example

```python
from authentik_openapi.models.authenticator_sms_challenge import AuthenticatorSMSChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorSMSChallenge from a JSON string
authenticator_sms_challenge_instance = AuthenticatorSMSChallenge.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorSMSChallenge.to_json())

# convert the object into a dict
authenticator_sms_challenge_dict = authenticator_sms_challenge_instance.to_dict()
# create an instance of AuthenticatorSMSChallenge from a dict
authenticator_sms_challenge_from_dict = AuthenticatorSMSChallenge.from_dict(authenticator_sms_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


