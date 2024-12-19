# AuthenticatorTOTPChallenge

TOTP Setup challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-totp']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**config_url** | **str** |  | 

## Example

```python
from authentik_openapi.models.authenticator_totp_challenge import AuthenticatorTOTPChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorTOTPChallenge from a JSON string
authenticator_totp_challenge_instance = AuthenticatorTOTPChallenge.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorTOTPChallenge.to_json())

# convert the object into a dict
authenticator_totp_challenge_dict = authenticator_totp_challenge_instance.to_dict()
# create an instance of AuthenticatorTOTPChallenge from a dict
authenticator_totp_challenge_from_dict = AuthenticatorTOTPChallenge.from_dict(authenticator_totp_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


