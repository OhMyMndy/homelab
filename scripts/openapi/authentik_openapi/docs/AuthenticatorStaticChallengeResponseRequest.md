# AuthenticatorStaticChallengeResponseRequest

Pseudo class for static response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-static']

## Example

```python
from authentik_openapi.models.authenticator_static_challenge_response_request import AuthenticatorStaticChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorStaticChallengeResponseRequest from a JSON string
authenticator_static_challenge_response_request_instance = AuthenticatorStaticChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorStaticChallengeResponseRequest.to_json())

# convert the object into a dict
authenticator_static_challenge_response_request_dict = authenticator_static_challenge_response_request_instance.to_dict()
# create an instance of AuthenticatorStaticChallengeResponseRequest from a dict
authenticator_static_challenge_response_request_from_dict = AuthenticatorStaticChallengeResponseRequest.from_dict(authenticator_static_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


