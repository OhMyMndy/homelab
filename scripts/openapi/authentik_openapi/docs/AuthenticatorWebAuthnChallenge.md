# AuthenticatorWebAuthnChallenge

WebAuthn Challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-webauthn']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**registration** | **Dict[str, object]** |  | 

## Example

```python
from authentik_openapi.models.authenticator_web_authn_challenge import AuthenticatorWebAuthnChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorWebAuthnChallenge from a JSON string
authenticator_web_authn_challenge_instance = AuthenticatorWebAuthnChallenge.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorWebAuthnChallenge.to_json())

# convert the object into a dict
authenticator_web_authn_challenge_dict = authenticator_web_authn_challenge_instance.to_dict()
# create an instance of AuthenticatorWebAuthnChallenge from a dict
authenticator_web_authn_challenge_from_dict = AuthenticatorWebAuthnChallenge.from_dict(authenticator_web_authn_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


