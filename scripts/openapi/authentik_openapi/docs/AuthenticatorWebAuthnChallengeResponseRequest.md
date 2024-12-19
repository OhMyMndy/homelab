# AuthenticatorWebAuthnChallengeResponseRequest

WebAuthn Challenge response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-webauthn']
**response** | **Dict[str, object]** |  | 

## Example

```python
from authentik_openapi.models.authenticator_web_authn_challenge_response_request import AuthenticatorWebAuthnChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorWebAuthnChallengeResponseRequest from a JSON string
authenticator_web_authn_challenge_response_request_instance = AuthenticatorWebAuthnChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorWebAuthnChallengeResponseRequest.to_json())

# convert the object into a dict
authenticator_web_authn_challenge_response_request_dict = authenticator_web_authn_challenge_response_request_instance.to_dict()
# create an instance of AuthenticatorWebAuthnChallengeResponseRequest from a dict
authenticator_web_authn_challenge_response_request_from_dict = AuthenticatorWebAuthnChallengeResponseRequest.from_dict(authenticator_web_authn_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


