# AuthenticatorValidationChallengeResponseRequest

Challenge used for Code-based and WebAuthn authenticators

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-validate']
**selected_challenge** | [**DeviceChallengeRequest**](DeviceChallengeRequest.md) |  | [optional] 
**selected_stage** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**webauthn** | **Dict[str, object]** |  | [optional] 
**duo** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.authenticator_validation_challenge_response_request import AuthenticatorValidationChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorValidationChallengeResponseRequest from a JSON string
authenticator_validation_challenge_response_request_instance = AuthenticatorValidationChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorValidationChallengeResponseRequest.to_json())

# convert the object into a dict
authenticator_validation_challenge_response_request_dict = authenticator_validation_challenge_response_request_instance.to_dict()
# create an instance of AuthenticatorValidationChallengeResponseRequest from a dict
authenticator_validation_challenge_response_request_from_dict = AuthenticatorValidationChallengeResponseRequest.from_dict(authenticator_validation_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


