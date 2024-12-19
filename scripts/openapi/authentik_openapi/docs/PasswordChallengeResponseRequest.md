# PasswordChallengeResponseRequest

Password challenge response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-password']
**password** | **str** |  | 

## Example

```python
from authentik_openapi.models.password_challenge_response_request import PasswordChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordChallengeResponseRequest from a JSON string
password_challenge_response_request_instance = PasswordChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(PasswordChallengeResponseRequest.to_json())

# convert the object into a dict
password_challenge_response_request_dict = password_challenge_response_request_instance.to_dict()
# create an instance of PasswordChallengeResponseRequest from a dict
password_challenge_response_request_from_dict = PasswordChallengeResponseRequest.from_dict(password_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


