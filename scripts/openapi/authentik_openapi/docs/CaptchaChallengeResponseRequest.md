# CaptchaChallengeResponseRequest

Validate captcha token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-captcha']
**token** | **str** |  | 

## Example

```python
from authentik_openapi.models.captcha_challenge_response_request import CaptchaChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CaptchaChallengeResponseRequest from a JSON string
captcha_challenge_response_request_instance = CaptchaChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(CaptchaChallengeResponseRequest.to_json())

# convert the object into a dict
captcha_challenge_response_request_dict = captcha_challenge_response_request_instance.to_dict()
# create an instance of CaptchaChallengeResponseRequest from a dict
captcha_challenge_response_request_from_dict = CaptchaChallengeResponseRequest.from_dict(captcha_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


