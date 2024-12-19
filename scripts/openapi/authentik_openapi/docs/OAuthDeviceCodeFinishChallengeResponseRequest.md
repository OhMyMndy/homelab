# OAuthDeviceCodeFinishChallengeResponseRequest

Response that device has been authenticated and tab can be closed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-provider-oauth2-device-code-finish']

## Example

```python
from authentik_openapi.models.o_auth_device_code_finish_challenge_response_request import OAuthDeviceCodeFinishChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthDeviceCodeFinishChallengeResponseRequest from a JSON string
o_auth_device_code_finish_challenge_response_request_instance = OAuthDeviceCodeFinishChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthDeviceCodeFinishChallengeResponseRequest.to_json())

# convert the object into a dict
o_auth_device_code_finish_challenge_response_request_dict = o_auth_device_code_finish_challenge_response_request_instance.to_dict()
# create an instance of OAuthDeviceCodeFinishChallengeResponseRequest from a dict
o_auth_device_code_finish_challenge_response_request_from_dict = OAuthDeviceCodeFinishChallengeResponseRequest.from_dict(o_auth_device_code_finish_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


