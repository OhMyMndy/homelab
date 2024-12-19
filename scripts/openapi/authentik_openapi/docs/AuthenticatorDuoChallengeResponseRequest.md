# AuthenticatorDuoChallengeResponseRequest

Pseudo class for duo response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-duo']

## Example

```python
from authentik_openapi.models.authenticator_duo_challenge_response_request import AuthenticatorDuoChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorDuoChallengeResponseRequest from a JSON string
authenticator_duo_challenge_response_request_instance = AuthenticatorDuoChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorDuoChallengeResponseRequest.to_json())

# convert the object into a dict
authenticator_duo_challenge_response_request_dict = authenticator_duo_challenge_response_request_instance.to_dict()
# create an instance of AuthenticatorDuoChallengeResponseRequest from a dict
authenticator_duo_challenge_response_request_from_dict = AuthenticatorDuoChallengeResponseRequest.from_dict(authenticator_duo_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


