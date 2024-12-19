# AuthenticatorStaticChallenge

Static authenticator challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-static']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**codes** | **List[str]** |  | 

## Example

```python
from authentik_openapi.models.authenticator_static_challenge import AuthenticatorStaticChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorStaticChallenge from a JSON string
authenticator_static_challenge_instance = AuthenticatorStaticChallenge.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorStaticChallenge.to_json())

# convert the object into a dict
authenticator_static_challenge_dict = authenticator_static_challenge_instance.to_dict()
# create an instance of AuthenticatorStaticChallenge from a dict
authenticator_static_challenge_from_dict = AuthenticatorStaticChallenge.from_dict(authenticator_static_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


