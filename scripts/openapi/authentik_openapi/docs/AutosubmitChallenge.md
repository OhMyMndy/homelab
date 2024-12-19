# AutosubmitChallenge

Autosubmit challenge used to send and navigate a POST request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-autosubmit']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**url** | **str** |  | 
**attrs** | **Dict[str, str]** |  | 
**title** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.autosubmit_challenge import AutosubmitChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of AutosubmitChallenge from a JSON string
autosubmit_challenge_instance = AutosubmitChallenge.from_json(json)
# print the JSON string representation of the object
print(AutosubmitChallenge.to_json())

# convert the object into a dict
autosubmit_challenge_dict = autosubmit_challenge_instance.to_dict()
# create an instance of AutosubmitChallenge from a dict
autosubmit_challenge_from_dict = AutosubmitChallenge.from_dict(autosubmit_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


