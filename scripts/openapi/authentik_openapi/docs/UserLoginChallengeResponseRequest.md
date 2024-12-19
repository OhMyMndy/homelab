# UserLoginChallengeResponseRequest

User login challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-user-login']
**remember_me** | **bool** |  | 

## Example

```python
from authentik_openapi.models.user_login_challenge_response_request import UserLoginChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserLoginChallengeResponseRequest from a JSON string
user_login_challenge_response_request_instance = UserLoginChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(UserLoginChallengeResponseRequest.to_json())

# convert the object into a dict
user_login_challenge_response_request_dict = user_login_challenge_response_request_instance.to_dict()
# create an instance of UserLoginChallengeResponseRequest from a dict
user_login_challenge_response_request_from_dict = UserLoginChallengeResponseRequest.from_dict(user_login_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


