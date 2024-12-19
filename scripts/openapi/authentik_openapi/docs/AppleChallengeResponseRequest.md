# AppleChallengeResponseRequest

Pseudo class for apple response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-source-oauth-apple']

## Example

```python
from authentik_openapi.models.apple_challenge_response_request import AppleChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppleChallengeResponseRequest from a JSON string
apple_challenge_response_request_instance = AppleChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(AppleChallengeResponseRequest.to_json())

# convert the object into a dict
apple_challenge_response_request_dict = apple_challenge_response_request_instance.to_dict()
# create an instance of AppleChallengeResponseRequest from a dict
apple_challenge_response_request_from_dict = AppleChallengeResponseRequest.from_dict(apple_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


