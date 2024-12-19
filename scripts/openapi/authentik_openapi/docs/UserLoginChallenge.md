# UserLoginChallenge

Empty challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-user-login']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 

## Example

```python
from authentik_openapi.models.user_login_challenge import UserLoginChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of UserLoginChallenge from a JSON string
user_login_challenge_instance = UserLoginChallenge.from_json(json)
# print the JSON string representation of the object
print(UserLoginChallenge.to_json())

# convert the object into a dict
user_login_challenge_dict = user_login_challenge_instance.to_dict()
# create an instance of UserLoginChallenge from a dict
user_login_challenge_from_dict = UserLoginChallenge.from_dict(user_login_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


