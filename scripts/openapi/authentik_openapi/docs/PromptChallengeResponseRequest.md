# PromptChallengeResponseRequest

Validate response, fields are dynamically created based on the stage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-prompt']

## Example

```python
from authentik_openapi.models.prompt_challenge_response_request import PromptChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptChallengeResponseRequest from a JSON string
prompt_challenge_response_request_instance = PromptChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(PromptChallengeResponseRequest.to_json())

# convert the object into a dict
prompt_challenge_response_request_dict = prompt_challenge_response_request_instance.to_dict()
# create an instance of PromptChallengeResponseRequest from a dict
prompt_challenge_response_request_from_dict = PromptChallengeResponseRequest.from_dict(prompt_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


