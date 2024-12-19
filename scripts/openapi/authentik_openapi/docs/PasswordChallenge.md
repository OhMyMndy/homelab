# PasswordChallenge

Password challenge UI fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-password']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**recovery_url** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.password_challenge import PasswordChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordChallenge from a JSON string
password_challenge_instance = PasswordChallenge.from_json(json)
# print the JSON string representation of the object
print(PasswordChallenge.to_json())

# convert the object into a dict
password_challenge_dict = password_challenge_instance.to_dict()
# create an instance of PasswordChallenge from a dict
password_challenge_from_dict = PasswordChallenge.from_dict(password_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


