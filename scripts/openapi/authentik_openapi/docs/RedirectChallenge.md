# RedirectChallenge

Challenge type to redirect the client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'xak-flow-redirect']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**to** | **str** |  | 

## Example

```python
from authentik_openapi.models.redirect_challenge import RedirectChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectChallenge from a JSON string
redirect_challenge_instance = RedirectChallenge.from_json(json)
# print the JSON string representation of the object
print(RedirectChallenge.to_json())

# convert the object into a dict
redirect_challenge_dict = redirect_challenge_instance.to_dict()
# create an instance of RedirectChallenge from a dict
redirect_challenge_from_dict = RedirectChallenge.from_dict(redirect_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


