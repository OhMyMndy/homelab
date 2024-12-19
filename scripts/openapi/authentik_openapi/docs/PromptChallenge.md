# PromptChallenge

Initial challenge being sent, define fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-prompt']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**fields** | [**List[StagePrompt]**](StagePrompt.md) |  | 

## Example

```python
from authentik_openapi.models.prompt_challenge import PromptChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of PromptChallenge from a JSON string
prompt_challenge_instance = PromptChallenge.from_json(json)
# print the JSON string representation of the object
print(PromptChallenge.to_json())

# convert the object into a dict
prompt_challenge_dict = prompt_challenge_instance.to_dict()
# create an instance of PromptChallenge from a dict
prompt_challenge_from_dict = PromptChallenge.from_dict(prompt_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


