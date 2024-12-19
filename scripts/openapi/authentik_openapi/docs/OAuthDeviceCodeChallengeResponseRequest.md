# OAuthDeviceCodeChallengeResponseRequest

Response that includes the user-entered device code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-provider-oauth2-device-code']
**code** | **int** |  | 

## Example

```python
from authentik_openapi.models.o_auth_device_code_challenge_response_request import OAuthDeviceCodeChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthDeviceCodeChallengeResponseRequest from a JSON string
o_auth_device_code_challenge_response_request_instance = OAuthDeviceCodeChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthDeviceCodeChallengeResponseRequest.to_json())

# convert the object into a dict
o_auth_device_code_challenge_response_request_dict = o_auth_device_code_challenge_response_request_instance.to_dict()
# create an instance of OAuthDeviceCodeChallengeResponseRequest from a dict
o_auth_device_code_challenge_response_request_from_dict = OAuthDeviceCodeChallengeResponseRequest.from_dict(o_auth_device_code_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


