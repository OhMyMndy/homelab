# AuthenticatorSMSChallengeResponseRequest

SMS Challenge response, device is set by get_response_instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-sms']
**code** | **int** |  | [optional] 
**phone_number** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.authenticator_sms_challenge_response_request import AuthenticatorSMSChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorSMSChallengeResponseRequest from a JSON string
authenticator_sms_challenge_response_request_instance = AuthenticatorSMSChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorSMSChallengeResponseRequest.to_json())

# convert the object into a dict
authenticator_sms_challenge_response_request_dict = authenticator_sms_challenge_response_request_instance.to_dict()
# create an instance of AuthenticatorSMSChallengeResponseRequest from a dict
authenticator_sms_challenge_response_request_from_dict = AuthenticatorSMSChallengeResponseRequest.from_dict(authenticator_sms_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


