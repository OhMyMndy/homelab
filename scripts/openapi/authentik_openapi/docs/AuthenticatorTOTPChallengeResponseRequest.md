# AuthenticatorTOTPChallengeResponseRequest

TOTP Challenge response, device is set by get_response_instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-totp']
**code** | **int** |  | 

## Example

```python
from authentik_openapi.models.authenticator_totp_challenge_response_request import AuthenticatorTOTPChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorTOTPChallengeResponseRequest from a JSON string
authenticator_totp_challenge_response_request_instance = AuthenticatorTOTPChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorTOTPChallengeResponseRequest.to_json())

# convert the object into a dict
authenticator_totp_challenge_response_request_dict = authenticator_totp_challenge_response_request_instance.to_dict()
# create an instance of AuthenticatorTOTPChallengeResponseRequest from a dict
authenticator_totp_challenge_response_request_from_dict = AuthenticatorTOTPChallengeResponseRequest.from_dict(authenticator_totp_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


