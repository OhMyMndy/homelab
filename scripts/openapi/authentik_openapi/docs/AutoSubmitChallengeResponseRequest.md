# AutoSubmitChallengeResponseRequest

Pseudo class for autosubmit response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-autosubmit']

## Example

```python
from authentik_openapi.models.auto_submit_challenge_response_request import AutoSubmitChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutoSubmitChallengeResponseRequest from a JSON string
auto_submit_challenge_response_request_instance = AutoSubmitChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(AutoSubmitChallengeResponseRequest.to_json())

# convert the object into a dict
auto_submit_challenge_response_request_dict = auto_submit_challenge_response_request_instance.to_dict()
# create an instance of AutoSubmitChallengeResponseRequest from a dict
auto_submit_challenge_response_request_from_dict = AutoSubmitChallengeResponseRequest.from_dict(auto_submit_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


